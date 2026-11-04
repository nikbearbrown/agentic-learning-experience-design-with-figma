# Chapter 13 - Testing With Learners, Not Pixels
*A compliant screen is still a hypothesis about a person.*

> **Rough draft - pre-research.** Protocol lead: FEA `examples/film-22/PROTOCOL.md`, explicitly unrun in that source. Evaluation leads: LXD Chapter 14 and AI-LXD Chapter 14. The protocol below is a draft for review, not institutional approval, a consent determination, or a completed study. No participants, quotes, scores, or outcomes are invented.

## The concept

By now an agent might build a screen that obeys every rule we have written. The answer stays hidden. Feedback explains. Hints preserve a reasoning step. Support is labelled. The progress view does not call completion mastery. That is a meaningful production achievement.

It still does not tell us whether a learner understands the task, uses the feedback, or can perform later without the support. We have been testing the design contract. This chapter begins testing the human encounter with it.

The blueprint proposes a small formative test with three to five learners, combining observation with a delayed retrieval check. That is enough to produce useful cases and reveal concrete problems. It is not a sample size that by itself establishes efficacy, represents all learners, or supports a broad causal claim. The purpose is to improve the design and report what happened honestly.

### Two Questions Need Different Observations

The first question is usability and interpretation: can the learner operate the item, understand what it asks, find help, and interpret the feedback? A think-aloud or moderated observation can expose those problems.

The second question concerns learning: what can the learner produce later under specified conditions? A delayed task can provide a limited observation of later performance. It does not automatically establish that the interface caused it, especially without a suitable comparison and a design that addresses alternative explanations.

Do not let one method answer both questions by habit. Thinking aloud may change how someone approaches the task. Moderator prompts can become help. Repeating the same item can produce familiarity. A delayed check needs its own instructions, scoring basis, and record of assistance.

### Plan the Claim Before Recruitment

Write a one-sentence claim the test could support. For this formative round:

> We will identify observed interaction and interpretation problems in a small set of intended users and describe their responses to a specified delayed task; we will not estimate a causal learning benefit.

That sentence limits the report in advance. It also changes the protocol. We need detailed observations of failures and recoveries, not an impressive average satisfaction score. We need to know who did not return, without converting absence into a wrong answer. We need to preserve which version each person used.

Choose participants relevant to the intended lesson and record the relevant characteristics privately at an appropriate level. Do not claim representativeness from convenience recruitment. If the intended learners have varied prior knowledge or access needs, state which cases you included and which you did not. Inclusion requires planning, not a sentence in the conclusion.

### Permission and Participation Come Before the Session

Do not recruit or collect data until the responsible institutional process, project owner, and applicable policies allow the activity. Ask the institution to determine any review or consent requirements; this book does not declare an activity exempt or provide legal advice. A draft script in a repository is not permission to conduct research.

Participation should not be confused with assessment in a course. If the moderator also teaches or grades potential participants, arrange an appropriate alternative recruitment and moderation process. Explain voluntariness, what will be recorded, how material may be used, retention, withdrawal arrangements, and whom to contact through the approved process.

The sibling protocol uses a concise spoken consent line for its proposed ten-minute test. That is a useful model of plain language, not a universally sufficient consent procedure. Use the wording and documentation required for this actual setting. Do not copy a line from the book and assume the ethical work is complete.

Keep identities, contact details, consent records, and raw recordings outside the public repository. Codes such as P01 are pseudonyms, not a guarantee of anonymity. A quote or unusual detail can identify someone. Publish only the appropriately reviewed and approved material, with unnecessary detail removed.

### The Delayed Task Needs Its Own Contract

Choose the delay before running the first session. A seven-day check can be an illustrative protocol choice for this lesson, not a universal optimum. Record the actual elapsed interval and any allowed window. A response collected much later should retain that fact rather than be labelled as though it arrived on schedule.

Use a new, human-reviewed case that targets the same performance if transfer is the question. Parallel does not mean proven equal in difficulty. Review the cases and state the remaining uncertainty. If you reuse an item, acknowledge the possibility of item-specific familiarity.

Write a rubric before seeing responses. For the diagnostic objective, the rubric might require a classification, a reason connected to the target task, and an explanation of the proposed change. Define partial or unresolved cases. Do not retrofit the rubric to make the prototype appear successful.

<!-- [TABLE: protocol stages with question, moderator action, assistance allowed, evidence collected, privacy treatment, and limits on interpretation] -->

### Score the Response, Not the Desired Story

Before the first delayed response arrives, write how each criterion will be judged and who will judge it. If feasible, keep the scorer unaware of irrelevant design-version information that could bias interpretation. Do not promise blinding where the response or setting makes it impossible. Record the actual procedure.

For a small formative test, a second reviewer can inspect disputed rubric decisions. The useful output is not necessarily an agreement coefficient from a tiny set. It can be a record of where the rubric was ambiguous and how the author resolved it. If the rubric changes, identify which responses were rescored and keep the original decision trail.

Do not use the same agent that designed the item as the sole judge of its success without scrutiny. It may be helpful as a comparison scorer or a consistency checker, but its fluent rationale is not independent ground truth. Human review of substantive judgments remains necessary for the claims this book makes.

### Missing Follow-Up Changes the Question

If only some participants return, the delayed observations concern those who returned under the recorded conditions. The missing people may differ in ways the study cannot observe. Do not explain their absence as disinterest, forgetting, or a design defect without evidence.

Report the number eligible for follow-up, the number contacted through the approved route, the number returned, and the number with usable responses. Keep the contact details private. Distinguish a late response, a technical failure, a withdrawal, and no response only when the records support those distinctions.

This does not make a small test useless. It makes its scope honest. You can still report a clear interaction failure observed in one session or a later explanation from a returning learner. What you cannot do is treat the observed subset as an unbiased estimate of everyone who used the lesson.

### A Repair Needs a Retest Question

Suppose the real observation suggests that Check is unclear. A revised label and a short instruction are reasonable hypotheses. The retest question should be specific: can a new participant predict what the action does before using it, and does the interaction preserve the intended commitment? "Do they like the new button?" is not the same question.

If the revised version uses different content, different support, and different instructions at once, report that bundle. You may learn whether the whole revised flow is usable, but not which individual change caused the difference. Keep the strength of the conclusion matched to the design of the comparison.

The report should end with the next decision, not just a list of issues. Which defect blocks further use? Which hypothesis needs another observation? Which requirement can be repaired directly from a demonstrated contradiction? A small formative study earns its place by improving these decisions, not by pretending to be a miniature randomized trial.

### Keep Designer Walkthroughs in Their Own Category

Before recruitment, the author and agent can inspect the task, rehearse the protocol, and find broken links. Call this a walkthrough or rehearsal. It can improve readiness, but it does not supply observations from intended learners.

A model prediction can also be useful. It may identify a plausible misreading to watch for, as the sibling protocol anticipates. Write the prediction before the session and compare it with actual observations afterward. Mark it seen, not seen in this test, or cannot tell. Do not treat not seen in a few sessions as proof that the risk does not exist.

This creates a productive role for AI without substituting it for people. The agent helps articulate hypotheses and prepare evidence containers. Real participants determine what happened under the tested conditions. The report can then distinguish a successful prediction from a surprising observation, both of which may inform a better design.

## What you'll be able to do

- **Write** a bounded formative protocol with separate usability and delayed-performance questions.
- **Pilot** the session without inventing participants or treating a pilot as the main result.
- **Record and report** assistance, version, delay, missingness, and access barriers.
- **Revise** a design from observed evidence while keeping causal claims within the study's limits.

**Plan:** all for the proposed prototype route, subject to current access and institutional permission. **MCP budget:** no live writes during participant sessions by default; preparation ceiling 20 requests, actual RUN. **Builds on:** Chapter 12 and an inspectable prototype. **Human dependency:** approved participation and actual learners.

## Talking to Figma

### Round 1: Freeze the Test Version

```text
Prepare a testable copy of the approved prototype. Record its revision, rules
version, item-content versions, and known limitations. Do not edit the test copy
during sessions. Build a protocol document and blank observation forms only.
Do not generate participant responses, quotes, timings, or results.

Separate usability tasks from the delayed task. Include assistance logging,
access barriers, failed saves, and missing follow-up. Keep all identity and
consent material outside the public repository. Mark institutional permission
and recruitment status pending until the human confirms them.
```

The frozen version matters because a small study can otherwise become a moving target. Fixing a defect between participants may be sensible for safety or usability, but it creates versions that must be reported separately. Do not combine them as if everyone used the same design.

> **RUN SLOT 13.1.** Save the prototype/version record, protocol, blank forms, rubric, permissions status, recruitment criteria, and known limits. No participant row should contain invented observations.

### A Proposed Session Script

Use this as a reviewable structure, not an approved consent document:

| Stage | Moderator task | Evidence |
|---|---|---|
| Orientation | Explain the test's purpose and approved participation terms | Confirmation under the approved process |
| Initial context | Collect only the relevant prior-knowledge information | Private bounded context record |
| Practice task | Ask the learner to use the prototype; observe without teaching | Actions, breakdowns, help requested |
| Feedback interpretation | Ask what the feedback means and what they would do next | Their explanation, if recording is permitted |
| Immediate task, if included | Use predefined conditions and rubric | Response with assistance context |
| Close | Explain follow-up and approved withdrawal/contact route | Follow-up status, privately managed |
| Delayed check | Present the reviewed task without unplanned coaching | Response, actual delay, assistance, missingness |

A moderator prompt can contaminate the learning evidence. If you explain the concept to rescue a session, record that assistance. The session may remain useful for usability but no longer supports the same interpretation of later performance. Do not hide help because it makes the design look worse.

### Pilot With One Person

Only after permission and recruitment conditions are satisfied, run a pilot. The pilot tests whether the instructions, prototype path, timing, and recording process are workable. Decide in advance whether pilot data will be excluded from the main formative report; do not choose based on how flattering it is.

Ask whether the delayed task can actually be delivered and returned without exposing private details in the repository. A beautiful protocol with no secure follow-up path is not ready to run.

> **RUN SLOT 13.2.** Record pilot version, actual problems, assistance, revisions, and the decision about pilot inclusion. If no pilot occurred, leave this slot unrun and explain the dependency, not a fictional result.

### Your Turn: Interpret Before Redesigning

After a real session, select one observation and write a bounded interpretation. "The learner opened the hint twice and asked what Check would do" is an observation. "The learner lacks motivation" is an unsupported explanation. "The commit action may be unclear" is a design hypothesis that can guide a repair.

Correct the relevant screen by hand in a revision copy, not the frozen test version. Explain why in your own words and link the correction to the observation code and version. Do not paste identifying quotes into the ledger merely to make the reason vivid.

> **RUN SLOT 13.3.** Save approved de-identified observation evidence, the interpretation with alternatives, the human diff and reason, and the new revision ID. Keep the raw private data separate.

### Round 4: The Agent Repairs Under Evidence

```text
Apply the approved revision to the working copy, preserving human constraints.
For each change, cite the de-identified observation or test case it addresses.
Distinguish observed behavior from my interpretation and from your hypothesis.
Do not generalize one participant's behavior to all learners.

Run design checks and prepare the next test version. Do not mark the repair
effective until it has been tested. Save the version diff and constraint result.
```

The agent may propose several plausible causes. Keep them separate from facts. A repair can be justified as a low-cost hypothesis even when the cause is not established. The report should say that rather than inventing certainty.

> **RUN SLOT 13.4.** Save the repair, rationale links, checks, unresolved hypotheses, and retest status. If the revised version is not retested, call it a proposed repair.

### Report Counts and Cases, Not a Victory Story

Use a results table with actual denominators:

| Measure | Result |
|---|---|
| Invited / participated / completed first session | RUN / RUN / RUN |
| Completed delayed task within chosen window | RUN of RUN eligible |
| Returned outside window | RUN |
| No usable delayed observation | RUN, with categories where appropriate |
| Responses meeting each predefined criterion | RUN counts with denominators |
| Access or prototype failures affecting interpretation | RUN |
| Versions used and moderator assistance | RUN |

Do not fill missing follow-up with zero scores. Describe what is unknown. Do not calculate a persuasive improvement percentage from incomparable tasks or a selectively reported subset. If you report a mean or percentage, keep the raw counts and contextual limits visible.

The conclusion should distinguish observed defects, proposed repairs, later performance under the specified conditions, and claims the study cannot support. "We observed a problem and revised it" is a useful result. It does not need to become "the redesign improved learning."

## The provenance this chapter adds

```json
{
  "chapter": 13,
  "protocol_status": "draft pending appropriate approval",
  "prototype_version": "RUN",
  "participants_observed": "RUN: never simulated",
  "delayed_results": "RUN",
  "human_reason": "RUN: verbatim, no identifying details",
  "repair_retested": "RUN or not-run",
  "causal_efficacy_claim": "not-supported-by-this-formative-design"
}
```

The ledger records the design process and approved de-identified links. It is not the place for participant identity mappings or consent records.

## The check

**The machine half:** protocol completeness, version consistency, missing fields, arithmetic, and separation of observations from blank slots. It can flag unsupported language; it cannot turn generated personas into participants.

**The human half:** appropriate permission, consent and recruitment process, moderation, content scoring, privacy review, and interpretation. The author remains responsible for what the report claims.

**What neither proves:** population-wide efficacy or a causal learning effect from a small uncontrolled formative test. Stronger claims need a stronger study designed for them.

## Exercises

**Warm-up**

1. *(Low; write.)* State one usability question and one delayed-performance question for the same item. Explain why they need different observations.
2. *(Low; report.)* Rewrite an invented causal conclusion as a bounded formative conclusion. Label the example invented.

**Application**

3. *(Medium; write.)* Draft a protocol with a delay, rubric, assistance policy, version record, and missing-data treatment before recruitment.
4. *(Medium; pilot.)* Run an authorized pilot or document why it remains pending. Do not simulate a learner to fill the slot.
5. *(Medium; interpret.)* Take one real observation and write two competing explanations. Propose a repair and a test that could distinguish them.

**Synthesis**

6. *(High; report.)* Prepare a report with one missing delayed response and one access-interrupted response, using hypothetical labelled data if no test has run. Keep both separate from wrong answers.
7. *(High; revise.)* Change the prototype between sessions and specify how the report should distinguish versions and participant exposure.

**Challenge**

8. *(Open; evaluate.)* Design the next study needed for a causal learning claim. Name comparison, assignment, measurement, sample planning, and implementation questions requiring expert review; do not claim this chapter's pilot supplies them.

## What you can now do

You can prepare and honestly report a small formative test, preserve the distinction between observed behavior and explanation, and revise a design without manufacturing a learning-success narrative.

## Credit the AI

**Planned contribution:** blank protocol, forms, version tracking, de-identified report structure, and proposed repairs. **Observed errors:** RUN. **Verification:** actual permitted sessions, human scoring and interpretation, and explicit limits. The agent does not stand in for learners or sign institutional permission.

## Next

The tested prototype is still not the delivered learning product. Chapter 14 packages the objective, state contract, evidence model, and known limits so they survive the move into code, Make, or an LMS.
