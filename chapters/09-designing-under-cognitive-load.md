# Chapter 9 - Designing Under Cognitive Load
*Removing effort is useful only when you know what the effort was doing.*

> **Rough draft - pre-research.** Learning lead: LXD Chapter 3, including its four-question diagnostic and caveats about load categories. Checking-pattern leads: the blueprint's `../agentic-creative-direction/` audit pattern and FEA `examples/film-24/SKILL.md` `[VERIFY]`. Proposed thresholds are project policies, not claims of universal instructional benefit or accessibility conformance. No audit has run against this chapter's screens.

## The concept

Suppose a practice screen feels difficult. The learner must compare two cases, move between a diagram and its explanation, and write a reason. An agent asked to simplify it could remove the comparison, bring the explanation closer, and replace the reason with a confirmation button. The resulting screen might be faster in every way. Only one of those changes may have removed unnecessary effort.

That is the central problem of load-aware production. "Less on screen" is a visual preference. "Less effort unrelated to the target learning" is a design argument that requires an objective and a learner context.

LXD Chapter 3 develops the distinction among material complexity, avoidable interface demands, and processing directed toward learning. It also notes that the category boundaries and measurement claims are not simple. I will use the distinction to ask better design questions, not pretend every moment of effort can be assigned a precise psychological quantity from a screenshot.

### Use the Diagnostic Before the Cleanup

For each friction point, ask four practical questions adapted from that chapter's approach:

1. What is the learner trying to do, according to the objective?
2. Is this effort directed at that performance or at managing the interface?
3. Can these learners plausibly succeed with the support available?
4. If we remove the effort, do we change what they practice?

Write the answers before requesting a redesign. The fourth question is the defense against an overly smooth lesson. If removing the explanation field eliminates explanation practice, the field was not merely clutter. If moving a caption next to the relevant diagram reduces visual search while preserving the comparison, that may remove a container burden without changing the target task.

Prior knowledge matters. A step-by-step scaffold may help one learner and force another through redundant material. Chapter 5 represents that difference as support conditions; this chapter checks whether each condition is usable and whether its content still serves its purpose.

### What the Machine Can See

Some defects are represented as measurable properties: text outside a frame, clipping, overlap, minimum sizes under the chosen project policy, missing token bindings, and contrast calculations where the required colors and backgrounds are known. A checker can inspect those properties and return evidence.

Other questions are semantic. Is the illustration relevant to the target reasoning? Does the hint reduce unnecessary search or remove the task? Is the reading level appropriate for these learners and this discipline? A language model may offer a useful critique, but it should not convert those judgments into deterministic compliance just because the report is JSON.

Separate three kinds of review:

| Review | Example question | Suitable result |
|---|---|---|
| Deterministic geometry/style | Does captured text overflow its frame? | Pass/fail with measured evidence |
| Heuristic/content review | Does this diagram appear related to the objective? | Concern/no concern/insufficient context, with reason |
| Learner observation | Can intended learners use it without losing the task? | Observed behavior with limits |

A reviewer that reports all three as Pass is difficult to trust. It hides the difference between a measured property, an interpretation, and an observation.

### Tokens Encode Constraints, Not Pedagogy by Themselves

The project uses named design tokens and an established visual system for eventual figures. The learner interface should likewise use a small set of named values rather than ad hoc per-screen choices. For this draft, `text/body`, `space/related`, `space/section`, and `color/text-primary` are illustrative token names, not a replacement palette or an implemented library.

A project might choose 16 as a minimum body-text size in its working design units. That is an example policy, not proof that 16 is readable for everyone or that a built page will meet any standard. The policy must state its unit, scope, exceptions, and corresponding runtime tests. Scaling, zoom, font metrics, language, and rendering all matter later.

The same is true of a contrast check. It needs the rendered foreground/background relationship, not just two token names. Transparency, images, states, and themes can change that relationship. A checker that cannot determine the effective background should say Cannot determine, not pick white and return a confident ratio. Current standards and test methods need primary-source checking before release `[VERIFY]`.

What makes tokens pedagogical is the reason for the constraint and its use in the task. A spacing token can keep a caption with the diagram it explains. It cannot decide which explanation belongs there. A minimum text policy can protect legibility while leaving the content irrelevant. Keep the human rationale alongside the machine property.

### Decoration Is Not a Category of File Type

A diagram may carry the task. A photograph may supply indispensable case evidence. A small icon may prevent repeated lookup. Removing them all because they are images would be as crude as adding them all because the lesson needs delight.

For every nonessential-looking element, write its claimed job. If the job is instructional, identify the objective or reasoning step it supports. If the job is orientation, feedback, or motivation, name that role without pretending it is direct assessment evidence. Then decide whether its cost is justified in the current screen.

The same critique applies to text. A dense block of prose can be irrelevant decoration in another form. Minimal visual styling does not guarantee minimal extraneous demand. The question is where the learner's attention has to go and why.

<!-- [TABLE: a load audit with factual columns separated from human diagnostic answers; include an example where removing effort destroys the objective] -->

### Thresholds Need an Exception Process

A checker may flag an item because the explanation exceeds a text budget. The budget can be useful for preventing accidental walls of prose. It can also be wrong for an explanation the objective genuinely requires. The response should not be automatic deletion or silent waiver.

Write an exception with scope and reason: this item needs the additional explanation, these states were reviewed, these layout alternatives were considered, and this human approved the choice. The exception should not disable the rule across the entire library. Nor should the agent create an exception merely because it cannot fit its first draft.

This is a general pattern for machine-checkable design systems. A rule can be valuable without being absolute. Its exception record preserves the reason it was relaxed and the checks that still apply. Chapter 12's rules file should carry that distinction so a fresh session does not treat one exception as permission to ignore the policy everywhere.

### Readability Is Not Only a Grade-Level Number

An agent can simplify sentences, replace terminology, and estimate a reading score. Those operations may help with review. They can also delete the very disciplinary distinction the lesson teaches. A short sentence that equates all difficult effort with bad design is easier to read and conceptually wrong.

For the demonstration lesson, preserve terms when learning to use them is part of the objective, explain them at the point of need, and remove unnecessary wording around them. Ask a human content reviewer to inspect meaning after simplification. A readability score should be a diagnostic prompt, not an automatic license to rewrite the concept.

The learner context matters here too. Technical vocabulary may be familiar to one audience and new to another. Keep those assumptions in the charter. If the agent cannot tell whether a term is known, it should flag the uncertainty rather than translate every word into a vague everyday substitute.

### Compare Attention Paths

One useful human review is to trace the information path the learner must follow. Where is the case? Where is the part of the diagram it refers to? Where is the response control? What must be remembered while moving between them? This is a structured inspection, not a measured record of eye movement.

Draw the proposed path on a review copy or describe it in the audit. Compare alternatives that keep related information together. Then ask whether the proposed repair makes the relevant relation easier to inspect without solving it for the learner. A diagram can be integrated so thoroughly with its explanation that it stops being a task and becomes an answer display.

### Recheck Shared Changes

When a fix changes a token or component, list the affected instances. The original screen may improve while a longer translated label now clips elsewhere, or a focus state loses distinction in another theme. A shared abstraction creates a shared verification obligation.

Keep the review proportional. You do not need to inspect every unchanged property after a local text correction. You do need to inspect the states that depend on the changed rule, binding, or layout. The agent should explain that scope before claiming the repair is complete. A useful audit report names both what it checked and why that coverage was sufficient for the change.

### A Good Check Can Disagree With the Designer

Do not tune the checker only until your current screen passes. Start from the declared policy, inspect a failure, and decide whether the screen or policy is wrong. If the policy changes, version it and rerun affected examples. Otherwise the audit becomes a ceremonial approval of whatever you already built.

This matters especially for a design system created alongside the book. The first screen can accidentally define the thresholds simply because it exists. Include a clean comparison and a deliberately defective sandbox case so the checker has opportunities to distinguish them. A rule that never rejects anything may be unnecessary or too weak; a rule that rejects every useful explanation may be mis-specified.

The author should be able to defend a disagreement in ordinary language. "I accepted this exception because the explanation supports the required comparison and these states still fit" is reviewable. "The agent said the audit was overly strict" is not a design reason. Keep the human decision explicit and retain the evidence that made the exception reasonable.

## What you'll be able to do

- **Diagnose** a friction point against an objective and learner context before changing it.
- **Encode** measurable project constraints as tokens and checker rules.
- **Separate** deterministic findings, heuristic concerns, and learner observations.
- **Revise** a screen without removing the thinking the objective requires.

**Plan:** all, provisional. **MCP budget:** planning ceiling 25 requests; actual RUN. **Builds on:** Chapters 4-7, plus the states from Chapter 8 where relevant.

## Talking to Figma

### Round 1: Inventory Before Judgment

```text
Inspect one approved practice screen across its support and feedback states.
Create a factual inventory of text, controls, diagrams, spacing, token bindings,
clipping, and visible state. Do not classify effort as useful or unnecessary yet.

Return a load-audit table with the four diagnostic-answer columns left for me.
Quote the objective and learner assumptions at the top. If either is missing,
stop the judgment step and ask for that context. Save raw evidence and scripts.
```

This ordering is deliberate. An agent can structure the audit before it has enough context to judge the effort. If it fills the verdicts anyway, it is doing the exact thing we are trying to prevent: treating its general interface preference as the lesson's objective.

You do not need a scientific estimate of working-memory load to find a detached caption or an unexplained control. You do need to avoid turning those observations into universal psychological measurements. Write "the learner must switch between these regions" before writing "this overwhelms working memory."

> **RUN SLOT 9.1.** Save the factual inventory, raw read evidence, objective quote, learner assumptions, and blank diagnostic table. Record any judgments the agent filled without authorization as a process defect, not a helpful head start.

### Specify the Checker

Create a checker contract with three outputs: deterministic findings, heuristic review requests, and unavailable evidence. The blueprint points to an existing design-audit pattern; inspect and reuse an appropriate existing implementation during the live work rather than writing a new geometry engine from memory `[VERIFY: blueprint Chapter 9 precedent]`.

An illustrative result record is:

```json
{
  "rule_id": "LAYOUT-TEXT-01",
  "screen_id": "S02",
  "state": "Partial/Draft",
  "result": "CANNOT-DETERMINE",
  "evidence": "RUN: no resolved font/layout metrics available",
  "requires": "rendered-state inspection",
  "kind": "deterministic"
}
```

This is an output-shape example, not a finding. Each real failure should name the property, measured value if available, expected policy, and evidence location. A reviewer should not have to guess which layer "text too small" refers to.

### Your Turn in Figma

Fill the diagnostic answers for one friction point. Suppose a diagram's explanation is on another frame. Ask whether moving it removes search while preserving the learner's comparison. Then inspect a reason field: would deleting it remove the performance itself? Use these as reasoning examples, not assumed findings about your file.

Correct an actual screen property by hand. Your reason should say which effort you changed and which effort you preserved. If the objective or prior-knowledge assumption is uncertain, record that uncertainty rather than force a neat classification.

> **RUN SLOT 9.2.** Save completed diagnostic answers, the human diff and reason, and unresolved learner assumptions. Keep factual observations separate from classifications even when they appear in the same table.

### Round 3: Repair Only the Authorized Burden

```text
Read my completed diagnostic row, correction, and active constraints. Apply the
approved repair to related states without removing the target comparison or
reasoning. Run deterministic checks first. Route semantic concerns to review.

For every change, state which measured defect or approved judgment it addresses.
Do not replace explanations with scores merely to fit a text budget. If content
does not fit, propose layout or sequencing alternatives and report the trade-off.
```

A repair should produce a before/after check, not just a new screenshot. If the agent changes the text, recheck the content contract. If it changes support visibility, recheck the state machine. If it changes spacing tokens, inspect all states that use them. A local visual fix can have a shared blast radius.

> **RUN SLOT 9.3.** Save the repair script, before/after audit, constraint result, and affected-state list. Report any human concern the machine could not adjudicate.

### Round 4: Test the Checker With a Mutation

In a separate sandbox, plant one deterministic defect and one semantic defect. For example, clip a response label and add an irrelevant illustration. Write ground truth first. The checker should catch what its evidence supports and route the semantic case to review rather than claim it measured cognitive load.

```text
Evaluate the sandbox with the approved checker. Do not modify it. For each
finding, distinguish measured failure from content concern. Use Cannot determine
when required evidence is unavailable. Compare results with the ground truth
only after producing the report. Keep planted defects separate from live ones.
```

The clean comparison matters too. Include an unchanged screen. A checker that flags every long explanation as clutter may score well on planted bad screens while systematically attacking necessary reasoning. False alarms are not just annoying; they can teach the author to remove the wrong things.

> **RUN SLOT 9.4.** Save ground truth, checker report, true/false/missed findings, and unavailable cases. Report counts. Do not estimate general accuracy from this small mutation test.

## The provenance this chapter adds

```json
{
  "chapter": 9,
  "objective_and_context": "RUN",
  "human_load_diagnosis": "RUN",
  "deterministic_audit": "RUN",
  "heuristic_concerns": "RUN",
  "human_reason": "RUN: verbatim",
  "mutation_test": "RUN: planted and observed defects separated"
}
```

This record can show whether an apparent simplification preserved the objective and whether the checker was judging only what its inputs supported.

## The check

**The machine half:** geometry, known property thresholds, resolved token use, required fields, and captured constraints. A deterministic pass is limited to the declared properties and states.

**The human half:** diagnose effort relative to the task, judge content relevance, and decide what support is appropriate for the learners. Do not outsource these conclusions merely because the agent can argue them fluently.

**What neither proves:** a numeric cognitive-load reduction or a learning benefit. A cleaner arrangement is a design hypothesis until appropriate evidence tests it.

## Exercises

**Warm-up**

1. *(Low; diagnose.)* Identify one effort you would remove and one you would preserve on the same screen. Tie each to the objective.
2. *(Low; separate.)* Classify three proposed checks as deterministic, heuristic, or learner-observation work. Explain the evidence each needs.

**Application**

3. *(Medium; encode.)* Write one token policy with units, scope, exceptions, and a runtime follow-up. Do not call it a universal learning rule.
4. *(Medium; diagnose.)* Complete the four-question audit for a reason field before asking the agent to simplify it.
5. *(Medium; revise.)* Repair a measured layout defect and rerun all affected support states. Record any newly introduced issue.

**Synthesis**

6. *(High; evaluate.)* Compare a sparse screen with a dense but task-relevant screen. Explain why visual density alone cannot settle the load judgment.
7. *(High; separate.)* Design a checker result that honestly returns Cannot determine. Specify what additional evidence would change that result.

**Challenge**

8. *(Open; evaluate.)* Plant a defect your checker should catch and a necessary difficulty it should leave alone. Test whether its recommendations preserve that boundary.

## What you can now do

You can separate avoidable container effort from the effort the objective needs, encode measurable constraints, and stop an audit from pretending to measure more than it can see.

## Credit the AI

**Planned contribution:** inventory, checker adaptation, repair, and mutation-test report. **Observed errors:** RUN, including premature classifications and false alarms. **Verification:** human diagnostic answers, raw property evidence, and independent review of planted versus observed findings.

## Next

An interface can be visually tidy and still exclude the learner from the task. Chapter 10 carries the contract beyond pixels into focus, semantics, alternatives, and tests that require a real build.
