# STATUS.md — Build State & Gate Sign-offs

**Book:** Agentic Learning Experience Design with Figma
**Current phase:** 0 — BLUEPRINT
**Last updated:** (set on each change)

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
