# Chapter 5 - Variables as Pedagogy: Support Levels as Modes
*The same task can need more help without needing a different answer.*

> **Rough draft - pre-research.** Learning leads: LXD Chapter 3 on worked examples and expertise reversal. Tool leads: FEA `examples/film-12/01-variables.js`, `02-component.js`, and `03-prototype.js` `[VERIFY]`. The support model below is a proposed contract, not an executed adaptation or validated adaptive policy.

## The concept

Imagine two learners facing the same diagnostic case. One has never distinguished the learner's task from the interface's demands. The other has designed practice activities for years. Giving both an empty explanation field is not equal support. Giving both a full worked solution is not necessarily better.

The task should remain identifiable as support changes. That is the design problem in this chapter. We will build three support conditions around one performance rather than create three unrelated activities and call the difference personalization.

LXD Chapter 3 treats worked examples, fading, and expertise reversal as decisions relative to prior knowledge and the task. I use that argument here without pretending a screen can diagnose expertise from confidence, speed, or one right answer. The interface can represent support conditions. Choosing when a learner should receive each condition requires an evidence policy.

### Separate Demonstration From Retrieval

Start with a distinction the component library must not blur. A **demonstration** shows a worked solution so the learner can study the reasoning. A **practice attempt** asks the learner to produce something before the solution is revealed. Both may use the same visual family. They have different evidence meanings.

If the Full mode contains the answer to the exact item being scored as independent practice, the learner is no longer retrieving that answer independently. That is not a small implementation defect. It changes the task. I therefore use a parallel example for Full support, clearly labelled as a demonstration, and retain a separate target item for the learner's attempt.

This is a design choice for our lesson. Some curricula deliberately use completion problems or open-reference performance. Those can be legitimate tasks. They must be named and interpreted as such. The rule is not "answers must never appear." It is "do not mislabel exposed-answer performance as independent retrieval."

### Three Support Conditions

For the demonstration unit, define these conditions:

| Support | Visible help | Learner still supplies | Evidence label |
|---|---|---|---|
| Full | A parallel worked case, diagnostic questions, explained step structure | A judgment and reason for the target case | Supported attempt |
| Partial | Diagnostic questions and an incomplete reasoning scaffold | Missing reasoning and the target judgment | Partly supported attempt |
| Independent | The target case and response controls; optional help clearly available | The full judgment and reason | Independent only if no help used |

Support condition and item state are different dimensions. An unanswered item in Partial support is not the same thing as a committed answer in Partial support. If you use one mode selector to encode both, the combinations become ambiguous. Keep `support_level` separate from `attempt_state`, and keep any appearance theme separate from both.

The word Independent names the requested condition, not a permanent label for the learner. If they open a hint, the observed attempt becomes supported. Do not conceal that assistance or punish it with a moralizing label. Record what happened so the interpretation stays honest.

### What Variables Can Carry

Variables let a design represent named values. Modes group alternative values under a selected condition. The sibling film-12 source creates color and string variables for four tutor states, then binds them in a component and connects prototype states. That is an inspectable local precedent, not proof that every desired support binding works `[VERIFY: FEA examples/film-12/01-variables.js and 02-component.js]`.

For the live chapter, verify which current types and properties support the bindings you need. A text label, visibility flag, layout dimension, and prototype condition are different capabilities. Do not imply that creating three modes automatically implements a support-state engine.

The proposed data contract is simpler than the API:

```json
{
  "support_level": "Partial",
  "attempt_state": "unanswered",
  "target_item": "LOAD-01",
  "show_parallel_example": false,
  "show_diagnostic_prompts": true,
  "show_target_solution": false,
  "assistance_used": false
}
```

This is illustrative state data, not a Figma API call. The agent should map it to currently supported bindings and list any fallback. If a binding is unavailable, explicit variants or separate prototype frames may be more honest than an elegant collection that does not control the rendered result.

### Fading Is a Hypothesis About Readiness

A mode is a representation. Fading is an instructional policy. Do not make a variable name carry a claim it cannot support. Switching to Independent after the learner has clicked Next twice is a schedule, not evidence that they are ready.

For this prototype, make transitions moderator-controlled or learner-selected and label them as such. A later implementation may use assessment history, but it needs a stated rule and a way to recover when the decision is wrong. Chapter 11 distinguishes supported from independent evidence; Chapter 13 tests how learners interpret the available help.

The trade-off is production simplicity against instructional validity. Three explicit support states are easier to inspect than a fully adaptive engine. They do not justify saying that the system adapts effectively. The prototype should expose that boundary rather than hide it behind the word personalized.

<!-- [TABLE: support level crossed with attempt state, showing that solution visibility depends on both and that demonstration content uses a parallel item] -->

### Model the Cross-Product Before It Becomes a Variant Explosion

Three support conditions and several attempt states create combinations. Add a visual theme, an error state, and a small-screen layout, and the library can become difficult to inspect. The answer is not to create a named variant for every imaginable combination without asking whether it is valid.

Make a state matrix first. Mark combinations valid, invalid by contract, or not implemented. For example, Full support with an unanswered target item is valid when the worked content concerns a parallel case. A condition that shows the target solution while reporting an unassisted independent response is invalid under this project's contract. A persistence error might be outside the design prototype but required in the build. Those three statuses should not look identical in the library reference.

The matrix helps the agent avoid improvising missing states. If a requested combination is invalid, it should explain the conflict and offer an allowed alternative. If it is valid but unimplemented, it can propose the work. If it is merely untested, it should not call it unsupported. Precise state language reduces both accidental compliance and unnecessary refusal.

### Inspect Inheritance and Overrides

The resolved appearance may depend on values inherited from a parent, a component default, or an instance override. The current mechanics need live checking, but the design question is stable: which value actually controls the thing the learner sees?

Ask the agent to trace one visible help element from its intended support condition to its resolved property. Then change the condition and inspect the result. If the layer stays visible because of an override, the collection can be correct while the screen is wrong. Conversely, the screen can look right because of a manual override while the reusable system is broken. Both cases matter before a new item is generated.

For this reason, keep a distinction between **contract test** and **screenshot test**. The screenshot tells you whether the current rendering meets the intended state. The contract test tells you whether changing the input produces the intended relationship. One correct picture is not a reusable support system.

### Let Learners Recover From a Bad Support Choice

A system can choose too little help. A learner can also choose Independent because they misunderstand what it means. The interface should offer a clear way to request support without destroying the response or pretending the earlier work never happened.

Likewise, a learner who has already studied a full worked example may want to try a new case without it. Do not make them repeatedly dismiss the same scaffold if the target task no longer needs it. That decision still requires an evidence policy; the interface should at least make the available path explicit and nonpunitive.

The important observation is not whether a mode selector looks intuitive to the designer. It is whether intended learners can predict what changes and what stays the same. Does changing support replace the question? Does it reveal the target answer? Does it affect how the response is interpreted? Chapter 13 can ask those questions directly rather than assuming that the names Full and Partial explain themselves.

This is also a reason not to expose every authoring control as a learner control. The author may need to preview all state combinations. The learner needs an understandable way to ask for help within the task. A raw variables panel is not an instructional interaction simply because the agent can manipulate it.

When you name the support controls, prefer language that describes the action over language that ranks the person. "Show a worked example" is a request. "Beginner mode" can sound like an identity judgment and may obscure what will change. The exact wording needs learner review, but the design principle is concrete: make help predictable without pretending the interface has diagnosed the learner. Keep the author's preview controls separate from that learner-facing choice, and test whether people can explain the consequence before activating it.

## What you'll be able to do

- **Design** support conditions that preserve a target performance while changing the help available.
- **Separate** support level, response state, theme, and observed assistance use.
- **Map** the contract to verified bindings or explicit fallbacks.
- **Evaluate** whether a support transition reflects evidence or merely elapsed interaction.

**Plan:** all, provisional; mode counts and bindings must be checked in the actual account. **MCP budget:** planning ceiling 25 requests; actual RUN. **Builds on:** Chapters 3-4.

## Talking to Figma

### Round 1: Build One Item in Three Conditions

Use one target item from the inventory. Supply a human-reviewed parallel worked case so the agent is not simultaneously inventing content, scoring logic, and support behavior.

```text
Build Full, Partial, and Independent support conditions for target item LOAD-01.
Keep support_level separate from attempt_state and visual theme.
Full shows the supplied parallel worked case, never the target solution before
commit. Partial shows the diagnostic scaffold. Independent hides that scaffold
but keeps an accessible route to request help. Label assistance honestly.

First inspect current variable types, mode availability, and binding support.
Propose a mapping table. If a required binding is unsupported, use an explicit
variant or frame fallback and report it. Do not invent an API capability.
Save scripts, read back resolved states, and follow PROVENANCE.md.
```

Review the mapping before drawing if it contains an unresolved information boundary. It is acceptable for the agent to stop with "I cannot verify this binding." It is not acceptable to draw all help layers and assume the mode name will hide them later.

Ask for screenshots of all three resolved conditions using the same target content. A screenshot of the variable collection alone does not show whether the frame uses it. Read-back should identify the selected condition, resolved values where available, and any hard-coded overrides.

> **RUN SLOT 5.1.** Save the mapping table, exact scripts, variable and binding evidence, three rendered states, and observed request count. Record unsupported properties and fallbacks. Do not substitute film-12's measured session for this chapter's budget.

### Work Through a Support Decision

Consider the target case: a learner must classify the effort spent repeatedly looking up a navigation symbol while attempting to compare two study schedules. The proposed Full support presents a different example in which a learner searches for an unexplained control before beginning the learning task. Its explanation demonstrates how to separate tool management from the target reasoning.

Partial support asks, "What is the learner trying to learn? Which part of the effort goes into managing the interface?" It leaves the classification and reason unanswered. Independent presents the case without those prompts. The target answer remains hidden in all three pre-commit conditions.

The difference is not the amount of text alone. Full models the process on another case. Partial cues the process. Independent asks the learner to initiate it. If the agent merely deletes every second sentence in Full to create Partial, it may remove the reasoning link while retaining the answer. Inspect the help by its instructional role, not its word count.

### Your Turn in Figma

Check one support boundary. Does the Full example accidentally use the target case's names or facts so closely that it gives away the classification? Does Partial still require a meaningful step? Does Independent hide the help button as well as the scaffold?

Correct the problem by hand. Keep the reason focused on the task. "Shorter" is a visual instruction; "the learner still has to decide which effort serves the objective" is an instructional rationale. The agent should record your words, not replace one with the other.

> **RUN SLOT 5.2.** Save the diff, your reason, the active constraints, and the affected support/attempt combinations. If a variable binding obscures the actual change, record the resolved values before and after as well as the visual result.

### Round 3: A New Item Uses the Same Support System

```text
Apply the approved support contract to a new item about worked-example fading.
Do not copy the first item's answer or example. Keep my constraints on the
original item. Show all pre-commit conditions, then one post-commit feedback
state. Report assistance use separately from the requested mode.

Run check-constraints. Flag any state combination that is unsupported or whose
solution visibility you cannot determine. Do not mark it passed by analogy.
```

A new item tests whether the abstraction is useful. Reusing the first item's content only tests whether the same drawing can be copied. The new example should preserve the role of help while changing the domain facts.

> **RUN SLOT 5.3.** Save the new item, condition matrix, constraint output, screenshots, and assistance labels. Compare human corrections needed on the first and second items, but do not infer a general efficiency gain from two items.

### Round 4: Test the Transition Boundary

Ask the agent to move between support levels before and after commitment. A change of support must not erase the learner's current response, silently reveal the key, or reset an assisted attempt into an independent one. These are proposed invariants for this demonstration.

```text
Test changing support while a response is still a draft, after commitment, and
after opening a hint. Use the transition table, not only screenshots. Preserve
the response and assistance history. If the prototype cannot model persistence,
label that limit and include the requirement in the handoff specification.
```

This is where a drawing becomes a behavioral specification. A static set of three frames can show alternatives. It cannot by itself demonstrate that changing support preserves data. If the prototype route cannot test that behavior, do not overstate it. Write the acceptance test for the built version.

> **RUN SLOT 5.4.** Record tested transitions, untouched transitions, persistence limits, and the handoff acceptance test. An unimplemented edge remains unimplemented even if both endpoint screenshots exist.

## The provenance this chapter adds

```json
{
  "chapter": 5,
  "support_contract": "Full | Partial | Independent",
  "binding_verification": "RUN",
  "parallel_example_review": "RUN",
  "human_reason": "RUN: verbatim",
  "new_item_generalization": "RUN",
  "adaptive_readiness_policy": "not-implemented"
}
```

This sketch separates a demonstrated representation from an untested instructional policy. It lets the final portfolio say exactly what the support system does.

## The check

**The machine half:** compare declared and resolved values, enumerate support/attempt combinations, detect missing bindings, check captured constraints, and flag assistance history that disappears. It cannot decide whether a parallel example is instructionally appropriate merely because the IDs differ.

**The human half:** judge whether each condition leaves the intended thinking with the learner, whether the scaffold fades a meaningful step, and whether requesting help is understandable and nonpunitive.

**What neither proves:** which fading schedule improves learning for this population. That needs evidence beyond a working switch. Do not promote a prototype control into a validated adaptive policy.

## Exercises

**Warm-up**

1. *(Low; separate.)* Explain the difference between Full support and post-commit feedback. Give a case in which confusing them would expose the answer.
2. *(Low; design.)* Write a Partial scaffold that cues a reasoning step without naming the target classification.

**Application**

3. *(Medium; map.)* Create a binding table with current evidence for every property. Include a fallback for one unavailable binding.
4. *(Medium; evaluate.)* Inspect three resolved states for hard-coded overrides. Report what the variable collection alone would have missed.
5. *(Medium; design.)* Add a fourth condition for a completion problem. State how its evidence differs from an independent attempt.

**Synthesis**

6. *(High; evaluate.)* A learner requests help after drafting half an explanation. Specify response preservation and assistance labeling across that transition.
7. *(High; separate.)* Propose a readiness rule and list the evidence it requires. Mark which inputs your prototype does not collect.

**Challenge**

8. *(Open; evaluate.)* Design a test that could show your three support conditions are not meaningfully different in what the learner must supply. State what result would make you redesign them.

## What you can now do

You can encode support without confusing it with answer exposure or learner expertise. You can inspect the resolved result rather than trusting mode names, and you can hand off the boundaries a prototype cannot execute.

## Credit the AI

**Planned contribution:** propose the binding map, construct states, and enumerate transitions. **Observed errors:** RUN, particularly answer leaks, meaningless fading, and overwritten assistance history. **Verification:** inspect the target performance in every condition and test a new item under the same contract.

## Next

Support is one dimension of an item. Chapter 6 builds the other reusable structure: what kind of response the learner gives, what counts as a valid item, and which parts of that contract an agent can actually check.
