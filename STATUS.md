# STATUS.md — Build State & Gate Sign-offs

**Book:** Agentic Learning Experience Design with Figma
**Current phase:** 0 — BLUEPRINT (GATE 0 unsigned). Chapters rough-drafted early; see the note below.
**Last updated:** 2026-11-03

> **Note, 2026-11-03.**
> - The author approved the 15-chapter outline in chat and asked for a hands-on rough draft of every chapter. Drafting ran **ahead of GATE 0 and GATE 1** at the author's direction.
> - Every chapter carries a "Rough draft — pre-research" banner. Figma facts come from `../figma-for-educational-ai` and are tagged `[VERIFY]`. Every agent output and learner result is a RUN slot, because nothing has been run against Figma yet.
> - No gate below has been signed. Only the author signs gates.

## Whole-Book Rough-Draft Pass, 2026-11-03

The author explicitly authorized: "write every chapter" and "You don't need my
approval for a rough draft," reserving editorial feedback until after reading.
This authorization applies to rough-manuscript drafting only, not research
verification, human rewrite, learner participation, publication, or gate signatures.

- All 15 numbered chapter files now exist, plus front matter and Appendices A-E.
- Chapters 1 and 12 were preserved without text changes. The other 13 numbered
  chapters and the front/back matter were added in this pass.
- Every chapter has an unsigned `rough_draft` verification sidecar. No sign-off
  was invented and no `verified: true` field was set.
- Reading copies: `output/rough-draft.html`, `output/rough-draft.epub`, and
  `output/rough-draft.md`. Editable sources remain in `chapters/`.
- `DRAFT-REVIEW.md` separates editorial decisions from research/live-run work.
- No live Figma session, learner study, measured tool budget, generated figure,
  or production integration was performed as part of writing this manuscript.

The formal current phase remains Blueprint, with all existing gates unsigned.

The agent reads this file before every phase. A phase may begin only when the
**previous** phase's gate below is checked **and** initialed by a human (or, for
non-human-only gates, confirmed by the agent with evidence linked).

> Marking a gate: replace `[ ]` with `[x]`, add who signed and the date, and link
> the evidence (a file path, a command's output, a commit). GATE 3 must be signed
> by a human.

---

## Spine

- [ ] **GATE 0 — TOC approved**
  - All `[NEEDS HUMAN INPUT]` resolved in vision/architecture/chapters-spec/risks; outline reflects thesis.
  - Signed: ______  Date: ______  Evidence: ______

- [ ] **GATE 1 — Sources solid**
  - Every chapter has `research/<slug>.md`; key claims sourced; no dead/hallucinated links.
  - Signed: ______  Date: ______  Evidence: ______

- [ ] **GATE 2 — Full draft exists**
  - Every outlined chapter drafted from research and meets its spec.
  - Signed: ______  Date: ______  Evidence: ______

- [ ] **GATE 3 — Author sign-off  (HUMAN ONLY)**
  - Human has read and rewritten every chapter into their own voice.
  - Signed (human): ______  Date: ______

- [ ] **GATE 4 — Claims verified**
  - Fact-check report complete; corrections applied; citations resolve.
  - Signed: ______  Date: ______  Evidence: ______

- [ ] **GATE 5 — Figures exist**
  - Every figure in the text exists as SVG + PNG (+ D3 where interactive) and renders.
  - Signed: ______  Date: ______  Evidence: ______

- [ ] **GATE 6 — Figure audit passes**
  - `DRY_RUN=1 node scripts/svg-visual-audit.mjs` → 0 flagged (or accepted exceptions listed).
  - Signed: ______  Date: ______  Evidence: ______

**→ When all spine gates are signed, the spine is complete.**

---

## Optional editions (post-spine)

Check off the ones chosen; see `conductor/editions/README.md`.

- [ ] Chapter Quizzes & Checks for Understanding
- [ ] Practice Exercises
- [ ] Worked Exercises & Solutions
- [ ] Key Terms & Definitions
- [ ] Flashcards / Anki Deck
- [ ] Further Reading Guide
- [ ] Interactive Quantum Simulations
- [ ] Browser-Based D3 Simulations
- [ ] Command-Line Lab Companion
- [ ] Command-Line Quick Reference
- [ ] LLM Learning Companion

### Voices (rewritten copies of `chapters/` → `voices/<voice>/`)
- [ ] Wonder voice
- [ ] Generic voice (OpenStax register)
- [ ] Socratic voice
- [ ] Sardonic voice (Griffiths register)
- [ ] Narrative voice (historical)
- [ ] Pragmatist voice (engineering)
- [ ] Teardown voice (design-critic; adds `/essay` `/nart` `/write` `/bookmap` + the `/done` finishing pass)
