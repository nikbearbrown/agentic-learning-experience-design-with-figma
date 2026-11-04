// snapshot.js: Figma Plugin API -> "alxd-snapshot/0.1" JSON of the frames being worked on.
//
// STATUS: UNTESTED against a live Figma file. Written against the Plugin API patterns that
// ../figma-to-godot/exporter/export.js ran successfully on 2026-10-20 (*Async variable
// lookups, try/catch around reads use_figma may reject). Its first live run is Chapter 2's
// RUN slot; record the result there and update this line.
//
// Run it through the Figma MCP server: load the figma-use skill, then pass this file's body
// to `use_figma`. Define `const OPTS = {frameIds: ["12:34", ...]}` above it to pick frames;
// without OPTS it snapshots the current selection, or every top-level frame on the page.
// The agent saves the returned JSON to provenance/snapshots/<round>.json, then runs
// `python3 tools/provenance/prov.py diff` against the previous round.
//
// It reads only. It never writes to the file, so it is safe to run at any point in a round.

const SCHEMA = "alxd-snapshot/0.1";
const _opts = typeof OPTS !== "undefined" ? OPTS : {};

const hex = (c, a = 1) => {
  const h = (v) => Math.round(v * 255).toString(16).padStart(2, "0").toUpperCase();
  return "#" + h(c.r) + h(c.g) + h(c.b) + (a < 1 ? h(a) : "");
};
const round1 = (n) => (typeof n === "number" ? Math.round(n * 10) / 10 : null);
const safe = (fn, fallback = null) => {
  try { return fn(); } catch (e) { return fallback; }
};

async function varName(id) {
  if (!id) return null;
  const v = await figma.variables.getVariableByIdAsync(id);
  return v ? v.name : null;
}

async function fillsOf(node) {
  const paints = safe(() => node.fills, []);
  if (!Array.isArray(paints)) return [];             // figma.mixed on mixed-style text
  const out = [];
  for (const p of paints) {
    if (p.visible === false) continue;
    if (p.type === "SOLID") {
      const bound = p.boundVariables && p.boundVariables.color;
      out.push({ color: hex(p.color, p.opacity ?? 1), var: bound ? await varName(bound.id) : null });
    } else {
      out.push({ type: p.type });
    }
  }
  return out;
}

async function componentOf(node) {
  if (node.type !== "INSTANCE") return null;
  const main = await node.getMainComponentAsync();
  if (!main) return null;
  const set = main.parent && main.parent.type === "COMPONENT_SET" ? main.parent.name : null;
  return { main: main.name, set };
}

function propsOf(node) {
  const p = safe(() => node.componentProperties, null);
  if (!p) return null;
  const out = {};
  for (const [k, v] of Object.entries(p)) out[k.split("#")[0]] = v.value;
  return out;
}

async function snap(node, parentId, nodes) {
  nodes[node.id] = {
    id: node.id,
    name: node.name,
    type: node.type,
    parent: parentId,
    x: round1(safe(() => node.x)),
    y: round1(safe(() => node.y)),
    w: round1(safe(() => node.width)),
    h: round1(safe(() => node.height)),
    visible: safe(() => node.visible, true),
    text: node.type === "TEXT" ? node.characters : null,
    fills: await fillsOf(node),
    component: await componentOf(node),
    props: propsOf(node),
    layout: safe(() => node.layoutMode, null) || null,
    annotations: safe(() => (node.annotations || []).map((a) => a.label || a.labelMarkdown || ""), []),
  };
  if ("children" in node && node.type !== "INSTANCE") {
    for (const child of node.children) await snap(child, node.id, nodes);
  }
}

async function snapshot() {
  let roots;
  if (_opts.frameIds && _opts.frameIds.length) {
    roots = [];
    for (const id of _opts.frameIds) {
      const n = await figma.getNodeByIdAsync(id);
      if (n) roots.push(n);
    }
  } else if (figma.currentPage.selection.length) {
    roots = figma.currentPage.selection.slice();
  } else {
    roots = figma.currentPage.children.filter((n) => n.type === "FRAME");
  }
  const nodes = {};
  for (const r of roots) await snap(r, null, nodes);
  return {
    schema: SCHEMA,
    taken_at: new Date().toISOString(),
    page: figma.currentPage.name,
    roots: roots.map((r) => r.id),
    nodes,
  };
}

return await snapshot();
