# Chapter 8 - Retrieval and Spacing Flows
*You can draw tomorrow's review screen without having built tomorrow.*

> **Rough draft - pre-research.** Learning lead: LXD Chapter 3 and its retrieval/spacing references. Tool lead: FEA `examples/film-23/MAKE-BRIEF.md`, explicitly a pending brief, plus `CAPABILITIES.md` `[VERIFY]`. The schedule below is illustrative, not an evidence-optimized prescription. No scheduler or Make application has been built for this chapter.

## The concept

A prototype can show a button labelled "Review tomorrow." That label does not create a tomorrow. It does not persist an attempt, compute a due time, survive a device change, or decide what happens when the learner returns a week late.

The visual design still matters. A due screen tells the learner why an item is back. An overdue screen can invite useful practice or turn a missed day into a punishment. A review queue can distinguish new work from revisiting prior work, or blend them so completely that the learner cannot interpret progress.

This chapter separates two tasks: representing a spaced-retrieval experience and implementing its scheduling policy. Figma can help us inspect the states and their meaning. A durable scheduler needs a real implementation with time, storage, and tests. An optional Make route may be a way to build that implementation if current access and capabilities support it. It is not automatically supplied by the design file.

### Spacing Is a Learning Decision, Not a Date Decoration

LXD Chapter 3 treats retrieval and distributed practice as learning-design mechanisms and points to primary research. This book uses that argument to require a meaningful review opportunity, not to declare one interval sequence best for all material, learners, and retention goals.

For a teaching example, use three sessions labelled Day 1, Day 3, and Day 10. Those are placeholders that make state changes visible. They are not a scientifically optimized schedule. The actual interval policy should depend on the lesson's purpose, the review horizon, the kind of performance, and the evidence available.

Likewise, not every repeat is retrieval. If the review screen opens with the answer visible, the learner may be restudying. If the same exact response is remembered from a recent attempt, success may say less about transfer than a new case would. Preserve the item-state rules from Chapter 7 and choose review items for the evidence you want.

### Separate the Queue From the Policy

The **queue** is what the learner sees now: items due, new items, unavailable work, and the next action. The **policy** decides how an event changes future due times and evidence status. A neat queue does not prove the policy is correct.

For this prototype, use a deliberately simple policy with explicit boundaries. A committed review attempt creates one attempt record. Its support and solution-exposure context remain attached. A scheduling rule selects the next due time according to a versioned policy. A missing attempt creates no correctness result. An overdue item remains available under a specified catch-up rule.

I do not want a button called Again to mean five different things. It might mean wrong, uncertain, wants more practice, or had help. Those are different observations. If a self-rating is used, call it a self-rating. Do not silently translate it into mastery. Chapter 11 will show why the distinction matters on the dashboard.

### Time Has Semantics

"Three days later" can mean seventy-two hours after submission or the start of a local calendar day three dates later. Neither interpretation is universally right. A classroom deadline may use an institution's time zone; a self-paced review may use elapsed time. State the policy and keep it consistent.

For an implementation brief, record an authoritative event timestamp, the relevant time zone or calendar policy, the policy version, and the computed due time. Do not let the learner's device clock silently become the authority for a multi-user service. If the prototype uses a manual day selector, label it as a simulation control and keep it outside the learner-facing claim.

Other edge cases follow immediately: a repeated submission, a refreshed page, an offline attempt synchronized later, and an item whose content changes after scheduling. The visual flow does not need to solve all of them now. The handoff does need to name them.

### The Required Screens

The demonstration flow needs these states:

| State | Learner question | What the interface must not imply |
|---|---|---|
| New | What should I try first? | New means weak or failing |
| Due | Why am I seeing this again? | A due item proves forgetting |
| Nothing due | Is there useful optional work? | No due work means permanent mastery |
| Overdue | Can I still continue? | A missed day erases prior evidence |
| Review attempt | What must I produce now? | A previously seen solution makes this independent |
| Review feedback | What should I revise? | One attempt settles durable learning |
| Return scheduled | When and why will I revisit? | The interval is an optimal prediction |
| Save/sync error | Was my work retained? | A failed save is a wrong answer |

The interesting trade-off is between simplicity and truth. "You're all done" is simple. "Nothing due under the current policy" is more accurate but can sound technical. Write learner-facing language that preserves the boundary without exposing the scheduling machinery as jargon.

<!-- [INFOGRAPHIC: three review sessions on a timeline, with separate lanes for learner-facing states, stored attempt events, and the scheduling policy; label intervals illustrative] -->

### A Worked Scheduling Example, With Its Assumptions Exposed

For a deliberately simple illustration, choose elapsed time from the first accepted session, with reviews after two and nine days. This yields the labelled Day 1, Day 3, and Day 10 sequence when the first session is called Day 1. The numbers are a demonstration choice, not a recommendation derived from evidence for this lesson.

Now ask what happens if the first review is completed late. One policy retains the original second due time. Another reanchors it to the late review. A third routes the learner to a shorter catch-up sequence. All can be drawn with the same three screens. They produce different real behavior. The policy must choose one, and its reason should be documented.

For this illustration, suppose the policy retains the original planned dates and shows any overdue review as available. That is a simple specification a learner can understand. It also means two reviews could become due close together after a long absence. The handoff should name that consequence and decide whether to cap or combine the queue. Do not discover the consequence only after a real learner returns late.

Next consider an assisted response. The scheduling rule may retain the same interval while the evidence model labels the response supported, or it may choose a different next review. Either way, keep the raw assistance event. Scheduling must not rewrite history to justify its choice.

### Boundary Tests for the Built Scheduler

Write small deterministic tests before trying the application over several actual days. A test clock can exercise time without waiting, provided the implementation exposes a controlled test interface. Keep that interface unavailable to normal learners and label test results as simulated-clock behavior, not longitudinal use.

Useful cases include just before due, exactly due, just after due, a late return with several due items, a duplicate attempt ID, and an edited item version. If the policy uses calendar dates, include the relevant local-date transition and any daylight-saving boundary that affects the chosen interpretation. If it uses elapsed durations, test that those durations are not accidentally implemented as local date arithmetic.

The expected outcome should be explicit before the run. "It looks about right" is not a scheduling test. Record the input event, policy version, clock value, expected due state, actual due state, and storage result. A failed test should remain in the report after repair, linked to the rerun.

### Notifications Are a Separate Product Decision

A scheduled review does not require an email or push notification. Adding one creates permission, frequency, identity, and delivery responsibilities. The prototype can describe a reminder, but the application must have an authorized way to send it and a clear way for the learner to control it.

For this book's core exercise, leave notifications out. The learner can return to a due queue. If a project adds reminders later, treat them as a separate bounded feature with appropriate review. Do not let an agent connect a real messaging service because a timeline annotation says "remind learner."

The omission is intentional scope control. It lets us test the learning-state and scheduling contract before adding another operational system. A small queue whose dates and records are correct is a stronger starting point than a wide feature set that cannot explain why an item is due.

### Keep Content Eligibility Separate From Due Time

An item can be due under the schedule and unavailable for another reason. Its rubric may be under review, the content may have changed, or an access alternative may be incomplete. Do not let the queue display it as ready merely because a date comparison is true.

Define eligibility as a separate condition in the implementation brief. A due but unavailable item should explain the next safe action without exposing private administrative details. Its absence from the active queue must not be interpreted as a successful review or an incorrect attempt. If an instructor replaces it, preserve which item version the learner actually encountered.

This separation also helps with optional practice. A learner may choose an eligible item before it is due. The policy needs to say whether that practice changes the future schedule and how the attempt is labelled. There is no universal answer in this prototype. The important point is that an early practice action should not quietly become the scheduled delayed check simply because both use the same screen.

Write these decisions down before observing the results. Otherwise a convenient label can change after the fact to make the review flow appear more complete than it was. The schedule, queue, and evidence model should agree on what happened while retaining their different jobs.

## What you'll be able to do

- **Design** a multi-session retrieval flow without confusing a pictured date with a running scheduler.
- **Specify** a versioned scheduling policy and its time semantics.
- **Distinguish** correctness, assistance, confidence, and missed follow-up.
- **Compare** a state prototype with an optional implemented route using observed cost and behavior.

**Plan:** all for the proposed state/specification route; optional Make section HE, both provisional. **MCP budget:** planning ceiling 24 requests for the state prototype; actual RUN. **Make/agent cost:** separate meters, RUN. **Builds on:** Chapters 6-7.

## Talking to Figma

### Round 1: Prototype the Sessions

```text
Create learner-facing states for New, Due, Nothing due, Overdue, Review,
Feedback, Return scheduled, and Save error. Reuse the approved item contract.
Use Day 1, Day 3, and Day 10 only as an illustrative schedule.

Add a clearly labelled moderator-only simulation control for the prototype.
Do not claim a durable clock, database, notification, or real schedule exists.
Annotate which transitions are simulated and which are implemented. Preserve
the Chapter 7 answer boundary and assistance history. Save scripts and evidence.
```

A prototype may support time-based animation or delayed transitions. That does not make it a persistent calendar service. The limitation is not that no notion of time can exist in a prototype; it is that our pictured review flow has not demonstrated scheduling across real sessions and devices. Use that precise language.

> **RUN SLOT 8.1.** Save the state map, exact scripts, screenshots, implemented/simulated transition list, and request count. Record how the simulation control is kept distinct from the intended learner experience.

### Write the Policy as a Contract

Before asking for an implementation, complete a policy record:

```json
{
  "policy_id": "demo-fixed-review-v1",
  "status": "illustrative; not validated",
  "time_basis": "RUN: choose elapsed-time or calendar policy",
  "intervals": "RUN: explicit units and anchor event",
  "late_return": "RUN: catch-up rule",
  "assisted_attempt": "RUN: scheduling treatment",
  "missing_followup": "no correctness inference",
  "duplicate_submission": "one accepted event per attempt_id",
  "content_revision": "RUN: invalidate, retain, or review manually"
}
```

The RUN fields are decisions to make, not absent evidence to fill with invented values. For an instructional exercise you can choose a simple rule and mark it as a choice. Do not claim that the choice was derived from a study unless you actually did that research.

For example, an elapsed-time demonstration can anchor each interval to the last accepted attempt. A calendar-day demonstration can anchor to a declared local date. Test the chosen policy at boundaries. Do not mix the two in implementation and call the discrepancy a display problem.

### Your Turn in Figma

Inspect the overdue state. Does it shame the learner, erase progress, or imply failure without an attempt? Rewrite it so the next learning action is clear. Then inspect Nothing due. Does it offer optional practice without claiming permanent mastery? Correct one actual problem and give your reason.

Your reason might concern the interpretation of missing evidence. That is not merely a tone preference. The progress model must agree with the wording. If the dashboard counts a missed review as wrong while the screen says "your work is saved," the contradiction belongs in the contract, not just the copy.

> **RUN SLOT 8.2.** Save the human diff and reason, updated state text, and any policy change required. Keep missing participation separate from observed incorrect answers.

### Round 3: Read the Schedule Back

```text
Read the scheduling annotations through the same path the implementation agent
will receive. Return the exact policy ID, anchor event, units, time basis, and
late-return rule you can recover. List anything missing or contradictory.
Do not infer a policy from the drawn distances between timeline labels.

Preserve the human correction and run check-constraints for supported snapshots.
```

This applies Chapter 3 to a new kind of meaning. An arrow from Day 3 to Day 10 may look self-explanatory to a reader. It does not specify whether an early retry resets the anchor or whether the next review remains tied to the first session. The policy must say.

> **RUN SLOT 8.3.** Save the raw read-back, recovered policy, missing fields, and constraint result. A missing policy field blocks claims about scheduler correctness even if the prototype flow is attractive.

### Optional Round 4: Build a Small Working Version

FEA's film-23 Make brief describes a flashcard application, but explicitly says it had not been run. Its credit examples are source-page illustrations, not observed costs for that brief `[VERIFY: FEA examples/film-23/MAKE-BRIEF.md]`. Do not cite them as this chapter's result.

If current access allows a Make or code route, provide a bounded implementation brief:

```text
Implement only the reviewed review-policy contract and its learner states.
Use synthetic content and test accounts, not real learner data. Store attempt
IDs, item/content version, policy version, authoritative timestamps, response,
assistance/exposure, and next_due. Keep identity data private.

Test duplicate submission, refresh, late return, no due items, save failure,
and the declared time boundary. Do not add notifications or publish anything.
Report current access requirements and meter readings before and after work.
```

Do not wire real accounts or a production backend just to demonstrate a queue. A local or controlled test implementation may be sufficient. If external storage is necessary, use the project's approved secure configuration path and keep credentials out of chat and source control.

> **RUN SLOT 8.4.** Save the brief, implementation provenance, test outputs, meter observations, and unimplemented requirements. If the optional route is unavailable, write unavailable, not failed learning design.

## The provenance this chapter adds

```json
{
  "chapter": 8,
  "schedule_status": "illustrative",
  "prototype_state_coverage": "RUN",
  "policy_readback": "RUN",
  "human_reason": "RUN: verbatim",
  "persistent_scheduler": "RUN: built, unavailable, or not attempted",
  "actual_cost": "RUN: separate meters"
}
```

The record prevents a future summary from collapsing a design, a brief, and a working application into one claim.

## The check

**The machine half:** validate policy fields, transition coverage, timestamp units, duplicate-event handling, and actual computed due times in a built test. In a design-only route, it can check specification completeness, not scheduler behavior.

**The human half:** judge whether the review asks for retrieval, whether its explanation makes sense to learners, and whether overdue language respects missing evidence. Review whether repeated items still fit the objective.

**What neither proves:** an optimal interval or a causal retention benefit for this lesson. A correctly implemented policy can still be instructionally weak. Chapter 13 collects limited learner evidence rather than making that leap.

## Exercises

**Warm-up**

1. *(Low; distinguish.)* Explain why Nothing due and Mastered are not equivalent states.
2. *(Low; specify.)* Define "three days later" in two different ways and name a case in which the difference affects the queue.

**Application**

3. *(Medium; design.)* Prototype a late return without turning missing participation into an incorrect answer.
4. *(Medium; specify.)* Write a policy for an assisted review attempt. State which part is an instructional choice rather than a research-backed optimum.
5. *(Medium; compare.)* If you build a scheduler, test one duplicate event and one time boundary. If not, write the acceptance tests and label them unrun.

**Synthesis**

6. *(High; distinguish.)* A learner selects Again after a correct answer. Specify how confidence, correctness, and scheduling are recorded without conflating them.
7. *(High; evaluate.)* Compare the state prototype and working route on inspectability, cost evidence, persistence, and access. Do not use predicted cost as measured cost.

**Challenge**

8. *(Open; design.)* Propose a study that could distinguish improvement from repeated item familiarity. State what this chapter's current prototype cannot tell you.

## What you can now do

You can design a review experience, state its scheduling contract, and distinguish simulation from implementation. You can also preserve the meaning of missed, assisted, and repeated attempts as work crosses sessions.

## Credit the AI

**Planned contribution:** state prototype, policy read-back, and optional implementation. **Observed errors and cost:** RUN. **Verification:** inspect raw policy evidence, exercise boundary tests in a real build, and keep unavailable or unrun routes explicit.

## Next

The review flow controls when effort occurs. Chapter 9 examines where the effort goes inside each screen, and which parts of that judgment can be checked automatically.
