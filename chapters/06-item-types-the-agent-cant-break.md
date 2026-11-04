# Chapter 6 - Item Types the Agent Can't Break
*A reusable component needs a contract for the thinking, not just the spacing.*

> **Rough draft - pre-research.** The title states a design ambition, not a guarantee. Component-description leads come from FEA `examples/film-07/` and `CAPABILITIES.md` `[VERIFY]`. The item examples are illustrative teaching content, not validated assessment instruments. No item batch or compliance result has been generated in Figma for this chapter.

## The concept

A multiple-choice component can be visually perfect and educationally weak. The options may be different lengths, one may contain the wording of the question, or two may be defensible under an unstated assumption. A component system that checks only spacing will faithfully reproduce those defects at scale.

This chapter gives the component a second contract. The first describes appearance and interaction. The second describes what an item must ask, what information it must withhold, how its key is justified, and which content checks remain human judgments.

I am not trying to make the agent an assessment expert by adding a paragraph to a component description. I am making its obligations inspectable. The word "can't" in the title should make you suspicious. Agents can ignore rules, rules can be incomplete, and a plausible item can still be wrong. The useful result is a library that catches more failures and makes uncaught failures easier to diagnose.

### The Item Type Changes the Evidence

Consider four ways to assess the same diagnostic concept.

A multiple-choice item asks the learner to discriminate among supplied alternatives. A short-answer item asks them to produce a reason. An ordering item asks for a sequence. A classification-with-justification item asks them to connect a label to a case. These are not interchangeable wrappers for the same evidence.

If the target is explaining why a navigation burden is unrelated to the learning objective, recognizing a category name provides weaker evidence than producing the explanation. But a short-answer field introduces scoring and accessibility work that a choice item may not. The task is to choose knowingly, not to rank item types on a universal ladder.

For this demonstration, the fourth type will be **case classification plus justification**. It fits LXD Chapter 3's diagnostic while making the rationale visible. A reader may substitute a different type when the objective requires it. The contract still needs the same fields: target performance, response form, scoring basis, reveal timing, support behavior, and accessibility handoff.

### A Description Is an Interface to the Next Agent

FEA's film-07 compares conditions involving component descriptions and an external rules file. The blueprint uses it as a precedent, but its results should not be generalized into "descriptions always work" `[VERIFY: FEA examples/film-07/measurements.json and saved contexts]`. Our test is whether the current read returns the description and whether a fresh agent acts on it for learning items.

A useful description is short enough to retrieve and precise enough to check. It names scope and points to the full rules. It should not contain the answer key for a learner-facing instance if a downstream export could expose it. Private authoring data and rendered learner content are separate concerns.

For a proposed choice component:

```text
Component: LearningItem/SingleChoice
Purpose: one committed response to one stated problem.
Required authoring fields: objective_id, item_id, stem, options, one key,
key_rationale, distractor_rationales, feedback, support contract.
Before commit: no key styling, correctness text, or answer-bearing hint.
After commit: explain the reasoning; do not only score.
Review: content expert confirms one defensible key under the stated assumptions.
References: R-ANSWER-01, R-FEEDBACK-01, R-ACCESS-01.
```

That is a proposed description, not evidence that any tool returned it. It also does not make the key secure. In a browser application, hiding a layer or CSS class is not a security boundary. Chapter 14 addresses where authoring keys and scoring logic belong in a real build.

### Properties, Variants, and Content

A property can represent a controlled option. A variant can represent a distinct configured state. A content field holds the actual question or explanation. Which of these Figma exposes in a particular read must be tested `[VERIFY: FEA CAPABILITIES.md and film-07 saved design context]`.

Use controlled properties for things the agent should not casually invent: item type, support condition, attempt state. Use content slots for the stem, options, and feedback. Keep identifiers stable when text changes, because the correction ledger needs to distinguish a rewritten option from a different item.

The contract should also specify what must not be inferred. A state called Correct is an authoring label, not evidence that a learner answered correctly. A component called ShortAnswer does not imply automatic grading. Avoid names that quietly import implementation promises.

### Four Illustrative Item Contracts

The following examples demonstrate structure. They need content review before use.

**Single choice.** A learner repeatedly opens a detached control legend while trying to compare two worked solutions. Which change most directly reduces tool-management effort while preserving the comparison? The proposed key is placing the necessary control explanation with the controls. Distractors should represent meaningful alternatives, not absurd actions. Each needs a rationale. If more than one change could be best under plausible assumptions, revise the stem rather than insisting the key is unique.

**Short answer.** Explain why replacing an unsupported generation task with a worked example might help a novice but be redundant for an experienced learner. The rubric should name required ideas, acceptable variations, and what would be insufficient. It should not demand exact textbook wording. The prototype can display a rubric or moderator feedback without pretending a scoring model has been validated.

**Ordering.** Put a declared instructional sequence in order: study a parallel worked example, complete a partial example, attempt a new case independently. The stem must say that this is the proposed sequence being recognized, not the only valid sequence for every learner. Ordering becomes invalid when several sequences are defensible but the interface accepts only one.

**Classification plus justification.** Classify a source of effort in a supplied case, then explain the classification using the stated objective and learner knowledge. A bare category is incomplete. The rubric must accept a justified challenge to an under-specified case rather than punishing the learner for noticing missing information.

The last point matters. A question with insufficient information is not repaired by adding a confident answer key. It is repaired by adding the missing condition or changing the scoring contract.

<!-- [TABLE: four item types with target evidence, required authoring fields, likely failure, machine check, and human content review] -->

### A Plausible Distractor Needs a Reason to Be There

For the single-choice example, the authoring record should explain each option. A distractor might confuse unnecessary control lookup with productive comparison. Another might remove the comparison itself in the name of speed. Another might add a worked example without addressing the unexplained control. Each represents a different reasoning error worth discussing.

Do not accept an option merely because it is false. An absurd distractor can make the correct answer recognizable without the intended discrimination. Nor should the key be the only option with a careful qualification while the others are blunt absolutes. Those cues let a learner answer a writing-pattern puzzle instead of the subject-matter question.

The agent can compare lengths, repeated terms, and suspicious wording. Those checks are clues, not a recipe for valid options. Equal-length alternatives can still be poor. A long correct answer is not automatically invalid. Require the content rationale and let the reviewer explain why a cue matters in this particular item.

### Short Answer Requires a Scoring Boundary

For the short-answer example, a proposed rubric can distinguish a complete explanation, a partial explanation, and an unresolved response needing human review. A complete explanation connects the support choice to the learner's prior knowledge and the task. A response that only repeats "expertise reversal" may name the concept without applying it. A response that identifies missing context may be more defensible than a confident but under-specified answer.

Write examples of acceptable reasoning as authoring material, clearly labelled illustrative, without turning them into the only accepted wording. If a later model scores responses, evaluate that scorer separately. The fact that the content-generation agent wrote a rubric does not validate its use as an automated judge.

This is a useful place for Cannot determine. An unclear response can require a follow-up rather than an automatic zero. But do not use that category to hide every difficult scoring decision. State the routing rule and who reviews the case. Otherwise unresolved responses accumulate without a learning action.

### The Batch Is a Test of a Process

A ten-item batch gives you a manageable set to inspect. It does not establish an error rate for all future items. Keep the requested distribution, the actually generated distribution, and the approved distribution separate. If the agent produces eight items and repeats two IDs, the batch did not contain ten independent proposals.

Track defect categories across revisions. Did a revised description reduce premature reveal while making feedback less explanatory? Did a new rubric fix one ambiguous item and reject legitimate alternative reasoning elsewhere? A single total pass count can conceal that trade-off.

When an item changes substantially, version it. The original failed proposal remains part of the audit history, while the revised content receives its own review. A later learner response must identify which version was presented. Otherwise a disputed answer can be judged against a rubric that did not exist when the learner responded.

Finally, keep item reuse intentional. Reusing a visual component is desirable. Reusing an answer pattern or case with only the names changed may not produce new evidence. The library should support production speed without making every question the same question in a different coat of paint. Ask the agent what variation changes the required reasoning and what variation is merely superficial.

## What you'll be able to do

- **Write** component contracts that specify evidence and behavior as well as layout.
- **Choose** an item type based on the target performance and scoring burden.
- **Audit** a generated batch for structural defects, content defects, and unresolved cases.
- **Revise** a rule using an observed failure without claiming the revised rule is universally reliable.

**Plan:** all, provisional. **MCP budget:** planning ceiling 30 requests for library construction and a bounded batch; actual RUN. **Builds on:** Chapters 4-5.

## Talking to Figma

### Round 1: Build the Library Before the Batch

```text
Create four learning-item component contracts: SingleChoice, ShortAnswer,
Ordering, and CaseClassificationWithReason. Use the supplied reviewed content
only for initial examples. Keep content, support_level, and attempt_state
separate. Put a concise contract and rule IDs in each component description.

Read back each contract through the actual path a fresh implementation agent
would use. Report missing fields or lost descriptions. Do not infer success
from the component name. Save scripts and follow the provenance loop.
```

Do not start with ten items. First verify that one instance of each type carries the intended contract. Otherwise the batch multiplies a representation problem that looks like a content-writing problem.

Ask the agent to distinguish its authoring schema from the learner-visible frame. A key can exist in the authoring record while remaining unavailable before commitment in the prototype. That separation must be explicit in the eventual handoff; merely hiding a shape is not an implementation strategy.

> **RUN SLOT 6.1.** Save component contracts, instance read-backs, scripts, screenshots, and the authoring-versus-rendered-content map. Record which contract statements were actually available to the next agent.

### Round 2: Generate a Ten-Item Proposal

Use a bounded distribution, such as four choice items and two of each other type. That is an illustrative audit batch, not an optimal test composition. Give the agent objective IDs and content boundaries. Require a key rationale or rubric for every item before it draws.

```text
Propose ten items using the approved contracts and objective map. Before
drawing, provide item_id, objective_id, target performance, scoring rationale,
support behavior, and any uncertainty. Do not fabricate sources for content.
Mark an item NEEDS-CONTENT-REVIEW if its key or rubric is ambiguous.

After review of the proposal, build only the authorized items. Preserve the
existing library and human corrections. Keep unresolved items out of the
approved set rather than treating them as correct by default.
```

The proposal step makes a content defect cheaper to fix. If the agent cannot justify why an ordering item has a unique sequence, no amount of component polish will supply that justification.

> **RUN SLOT 6.2.** Save the proposal, authorization boundary, built batch, and audit table. Use one row per item and distinguish structural pass from content review. An unreviewed rationale is not a validated key.

### Your Turn in Figma

Choose one real failure from the batch. It might be an answer cue, a distractor that is partly correct, a short-answer rubric that rewards terminology instead of reasoning, or an ordering item with two valid sequences. If none appears, report that rather than inventing a failure for the book's argument.

Correct the content or component by hand and explain why. Then decide whether the repair is local or general. Changing a distractor is local. Requiring the stem to state the learner's prior knowledge may be a reusable rule. The ledger should preserve the actual correction; Chapter 12 will compile general rules from it.

> **RUN SLOT 6.3.** Save the diff, your reason, the local/general classification, and the affected contract. Record whether the correction changed the evidence the item collects.

### Round 4: Generalize Without Copying

```text
Read the correction and its reason. Propose a contract revision, distinguishing
the local fix from the general rule. Do not edit an author-protected rules file
without authorization. Apply the approved contract to two new items on
different concepts. Keep the corrected item intact and run check-constraints.

Report whether each new item requires expert content judgment even if every
structural check passes. Do not call a schema-valid item pedagogically valid.
```

A contract revision that only says "do not use this distractor" may pass the original item and fail the next one. A revision that says "all distractors must be wrong" is too vague to inspect. A better instruction requires the authoring record to state why each distractor is wrong under the stem's explicit assumptions and routes disagreement to content review.

> **RUN SLOT 6.4.** Save proposed and approved contract versions, the two new items, constraint results, and remaining review questions. Compare failure types, not just total passes.

### The Audit Table

Keep these verdicts separate:

| Check | Evidence | Verdict vocabulary |
|---|---|---|
| Required fields exist | Authoring record | Pass/fail |
| One key declared for single choice | Authoring record | Pass/fail |
| One key defensible | Expert reasoning about the stem | Pass/fail/unresolved |
| No pre-commit answer cue | All reachable pre-commit states | Pass/fail/not tested |
| Feedback explains | Actual feedback and objective | Pass/fail/unresolved |
| Access contract present | Annotation or handoff record | Present/missing |
| Built accessibility works | Runtime tests | Pass/fail/not run |

This prevents a common inflation: ten structurally complete items become "ten valid questions" in the summary. A good audit can say that all ten have fields, six passed content review, two need revision, and two remain unresolved. That is more useful than a single impressive percentage.

## The provenance this chapter adds

```json
{
  "chapter": 6,
  "library_contracts": "RUN",
  "batch_size_planned": 10,
  "batch_size_built": "RUN",
  "structural_results": "RUN",
  "content_review_results": "RUN",
  "human_reason": "RUN: verbatim",
  "new_item_test": "RUN"
}
```

The distinction between planned and built counts is intentional. A failed batch build must not be reported as ten observed items merely because ten were requested.

## The check

**The machine half:** validate required fields, allowed states, key cardinality, stable IDs, and missing rationales. Test rendered answer cues where the representation permits it. String rules can detect prohibited phrases but cannot establish that a distractor is plausible or a rubric is fair.

**The human half:** judge item validity, ambiguity, alignment, and the reasoning demanded. Check whether an alternative answer reveals a defect in the question rather than a defect in the learner.

**What neither proves:** that the item discriminates reliably or predicts later performance. A small design audit is not psychometric validation. Report it as a design audit.

## Exercises

**Warm-up**

1. *(Low; choose.)* Pick two item types for one objective. State the different evidence each would collect.
2. *(Low; write.)* Write a six-line contract for a new item type, including one requirement a machine can check and one it cannot.

**Application**

3. *(Medium; audit.)* Audit a ten-item proposal before drawing. Count structural failures, content failures, and unresolved cases separately.
4. *(Medium; write.)* Rewrite an ambiguous stem so that its key is defensible without adding a clue to the answer.
5. *(Medium; revise.)* Correct one item and test the proposed general rule on two new concepts. Preserve the failed attempts in the record.

**Synthesis**

6. *(High; choose.)* Replace a choice item with short answer. Update the evidence interpretation, scoring contract, support states, and access handoff, not only the input control.
7. *(High; audit.)* Design a case in which a learner's objection should receive credit. Specify how the rubric avoids treating all disagreement as correctness.

**Challenge**

8. *(Open; evaluate.)* Create a deliberately schema-valid but educationally invalid item. Ask an independent reviewer to find the defect and report whether the contract needs a new check or a human gate.

## What you can now do

You can build a library whose reusable unit includes the learner's task and scoring basis. You can also explain why structural validity, content validity, and runtime behavior need different evidence.

## Credit the AI

**Planned contribution:** library construction, item proposals, structural audit, and a transfer test of revised contracts. **Observed errors:** RUN. **Verification:** content expert reviews keys and rubrics, the actual read-back tests description survival, and unreviewed items remain unreviewed.

## Next

An item contract still needs a precise account of what happens after the learner acts. Chapter 7 defines commitment, feedback, hints, and retry as a state machine so the interface cannot casually give away the very performance it asks for.
