# Chapter 7 - Feedback, Hints, and the Answer You Don't Show
*The important part of the screen is often the information that has not appeared yet.*

> **Rough draft - pre-research.** Learning leads: LXD Chapter 3 and *AI for Learning Experience Design* Chapters 3 and 6. Prototype-tool lead: FEA `examples/film-12/03-prototype.js` `[VERIFY]`. State tables and example feedback are proposed designs. No transition, agent response, or learner outcome below has been observed for this chapter.

## The concept

Suppose an item asks the learner to distinguish effort spent managing a tool from effort spent learning the target material. The learner selects a category. Before they press Check, the choice turns green and an explanation slides into view. The interface has technically collected a click. It has not necessarily collected the commitment the designer intended.

The defect is not the green. It is that selection and commitment have been treated as the same event without saying so. An agent building a familiar form can make that decision for you. This chapter takes it back.

We will specify the item as a state machine: a set of named states, the actions that connect them, and the information allowed in each. The diagram is not decoration. It is a contract for what the learner can know before and after each action.

### Selection Is Not Necessarily Commitment

For our demonstration, selection is an editable draft. Commitment occurs when the learner deliberately submits the response. Other designs can use immediate selection as commitment, but the interaction must communicate that consequence and the evidence policy must match it.

Why separate them here? The objective includes giving a reason. A learner may change a category while composing that reason. We want one submitted judgment and rationale, not a series of exploratory clicks misreported as repeated attempts.

Define the event precisely: `commit_attempt` stores the response and assistance context for this attempt. It does not mean "the learner learned," "the response is correct," or "advance to the next item." These are separate transitions and interpretations.

The prototype can demonstrate a proposed sequence. Whether a real build stores the event once, preserves it on refresh, and keeps a private answer key out of premature disclosure requires runtime tests. Do not ask the canvas to prove a persistence or security property it does not implement.

### The Proposed State Machine

Here is the contract for one practice attempt:

| State | Learner can do | Information available | Next transitions |
|---|---|---|---|
| Unanswered | Read, draft, request hint | Case and permitted support | Draft, hint, exit |
| Draft | Edit response and reason | Same; no correctness signal | Commit, hint, clear, exit |
| Hint open | Read a bounded cue, return to draft | Hint plus prior permitted content | Draft, another allowed hint, exit |
| Committed | See submitted response and status | Submission recorded; scoring may be pending | Feedback, scoring error |
| Feedback | Inspect explanation and their response | Key/rubric as authorized for this task | Retry policy, next item, exit |
| Retry | Attempt a specified task again | Depends on prior exposure | Commit with retry/exposure label |
| Error/recovery | Recover without losing the draft | Error explanation; no accidental key | Return or safe exit |

This is not a universal learning sequence. It is the explicit sequence we choose for the lesson. A demonstration screen is outside this independent-attempt contract. So is a final assessment whose feedback policy intentionally differs. Write the scope instead of turning a local rule into a law.

A crucial invariant is that the target key cannot become available through a pre-commit path intended to preserve retrieval. That includes hints, hover styles, labels, alt text, accessible names, and transition previews in the built product. A screenshot of the default state cannot prove all of those paths safe.

### Feedback Has a Job Beyond Verdict

Verification feedback tells the learner whether the response meets a criterion. Elaborated feedback explains the relevant reasoning, misconception, or next step. LXD Chapter 3's friction diagnostic and the AI-LXD tutoring chapter supply the learning-design leads; the current manuscript does not attach a universal effect size or timing rule to them.

For a proposed incorrect response about tool-management effort, compare:

> Not quite. Try again.

with:

> Your explanation treats every difficult step as useful practice. In this case the learner's goal is to compare study schedules, not memorize navigation symbols. The repeated symbol lookup consumes effort without practicing that comparison. Keep the comparison; clarify the control.

The second is not always the right length for the screen. It is better specified because it connects the learner's reasoning to the objective. The agent can then help edit the wording without deleting the causal explanation.

For a correct response, do not settle for praise alone. Confirm the reason that makes the answer defensible and mark any boundary. A learner can select a key by guessing. Feedback should help them see why the reasoning matters, not pretend the selection proves it was already present.

### A Hint Must Leave Something to Do

A hint can direct attention, name a diagnostic question, or provide a partial step. Its quality depends on the task. A hint that eliminates all but one choice may preserve the appearance of a question while ending the discrimination it was supposed to support.

For the demonstration item, a proposed ladder is:

1. Re-state the target: "What is the learner supposed to be practicing here?"
2. Direct attention: "Separate comparing schedules from figuring out how the controls work."
3. Scaffold the reason: "Complete this: the extra lookup does/does not practice ___ because ___."

These are illustrative and require content review. The third rung may be too close to the answer for some item versions. Do not approve it because it is called Hint 3. Ask whether the learner still has to perform the target discrimination and explanation.

If a learner needs the solution, provide a clearly labelled way to study it when appropriate. Do not make them exhaust an obscure hint ladder or pretend solution viewing was an independent attempt. The ethical choice is not between withholding indefinitely and giving away everything. It is to make the task, help, and evidence interpretation explicit.

### Retry Is Not a Time Machine

Once the learner has seen the target solution, a retry of the same item is answer-exposed practice. It may be useful, but it is not a clean second observation of independent retrieval. Record it accordingly or use a parallel item with the same objective and reviewed difficulty.

Likewise, opening a hint does not become unobserved just because the learner closes it. The interface can return to the Draft state while assistance history remains true. Otherwise the progress view can label an assisted response independent merely because the panel was closed at submission.

<!-- [INFOGRAPHIC: item state machine with a marked information boundary at commit and separate assistance/exposure history that persists across visible states] -->

### Inspect the Whole Hint Ladder, Not Just Each Rung

A hint can be safe in isolation and revealing in combination. The first may eliminate two options, the second may eliminate a third, and the learner can identify the key without doing the target reasoning. A review that checks each string for the answer's exact wording will miss the cumulative leak.

Review the information available after every prefix of the ladder: no hints, hint one, hints one and two, all hints. Also check whether the interface permits opening them out of order. The unit of review is the reachable information state, not merely the text block.

This does not mean every narrowed choice is wrong. Scaffolding deliberately reduces the task. The question is whether the remaining performance matches the evidence label. If a later rung turns an independent classification into guided completion, say so and record the assistance. The defect is often not the help itself but an unchanged claim about what the learner demonstrated.

### Feedback Should Not Invent a Mental State

An option choice supports a limited statement: the learner selected that option under these conditions. It may be consistent with a misconception, but it does not prove the learner held it. They may have misread the stem, clicked accidentally, or reasoned from an assumption the item failed to state.

Use language tied to the submitted reasoning. "This option would remove the comparison the objective asks you to practice" critiques an action. "You always avoid difficult thinking" invents a trait and adds a judgment the evidence does not support. The former is also more useful for revision.

For an open response, quote only the relevant content privately during review and avoid exposing sensitive text in public examples. The agent can suggest a response-specific explanation, but a deployed tutoring model requires its own guardrails and evaluation. This chapter's prototype does not establish those capabilities by displaying a conversational bubble.

### Commit Failure Must Not Become Learning Failure

The built application may fail between pressing Check and saving the attempt. A state machine that goes straight from click to feedback may conceal the missing record. For a real product, define pending, saved, and failed states as needed. The learner should not lose a carefully written explanation or receive a false assurance that it was stored.

The same issue arises on repeated activation. The learner may press the control twice because the interface gives no response. Under a one-attempt contract, the implementation should not create two accepted attempts. A proposed idempotent submission boundary belongs in the handoff and its tests; drawing a disabled button is only part of the intent.

These operational states are not distractions from pedagogy. If they corrupt the attempt record, the progress view and learner study interpret the wrong event. A reliable learning interface needs to preserve what the learner actually did before it can claim to interpret the result.

At the end of the state review, ask a deliberately plain question: what could the learner know now that they could not know one action ago? Answer it for selection, hint, commit, feedback, and retry. If the answer changes without a corresponding evidence-state update, the contract is incomplete. This information ledger is often easier to review than a large diagram, and it gives the implementation agent a direct account of the boundary the pixels are meant to preserve.

## What you'll be able to do

- **Define** commitment and permitted information for each item state.
- **Write** feedback that explains the reasoning relevant to an objective.
- **Build and red-team** a hint ladder for answer leaks through multiple paths.
- **Specify** retry and recovery without erasing assistance or answer exposure.

**Plan:** all, provisional. **MCP budget:** planning ceiling 30 requests; actual RUN. **Builds on:** Chapters 5-6.

## Talking to Figma

### Round 1: Draw the Transition Table First

```text
For item LOAD-01, implement the supplied state contract. Before drawing, return
a transition table with source state, action, guard, destination, visible
information, and recorded evidence. Selection is draft; Check commits.

Keep support_level, assistance history, and solution exposure separate from the
visible attempt state. Use only currently verified prototype operations. Label
anything the prototype cannot execute as a handoff requirement, not a pass.
Save scripts and follow PROVENANCE.md.
```

The transition table should identify guards. A guard is a condition that must hold before an action can proceed. In this demonstration, committing an empty response should prompt recovery rather than reveal the key. If an explanation is required, the contract must define what counts as supplied without pretending that nonempty text is meaningful reasoning.

The sibling film-12 script uses component transitions for a tutor-state example. It is a useful source to inspect, not an unmodified script for this item `[VERIFY]`. Any adaptation needs current API checks and a live run. Save the actual implementation script after the agent writes it; do not substitute an idealized transcript.

> **RUN SLOT 7.1.** Save the transition table, guard definitions, exact scripts, implemented edges, and known prototype limits. Separate endpoint frames from transitions actually exercised.

### Round 2: Add Feedback and a Hint Ladder

Provide a reviewed answer rationale and two misconception rationales. Ask the agent to draft feedback around those, not invent a model of the learner from one click.

```text
Draft feedback for the supplied key and misconceptions. Each response must
connect the submitted reasoning to the objective. Do not diagnose a learner
trait or claim to know why they chose an option. Label the text as proposed.

Add three bounded hints. For each, state the reasoning step still left to the
learner. Keep the target solution unavailable through every pre-commit path.
If a hint effectively determines the answer, flag it rather than defending it.
```

Review the wording as content before reviewing its fit in the frame. If the agent shortens the feedback to make the layout tidy, check whether the explanation survived. A component's text budget should be a design constraint with alternatives, not a reason to delete the part that teaches.

> **RUN SLOT 7.2.** Save proposed and approved feedback, hint rationales, rendered states, and unresolved content questions. Record whether any hint was rejected or replaced.

### Your Turn in Figma

Follow a real path through the prototype. Choose an option, edit it, open a hint, close it, commit, inspect feedback, and request a retry. At each point ask what the learner now knows and what the record now claims.

Correct the first important defect you observe. It may be a leaked answer, feedback that attributes a motive to the learner, or a retry label that overstates independence. Give your reason after the agent presents the captured change. If no failure occurs, record that outcome and choose a deliberate test mutation in a sandbox, clearly labelled as planted rather than observed agent failure.

> **RUN SLOT 7.3.** Save the path, defect evidence, human diff and reason, and constraints. Keep planted defects separate from naturally observed defects in all summaries.

### Round 4: The Agent Repairs and Red-Teams

```text
Preserve the human correction and repair related states. Then test every
pre-commit route in the transition table, including empty submission, changing
selection, opening/closing hints, repeated Check, Back, and exit/re-entry where
the prototype supports them. Report untestable routes explicitly.

For retry, distinguish same-item solution-exposed practice from a new parallel
item. Do not reset assistance or solution-exposure history to make a score look
independent. Run check-constraints before recording.
```

A route audit needs explicit coverage. "Tested the flow" is not enough. List each edge and result. An agent may faithfully click the happy path while never testing an empty submission or a return from the hint panel. The untested paths are where a subtle information leak can live.

For a built version, extend the test to keyboard focus, accessible names, network and storage behavior, and authoring data exposure. These remain handoff acceptance tests until the build exists. Chapter 10 and Chapter 14 carry them forward.

> **RUN SLOT 7.4.** Save edge coverage, constraint output, leaks found, repairs, and runtime-only acceptance tests. A not-run edge must remain not run in the chapter's final verdict.

## The provenance this chapter adds

```json
{
  "chapter": 7,
  "commit_definition": "explicit Check submission",
  "transition_coverage": "RUN",
  "hint_content_review": "RUN",
  "human_reason": "RUN: verbatim",
  "observed_answer_leaks": "RUN",
  "planted_test_defects": "RUN: separate from observed failures",
  "runtime_checks": "not-run"
}
```

This sketch records more than the final screenshot. It can explain which path exposed a solution and which human correction became the next reusable rule.

## The check

**The machine half:** enumerate states and edges, test declared guards, locate explicit key styling or text in observable pre-commit states, and preserve captured constraints. A machine cannot establish that a hint is safe merely because it does not contain the key's exact words.

**The human half:** judge whether feedback explains, whether a hint leaves meaningful work, and whether the learner can recover without confusion or shame. Review every claim about the learner's reasoning against what was actually submitted.

**What neither proves:** that the timing and wording improve retention for the intended population. We have a behavioral contract and content review, not a learning-effect estimate.

## Exercises

**Warm-up**

1. *(Low; define.)* Write an exact commitment event for a short-answer item. Name one action that looks like commitment but is not under your contract.
2. *(Low; write.)* Replace "Correct!" with feedback that explains one reason and one boundary without adding unsupported claims about the learner.

**Application**

3. *(Medium; build.)* Construct a three-rung hint ladder and write what thinking remains after each rung. Reject any rung that ends the target task.
4. *(Medium; red-team.)* Audit all pre-commit paths for one item. Include at least one route that is not the happy path and record untestable routes.
5. *(Medium; specify.)* Design recovery from an interrupted submission. State which response and assistance data must survive.

**Synthesis**

6. *(High; specify.)* Compare same-item retry with a parallel-item retry. Update both the feedback and progress interpretations.
7. *(High; evaluate.)* A learner asks to view the solution without attempting. Specify a humane route that does not misclassify the resulting activity as independent retrieval.

**Challenge**

8. *(Open; red-team.)* Design an answer leak that does not appear in the default screenshot and does not repeat the exact answer text. Test whether the reviewer can detect it from the available evidence.

## What you can now do

You can specify the information boundary around an attempt, write feedback tied to reasoning, and keep assistance and exposure visible in the evidence record. You can also say exactly which behavior a prototype has not proved.

## Credit the AI

**Planned contribution:** state table, prototype adaptation, proposed feedback, and route audit. **Observed errors:** RUN. **Verification:** inspect transitions and content yourself, distinguish planted from observed defects, and never convert a missing runtime test into a pass.

## Next

An item can preserve a useful retrieval attempt and still appear at the wrong time. Chapter 8 moves from the within-item state machine to the states a learner encounters across days.
