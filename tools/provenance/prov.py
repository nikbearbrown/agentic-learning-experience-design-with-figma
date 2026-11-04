#!/usr/bin/env python3
"""prov.py: the provenance ledger for a human-in-the-loop Figma project.

Figma can't hold this record by itself. Through the MCP server an agent can't name a version or
write a comment, use_figma forbids setPluginData, and Figma's version history credits every agent
edit to the signed-in human. So every round of draw -> correct -> redraw goes into provenance.json,
next to snapshots taken with snapshot.js. See PROVENANCE.md for the loop.

Usage:
  prov.py init --project NAME --lesson TEXT --file-ref LOCALNAME [--ledger provenance.json]
  prov.py diff A.json B.json [--json]
  prov.py record --actor agent|human --snapshot S.json --intent TEXT [--why TEXT] [--prompt TEXT]
                 [--script PATH] [--screenshot PATH] [--chapter N] [--calls N]
                 [--check NAME=pass|fail|not-run ...] [--free] [--release c1,c2]
                 [--override-why TEXT] [--ledger provenance.json]
  prov.py check-constraints S.json [--ledger provenance.json]
  prov.py log [--ledger provenance.json]
  prov.py stamp-text [--round rN] [--ledger provenance.json]
  prov.py validate [--ledger provenance.json]

Standard library only. File keys never go in the ledger: --file-ref is a local name you map to the
key yourself, outside the repo.
"""
import argparse, datetime, json, os, sys

SCHEMA_ID = "alxd-provenance/0.1"
HERE = os.path.dirname(os.path.abspath(__file__))
STAMP_PREFIX = "Provenance ·"
POS_TOL = 0.5  # px; anything smaller is rounding, not a move

# Which snapshot fields each change kind compares, and the constraint property it creates.
FIELDS = [
    ("renamed", ("name",), "name"),
    ("reparented", ("parent",), "parent"),
    ("moved", ("x", "y"), "position"),
    ("resized", ("w", "h"), "size"),
    ("text", ("text",), "text"),
    ("fills", ("fills",), "fills"),
    ("visible", ("visible",), "visible"),
    ("props", ("props",), "props"),
    ("component", ("component",), "component"),
    ("layout", ("layout",), "layout"),
    ("annotations", ("annotations",), None),  # notes, not design: never a constraint
]
PROPERTY_FIELDS = {prop: fields for _, fields, prop in FIELDS if prop}


def now():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def load(path):
    with open(path) as f:
        return json.load(f)


def save(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, path)


# --- diff ---------------------------------------------------------------------

def _value(node, fields):
    if len(fields) == 1:
        v = node.get(fields[0])
        if fields[0] == "annotations":
            v = [a for a in (v or []) if not a.startswith(STAMP_PREFIX)]
        return v
    return {f: node.get(f) for f in fields}


def _differs(kind, before, after):
    if kind in ("moved", "resized"):
        for k in before:
            b, c = before[k], after.get(k)
            if b is None or c is None:
                if b != c:
                    return True
            elif abs(b - c) > POS_TOL:
                return True
        return False
    return before != after


def diff(a, b):
    """Changes from snapshot a to snapshot b, as a list of dicts."""
    na, nb = a.get("nodes", {}), b.get("nodes", {})
    out = []
    for nid in na:
        if nid not in nb:
            out.append({"node": nid, "name": na[nid].get("name"), "change": "removed", "before": True, "after": False})
    for nid in nb:
        if nid not in na:
            out.append({"node": nid, "name": nb[nid].get("name"), "change": "added", "before": False, "after": True})
    for nid in na:
        if nid not in nb:
            continue
        for kind, fields, _ in FIELDS:
            before, after = _value(na[nid], fields), _value(nb[nid], fields)
            if _differs(kind, before, after):
                out.append({"node": nid, "name": nb[nid].get("name"), "change": kind, "before": before, "after": after})
    return out


def describe(c):
    name = f"{c['name']} ({c['node']})"
    if c["change"] in ("added", "removed"):
        return f"{c['change']}: {name}"
    return f"{c['change']}: {name}: {json.dumps(c['before'], ensure_ascii=False)} -> {json.dumps(c['after'], ensure_ascii=False)}"


# --- constraints ----------------------------------------------------------------

def constraints_from(changes, round_id, why, start):
    out, n = [], start
    for c in changes:
        if c["change"] in ("added", "removed"):
            prop, value = "exists", c["after"]
        else:
            prop = next((p for k, _, p in FIELDS if k == c["change"]), None)
            if not prop:
                continue
            value = c["after"]
        n += 1
        out.append({"id": f"c{n}", "node": c["node"], "name": c["name"], "property": prop, "value": value,
                    "from_round": round_id, "why": why, "released_in": None, "release_why": None})
    return out


def active(ledger):
    return [c for c in ledger.get("constraints", []) if not c.get("released_in")]


def violations(ledger, snap):
    nodes, out = snap.get("nodes", {}), []
    for c in active(ledger):
        node = nodes.get(c["node"])
        if c["property"] == "exists":
            if (node is not None) != c["value"]:
                out.append({"constraint": c["id"], "node": c["node"], "name": c["name"],
                            "expected": "present" if c["value"] else "absent",
                            "found": "present" if node is not None else "absent"})
            continue
        if node is None:
            out.append({"constraint": c["id"], "node": c["node"], "name": c["name"],
                        "expected": c["value"], "found": "node removed"})
            continue
        found = _value(node, PROPERTY_FIELDS[c["property"]])
        kind = {"position": "moved", "size": "resized"}.get(c["property"], c["property"])
        if _differs(kind, c["value"], found):
            out.append({"constraint": c["id"], "node": c["node"], "name": c["name"],
                        "property": c["property"], "expected": c["value"], "found": found})
    return out


# --- validation (a small subset of JSON Schema: type, required, properties, items, enum) -----

def _check(value, schema, path, errors):
    t = schema.get("type")
    if t:
        types = t if isinstance(t, list) else [t]
        ok = {
            "object": isinstance(value, dict), "array": isinstance(value, list),
            "string": isinstance(value, str), "boolean": isinstance(value, bool), "null": value is None,
            "integer": isinstance(value, int) and not isinstance(value, bool),
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        }
        if not any(ok.get(x, True) for x in types):
            errors.append(f"{path}: expected {t}")
            return
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in {schema['enum']}")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing '{key}'")
        for key, sub in schema.get("properties", {}).items():
            if key in value:
                _check(value[key], sub, f"{path}.{key}", errors)
    if isinstance(value, list) and "items" in schema:
        for i, item in enumerate(value):
            _check(item, schema["items"], f"{path}[{i}]", errors)


def validate(ledger):
    errors = []
    _check(ledger, load(os.path.join(HERE, "schema.json")), "$", errors)
    for r in ledger.get("rounds", []) if isinstance(ledger.get("rounds"), list) else []:
        if r.get("actor") == "human" and not (r.get("why") or "").strip():
            errors.append(f"$.rounds[{r.get('id')}]: a human round needs the human's 'why'")
    return errors


# --- commands -------------------------------------------------------------------

def cmd_init(a):
    if os.path.exists(a.ledger):
        sys.exit(f"{a.ledger} already exists; not overwriting it")
    save(a.ledger, {"schema": SCHEMA_ID, "project": a.project, "lesson": a.lesson, "file_ref": a.file_ref,
                    "created_at": now(), "rounds": [], "constraints": []})
    print(f"wrote {a.ledger}")


def cmd_diff(a):
    changes = diff(load(a.a), load(a.b))
    if a.json:
        print(json.dumps(changes, indent=2, ensure_ascii=False))
    else:
        print("\n".join(describe(c) for c in changes) or "no changes")


def parse_checks(items):
    out = []
    for item in items or []:
        name, _, result = item.partition("=")
        if result not in ("pass", "fail", "not-run"):
            sys.exit(f"--check {item!r}: result must be pass, fail or not-run")
        out.append({"name": name, "result": result})
    return out


def cmd_record(a):
    ledger = load(a.ledger)
    base = os.path.dirname(os.path.abspath(a.ledger))
    rounds = ledger["rounds"]
    rid = f"r{len(rounds) + 1}"
    snap = load(os.path.join(base, a.snapshot) if not os.path.isabs(a.snapshot) else a.snapshot)
    prev = rounds[-1]["snapshot"] if rounds else None
    changes = diff(load(os.path.join(base, prev)), snap) if prev else []

    if a.actor == "human" and not (a.why or "").strip():
        sys.exit("a human round needs --why: ask the human for one line on why they made the change")

    found = violations(ledger, snap) if a.actor == "agent" else []
    if found and not (a.override_why or "").strip():
        for v in found:
            print(f"VIOLATION {v['constraint']}: {v['name']} ({v['node']}) expected {json.dumps(v['expected'])}, "
                  f"found {json.dumps(v['found'])}", file=sys.stderr)
        sys.exit(2)  # the agent undid a human correction: stop and ask before recording

    released = [x for x in (a.release or "").split(",") if x]
    for c in ledger["constraints"]:
        if c["id"] in released:
            if not (a.why or "").strip():
                sys.exit("releasing a constraint needs --why in the human's words")
            c["released_in"], c["release_why"] = rid, a.why

    added = []
    if a.actor == "human" and not a.free:
        added = constraints_from(changes, rid, a.why, len(ledger["constraints"]))
        ledger["constraints"] += added

    rounds.append({
        "id": rid, "actor": a.actor, "at": now(), "chapter": a.chapter, "intent": a.intent,
        "prompt": a.prompt, "script": a.script, "snapshot": a.snapshot, "screenshot": a.screenshot,
        "diff": changes, "why": a.why, "constraints_added": [c["id"] for c in added],
        "constraints_released": released, "violations_overridden": found, "override_why": a.override_why,
        "checks": parse_checks(a.check), "calls_used": a.calls,
    })
    errors = validate(ledger)
    if errors:
        sys.exit("ledger would be invalid:\n  " + "\n  ".join(errors))
    save(a.ledger, ledger)
    print(f"recorded {rid} ({a.actor}): {len(changes)} change(s), {len(added)} constraint(s) added, "
          f"{len(active(ledger))} active")


def cmd_check(a):
    found = violations(load(a.ledger), load(a.snapshot))
    for v in found:
        print(f"VIOLATION {v['constraint']}: {v['name']} ({v['node']}) expected {json.dumps(v['expected'])}, "
              f"found {json.dumps(v['found'])}")
    if not found:
        print("ok: no human correction was undone")
    sys.exit(1 if found else 0)


def cmd_log(a):
    ledger = load(a.ledger)
    cell = lambda s: str(s if s is not None else "").replace("|", "\\|").replace("\n", " ")
    print(f"# Provenance: {cell(ledger['project'])}\n")
    print(f"Lesson: {cell(ledger['lesson'])}. {len(ledger['rounds'])} rounds, "
          f"{len(active(ledger))} active constraints.\n")
    print("| Round | Who | When (UTC) | Intent | Changes | Why | Constraints | Checks | Calls |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in ledger["rounds"]:
        cons = " ".join([f"+{c}" for c in r["constraints_added"]] + [f"−{c}" for c in r["constraints_released"]])
        checks = ", ".join(f"{c['name']}: {c['result']}" for c in r["checks"])
        print(f"| {r['id']} | {r['actor']} | {cell(r['at'])} | {cell(r['intent'])} | {len(r['diff'])} | "
              f"{cell(r['why'])} | {cons} | {cell(checks)} | {cell(r['calls_used'])} |")


def cmd_stamp(a):
    ledger = load(a.ledger)
    if not ledger["rounds"]:
        sys.exit("no rounds yet")
    r = next((x for x in ledger["rounds"] if x["id"] == a.round), None) if a.round else ledger["rounds"][-1]
    if not r:
        sys.exit(f"no round {a.round}")
    print(f"{STAMP_PREFIX} {r['id']} · {r['actor']} · {r['at'][:10]} · "
          f"{len(active(ledger))} human corrections held · ledger {os.path.basename(a.ledger)}#{r['id']}")


def cmd_validate(a):
    errors = validate(load(a.ledger))
    print("\n".join(errors) or "valid")
    sys.exit(1 if errors else 0)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    def with_ledger(p):
        p.add_argument("--ledger", default="provenance.json")
        return p

    p = with_ledger(sub.add_parser("init"))
    p.add_argument("--project", required=True)
    p.add_argument("--lesson", required=True)
    p.add_argument("--file-ref", required=True, help="a local name for the Figma file, never its key")
    p.set_defaults(fn=cmd_init)

    p = sub.add_parser("diff")
    p.add_argument("a")
    p.add_argument("b")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_diff)

    p = with_ledger(sub.add_parser("record"))
    p.add_argument("--actor", choices=["agent", "human"], required=True)
    p.add_argument("--snapshot", required=True)
    p.add_argument("--intent", required=True)
    p.add_argument("--why")
    p.add_argument("--prompt")
    p.add_argument("--script")
    p.add_argument("--screenshot")
    p.add_argument("--chapter", type=int)
    p.add_argument("--calls", type=int)
    p.add_argument("--check", action="append")
    p.add_argument("--free", action="store_true", help="human edits that should not become constraints")
    p.add_argument("--release", help="comma-separated constraint ids the human is letting go")
    p.add_argument("--override-why", help="the human's words approving an agent round that undid a correction")
    p.set_defaults(fn=cmd_record)

    p = with_ledger(sub.add_parser("check-constraints"))
    p.add_argument("snapshot")
    p.set_defaults(fn=cmd_check)

    p = with_ledger(sub.add_parser("log"))
    p.set_defaults(fn=cmd_log)

    p = with_ledger(sub.add_parser("stamp-text"))
    p.add_argument("--round")
    p.set_defaults(fn=cmd_stamp)

    p = with_ledger(sub.add_parser("validate"))
    p.set_defaults(fn=cmd_validate)

    a = ap.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
