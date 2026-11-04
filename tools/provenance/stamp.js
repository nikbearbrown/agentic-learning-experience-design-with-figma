// stamp.js: write (or replace) the one provenance annotation on each frame being worked on.
//
// STATUS: UNTESTED against a live Figma file. The write pattern, `node.annotations = [{label}]`,
// read back correctly through use_figma on 2026-09-27 (FEA youtube/ai-explainer-component-intent/
// evidence/EXPERIMENT.md). Annotations on a component set were dropped and FigJam refuses them
// (FEA CAPABILITIES.md), so stamp frames only. First live run: Chapter 2's RUN slot.
//
// Define above this file, using the text from `prov.py stamp-text`:
//   const OPTS = {frameIds: ["12:34"], label: "Provenance · r3 · human · …"};
// Every other annotation on the frame (review notes, rules) is kept as it was.

const PREFIX = "Provenance ·";
const _opts = typeof OPTS !== "undefined" ? OPTS : {};
if (!_opts.label || !_opts.label.startsWith(PREFIX)) throw new Error("OPTS.label must start with '" + PREFIX + "'");

const keep = (a) => {
  // Pass back exactly one of label / labelMarkdown, as the API expects.
  const out = a.labelMarkdown ? { labelMarkdown: a.labelMarkdown } : { label: a.label || "" };
  if (a.categoryId) out.categoryId = a.categoryId;
  if (a.properties && a.properties.length) out.properties = a.properties;
  return out;
};

const results = [];
for (const id of _opts.frameIds || []) {
  const node = await figma.getNodeByIdAsync(id);
  if (!node || node.type !== "FRAME") {
    results.push({ id, stamped: false, reason: node ? "not a frame: " + node.type : "not found" });
    continue;
  }
  const others = (node.annotations || [])
    .filter((a) => !((a.label || a.labelMarkdown || "").startsWith(PREFIX)))
    .map(keep);
  node.annotations = [...others, { label: _opts.label }];
  results.push({ id, stamped: true, annotations: node.annotations.map((a) => a.label || a.labelMarkdown) });
}
return results;
