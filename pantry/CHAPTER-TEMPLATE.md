# Chapter template: rough draft, pre-research

Every chapter in `chapters/` follows this shape. `chapters/01-the-screen-that-teaches-nothing.md` is the model. Target: 3,000–4,000 words.

```markdown
# Chapter N — Title
*Italic subtitle that compresses the chapter's tension.*

> **Rough draft — pre-research.** Figma facts here come from the sibling repo
> `../figma-for-educational-ai` and are tagged [VERIFY] until Phase 1 re-checks them.
> Every agent output is a RUN slot, to be filled with a real run. Nothing below is a recorded result unless it says so.

## The concept
What this chapter teaches, in two halves:
- the learning-design principle (cite the LXD book chapter, or *AI for LXD*, by file)
- the Figma idea that carries it (components, variables, annotations…)
Teardown register: explain the machinery, name what the default optimizes for, name the trade-off.
About 900–1,300 words. Nik Bear Brown in the first person.

## What you'll be able to do
- 3–4 objectives with action verbs (never "understand")
- **Plan:** all | HE · **MCP budget:** estimate ~N calls (to be measured) · **Builds on:** Ch X

## Talking to Figma
The loop from PROVENANCE.md, applied to this chapter's build. 1,200–1,700 words.

### Round 1: the agent draws
The exact prompt, in a fenced block. What the agent should do (tools, in order). Then:

> **RUN SLOT r1.** Paste: the agent's reply, the script path (`provenance/scripts/r1.js`),
> the screenshot, the `prov.py record` output. *What to look for:* …

### Your turn in Figma
What you check, with the chapter's check list, and what to change by hand. What to tell the agent: "done", then your one-line why.

> **RUN SLOT r2.** Paste: the `prov.py diff` output, your why, the constraints it created.

### Round 3: the agent redraws
The follow-up prompt. It must reference the active constraints. The check-constraints step. Then:

> **RUN SLOT r3.** …

(More rounds if the chapter needs them. Stop when the chapter's check passes.)

## The provenance this chapter adds
A short JSON fragment of the ledger rounds this chapter produces, with RUN placeholders for real values. Say what the record lets you answer later.

## The check
- **The machine half:** what a script or check-constraints can verify.
- **The human half:** what only you, or a learner, can judge.
- What neither can see.

## Exercises
**Warm-up** (2–3) · **Application** (3–4) · **Synthesis** (2–3) · **Challenge** (1–2). Each names the objective it tests. No solutions inline.

## What you can now do
Capabilities, not topics.

## Credit the AI
What the agent did, what it got wrong (RUN-dependent: say "fill from r1–rN"), and how you check it.

## Next
One paragraph bridging to the next chapter.
```

## Rules

- **No fabrication.** Never write what the agent "returned" or "did" as fact. Use RUN slots. Prompts, checklists, tool sequences and expectations ("the agent *should*…") are fine. Hypotheses are labeled as hypotheses.
- **Figma facts** cite their FEA source (file, and date where given) and carry `[VERIFY]`. Never describe a Figma feature from memory. Tool names must be in FEA's saved tool list.
- **Teardown voice** (`voices/teardown/VOICE.md`). Forbidden: "One could argue", "It seems as though", "The UX could be improved", "innovative", "revolutionary", "premium", "sleek", "obviously", "clearly". Use: "Here's what's actually happening…", "They optimized for X at the expense of Y", "The interesting trade-off is…".
- **The running lesson** is a practice unit for *Experience Design for EdTech* Ch 3, "The Cognitive Machinery" (`../learning-experience-design-lxd/chapters/03-the-cognitive-machinery-load-difficulty-and-durable-learning.md`). It covers working memory; intrinsic, extraneous and germane load; the worked-example effect and expertise reversal; retrieval vs restudy; spacing; interleaving; and the four-question friction diagnostic.
- **Visual suggestions** go inline as `<!-- → [IMAGE|TABLE|INFOGRAPHIC|CHART: specific content] -->`.
- **Plan tags:** **all** (any Education account, including K-12, since the MCP server runs on Claude's side) or **HE** (Figma AI, Make, Sites).
- No learner names, emails, file keys or account IDs.
