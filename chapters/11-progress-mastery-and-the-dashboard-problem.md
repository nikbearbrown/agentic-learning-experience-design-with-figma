# Chapter 11 - Progress, Mastery, and the Dashboard Problem
*A number becomes dangerous when its label promises more than its data.*

> **Rough draft - pre-research.** Learning/analytics leads: LXD Chapters 1, 13, and 14; AI-LXD Chapter 7 on adaptive systems. The records and policies below are illustrative design examples, not learner data or validated mastery estimates. Figma annotation/read-back claims remain `[VERIFY]`. No dashboard has been run for this chapter.

## The concept

Imagine a progress screen announcing "100% mastered" because the learner opened every card. The arithmetic can be correct: all cards were opened. The interpretation is wrong. A completion count has been renamed as a claim about capability.

An agent can create this mistake without a single bug in the interface. Ask for a student dashboard and it may produce progress bars, streaks, time studied, and a mastery ring. The visual language is familiar. What matters is which event feeds each number and what decision the number is supposed to support.

This chapter builds two views: a learner view for deciding what to practice next and an instructor view for deciding where teaching or investigation is needed. Neither should confuse activity with learning evidence. Both should retain uncertainty instead of replacing missing data with a reassuring percentage.

### Four Layers Between an Event and a Decision

Keep four layers explicit.

An **event** is something observed or recorded: opened a hint, committed a response, encountered a save error. An **attempt record** groups the relevant events and context for one response. An **evidence interpretation** says what that attempt suggests under a declared policy. A **decision** uses that interpretation: recommend review, retain support, or ask an instructor to inspect a case.

The layers can fail independently. An event may not save. An attempt may be duplicated. The evidence policy may treat an assisted response as independent. The decision may be too strong for the evidence. A chart alone cannot tell you which happened.

Chapter 8 already gives us a scheduling policy version. This chapter adds an evidence-policy version. Keep them distinct. Deciding when an item should return is not the same as deciding what the last response establishes.

### Completion Is Useful When Honestly Named

I am not banning activity metrics. Completion can help a learner find unfinished work. Time can reveal a technical problem worth investigating. A streak can reflect a chosen routine. None becomes learning evidence merely by sitting next to a book icon.

Name the metric literally. "Viewed 6 of 8 activities" is an activity summary. "Two independent attempts available for review" is an evidence summary. "Mastered 75%" needs a defined model, scope, uncertainty, and supporting data. If those do not exist, remove the mastery label rather than invent a threshold to justify the visual.

The learner view should answer three questions: what have I tried, what evidence do I currently have, and what is a sensible next step? The instructor view should answer where evidence suggests a shared difficulty, where observations are missing, and where the data or item itself may be defective.

### A Provisional Evidence Vocabulary

For the demonstration, use descriptive states rather than a binary mastery claim:

| State | Meaning under this design | What it does not mean |
|---|---|---|
| Not yet observed | No usable attempt for this objective | Cannot do it |
| Supported practice | A response was produced with recorded help/exposure | Independent performance |
| Independent observation | A usable response without recorded assistance under the task contract | Durable mastery |
| Delayed observation | A response collected after the specified delay | General transfer or causation |
| Needs review | A stated rule or human review requests another look | A fixed learner deficit |
| Evidence unavailable | Access, save, or other issue prevents interpretation | Incorrect answer |

These states may overlap. An independent delayed observation carries two dimensions. Do not force them into one mutually exclusive status if doing so discards important context. A compact UI can show a main status and details, but the data model should keep the underlying facts.

If the author later chooses to use the word mastery, define the decision policy separately and label it provisional until validated for its purpose. Do not imply that this vocabulary is a standardized psychometric model. It is a transparent reporting design for a small practice unit.

### Illustrative Data: Same Score, Different Meaning

Consider four synthetic attempt records for one objective. They are invented examples, not participants:

| Attempt | Result | Context | Defensible display |
|---|---|---|---|
| A | Meets reviewed rubric | Full support, parallel example visible | Supported practice met criterion |
| B | Meets reviewed rubric | Independent, first response to a new case | Independent observation met criterion |
| C | Meets reviewed rubric | Same item after solution viewing | Solution-exposed retry met criterion |
| D | No usable response | Input could not be operated | Evidence unavailable; access issue |

Counting A, B, and C as three equivalent mastery demonstrations loses the reason we recorded support. Counting D as wrong converts a barrier into a content judgment. The interface needs enough detail to prevent both shortcuts.

Now imagine two more delayed observations: one meets the rubric and one does not. The dashboard should show the counts and context. At this scale, a percentage without the denominator is especially misleading. One event can change it sharply. The appropriate next action may be to inspect the item and the rubric, not diagnose the learner.

### The Learner View

Use objective names that the learner can interpret, not only internal codes. Show the next action and why it is recommended. "Try a new case without the scaffold" explains a different learning purpose from "Repeat question 2."

Let learners inspect the basis of a summary: the last relevant attempt, assistance used, whether the item was repeated, and whether a delayed check exists. Do not make them reverse-engineer an opaque ring. A simple table may be more useful than a dashboard full of visual certainty.

Avoid punishing help-seeking. The record can say a response was supported without making support a badge of failure. The instructional decision is whether the next task should test independence, provide more help, or investigate a barrier.

### The Instructor View

The instructor needs aggregation that preserves denominators and missingness. "4 of 7 usable independent responses need review; 3 invited learners have no usable observation" says more than "57% struggling." It also makes clear that the latter three were not observed to struggle.

Use this sentence as an illustrative reporting pattern, not a result. Real counts belong in RUN slots. Do not put identifiable learner details in the public manuscript or repository. A small group can be recognizable even after names are removed; prepare aggregate or approved de-identified reporting appropriate to the setting.

The dashboard should make item defects visible too. If many responses challenge the same ambiguous key, that may be an item-review problem. Do not force every alert to point at a learner deficit because the interface was called a learner dashboard.

<!-- [TABLE: data lineage from commit event through assistance-aware attempt record to evidence label and next-step decision; mark where each claim can fail] -->

### Separate Recency From Ability

A last-response display is easy to compute. It can also be misleading. A correct independent response followed by an access failure should not automatically become "does not understand." An old correct response should not silently become permanent mastery. The policy needs to say how it treats recency and what it means by current evidence.

For the small demonstration, one transparent approach is to display the latest usable observation with its date and context, plus any later unavailable event separately. That is a design proposal, not a validated ability estimate. It keeps the record interpretable without inventing a hidden decay model.

If a later product uses a statistical estimate, the interface should identify the model and uncertainty appropriate to its purpose. Do not add a confidence percentage because the dashboard has room for another number. A percentage labelled confidence needs an interpretation, a calibration basis, and evidence that supports its use.

### Aggregation Can Hide the Instructional Question

Suppose one objective contains several item types. A single average may combine recognition, explanation, supported completion, and new-case performance. The number is easy to compare and difficult to interpret. Before aggregating, ask whether the observations are intended to support the same claim under the same conditions.

An instructor may need a grouped view by misconception or rubric criterion instead of by screen. The learner may need a next-step view by objective instead of a rank among peers. These are different decisions and may need different displays of the same records.

Do not turn small differences into a leaderboard by default. Apart from privacy and motivation questions, a rank can imply precision the measurement does not support. If comparison is genuinely needed, state the purpose and uncertainty. The default in this book is to support an instructional action, not a competition the objective never requested.

### Make the Data Contract Inspectable

Each metric should name its source fields and transformation. For example, an independent-observation count might include accepted attempts with assistance false and solution exposure false under a particular item policy. It also needs a rule for retries, duplicate IDs, deleted items, and unresolved scoring. Without those conditions, the same label can mean different things across builds.

Keep raw observations distinct from derived labels. If the policy changes, the raw attempt should not be rewritten to fit the new interpretation. This lets a reviewer reconstruct what the learner actually did and see why the display changed. An opaque summary without lineage makes correction much harder.

The implementation may later use an analytics standard or platform-specific event format. That choice needs current research and interoperability tests. This chapter's neutral event dictionary is not a claim of conformance to any such standard. Preserve the semantic contract first, then map it explicitly to the selected format rather than adopting an acronym and assuming the meaning follows.

### Make the Next Action Reversible

A recommendation can be wrong. The learner may have knowledge the current record does not capture, or an attempt may have been mis-scored. The progress view should provide a route to inspect the basis of the recommendation and, where appropriate, request a new case or human review.

Do not let a status label become a permanent identity. Needs review should point to an action and its evidence, not mark the person as a weak learner. If an item defect is confirmed, the policy should explain how affected summaries are handled without rewriting the original response. Keep the observation and the correction distinct.

For instructors, a useful review view shows why a case was flagged and which decision remains theirs. It should not encourage bulk acceptance of automated judgments merely because the table contains many rows. Grouping similar cases can save effort while leaving the substantive review visible.

### Empty States Are Evidence Policies Too

Design the view before any usable attempts exist. If the screen must show a zero-filled mastery chart to avoid looking empty, the visual form is driving an unsupported interpretation. Use a literal state such as no independent observations yet, with a clear next task.

Also design the state in which data are temporarily unavailable. A failed query is not the same as no attempts. A stale cached summary is not necessarily current. The implementation should expose the distinction at the appropriate level without overwhelming the learner with system detail. The designer's job is to preserve meaning, not to display every diagnostic field.

These states are easy to overlook because they are not the success screenshot. They are part of the dashboard's truthfulness. Include them in the synthetic dataset and route review before the view is considered complete.

## What you'll be able to do

- **Trace** every displayed learning claim to events, context, and a versioned interpretation policy.
- **Distinguish** activity, support, independent evidence, delayed evidence, and unavailable observations.
- **Design** learner and instructor views around decisions rather than decorative metrics.
- **Audit** aggregation for missingness, duplicate attempts, and unjustified labels.

**Plan:** all, provisional. **MCP budget:** planning ceiling 25 requests; actual RUN. **Builds on:** Chapters 4, 7, 8, and 10.

## Talking to Figma

### Round 1: Define the Data Before the Chart

```text
Create a metric dictionary before drawing a dashboard. For every proposed
display, name the learner/instructor decision, source event or record,
denominator, assistance/exposure treatment, missing-data treatment, policy
version, and claim limitation. Use only clearly labelled synthetic data.

Remove or rename any metric whose learning interpretation is unsupported.
Do not derive mastery from views, minutes, streaks, or completion alone.
```

The dictionary should include who owns a policy change. An agent should not silently change the definition of Needs review to improve the appearance of a chart. When a policy changes, the display must identify whether historical data were reinterpreted or remain under the old policy.

> **RUN SLOT 11.1.** Save the metric dictionary, synthetic dataset, proposed policy, and rejected metrics. Record unresolved interpretation decisions before drawing.

### Round 2: Draw Both Views

```text
Build a learner progress view and an instructor overview from the approved
metric dictionary. Use synthetic records with supported, independent,
solution-exposed, missing, and access-interrupted attempts. Show useful empty
and unavailable states as well as successful ones.

Annotate data lineage and policy IDs on tested frame locations. Read the
annotations back. Do not invent real-time data connections or predictive models.
Save scripts and follow PROVENANCE.md.
```

Make the next learning action prominent without turning it into a command the learner cannot question. If the policy recommends another independent case, the view should explain that the previous success used support. It should not say the learner has failed.

> **RUN SLOT 11.2.** Save both views, scripts, annotation read-back, state coverage, and all synthetic data labels. Keep invented counts out of the chapter's results section.

### Your Turn in Figma

Find a label that overstates the underlying data. Replace "mastered" with a descriptive observation if that is what the evidence supports. Or fix a chart that hides the number of missing responses. Give your reason after the diff.

Do not make the repair only cosmetic. If a denominator is wrong, changing the caption does not repair the calculation. If assistance was discarded, the data contract must change. Record whether your correction affected wording, computation, policy, or all three.

> **RUN SLOT 11.3.** Save the human diff and reason, the corrected metric definition, and any calculation or schema change required. A drawn number is not a tested computation.

### Round 4: Test Counterfactual Records

```text
Preserve the correction. Evaluate the display rules against these synthetic
mutations: duplicate the same attempt ID; remove a delayed response; add a hint
event before a correct response; replace a wrong response with a save error;
and change the evidence-policy version. State the expected display first.

If the prototype has no executable data model, produce a rule-table evaluation
and mark runtime computation not implemented. Do not claim a data test from
manually changing the text of a chart.
```

This is a small but powerful test. The interface should respond differently when the same correct answer becomes assisted or when a missing response becomes an actual wrong response. If the headline stays the same under every mutation, perhaps it is not representing the distinction the lesson requires.

> **RUN SLOT 11.4.** Save expected and actual results, implementation status, constraint output, and any unresolved policy conflict. Use counts with denominators in the report.

## The provenance this chapter adds

```json
{
  "chapter": 11,
  "dataset": "synthetic only",
  "metric_dictionary": "RUN",
  "evidence_policy": "RUN: ID and version",
  "human_reason": "RUN: verbatim",
  "mutation_results": "RUN",
  "runtime_data_connection": "RUN: implemented or not implemented"
}
```

The record gives the final handoff a lineage from data to displayed claim. Without that lineage, a dashboard can become an attractive repository of unsupported interpretations.

## The check

**The machine half:** required data fields, duplicate-event handling in a real implementation, denominator calculations, missingness rules, and policy references. A prototype-only route can check the specification and synthetic examples, not a live data service.

**The human half:** decide whether the claim and next action are justified, whether help-seeking is represented respectfully, and whether the aggregation conceals an item defect or access barrier.

**What neither proves:** a validated mastery model, a reliable prediction of future learning, or a causal effect of the design. Those require evidence beyond a well-labelled dashboard.

## Exercises

**Warm-up**

1. *(Low; distinguish.)* Rename three activity metrics so their labels state exactly what was observed.
2. *(Low; trace.)* Trace one evidence label through event, attempt, policy, and decision.

**Application**

3. *(Medium; design.)* Create a learner view for an objective with no usable observations. Keep it actionable without implying failure.
4. *(Medium; audit.)* Compare two correct responses, one assisted and one independent. Show what the display should preserve.
5. *(Medium; audit.)* Evaluate a missing delayed response and an observed incorrect delayed response separately. Explain the denominator in each summary.

**Synthesis**

6. *(High; trace.)* Change a policy version and specify how historical summaries are labelled or recomputed.
7. *(High; design.)* Add an instructor alert for a possibly ambiguous item rather than a struggling learner. State the evidence that warrants inspection, not a final diagnosis.

**Challenge**

8. *(Open; evaluate.)* A stakeholder insists on one mastery percentage. Write the minimum model, evidence, uncertainty, and validation work that would make such a number defensible, and what you will display until then.

## What you can now do

You can build progress views whose labels match their evidence, preserve assistance and missingness, and explain the decision behind each metric instead of using activity as a stand-in for learning.

## Credit the AI

**Planned contribution:** metric dictionary, synthetic views, lineage annotations, and mutation tests. **Observed errors:** RUN. **Verification:** compare every claim with its underlying policy and records; never report synthetic values as learner outcomes.

## Next

The component library now carries rules about support, item content, feedback, scheduling, load, access, and evidence. Chapter 12 gathers those rules and the reasons behind your corrections into a contract a fresh session can load.
