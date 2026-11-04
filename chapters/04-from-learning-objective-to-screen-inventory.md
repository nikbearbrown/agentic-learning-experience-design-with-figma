# Chapter 4 - From Learning Objective to Screen Inventory
*A screen earns its place by collecting evidence, not by filling a step in a funnel.*

> **Rough draft - pre-research.** Learning-design leads come from the sibling LXD Chapters 3 and 6. FigJam read-back leads come from FEA `CAPABILITIES.md` and `experiments/log.csv` `[VERIFY]`. The example inventory is a proposed design, not a delivered lesson or a learner result.

## The concept

Suppose you tell an agent, "Turn this chapter into an interactive lesson." It can produce an introduction, some content panels, a quiz, and a completion screen. Nothing in that sequence forces it to ask what the learner will be able to do. A chapter is a container of material. A learning experience is an arrangement of opportunities to perform, receive support, and produce evidence.

The difference appears in a small design decision. If the objective is to diagnose a source of unnecessary effort in a learning interface, recalling the definition of extraneous load is not enough. A learner could choose the correct definition and still remove a useful retrieval task from the next screen. The evidence needs a case, a judgment, and a reason tied to the objective.

I want an inventory that makes that mismatch visible before the agent draws. We will map objective to evidence, evidence to interaction, and interaction to screen states. The output is not a storyboard full of approved-looking rectangles. It is a traceable design contract.

### Write the Performance Before the Interface

For the demonstration lesson, a working objective is:

> Given a short description of a practice activity and its learners, identify one source of avoidable interface effort, distinguish it from effort needed for the target learning, and justify a change that preserves the target performance.

This is a design proposal derived from LXD Chapter 3, not a validated assessment. Notice what it specifies: the situation, the action, and the standard for the explanation. It also prevents a misleading shortcut. "Remove friction" is not an adequate answer because some effort may be the activity's point.

Compare that with "understand cognitive load." The latter names a topic but does not tell the agent what a screen must make the learner do. It invites content presentation as a substitute for evidence. A screen with three definitions might support instruction; it cannot by itself establish the performance above.

I do not want to solve every objective with a response box. The objective determines the evidence, and the evidence determines the interaction. Some performances require a sequence, a diagram, a prediction, or an explanation to another person. Choose the lightest interaction that still distinguishes a defensible performance from a lucky or copied answer.

### Evidence Is Not the Same as an Event

"Clicked Check" is an event. "Selected option C" is a response. "Explained why this extra search step is unrelated to the stated objective" is evidence relevant to this particular performance. Events help reconstruct the session, but they become learning evidence only through a defensible interpretation.

For our objective, I would collect the classification, the learner's reason, whether support was used, and whether the case was familiar. A correct classification after the solution was shown should not receive the same interpretation as an unsupported explanation on a new case. Chapter 11 builds this distinction into the progress view. Here we make sure the data will exist.

Do not collect everything because an agent can generate fields. Every field adds work, privacy responsibility, and an interpretation someone may misuse. If a field does not inform an instructional decision, a usability question, or a required audit, ask why it is there.

### A Screen Is Often Several States

An item may need an unanswered state, a selected-but-uncommitted state, feedback, a hint, and a retry. Counting those as five different objectives would be absurd. Counting them as one static screenshot would conceal the information boundaries between them.

I separate a **screen family**, which serves a task, from its **states**, which represent what the learner can currently see or do. Each inventory row names both. This gives the agent a way to reuse a component without collapsing meaningful differences.

The demonstration inventory begins like this:

| ID | Objective/evidence | Interaction | Required states | Evidence limitation |
|---|---|---|---|---|
| S01 | Orient to the task; no mastery inference | Read goal and start | Ready, unavailable | Starting is not learning |
| S02 | Diagnose effort in a familiar case | Choose category and explain | Unanswered, draft, committed, feedback | Recognition may cue the explanation |
| S03 | Identify a needed support step | Complete a partial worked example | Full, partial, independent support | Supported performance is not independent mastery |
| S04 | Compare two review plans | Predict and justify | Prediction, committed, explanation | A proposed schedule is not a tested optimum |
| S05 | Apply the diagnostic to a new case | Short explanation | Draft, committed, rubric feedback | Scoring needs a human-reviewed rubric |
| S06 | Revisit after a delay | Parallel transfer item | Due, unavailable, submitted | Missing follow-up is not failure |
| S07 | Interpret current evidence | Progress view | New, supported, independent, needs review | The summary depends on its data policy |

These are proposed screen families, not instructions to make seven full pages. The implementation might reuse one layout for S02 and S05. The learning distinctions should remain in the inventory even if the visual structure is shared.

### Where the Map Lives

The blueprint proposes a FigJam table because the sibling experiments report better text recovery from tables than from multi-line stickies. The same notes record a sticky read returning only the first line `[VERIFY: FEA CAPABILITIES.md, FigJam annotations/read-back note; experiments/log.csv]`. That is a narrow observation, not a permanent product law.

So we test the current read path. If it loses critical text, keep a plain structured copy alongside the board and make its authority explicit. The board is a collaborative surface; it is not useful as the sole source of truth if the next agent receives only half its contract.

Stable IDs matter more than visual grouping here. `OBJ-01`, `S02`, and `EVID-EXPLANATION` can travel through a table, an annotation, a component description, and a handoff package. An arrow that looks connected to the right box may not carry that relation in the returned data. Write the relation as data and use the arrow to help the human see it.

<!-- [TABLE: the objective-to-evidence-to-screen map with unsupported inferences highlighted, especially completion versus learning] -->

### The Inventory Must Include Recovery

An objective map can be aligned and still assume a frictionless session. What happens if the learner leaves while drafting, cannot operate an input, or reaches a state with no usable next action? These are not additional learning objectives. They are conditions under which the planned evidence might fail to exist.

Add recovery requirements to the relevant screen family. Preserve a draft where the product promises to preserve it. Distinguish leaving voluntarily from a save failure when the implementation can observe the difference. If it cannot, do not invent that distinction in the dashboard. The inventory should carry uncertainty forward rather than manufacture data to satisfy a later view.

This also helps control scope. If a screen depends on a durable account and storage service that the workshop does not provide, identify the dependency before asking the agent to draw a saved-progress badge. You can choose a session-only prototype and label the limit. A smaller honest product is better specified than an imaginary complete one.

### Reuse Without Losing Traceability

Suppose S02 and S05 share the same visual layout. It is sensible to implement one component. It is not sensible to merge their evidence records if one is a familiar supported case and the other is a new independent case. The screen family can be reused while objective, item, support, and exposure identifiers remain distinct.

This is where the inventory becomes an interface between the learning designer and the production agent. It tells the agent which differences are visual and which are meaningful. Without that instruction, the agent may simplify the data along with the layout and erase the comparison you planned to make later.

Keep a revision note when the mapping changes. If S05 no longer collects a free explanation because the delivery platform cannot support it, the objective/evidence relationship has changed even if the screen still contains a question. Record the consequence before moving on. A later handoff cannot preserve a contract that was quietly altered during inventory cleanup.

The final inventory is therefore not frozen forever. It is versioned. Its value is that a change can be traced back to a learning or operational reason, rather than disappearing into an agent's instruction to simplify the flow.

Before approving the inventory for a build, read only the learner-performance column from top to bottom. Does it describe a coherent progression, or a collection of content types? Then read only the evidence-limit column. If every row claims complete certainty, the map is probably concealing assumptions. These two quick readings expose problems that a polished storyboard can make surprisingly easy to overlook.

## What you'll be able to do

- **Write** an objective as an observable performance with a stated context and standard.
- **Map** that performance to evidence, interactions, and screen states.
- **Detect** screens without an objective and objectives without an opportunity to perform.
- **Store and read back** the map without relying on visual proximity alone.

**Plan:** all, provisional. **MCP budget:** planning ceiling 20 requests; actual RUN. **Builds on:** Chapter 3's read-path matrix. **Personal project:** choose one lesson you are entitled to redesign; keep sensitive content private.

## Talking to Figma

### Round 1: The Agent Builds the Map, Not the Lesson

Give the agent the working objective, a short content summary from LXD Chapter 3, and the inventory above as a proposed starting point. Do not ask for attractive screens yet.

```text
Create an objective-to-evidence map for the demonstration practice unit.
Use stable IDs. For every proposed screen family, name the objective, learner
performance, evidence collected, required states, and what cannot be inferred.
Put the map in a FigJam table if the current tools support reliable read-back.
Keep a plain structured copy of the same contract. Do not draw the lesson UI.

Flag objectives with no evidence and screens with no objective. Treat the
provided inventory as a proposal you may question, not an approved answer.
Save the exact script and follow the provenance loop for supported changes.
```

The agent should distinguish author-provided objectives from its own suggestions. An automatically invented objective can make every screen look aligned by changing the target after the design exists. That is not alignment. Label proposed additions and let the author decide.

> **RUN SLOT 4.1.** Save the map, script, read-back response, proposed changes, and traceability check. Record whether all cells and relations survived the chosen representation. A map that only looks complete is not a pass.

### A Worked Reasoning Example

Take S02, the familiar-case diagnostic. Suppose the case describes a learner switching repeatedly between a question and a detached definition panel. The target is not "prefer fewer clicks." It is to explain whether that switching serves the learning objective.

First identify the evidence: a classification plus a reason that names the learner's task. Next choose the interaction: an option selection alone is insufficient, so add a short explanation or a structured reason choice that can distinguish plausible misconceptions. Then define the states: the key is hidden in the response state; the explanation is available after commitment; a hint can direct attention to the task without naming the classification.

Now list what this interaction cannot establish. A single familiar example does not show transfer. An explanation produced after the key is shown does not demonstrate the same retrieval as an independent answer. A learner unable to operate the input provides unusable evidence about the target concept. Each limitation creates a requirement in a later chapter.

This is the inventory doing real work. It is not describing a screen after the fact. It is exposing why the screen needs certain states and why the progress view must not overinterpret them.

### Your Turn in FigJam

Inspect the map for one of two errors: a decorative or administrative screen presented as learning evidence, or an important performance with no place to occur. Correct one row by hand. Keep the before/after relation visible.

Tell the agent you are done. After the diff, explain why. If your correction changes the objective rather than the representation, say so. That is a different kind of authorship and should not disappear into "updated table text."

> **RUN SLOT 4.2.** Save the captured diff, your reason, the affected IDs, and the updated traceability report. If the snapshot helper does not support the board, say so and save the board read-back plus a human-confirmed text diff. Do not claim the design-file helper validated an unsupported document type.

### Round 3: The Agent Proposes a Screen Inventory Under the Corrected Contract

```text
Read the corrected map and active constraints. Propose the smallest screen
inventory that lets the learner produce the specified evidence. Reuse screen
families where appropriate, but keep distinct learning states explicit.

For each screen, give its objective ID, input, reveal condition, evidence output,
and next state. List every proposed screen you removed and why. Do not delete
human-authored work. Ask before changing an objective or releasing a constraint.
```

Review the resulting inventory as a set of claims. A welcome screen might be necessary for consent, orientation, or navigation. It does not need to pretend it proves learning to justify its existence. Name its operational role. The standard is not "every pixel measures mastery." It is "no screen is mistaken for evidence it does not collect."

> **RUN SLOT 4.3.** Save the inventory, removed-screen proposals, constraint result, and the agent's unresolved questions. Mark each question as a content, evidence, state, access, or implementation issue.

### Round 4: Apply the Method to Your Lesson

Choose a bounded lesson, not a semester. A useful first project has one central performance, a small number of concepts, and content you can legally and ethically use. Keep the choice provisional until you can describe what a learner would do differently afterward.

Write one objective and one counterexample: a learner who completes the proposed screens but cannot perform the objective. Ask the agent to find where that learner could slip through. This is an adversarial alignment test, not a request to invent a learner result.

```text
Here is my lesson objective and a hypothetical learner who could finish without
meeting it. Audit my inventory for that loophole. Suggest the smallest change
that would expose it. Do not add more content unless it supports the evidence.
Label all imagined behavior as hypothetical. Do not simulate participant data.
```

The counterexample is often more revealing than a checklist of action verbs. A verb such as analyze does not rescue an activity that only asks the learner to recognize a quoted definition. Inspect the actual response demanded.

> **RUN SLOT 4.4.** Save your lesson charter, evidence map, counterexample, proposed repair, and final provisional inventory. These become the capstone's starting artifacts.

## The provenance this chapter adds

```json
{
  "chapter": 4,
  "objective_ids": ["OBJ-01"],
  "map_readback": "RUN",
  "human_correction": "RUN: verbatim reason and affected IDs",
  "orphan_screens": "RUN",
  "unassessed_objectives": "RUN",
  "personal_lesson_charter": "RUN"
}
```

This reporting sketch links design changes to objectives. Later it lets you distinguish a visual revision from a change to what the lesson claims to teach.

## The check

**The machine half:** verify IDs, required fields, references, missing states, orphan screens, and missing read-back text. A complete row is not a valid objective. A machine can enforce the schema without understanding the performance.

**The human half:** judge whether the evidence actually distinguishes the target capability from guessing, copying, or interface skill. Decide whether a screen's cost is justified and whether the lesson is small enough to test.

**What neither can see yet:** whether the proposed activity produces durable learning. This is a design argument awaiting learner evidence, not an efficacy result.

## Exercises

**Warm-up**

1. *(Low; write.)* Rewrite "understand retrieval practice" as a performance with a context and a standard. Name one response that would look successful but fail your standard.
2. *(Low; detect.)* Identify an operational screen in your inventory and explain why it need not count as learning evidence.

**Application**

3. *(Medium; map.)* Map one objective to two possible interactions. Explain what evidence each loses or gains.
4. *(Medium; read back.)* Put a requirement in two board representations and compare the actual returned text. Do not infer a general rule from one trial.
5. *(Medium; detect.)* Ask the agent to find an orphan screen and an unassessed objective. Verify both findings yourself.

**Synthesis**

6. *(High; map.)* Design a counterexample learner who passes your first inventory without the target performance. Repair the loophole without doubling the lesson's length.
7. *(High; evaluate.)* A stakeholder asks for a completion badge. Specify its operational role and the learning claim it must not make.

**Challenge**

8. *(Open; write and evaluate.)* Choose an objective for which a screen-only assessment is inadequate. Design the external evidence step and show how the screen inventory should acknowledge its limit.

## What you can now do

You can justify a screen in terms of the performance it supports or evidence it collects. You can also identify where completion could conceal failure and preserve the objective as the agent changes the interface.

## Credit the AI

**Planned contribution:** structure the map, identify traceability gaps, and propose a bounded inventory. **Observed errors:** RUN, especially invented objectives and unjustified evidence claims. **Verification:** inspect the learner's actual required response, test a counterexample, and compare board read-back with the source.

## Next

The inventory tells us what the learner must do. Chapter 5 asks how much support the interface should provide while they do it, and how that support can change without changing the objective.
