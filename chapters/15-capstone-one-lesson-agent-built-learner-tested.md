# Chapter 15 - Capstone: One Lesson, Agent-Built, Learner-Tested
*The final artifact is the lesson and the argument for why it has this shape.*

> **Rough draft - pre-research.** This chapter is a project brief and assessment framework, not a completed capstone. All baseline, build, learner-test, cost, and comparison values remain RUN. Figma capabilities and platform access require current checks `[VERIFY]`. No human approval, participant result, or learning gain is implied by the rubric.

## The concept

At the beginning of the book, we asked an agent for a practice quiz and inspected what arrived. We did not assume it failed, and we did not assume a good-looking result taught anything. The capstone returns to that discipline with a richer set of tools and a lesson you care about.

Your task is to redesign one bounded learning experience. Not an entire course. Not a dashboard with no lesson behind it. One experience with an objective, a learner context, evidence, support, a working state contract, and a delivery plan.

The final portfolio should let another person answer four questions. What must the learner do? How does the interface preserve that work? What evidence was actually collected? What remains unknown? If the portfolio cannot answer them, more screens will not make it complete.

### Keep the Lesson Small Enough to Be Honest

Use the lesson charter from Chapter 4 as a starting point. Revisit it rather than treating it as permanent. The chapters may have exposed an objective that was too broad, an interaction that could not collect the evidence, or a platform constraint that changes the feasible scope.

A good capstone can have one central performance and a handful of reviewed items. The point is not content volume. It is a complete reasoning chain from objective through implementation and observation. An incomplete small project can be described honestly; a sprawling project often hides incompleteness behind quantity.

State the intended learners, relevant prior knowledge, setting, access assumptions, and known exclusions. Do not invent a detailed persona to make the charter feel researched. If prior knowledge is unknown, flag it and decide how the design will handle the uncertainty.

### Choose the Baseline Before the Redesign

There are two comparisons to keep separate. Chapter 1's demonstration baseline shows the book's running lesson before its later rules. Your personal capstone should also have its own baseline if you want to claim improvement on that lesson.

Do not compare a weak demonstration screen with a different, easier capstone task and call the difference a measured gain. Keep task, model/client configuration where relevant, input context, and scoring method documented. If conditions change, report the change. You can still make a useful design comparison without claiming a controlled experiment.

Score the baseline before repairing it. Keep the five checks from Chapter 1 as a continuity measure, then add the richer checks learned later. The original five are not a complete learning-quality instrument. In particular, its keyboard check concerns design intent, while runtime access needs separate evidence.

If the baseline already passes all five, do not weaken it for narrative drama. The capstone can test repeatability, fresh-session transfer, a new item type, or preservation through handoff. The book's narrower thesis is valuable: making a good result reproducible under explicit constraints.

### The Portfolio Is a Chain of Evidence

Organize it so a reader can follow the project:

| Artifact | Question it answers |
|---|---|
| Lesson charter | What performance, for whom, under what conditions? |
| Baseline record | What happened before the explicit design system? |
| Objective/evidence/screen map | Why does each interaction exist? |
| Component and support contracts | What must remain invariant across items? |
| Scripts, snapshots, screenshots, ledger | What actually changed, by whom, and why? |
| Rules file and independent review | Can a fresh agent recover and check the contract? |
| Learner-test report or pending protocol | What human evidence exists, and what does not? |
| Handoff and acceptance slice | What survived in the delivery route? |
| Reflection and limits | Which claims are earned and which remain hypotheses? |

The privacy boundary applies to the whole portfolio. A tidy ledger does not excuse publishing an account key in a screenshot or an identifying learner quote in a reflection. Review the complete package before sharing.

### A Rubric for the Project, Not a Promise of Learning

Use a descriptive rubric with four levels: missing, specified, implemented, and evidenced. These are project states, not numeric claims about learning. A specification can be excellent and still unimplemented. An implementation can work and still lack learner evidence.

Assess the following dimensions separately:

| Dimension | Evidence sought |
|---|---|
| Alignment | Objective, performance, and evidence agree; loopholes considered |
| Learning interaction | Answer boundary, feedback, support, and retry are explicit |
| Reusable system | Rules travel through actual read paths and a fresh-session test |
| Access | Design contract and appropriately scoped runtime tests |
| Evidence integrity | Assistance, exposure, missingness, versions, and limits preserved |
| Learner inquiry | Appropriate permissions, actual observations, bounded interpretation |
| Delivery | Tested slice or explicit unimplemented requirements |
| Authorship and provenance | Human corrections and reasons remain traceable |

Do not average the dimensions into a number that conceals a critical failure. A beautiful library does not compensate for fabricated learner data. A passed layout audit does not compensate for a premature answer reveal. Record any nonnegotiable release blocker separately.

<!-- [TABLE: capstone evidence matrix with missing/specified/implemented/evidenced columns; show that strong specification and absent live evidence can coexist] -->

### Budget the Iterations You Actually Need

Use your earlier request logs to estimate a bounded sequence of sessions. Include inspection, drawing, human correction, read-back, independent review, and failures. Do not multiply the book's planning ceilings and call the result an observed project cost.

Decide in advance what triggers a scope review. Repeated inability to preserve a critical state, unavailable platform access, a content ambiguity, or missing learner participation may require a different plan. The agent should not keep producing screens to look busy while the evidence chain remains blocked.

A good stopping rule concerns the objective and acceptance criteria. "All essential states are specified, implemented where required, and checked within the declared scope" is a useful boundary. "The agent has used the whole daily allowance" is not. When a test cannot run, record the dependency and move the project to an honest pending state.

### Write a Failure Account Worth Reading

Select two or three consequential moments from the ledger. For each, show the original requirement, the observed failure or uncertainty, your correction and reason, the agent's next action, and the result of the relevant check. The account should explain a decision, not merely display process screenshots.

Include a null result when it matters. Perhaps a rules file added no visible benefit beyond component descriptions under the tested conditions. Perhaps a fresh agent asked the right question before drawing. Perhaps the original screen passed all five baseline checks. Those outcomes refine the thesis; they are not editorial problems to hide.

Do not reconstruct a clean conversation from memory. Use the saved prompts and responses, with private details removed appropriately. If a record is missing, say so. The credibility of the capstone depends on distinguishing what happened from what would have been a nice demonstration.

### The Author's Review Is Not Another Agent Pass

At the end, read the experience as the person responsible for its learning claim. Does the task still match the objective you wanted? Has production convenience narrowed the performance without your noticing? Are the reasons in the rules file still yours, or have they become generic slogans the agent can satisfy without understanding their scope?

This is the point of the human role in the AI+1 method. The agent can gather artifacts, identify contradictions, and propose a report. It cannot decide what the book or lesson should ultimately stand for on the author's behalf. Human review is not a final checkbox added after automatic production. It is the judgment that gives the production a direction.

Your final reflection should therefore include one decision you would keep, one you would revisit, and one uncertainty you will not disguise as a finding. That is a stronger conclusion than a universal claim about AI-assisted design. It gives the next iteration somewhere real to begin.

When you present the capstone, begin with the performance, show one consequential correction, and state one evidence limit before opening the polished prototype. That order keeps the audience from judging the entire project by its first attractive screen. It also makes the human contribution visible: not simply approving what the agent produced, but deciding what the experience must preserve and what the available evidence permits you to claim.

## What you'll be able to do

- **Complete** an objective-to-handoff design chain for one bounded lesson.
- **Direct and correct** an agent while preserving the reasons behind human changes.
- **Compare** baseline and final work without changing the scoring rules afterward.
- **Defend** the project's claims and limits using actual artifacts and observations.

**Plan:** all for the core design route; optional routes depend on current access. **MCP budget:** define a project ceiling from observed chapter costs before running; actual RUN. **Builds on:** the whole book. **Human dependencies:** author decisions and any authorized learner participation.

## Talking to Figma

### Stage 1: The Agent Audits the Charter

```text
Read my lesson charter and objective map. Identify scope, evidence, content,
access, and delivery uncertainties. Do not silently resolve author decisions.
Propose the smallest complete capstone that preserves the target performance.
List required artifacts and a session budget based on actual earlier records,
not this draft's planning ceilings. Do not begin a large build yet.
```

Choose the scope and record your decision. Authorization to draft the book is not authorization for an agent to recruit learners, publish a product, or change an institutional course. Keep those boundaries explicit in the project brief.

> **RUN SLOT 15.1.** Save charter revision, scope decision, unresolved assumptions, planned budget, and actual authorization boundaries.

### Stage 2: Capture the Personal Baseline

Use the thin Chapter 1 request on your lesson with the documented initial context. Save the exact prompt and available tool/configuration information. Do not feed the final rules into the baseline and then describe it as unguided.

```text
Build the bounded baseline practice experience from the supplied lesson content.
Use only the stated initial context. Save exact prompts, scripts, responses,
snapshots, and screenshots. Do not repair it before the human scores it.
Do not invent outcomes if the build cannot run.
```

Score independently before reading the agent's self-evaluation. A disagreement is useful data about the rubric or the agent's inspection, not an inconvenience to remove. Preserve both verdicts with their evidence.

> **RUN SLOT 15.2.** Save the personal baseline, human and agent scores, discrepancies, and untestable checks. If there is no live baseline, the project cannot claim a measured before/after design improvement.

### Stage 3: Build Through Human Corrections

Apply the relevant chapters in dependency order: objective map, support, item contracts, feedback, review flow if needed, load, access, and evidence views. Not every lesson needs a persistent scheduler or instructor dashboard. An omitted feature is acceptable if the objective and delivery context do not require it. Record the reason rather than adding features to complete a checklist.

At each round, inspect the actual result, make or approve the human correction, and supply the reason. Keep reasons specific enough to guide later work. "Looks better" may be true, but it does not tell the next agent what learning obligation changed.

```text
Build the next authorized slice only. Read active constraints and relevant
component/rules versions first. State the objective and evidence this slice
serves. Save the script, inspect the result, and run supported checks before
recording. Stop on a constraint violation or missing critical requirement.
Do not manufacture a human reason or release.
```

> **RUN SLOT 15.3.** Save the actual round log, scripts, snapshots, screenshots, human reasons, check results, and request/cost ledger. The capstone should show selected failures and repairs, not only its final frame.

### Stage 4: Test Transfer to a Fresh Session

Compile the rules as Chapter 12 describes. Ask a fresh session to build one new item or state from the package alone. Keep the original work intact. Ask an independent reviewer to inspect the result with the allowed evidence and without editing it.

This test has a bounded purpose: can the contract travel beyond the conversation that produced it? It does not establish that every future agent will comply. A failure should identify missing context, ambiguous rules, ignored instructions, or insufficient checks where the evidence permits that diagnosis.

> **RUN SLOT 15.4.** Save the fresh-session input package, result, independent findings, false alarms or misses, and any rule revision. Keep reruns labelled; do not replace a failure silently with the best attempt.

### Stage 5: Obtain Human Evidence, or State the Dependency

If appropriate permissions and participants are available, run the Chapter 13 protocol and report actual observations and delayed responses. If not, deliver a test-ready prototype and a pending protocol. That is an incomplete learner-tested capstone, not a reason to create fictional results.

The title names the target outcome. Your portfolio status must name what actually exists. "Agent-built, design-reviewed, learner test pending" is a useful and honest project state. The author can then decide whether to proceed, reduce scope, or wait for participants.

> **RUN SLOT 15.5.** Save approved de-identified report, actual sample and delay, missingness, revisions, and limits; or explicitly record why learner testing remains pending.

### Stage 6: Handoff and Final Comparison

Build and test the Chapter 14 acceptance slice if the delivery route is authorized and available. Then rescore the final design using the same five baseline checks and the additional project rubric. Keep design-intent checks separate from runtime results.

| Check | Baseline | Final | Evidence/limit |
|---|---|---|---|
| Answer boundary | RUN | RUN | Tested paths or untested states |
| Explanatory feedback | RUN | RUN | Actual content and human review |
| Hint preserves work | RUN | RUN | Item-specific reasoning review |
| Task-relevant presentation | RUN | RUN | Objective/context diagnosis |
| Keyboard design intent | RUN | RUN | Annotation/focus-state evidence |
| Runtime access | Not inferred from canvas | RUN/not run | Actual environment and scope |
| Delayed learner evidence | RUN/not collected | RUN/not collected | No automatic causal inference |

A higher final design score supports a statement about the reviewed design under this rubric. It does not by itself support a learning-gain claim. A delayed observation can add human evidence while still leaving causation unresolved. Keep those conclusions in separate sentences.

> **RUN SLOT 15.6.** Save final comparison, acceptance results, actual total cost, unresolved blockers, and portfolio privacy review. No release or book gate is signed by the agent.

## The provenance this chapter adds

```json
{
  "chapter": 15,
  "lesson": "RUN: bounded personal lesson",
  "baseline": "RUN",
  "human_correction_history": "RUN",
  "fresh_session_test": "RUN",
  "learner_test": "RUN or pending",
  "handoff_slice": "RUN or not implemented",
  "final_claims_and_limits": "RUN",
  "human_signoff": "not-supplied-by-agent"
}
```

The capstone record makes it possible to inspect the work without relying on the author's retrospective confidence. It also shows where human judgment, rather than automatic production, changed the result.

## The check

**The machine half:** artifact presence, IDs, versions, captured constraints, test outputs, arithmetic, and flagged claim language. A complete folder is not a complete learning argument.

**The human half:** scope, content validity, meaningful support, appropriate participation, interpretation, authorship, and any release decision. These do not become machine judgments merely because the portfolio has a rubric.

**What neither proves:** a general advantage of all agentic design, universal rule reliability, or causal learning improvement. This is one documented project. Its value is inspectability and the quality of the reasoning it exposes.

## Exercises

**Warm-up**

1. *(Low; complete.)* Write the smallest capstone scope that includes a real performance and evidence path. Name one tempting feature you will omit and why.
2. *(Low; compare.)* Identify two ways a before/after comparison could become unfair. Specify the records needed to detect them.

**Application**

3. *(Medium; direct.)* Complete one full draw/correct/redraw cycle with a verbatim human reason and a preserved constraint.
4. *(Medium; compare.)* Score a baseline before repair and a final state under the same rubric. Report disagreements and cannot-determine cases.
5. *(Medium; defend.)* Prepare the portfolio manifest and label every artifact missing, specified, implemented, or evidenced.

**Synthesis**

6. *(High; defend.)* Write a one-page account of what improved, what did not, and which claims you cannot make. Link every factual claim to an artifact.
7. *(High; complete.)* Run a fresh-session build and independent review. Revise one rule from a real failure or report that the tested conditions produced no failure.

**Challenge**

8. *(Open; evaluate.)* Identify the finding that most threatens your preferred story about the project. Design the next test that would take it seriously rather than explain it away.

## What you can now do

You can carry a lesson from objective to an inspectable build and a bounded evidence report. You can explain which decisions the agent made, which you corrected, why the corrections matter, and what remains untested.

## Credit the AI

**Planned contribution:** bounded production, artifact management, checks, fresh-session construction, and review assistance. **Observed errors and actual cost:** RUN. **Verification:** actual artifacts, human reasons, permitted learner observations, and scoped runtime tests. The AI does not supply the author's judgment or fabricate missing evidence.

## After the Capstone

The lesson is not finished because the agent stopped drawing. It becomes defensible when its claims match its evidence and its unresolved questions are visible. Keep the rules that proved useful, revise those that did not, and let a later observation challenge a decision you currently like. That is the working craft this book is trying to teach.
