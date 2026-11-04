# PROVENANCE.md: the draw → correct → redraw loop, and its record

## Executive summary

**What this is.** This is the working method every chapter of this book uses, plus the record it keeps. The agent draws in Figma through the MCP server. You correct the drawing in Figma with your own hands. The agent reads what you changed, asks you why, and redraws without undoing your corrections. Every round goes into `provenance.json`.

**Why it needs its own file.** Figma can't keep this record by itself.
- Through the MCP server, an agent can't name a version or write a comment. `saveVersionHistoryAsync` and `devStatus` return "is not a supported API", and the server has no comment tool. Source: FEA `CAPABILITIES.md`, checked 2026-09-27. `[VERIFY]`
- `use_figma` forbids `setPluginData`, so the agent can't hide a record inside the layers (F2G `exporter/export.js`). `[VERIFY]`
- Figma's version history credits every agent edit to the signed-in human (FEA `examples/frictional-version-log/figma_version_log.py`). In Figma's own history you and the agent are the same person. `[VERIFY]`

So the record of truth is a JSON file in your project. Figma holds one pointer to it: a single annotation on each frame naming the current round.

**What's tested.**
- `tools/provenance/prov.py` passes its 10 local tests (`python3 -I tools/provenance/test_prov.py`).
- `snapshot.js` and `stamp.js` have **not** been run against a live file yet. Their first run is Chapter 2's RUN slot.

---

## The loop

One **round** is one actor's turn. Rounds alternate, but nothing forces it: two agent rounds in a row is fine, and so is two human rounds.

```
 ┌──────────────── agent round ────────────────┐   ┌──────── human round ────────┐
 whoami → draw (use_figma) → snapshot → check     you edit in Figma → "done"
        → stamp → screenshot → record rN           → snapshot → diff → "why?"
                                                   → record rN+1 (constraints)
 └──────────────────────────────────────────────┘   └─────────────────────────────┘
                     ↑                                          │
                     └──────── redraw under constraints ────────┘
```

### Agent round

1. **`whoami`, first thing in every session.** This confirms which team and seat the agent is acting as (ACD rule). Education shows up as "Student tier", even for a verified educator (FEA `CAPABILITIES.md`). `[VERIFY]`
2. **Draw.** The agent writes a `use_figma` script, saves it to `provenance/scripts/rN.js`, and runs it.
3. **Snapshot.** The agent runs `tools/provenance/snapshot.js` through `use_figma` on the frames it touched and saves the result to `provenance/snapshots/rN.json`.
4. **Check constraints.** `python3 tools/provenance/prov.py check-constraints provenance/snapshots/rN.json`. If this prints a VIOLATION, the agent has undone one of your corrections, so it **stops and asks you**. You either tell it to put your correction back, or let the correction go (`--release`) in your own words.
5. **Stamp.** `prov.py stamp-text` prints the annotation text, and `stamp.js` writes it onto each frame. It replaces only the earlier `Provenance ·` note and keeps every other annotation.
6. **Screenshot.** `get_screenshot` on the frame, so you and the agent see the same thing.
7. **Record.**
   ```
   prov.py record --actor agent --snapshot provenance/snapshots/rN.json --intent "…" \
       --prompt "…" --script provenance/scripts/rN.js --chapter C --calls K --check name=pass|fail|not-run
   ```
   The agent then tells you, in one short message, what it drew, which checks passed, failed or did not run, and what it wants you to look at.

### Human round

1. **You edit in Figma.** Move things, rewrite text, hide layers, swap a variant: whatever the screen needs. Then tell the agent "done".
2. **Snapshot.** The agent snapshots the same frames to `provenance/snapshots/rN+1.json`.
3. **Diff.** `prov.py diff` shows every change you made. The agent reads them back to you in plain words.
4. **Why.** The agent asks for **one line on why**, and records your words exactly. It never writes the why for you. A round without a why is refused (`prov.py` exits with an error).
5. **Record.**
   ```
   prov.py record --actor human --snapshot provenance/snapshots/rN+1.json --intent "…" --why "your words"
   ```
   Each change becomes a **constraint**: a fact about the screen the agent must keep. Add `--free` if you were only exploring and don't want your edits held. Add `--release c3` to let an earlier constraint go.

### The hard rule

**The agent never undoes a human correction without asking.** The ledger enforces this. An agent round that breaks a constraint can't be recorded (exit code 2) until the agent puts the correction back, or until you approve the change in your own words (`--override-why`). Both outcomes are kept in the ledger.

---

## Files

```
provenance.json                 the ledger: rounds and constraints (schema: tools/provenance/schema.json)
provenance/scripts/rN.js        the exact use_figma script each agent round ran
provenance/snapshots/rN.json    snapshot.js output at the end of each round
provenance/screenshots/rN.png   optional: only if your setup can save get_screenshot images [VERIFY]
```

- **No file keys in the ledger.** `file_ref` is a local name. Keep the mapping to the real key outside the repo, the same way FEA's review tool keeps its keys.
- **No learner names, emails or account IDs**, anywhere (FEA rule 6).

## What a round costs

**Planning estimate, to be measured in Chapter 2:**
- an agent round is about 4 MCP calls: draw, snapshot, stamp, screenshot
- a human round is 1 call: the snapshot

Folding the stamp into the draw script saves a call. On Education the server allows 200 calls a day and 10 a minute (FEA `CAPABILITIES.md`, 2026-09-26) `[VERIFY]`. Five correction cycles on one screen is therefore about 25 calls, roughly an eighth of a day. Every chapter states the budget it was measured at.

## What the record is for

- **For you:** a design history with reasons. "Why is the hint button there?" has an answer: round 4, your words.
- **For the next agent:** active constraints are rules it reads before drawing. They're a rules file that writes itself (Chapter 12).
- **For a course:** process evidence. An instructor can grade the corrections and the reasons, not only the final screen. FEA's `figma_version_log.py` does the same job from Figma's own history, but it can't tell agent from human, and this ledger can.

## Commands

```
python3 tools/provenance/prov.py init --project NAME --lesson "…" --file-ref LOCALNAME
python3 tools/provenance/prov.py diff A.json B.json
python3 tools/provenance/prov.py record …              # see above
python3 tools/provenance/prov.py check-constraints S.json
python3 tools/provenance/prov.py log                   # Markdown history for your portfolio
python3 tools/provenance/prov.py stamp-text            # the annotation text for stamp.js
python3 tools/provenance/prov.py validate
```

Following AI+1 rule P5, **the agent runs these**. You talk; it types.
