# Chapter 3 - How the Agent Sees a Frame
*The screen you recognize and the structure the agent reads are not the same object.*

> **Rough draft - pre-research.** Figma read-path claims are dated leads from FEA `CAPABILITIES.md`, `examples/film-03/`, and `examples/review-notes/evidence/figma-results.md` `[VERIFY]`. No comparison or rebuild described below has run for this book.

## The concept

Imagine a practice screen with a question above four options. The correct answer is not visibly marked. A note beside the frame says, "Do not reveal the key before commitment." To you, the intention is easy to read. You see the screen and the note together. Whether the agent gets that intention depends on which representation it receives.

A screenshot supplies pixels. A structural read supplies selected properties. A design-context response may supply generated code and metadata. None is the design itself in full. Each is a translation made for a purpose. The important question is not which one is richest in the abstract. It is which one preserves the particular rule the next task needs.

This is why I resist the phrase "the agent has the file." Has it seen the relevant frame, the component definition, the variable collection, the annotation, the current mode, and the surrounding lesson objective? Those are different observations. The agent can sound certain after receiving only one of them.

### Pixels Show an Outcome, Not Its Cause

A screenshot is good evidence of what a particular state looks like. It can expose clipping, a correct-answer tint, and an explanation too distant from the diagram it explains. But pixels do not tell you whether a label is hard-coded, bound to a variable, inherited from a component, or overridden in an instance.

Two screenshots can look identical while behaving differently on the next edit. One may be a reusable item whose response state is explicit. The other may be a collection of unrelated shapes. If the task is visual review, both images may be sufficient. If the task is generating a second item without breaking the learning rule, that hidden difference matters.

The reverse also happens. A screenshot may look harmless while a hidden answer layer, unintended transition, or descriptive label contains information the built interface must not expose too soon. A visual check cannot certify an information boundary it cannot observe.

### Structure Is an Interpretation Too

The blueprint proposes comparing `get_metadata`, `get_design_context`, and `get_screenshot`, with a separate variable read where needed. Those names come from the sibling tool records `[VERIFY: FEA saved tools-and-prompts source, September 27, 2026]`. Do not assume that any one response contains all the information another tool can obtain.

Metadata can help locate and identify nodes. Design context can help an implementation agent reconstruct a screen. The sibling examples describe a React/Tailwind-shaped response, but the exact current format and requested framework need confirmation `[VERIFY: FEA film-03 and CAPABILITIES.md]`. Generated code is not proof that a learning requirement has been implemented. It may be an interpretation of the design, with its own omissions.

The right habit is to save the actual response before interpreting it. If a rule is missing, distinguish three possibilities: it was absent from the source, it was present but not returned by this read, or it was returned and the next agent ignored it. Each calls for a different fix. Adding more prose to a missing read is not the same intervention as making a returned instruction more precise.

### Where a Rule Can Live

The sibling project provides useful leads about component descriptions and frame annotations. It also records an important failure: annotations on component sets were not returned in the tested reads even though they remained in the file. A nearby variant's annotation was not established by that observation. Do not generalize from "frame worked" to "every node works" `[VERIFY: FEA CAPABILITIES.md, annotations row]`.

For this book, treat every proposed storage location as a hypothesis to test:

| Location | What we want it to carry | Read-back question |
|---|---|---|
| Layer name | Role, not just appearance | Does the response distinguish prompt, hint, and explanation? |
| Component description | Reusable item contract | Does the next agent receive it for the selected instance? |
| Variable and mode | Explicit state or support value | Which tool returns the resolved and alternative values? |
| Frame annotation | Requirement and rationale | Does it survive this exact selection and read path? |
| External rules file | Cross-screen rules | Was the file actually loaded before the write? |
| Nearby visual note | Context for a human | Is its text included, only pictured, or omitted? |

The answer is not to duplicate every paragraph into every location. Duplicated rules drift. Use stable identifiers and one authoritative statement, with short local pointers that are tested for survival. A frame can name `R-ANSWER-01`; the rules file defines it; the component description states the local consequence. When they disagree, stop and resolve the conflict rather than averaging their meanings.

### Naming Is a Small Interface

`Rectangle 47` tells the next agent almost nothing. `Feedback/incorrect/explanation` carries a role. But a name is not an instruction engine. Naming a layer `AnswerHidden` does not hide it, and naming a frame `Accessible` does not make its eventual code accessible.

I use names to reduce ambiguity, properties to represent the current state, and rules to explain what must remain true. Keep those jobs separate. A descriptive name can be a useful clue while still being stale. Ask for evidence from the actual property or state, not from the label that claims it.

In the demonstration lesson, the difference between "support" and "answer" is especially important. A worked example can legitimately contain an answer. An independent retrieval item should not expose its key before commitment. The rule needs a scope, not just a prohibition on the word answer.

<!-- [INFOGRAPHIC: one Figma frame feeding three read paths; mark which evidence each path can carry, with unknowns visibly distinct from omissions] -->

### A Read-Path Failure Has a Small Anatomy

Suppose the source contains a frame annotation saying the learner must submit a reason, but the recovered contract mentions only selecting an option. Do not immediately conclude that annotations do not work. Begin with the exact selection. Was the agent reading the annotated frame, an inner component, or an instance elsewhere? Then inspect the raw response. Was the annotation absent, truncated, transformed into another attribute, or present but ignored?

Next inspect the rebuild request. Did it tell the agent to recover the learning contract, or only to reproduce the visible layout? An agent can faithfully perform the latter while failing the former. That is a task-definition problem as well as a representation problem. Finally check whether another supplied artifact contradicted the annotation. If a component description calls the reason optional while the frame calls it required, the file has a conflict that no amount of context can resolve automatically.

These possibilities suggest a compact diagnostic sequence: source, selection, response, task, conflict, action. Save evidence at each step. The aim is to change one cause at a time where practical, not run an elaborate experiment for every label. A narrow comparison can prevent a broad but useless conclusion such as "agents cannot read learning intent."

### Minimum Context Is a Maintained Artifact

The minimum context package should have a version and a loading order. For a local item edit, it might include the objective row, the selected instance, its component description, the current support/attempt state, and relevant rules. For a new lesson, it needs the larger evidence map. For an implementation task, it needs access and persistence requirements too.

Define what the agent does when part of the package is unavailable. It should not fill a missing rubric with a plausible one and continue as though it was approved. It can propose a draft rubric, label it, and wait for the content decision while doing unrelated safe preparation. The difference is whether the invented material is presented as an author requirement.

The package should also say what not to load. Private learner records are not needed to reconstruct a component. Credentials are not design context. The smallest sufficient package is often safer as well as cheaper, but sufficiency must be tested. Saving context by omitting the objective can make a technically successful rebuild instructionally wrong.

Over time, record which missing fields actually caused problems. That history is more useful than growing an enormous default prompt. Chapter 12 will use it to define the fresh-session loading contract. We are not trying to preserve every sentence from the conversation. We are identifying the small set of durable decisions the next session needs to act responsibly.

The final read-path map should include a confidence boundary, not a confidence score. State the selection and task for which the observation holds. "The description appeared for this instance under this read" is precise. "Component descriptions survive" is broader and may be false elsewhere. The more carefully you scope the first statement, the easier it is for another reader to reproduce it or discover a meaningful difference.

## What you'll be able to do

- **Compare** three representations of one frame using saved evidence rather than the agent's summary.
- **Locate** a lost learning requirement in the source, the read path, or the interpretation step.
- **Restructure** names and rule placement so a fresh-session rebuild has an explicit contract.
- **Evaluate** a reconstruction without confusing a close screenshot match with preserved pedagogy.

**Plan:** all, provisional. **MCP budget:** planning ceiling 24 requests for a bounded comparison; actual RUN. **Builds on:** Chapters 1-2 and the baseline screen.

## Talking to Figma

### Round 1: Freeze the Question Before Reading

Choose one baseline frame. Write a short ground-truth card yourself: the objective, the response the learner should produce, when the key may be revealed, and what the hint is allowed to reveal. Do this before asking an agent what the design means. Otherwise the agent's interpretation can quietly become your definition of correctness.

```text
Inspect one designated practice frame without editing it. Save separate raw
outputs for get_screenshot, get_metadata, and get_design_context, using the
currently available equivalents if names changed. If variable definitions are
needed, fetch them separately and say why. Keep the selections identical.

For each statement on my ground-truth card, report returned, omitted, or cannot
determine, with the exact evidence location. Do not infer hidden properties from
the screenshot or treat a layer name as proof of its behavior.
```

The agent should not repair the frame yet. This is a diagnostic round. If it changes the source while investigating, the comparison no longer concerns one stable frame. Save the observed revision or snapshot identifier with each response so a later reviewer can detect that problem.

> **RUN SLOT 3.1.** Save the ground-truth card, raw responses, selection and revision evidence, and a requirement-by-read-path matrix. Record tool errors as errors, not as evidence that a property does not exist.

### Run a Meaning Test, Not Only a Text Search

Finding the phrase "hide the answer" in a response is a useful first check. It is not enough. A response might contain the phrase in an irrelevant comment or return two contradictory instructions. Conversely a requirement can survive as an explicit state relationship without repeating your exact sentence.

Use two columns. The first asks whether the exact requirement or identifier appears. The second asks whether the response carries enough information to act on it. If the latter is your interpretation, label it as a judgment. A machine can count strings; it cannot settle the design intention by counting alone.

For example, a note saying "answer after commit" lacks a definition of commit. Does selecting an option count? Does pressing Check count? Does opening the first hint count? This is a weakness in the source contract, not necessarily a read-path failure. Chapter 7 will define the transition precisely. Record the ambiguity now so you can see what later chapters actually fix.

### Your Turn in Figma

Correct one storage decision, not the entire screen. Rename a vague feedback layer. Move a requirement from an unreturned container to a tested frame annotation, if your account permits it. Add a short component description with a rule identifier. Keep the learner-facing text unchanged for this experiment so that the intervention is easier to interpret.

Tell the agent you are done and give your reason after it presents the diff. A suitable reason might concern the placement of a rule, but use your own words. The agent must not convert a missing description into a supposed human correction before you make or approve it.

> **RUN SLOT 3.2.** Record the captured diff, your verbatim reason, and a second read of the changed location. State whether the requirement now appears. If it still does not, retain that failure rather than moving through locations until one works without recording the unsuccessful attempts.

### Round 3: A Fresh Session Rebuilds

A session that watched you repair the source has extra context. To test whether the contract travels, use a fresh session with no repair conversation. Give it the designated read artifacts and the rules file you want available, not the answer to the experiment.

```text
Rebuild this one practice screen in a separate sandbox frame from the supplied
design evidence. First state the learning contract you can actually recover.
List missing or conflicting requirements before drawing. Do not consult the
earlier editing conversation. Preserve the existing human constraints and do
not change the original frame. Save the write script and all check results.
```

The next agent may ask for missing context. That is a useful outcome. A reconstruction that acknowledges it cannot determine reveal timing is more trustworthy than one that invents a timing rule and happens to match your intention.

Compare the reconstruction against two rubrics: visual correspondence and learning-contract correspondence. The original may itself contain a learning defect. Do not call the rebuild better merely because it reproduced that defect precisely. You need both a fidelity observation and a judgment about what was faithfully copied.

> **RUN SLOT 3.3.** Save the fresh-session inputs, recovered contract, missing-context questions, rebuild script, screenshot, and both rubrics. Report what passed, failed, and remained untestable. Fill no keyboard-runtime verdict from a static frame.

### Round 4: Change the Selection

Read the component definition and an instance separately, where the available tools support it. Repeat the requirement search and record differences. The unit selected for a read can matter as much as the tool chosen. A lesson-level objective on a distant page is not guaranteed to accompany a selected button.

The economical response is not "always read the entire file." That can be expensive and still ambiguous. Define the minimum context package for each task: local item state, relevant component contract, objective identifier, and applicable rules. Then test that package on a new item.

> **RUN SLOT 3.4.** Save the selection comparison and your proposed minimum context package. Mark any untested selection as untested. This becomes an input to Chapter 12's loading instructions.

## The provenance this chapter adds

```json
{
  "chapter": 3,
  "comparison": "RUN: screenshot, metadata, design context",
  "source_requirement": "RUN: human ground truth",
  "lost_at": "RUN: source, read path, interpretation, or unknown",
  "human_reason": "RUN: verbatim",
  "fresh_session_rebuild": "RUN",
  "runtime_accessibility": "not-run"
}
```

This is a reporting sketch. The live round identifiers belong in the actual ledger. Its value is diagnostic: when a later agent breaks a rule, you can ask whether the rule was ever in the context it received.

## The check

**The machine half:** compare raw outputs, locate rule identifiers, flag conflicting versions, and test captured constraints. A string appearing in a response does not prove obedience. An absent string does not prove the whole requirement was absent.

**The human half:** judge whether the recovered contract expresses the intended task and whether the rebuilt state still asks the learner to do that task. Review both false confidence and unnecessary requests for clarification.

**What neither can see:** an agent's complete internal interpretation. We observe inputs and actions, not a mind-reading account of why it acted. Report the visible failure and plausible causes separately.

## Exercises

**Warm-up**

1. *(Low; compare.)* Name one question a screenshot answers better than a structural read and one question it cannot answer at all.
2. *(Low; locate.)* Identify a label in your file that claims more than its properties establish. Rewrite the label without changing behavior.

**Application**

3. *(Medium; compare.)* Read the same frame three ways. Build the requirement matrix from the saved outputs, not the agent's summary.
4. *(Medium; restructure.)* Move one requirement to a different storage location and rerun the identical read. Report the actual difference, including a null result.
5. *(Medium; evaluate.)* Ask a fresh session to recover the contract without rebuilding. Score omissions and invented requirements separately.

**Synthesis**

6. *(High; evaluate.)* Design two screens that look identical but carry different state contracts. Explain how the context package should reveal the difference.
7. *(High; locate.)* A rule appears in the response but is broken in the rebuild. Write three competing explanations and the smallest next test that distinguishes them.

**Challenge**

8. *(Open; restructure.)* Specify the smallest context package that supports a new item without reading the whole file. Test it against one unfamiliar item type and report where it fails.

## What you can now do

You can trace a learning rule through an actual read path, isolate a translation failure, and ask a fresh session to reconstruct intent without leaking the expected answer. You also know why a screenshot match is only one kind of success.

## Credit the AI

**Planned agent contribution:** collect representations, compare evidence, and rebuild a bounded frame. **Observed mistakes:** RUN, including omitted or invented requirements. **Verification:** keep raw responses, use human ground truth written first, and compare the reconstructed contract independently.

## Next

Now we know how meaning can disappear between a file and an agent. Chapter 4 decides what meaning needs to be there in the first place: the objective, the evidence, and the screens that collect it.
