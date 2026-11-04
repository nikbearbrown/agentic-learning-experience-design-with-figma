# Chapter 10 - Accessible Learning Items
*If the learner cannot operate the item, the response is evidence about the barrier.*

> **Rough draft - pre-research.** Learning lead: LXD Chapter 9 on variability, accessibility, and the limits of broad UDL claims. Figma annotation/read-back leads: FEA `CAPABILITIES.md` `[VERIFY]`. This chapter proposes design and test contracts; it does not certify compliance with any standard. Current standards, platform behavior, and institutional requirements need primary-source review before release.

## The concept

Imagine a learner who understands the case but cannot move an ordering tile without a mouse. The system records an incomplete answer. If the dashboard interprets that as a conceptual weakness, the interface has converted an access barrier into a false claim about learning.

This is why accessibility belongs inside the item contract, not in a final polish pass. It affects what the response means. A task that cannot be operated, perceived, or interpreted by the intended learner cannot give us the evidence we thought we were collecting.

Figma can carry requirements and show proposed states. It cannot, by itself, prove how a browser's focus order, semantic controls, assistive technology, zoom behavior, or error recovery will work in the implementation. This chapter makes the distinction operational rather than burying it in a disclaimer.

### Three Layers of Evidence

Separate **design intent**, **implementation behavior**, and **learner experience**.

Design intent includes a visible focus state, a label specification, a proposed reading order, an alternative response method, and state annotations. Implementation behavior includes the actual semantic controls, focus movement, keyboard operation, accessible names, announced feedback, and layout under relevant settings. Learner experience concerns whether intended people can use those features to do the learning task.

The layers support one another but do not collapse. An annotation saying "keyboard accessible" is not implementation evidence. A passing automated scan is not a complete account of learner experience. A successful session with one person does not prove universal access. The book should say exactly which layer was examined.

### Preserve the Construct While Changing the Route

The construct is the capability the item is intended to assess. In our case, it is a diagnosis and explanation about learning effort. Dragging a tile is not the construct unless the lesson explicitly aims to teach dragging.

An ordering task should therefore have a non-drag way to produce the same ordering when required by the access contract. A diagram task may need an equivalent description, a structured data representation, or another interaction. The alternative should preserve the target reasoning without accidentally giving away the answer.

This takes judgment. A text alternative that names the correct classification can turn a reasoning problem into a lookup. An alternative that omits a relation visible in the diagram can make the task harder or impossible. Do not approve equivalence by checking that an `alt` field is nonempty. Compare the information and work available through each route.

Sometimes the medium is part of the target. If learners are interpreting a visual notation, a purely textual substitute may not assess the identical skill. State that boundary and design an appropriate accessible learning route with relevant expertise. Do not claim equivalence simply to close a checklist.

### Focus Is a State, Not a Decorative Outline

The design should specify where focus begins, how it moves among controls, what happens when a hint or feedback region opens, and where it returns when a transient region closes. The built version must then be tested with the actual input and assistive-technology combinations in scope.

A focus ring drawn around a rectangle shows intent. It does not make the rectangle focusable. Likewise, visually placing the question before the answer options does not guarantee a meaningful reading order in code. These properties need explicit handoff fields and implementation tests.

For our item, write a proposed focus contract rather than prescribe a universal key sequence for every widget. Native controls and established platform patterns should be preferred in implementation. If the agent proposes a custom control, require a reason and a current authoritative pattern before it invents keyboard behavior `[VERIFY: chosen platform and accessibility pattern]`.

### Labels and Feedback Can Leak Answers

Chapter 7's information boundary applies to more than visible text. A response option's accessible name must not contain correctness information before commitment. A hidden explanation must not be announced prematurely. A color-only correctness cue excludes some interpretations and may also conceal missing feedback content.

The design contract should list learner-facing names, descriptions, errors, and feedback announcements by state. Keep authoring names such as `CorrectOption` out of the rendered semantics unless deliberately transformed. A design-file layer name can be useful for authors and inappropriate as a learner-facing label.

After commitment, feedback needs to be available without forcing the learner to discover an unannounced change. The exact mechanism depends on the implementation. Specify the intended experience and test the chosen mechanism, rather than treating one annotation as a complete technical solution.

### UDL Is Not a Substitute for Specific Requirements

LXD Chapter 9 discusses variability and contested claims around broad frameworks. This book does not need to settle that evidence debate to require operable controls, meaningful labels, understandable errors, and alternatives that preserve the task.

Offering three formats does not guarantee that any of them is usable. Giving learners choices can introduce its own navigation burden. Use variability thinking to ask what barriers are likely for the intended learners, then write concrete requirements and test them. Do not use a UDL label as a compliance badge or a causal learning claim.

<!-- [TABLE: accessibility evidence ladder showing design annotation, implemented property, manual test, and learner observation; no row should imply that an earlier layer proves a later one] -->

### An Access Handoff Is a Set of Testable Sentences

Avoid annotations such as "make accessible" or "screen-reader friendly." Replace them with observable expectations. The question has a meaningful programmatic label. The response controls have names that do not reveal the key. A learner can reach and operate the required actions without dragging. Opening a hint does not discard the draft. Feedback becomes available in an understandable way. Closing a transient region returns the learner to an appropriate place.

These sentences are still not implementation evidence. They are better requirements because a tester can act on them. Each should identify the relevant state, platform, and expected result. Where a native control supplies established behavior, preserve that behavior rather than replacing it with a custom pattern for visual novelty.

For a disabled or unavailable action, specify how the learner discovers the reason and what they can do next. A button that simply stops responding can look like a conceptual failure when it is a validation or system-state problem. Keep the error attached to the relevant input and preserve the work already entered.

### Test the Whole State Family

An item that works in its initial state can fail when feedback appears. A new region may be visually obvious but unreachable or unexplained through another access route. A hint can obscure the response controls. A retry can move the learner to the top of the page without context. These are state-machine defects as well as access defects.

Use Chapter 7's transition table as the test index. Add expected access behavior to each relevant edge. Do not create a separate accessibility checklist that never reaches hint, error, retry, and support-change states. The learning interface is the reachable family of states, not the first frame.

Likewise, inspect the interaction under the relevant display conditions. A design that depends on a fixed line length may break when text grows or the viewport changes. The actual runtime requirements need current authoritative review, but the design can already avoid assuming that one screenshot size is the only valid presentation.

### Alternatives Need Version Control Too

If the main case changes, its alternative may become stale. A table can retain an old interval while the timeline shows a new one. A description can refer to a removed label. The two routes then ask different questions even though both pass a superficial completeness check.

Link the alternative to the item-content version and include it in the content review. When the agent edits the item, require a comparison of the information available through each route. The review should identify added facts, missing facts, and answer-bearing interpretations, not merely whether the text was updated.

### Treat Specialist Review as Collaboration

The author need not pretend to be expert in every assistive technology. The useful response to a limit is to prepare a precise test case and bring it to someone qualified to review it. The agent can help package the state, requirement, and reproduction steps. It should not fill the expertise gap with a confident simulated user narrative.

When a real learner encounters a barrier, record the barrier and the environment without turning one person's experience into a universal claim. Their observation can reveal a concrete defect and motivate a repair. It does not remove the need to test other relevant routes, and it does not authorize publishing identifying details. Good collaboration keeps both the specificity of the observation and the limits of the conclusion.

### Make Unrun Tests Visible to the Next Owner

A handoff should not hide an untested access route in a general limitations paragraph. Put it in the acceptance matrix with an owner and the evidence needed to close it. For example, an assistive-technology combination unavailable in the current environment remains not run, even if a different combination passed.

This is not a demand for infinite testing. It is a demand for honest scope. Prioritize the intended learners, platform, interaction risks, and authoritative requirements with the responsible people. Then state that scope so the next owner does not mistake a useful partial test for complete coverage.

The same discipline applies to a proposed alternative that has passed content review but no user trial. It may be a defensible design ready for testing. It is not yet an observed successful route. Preserving that distinction helps the next round ask the right question instead of repeating a broad claim that no one actually tested.

## What you'll be able to do

- **Annotate** an item with explicit focus, semantics, feedback, and alternative-route requirements.
- **Evaluate** whether an alternative preserves the information and performance of the task.
- **Distinguish** canvas intent, built behavior, and learner evidence.
- **Design** tests that detect access barriers without misclassifying them as conceptual errors.

**Plan:** all for design/specification work, provisional. **MCP budget:** planning ceiling 25 requests; actual RUN. **Runtime tests:** separate, not run until a build exists. **Builds on:** Chapters 6-9.

## Talking to Figma

### Round 1: Add the Access Contract

Choose one choice item and one ordering or diagram item. They exercise different risks. Supply the objective and state table so the agent knows what must remain hidden and what performance the alternative must preserve.

```text
For the two selected items, propose an accessibility handoff contract with:
learner-facing labels, semantic control intent, reading order, focus behavior,
keyboard/non-pointer route, error recovery, feedback availability, and any
equivalent alternative. Separate each state before and after commitment.

Annotate supported frame locations and test the actual read-back. Do not claim
the canvas proves runtime accessibility. Use established platform patterns in
the proposed build; flag any custom interaction needing further review.
Save scripts and follow the provenance loop.
```

The contract should identify a requirement's owner. The designer can propose the reading order. The implementer must create it. A tester must exercise it. A content expert must review whether an alternative leaks an answer or changes the construct. Shared responsibility is not a reason to leave the field ownerless.

> **RUN SLOT 10.1.** Save state-specific contracts, annotation read-back, proposed focus states, alternatives, and owner assignments. Mark every runtime property as not run unless tested in a real build.

### A Worked Alternative Review

Suppose the item shows two study schedules on a timeline and asks which arrangement creates more distributed practice under stated conditions. A proposed alternative could list the study events in a table with elapsed intervals. That may preserve the temporal information without requiring the timeline's visual encoding.

Now check the task. If the objective is reasoning about spacing, the table may be a defensible route. If the objective is reading a particular chart form, the table changes the assessed performance. The same alternative can be appropriate for one objective and not equivalent for another.

Also check the wording. "Schedule A, the spaced schedule" exposes the classification. A neutral table should carry the same event information without the answer-bearing label. This is why accessibility content belongs in the item review, not an unrelated asset list.

No learner has performed this alternative in the current manuscript. We are reviewing a design proposal. A live pilot must test whether the representation is understandable to the intended people and whether it introduces new barriers.

### Your Turn in Figma

Inspect the annotations and the alternative side by side with the source item. Correct one concrete mismatch: missing information, a leaked conclusion, a focus return left unspecified, or a control label with no clear action. If you are not qualified to judge a particular assistive-technology behavior, flag it for a specialist rather than inventing a confident correction.

After the agent presents the diff, state your reason. Preserve that reason verbatim. It may say "this alternative tells the learner which schedule is spaced before they decide" rather than simply "change alt text." The former can become a reusable information-boundary rule.

> **RUN SLOT 10.2.** Save the human correction, reason, equivalence review, and unresolved specialist questions. Record whether the change affects only presentation or the actual assessed performance.

### Round 3: Carry the Contract Into a Built Sample

If a runtime sample exists or can be created within the authorized handoff work, select one item rather than claiming the entire lesson is accessible. Keep it private and use synthetic responses.

```text
Implement one reviewed item using native or established controls where possible.
Preserve the learning state machine and all access annotations. Do not publish.
Create a test matrix for keyboard-only operation, meaningful names and reading
order, focus on feedback/recovery, relevant zoom/reflow conditions, and the
alternative route. Use current authoritative requirements for the chosen target.

Run only tests the available environment supports. Save exact results and mark
unsupported device/assistive-technology combinations not run. Do not claim full
standards conformance from an automated scan or a single manual test.
```

This is an optional bridge to Chapter 14, not permission to fabricate a working sample in the text. If no build is available, write the test cases now and retain not run. The chapter still produces a useful, inspectable handoff contract.

> **RUN SLOT 10.3.** Save implementation provenance if present, test environment, exact steps, observed results, and limitations. If absent, save unrun acceptance tests instead. Do not summarize both situations as "accessibility tested."

### Round 4: Test the Evidence Interpretation

Review a hypothetical incomplete response caused by an access barrier. Specify how the event should be recorded: access issue, interrupted attempt, or unavailable evidence under the chosen model, not automatically wrong. Do not invent participant observations to populate the example.

Ask the agent to trace that event into the progress specification. If the dashboard cannot represent it, Chapter 11 must add the distinction. An accessible item and a misleading evidence model are not a coherent system.

> **RUN SLOT 10.4.** Record the evidence-model decision, dashboard implications, and any real implementation test. Keep hypothetical cases labelled hypothetical throughout the report.

## The provenance this chapter adds

```json
{
  "chapter": 10,
  "design_contract_review": "RUN",
  "alternative_equivalence_review": "RUN",
  "human_reason": "RUN: verbatim",
  "built_sample": "RUN: present or not built",
  "runtime_test_matrix": "RUN or not-run",
  "conformance_claim": "none"
}
```

The record prevents a visual annotation from later becoming a blanket claim of accessibility. It also links the alternative's rationale to the objective it must preserve.

## The check

**The machine half:** required labels and annotations, token/property checks within available evidence, and automated runtime checks where implemented. It can flag missing values; it cannot certify an alternative's instructional equivalence from a nonempty description.

**The human half:** review focus and interaction behavior in the actual build, content equivalence, understandable recovery, and learner experience. Bring in relevant expertise rather than treating a general agent as a substitute for every user or specialist.

**What neither proves:** universal usability, legal compliance, or learning effectiveness. Scope the actual environments, users, requirements, and tests. A limited result can still be valuable when it is honestly described.

## Exercises

**Warm-up**

1. *(Low; distinguish.)* Give one example each of design intent, implementation evidence, and learner evidence for the same control.
2. *(Low; annotate.)* Write pre-commit and post-commit names/descriptions for an option without leaking correctness.

**Application**

3. *(Medium; evaluate.)* Design a non-drag route for an ordering task. Explain why it preserves the target performance or why equivalence is not justified.
4. *(Medium; annotate.)* Specify focus behavior for opening and closing a hint and displaying feedback. Mark the runtime test needed for each.
5. *(Medium; design.)* Write an error-recovery test that preserves the learner's draft. Run it only if a build exists and record the actual environment.

**Synthesis**

6. *(High; evaluate.)* Compare a timeline and a table alternative for two different objectives. Show how the judgment changes with the construct.
7. *(High; distinguish.)* Trace an inaccessible response through the progress model without converting it into a conceptual failure.

**Challenge**

8. *(Open; design.)* Create a test matrix for the intended learners and platform. Explain the most important environment it does not cover and how that limits the release claim.

## What you can now do

You can write an access contract that survives handoff, preserve the target task across alternatives, and state precisely what the canvas and the current tests do not prove.

## Credit the AI

**Planned contribution:** contract drafting, annotation, a possible built sample, and test documentation. **Observed errors:** RUN, especially answer-bearing alternatives and overstated test claims. **Verification:** state-specific content review, actual runtime observations, and relevant human expertise.

## Next

Once the learner can produce a response, the system still has to interpret it responsibly. Chapter 11 builds progress views that distinguish independent evidence, supported practice, missing observations, and unresolved barriers.
