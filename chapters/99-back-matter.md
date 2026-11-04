# Appendices and Working References

> **Rough-draft reference layer.** These appendices consolidate the manuscript's proposed contracts. They are not a record of completed builds, approved human reasons, measured budgets, or current tool entitlements. RUN and `[VERIFY]` markers retain their meaning here. No appendix signs a production gate.

## Appendix A: Learning Component Library Reference

The library is a set of reusable learning contracts with visual implementations, not just a collection of screen shapes. Each entry needs an identifier, purpose, content schema, allowed states, support behavior, reveal rule, access contract, evidence interpretation, and human-review boundary.

### A.1 The Common Item Contract

| Field | Required meaning |
|---|---|
| `item_id` and `content_version` | Stable item identity plus the version actually presented |
| `objective_id` | Performance the item is intended to support or assess |
| `item_type` | Response form, not a claim of automatic grading |
| `stem` and source | Reviewed task content and its source status |
| `key_or_rubric` | Authoring basis for scoring, with human-review status |
| `support_level` | Requested help condition, separate from observed help use |
| `attempt_state` | Current interaction state, separate from support and theme |
| `assistance` and `solution_exposure` | Context needed to interpret the attempt |
| `feedback` and `hints` | Reviewed content with explicit reveal conditions |
| `access_contract` | Semantics, focus, alternatives, errors, and runtime tests |
| `evidence_policy` | Versioned interpretation, including missing/unusable cases |
| `rule_refs` | Applicable reusable rules and authorized exceptions |

This is a neutral contract for the book. It is not a validated Figma, LMS, analytics, or provenance schema. Map it explicitly to the selected implementation and retain the meaning of every field.

### A.2 Components Built Through the Book

| Component/family | Purpose | Distinctive requirement | Chapter |
|---|---|---|---|
| Support scaffold | Change help while preserving the target task | Parallel worked example must not be misreported as independent target retrieval | 5 |
| Single choice | Discriminate among reviewed alternatives | One defensible key under explicit assumptions; rationale for distractors | 6 |
| Short answer | Produce reasoning | Reviewed rubric, acceptable variation, unresolved-response route | 6 |
| Ordering | Produce a sequence | Unique or explicitly accepted alternative sequences; non-drag route where required | 6, 10 |
| Case classification plus reason | Connect a category to a stated case | Classification alone does not satisfy an explanation objective | 6 |
| Feedback region | Explain the result and next learning action | State-specific content; no unsupported diagnosis of the learner | 7 |
| Hint ladder | Support a reasoning step | Review cumulative information, not only individual strings | 7 |
| Review queue | Show new, due, late, and unavailable work | Versioned scheduling policy; missing is not wrong | 8 |
| Progress evidence view | Support next-step decisions | Activity, assistance, independence, delay, and missingness stay distinct | 11 |

The actual library file, instance read-backs, and resolved state screenshots remain RUN. Do not distribute this reference as if a duplicable production library already exists.

### A.3 State Review Card

For every item, inspect at least the unanswered, draft, hint, committed, feedback, retry, and error/recovery states that the design requires. Cross those with valid support conditions. Mark a combination valid, invalid by contract, not implemented, or not tested. These are different statuses.

For every reachable pre-commit information state, ask whether the learner can obtain the target key through visible text, style, cumulative hints, accessible names, or another implemented path. For every post-commit state, ask what happened to the response, assistance history, and interpretation. A default screenshot is not the whole item.

### A.4 Review Ownership

The agent can produce and inspect structure. A content expert reviews keys, rubrics, and task alignment. The author decides learning trade-offs and human-constraint releases. Implementation and access specialists test the built route. Actual learners supply observations no agent can fabricate. The responsibilities can be shared by people, but none should be silently assigned to an unvalidated automatic pass.

## Appendix B: Call-Budget Ledger

### B.1 Plan Before Running

Use an observed current allowance, not a number copied from this draft. Keep a local session ceiling below the available allowance and reserve room for diagnosis. The chapter ceilings are planning examples. They are not measured consumption and should not be added together as a book cost.

| Session field | Value |
|---|---|
| Date, connection/client version | RUN |
| Intended local file alias and allowed write scope | RUN |
| Current access/allowance evidence | RUN, redacted |
| Planned session ceiling | RUN |
| Required observations | RUN |
| Diagnostic reserve | RUN |
| Stop conditions | RUN |

### B.2 Record Every Request

| Order | Round | Tool/operation | Purpose | Result | Retry relation | Meter evidence |
|---|---|---|---|---|---|---|
| RUN | RUN | RUN | RUN | success/failure/unknown | RUN | observed/unavailable |

Count the request history you actually observed. Do not erase errors or count one multi-request round as one request. Keep local processing, MCP requests, agent usage, and Figma AI/Make credits separate. If a provider's charging behavior is unclear, mark it unclear and retain the displayed evidence.

### B.3 Reconcile After Running

Report planned versus actual requests, actual visible meter changes, failed attempts, and the largest source of variation. A missing meter reading is not zero cost. An unchanged meter during one operation does not establish a universal free-use rule.

Useful explanations name causes: repeated inspection, wrong target, a permission error, a script defect, extra screenshots, or a necessary recovery. "The agent used too many calls" is a conclusion without a diagnosis. The record should suggest what to change in the next session.

### B.4 Stop Card

Stop production when identity is wrong, the target is uncertain, a critical constraint fails, a write produces unexpected destructive behavior, required evidence is missing, or the session ceiling is reached. Preserve the attempt, inspect the actual state, and choose a bounded diagnostic action. Never retry a broad write blindly after a partial failure.

## Appendix C: Dated MCP Tool and Read-Path Leads

**Source date:** September 26-27, 2026, in FEA's saved capability and tool records. **This book's current live verification:** not run. This is a research checklist, not a current exhaustive tool reference. Recheck names, availability, permissions, response shape, limits, and billing before teaching a live session.

| Name in the blueprint/source | Intended use in this book | Verification needed |
|---|---|---|
| `whoami` | Confirm session identity and account context | Current returned fields; redaction and identity limits |
| `create_new_file` | Make a disposable sandbox where supported | Current permissions, destination, and supported file types |
| `use_figma` | Execute bounded canvas scripts | Current skill/API surface, write permissions, restrictions |
| `get_screenshot` | Observe one rendered state | Selection, fidelity, output handling, and supported save path |
| `get_metadata` | Locate nodes and inspect available structure | Exact fields and omissions for the chosen selection |
| `get_design_context` | Supply design evidence to another agent | Current response format and learning-rule survival |
| `get_variable_defs` | Inspect variable definitions | Resolved versus alternative values and scope |
| `get_figjam` | Read the objective/evidence map | Current table/sticky text recovery and board limitations |
| `generate_diagram` | Optional structured diagram creation | Current availability and whether required relations survive read-back |
| `search_design_system` | Locate reusable components | Current indexing, selection behavior, and available context |

`create_design_system_rules` is described by the blueprint as a prompt/workflow. Do not silently list it as an executable tool without checking the current interface. A workflow name, a skill name, a tool, and a Plugin API method are different kinds of operation.

### C.1 Read-Path Findings That Need Replication

FEA's annotation notes record frame annotations returned through a design-context read, component-set annotations omitted in tested examples, and limited text recovery from a FigJam sticky. They also caution that an untested variant location is not established by those observations. All are dated leads `[VERIFY]`.

The new chapter must save the exact selection and raw response. If the current product behaves differently, report the difference. Do not force the result to match the older source. Date the new evidence and update the manuscript's current claim without deleting the historical record.

### C.2 Account Facts Are Not a Universal Tier Table

The sibling account was a verified higher-education account with a particular seat and institutional context. Its September limits and enabled features do not establish the current entitlement of every reader. The plan tags in this rough manuscript are provisional. Optional Make, backend, export, and platform routes need their own current checks.

### C.3 Source Locations

- `../figma-for-educational-ai/CAPABILITIES.md`
- `../figma-for-educational-ai/experiments/log.csv`
- `../figma-for-educational-ai/youtube/show-tell-what-a-day-costs/evidence/sources/tools-and-prompts.txt`
- `../figma-for-educational-ai/examples/review-notes/evidence/figma-results.md`
- `../figma-for-educational-ai/examples/film-03/`
- `../figma-for-educational-ai/examples/film-07/`
- `../figma-for-educational-ai/examples/film-12/`

Keep the book self-contained at the research stage by gathering reviewed notes and approved excerpts. These relative source pointers locate the drafting leads; they are not a finished external bibliography.

## Appendix D: Complete Proposed Learning Rules File

The following is a complete **rough-draft model**, not the approved `LEARNING-RULES.md` that Chapter 12 compiles from actual corrections. The operational rules are written out so the author can review them. Human reasons and source rounds remain unfilled because no canvas correction rounds have run for this manuscript. Never present the proposed rationale below as the author's recorded verbatim reason.

### Header and Loading Contract

```text
LEARNING-RULES.md
Status: proposed rough-draft model, not human-approved
Scope: demonstration practice unit; exceptions require explicit scope
Authority: approved objective/evidence map and human-authored constraints
Version: draft-v1

Before writing: load the relevant objective row, item/component contract,
current support/attempt state, applicable rules, and active human constraints.
Report missing or conflicting requirements before editing their scope.
Never manufacture a human reason, correction, approval, or release.
```

### R1: Preserve the Pre-Commit Information Boundary

**Do:** define commitment and permitted information for each task. **Do not:** expose the target key through styling, text, cumulative hints, semantics, or another reachable pre-commit route intended to preserve retrieval. **Proposed rationale:** exposure changes what the response demonstrates. **Human why/source round:** RUN. **Check:** state/route audit; built data/semantics tests where applicable. **Exception:** clearly labelled demonstration or solution-study activity, not reported as independent target retrieval.

### R2: Preserve the Target Performance

**Do:** identify the objective and required learner response before changing an interaction. **Do not:** replace explanation, retrieval, or comparison with a simpler action while claiming the objective is unchanged. **Proposed rationale:** production convenience can remove the work the lesson intends. **Human why:** RUN, verbatim. **Source round:** RUN. **Check:** objective-to-evidence audit and counterexample learner. **Exception:** an author-approved objective/scope revision, recorded explicitly.

### R3: Keep Hints as Bounded Support

**Do:** state the reasoning step left to the learner after every reachable hint combination. **Do not:** rename the solution as a hint or erase help use when the hint closes. **Proposed rationale:** assistance is useful but changes the evidence context. **Human why/source round:** RUN. **Check:** cumulative hint review and assistance-history tests. **Exception:** a labelled solution-view route with the correct exposure interpretation.

### R4: Explain Feedback

**Do:** connect feedback to the submitted reasoning, reviewed key/rubric, and objective. **Do not:** use a score or praise as the entire explanation when the task requires reconciliation. Do not invent learner motives or traits. **Proposed rationale:** the learner needs a defensible account of the result. **Human why/source round:** RUN. **Check:** content review across correct, incorrect, partial, and unresolved responses. **Exception:** a task-specific, author-approved feedback policy with its reason recorded.

### R5: Separate Support From Attempt State

**Do:** keep support condition, visible state, observed assistance, solution exposure, and theme distinct. **Do not:** infer expertise from a mode name or count exposed-answer retries as independent evidence. **Proposed rationale:** the same visible score can arise under different conditions. **Human why/source round:** RUN. **Check:** state matrix, resolved bindings, and evidence-policy tests. **Exception:** none to the requirement to label observed conditions honestly; support policies themselves may vary by task.

### R6: Keep Item Content Reviewable

**Do:** require stable IDs, content versions, objective references, key/rubric rationale, and a human-review state. **Do not:** equate schema validity with content validity or auto-approve an ambiguous key. **Proposed rationale:** reusable structure cannot guarantee a defensible question. **Human why/source round:** RUN. **Check:** structural audit plus expert content review. **Exception:** an explicitly labelled draft proposal remains outside the approved item set.

### R7: Remove Container Burden Without Removing Learning

**Do:** use the objective and learner context to diagnose effort. Run geometry and declared style checks before content judgments. **Do not:** remove a reasoning step because it slows completion or call a heuristic critique a measured load reduction. **Proposed rationale:** ease and learning are different design targets. **Human why/source round:** RUN. **Check:** four-question diagnostic, deterministic audit, and human review. **Exception:** scoped policy exceptions approved and documented, not silent global waivers.

### R8: Preserve Access to the Task

**Do:** specify labels, semantics, focus, alternatives, recovery, and runtime tests by state. **Do not:** infer runtime accessibility from a canvas or leak the answer through an alternative. **Proposed rationale:** an access barrier corrupts the intended evidence. **Human why/source round:** RUN. **Check:** design review, built tests, and relevant user/specialist review. **Exception:** an unresolved barrier is a declared blocker or limitation, not an invisible pass.

### R9: Specify Time and Persistence Honestly

**Do:** version the scheduling policy, define time semantics, preserve accepted attempts, and test edge cases in a real implementation. **Do not:** call a pictured date a running scheduler or treat a missing follow-up as wrong. **Proposed rationale:** cross-session behavior requires more than state drawings. **Human why/source round:** RUN. **Check:** policy read-back and implementation boundary tests. **Exception:** a labelled simulation may demonstrate states but makes no persistence claim.

### R10: Match Progress Labels to Evidence

**Do:** preserve activity, support, exposure, independence, delay, missingness, and unavailable observations. Name denominators and policy versions. **Do not:** derive mastery from completion or silently rewrite raw events to fit a summary. **Proposed rationale:** a display label is a claim about data. **Human why/source round:** RUN. **Check:** metric lineage and synthetic mutation tests. **Exception:** activity metrics are allowed when literally labelled and not substituted for learning.

### R11: Protect Human Corrections and Their Reasons

**Do:** read active constraints, save the actual script, snapshot supported properties, and check before recording. Preserve human reasons verbatim. **Do not:** undo a correction, invent its reason, or release it without the responsible human's words. **Proposed rationale:** the next round should retain author judgment. **Human why/source round:** RUN. **Check:** ledger validation, constraint checks, and human inspection of uncaptured properties. **Exception:** a narrow recorded human release; never a silent agent override.

### R12: Keep Claims Within Observed Evidence

**Do:** distinguish proposed, executed, observed, and independently checked work. Keep RUN, not-run, unavailable, and Cannot determine explicit. **Do not:** simulate learner results, reconstruct idealized transcripts, fabricate costs, or claim a release/gate was signed. **Proposed rationale:** inspectable uncertainty is more useful than a false success story. **Human why/source round:** RUN. **Check:** artifact/claim audit and human review. **Exception:** illustrative examples are allowed only when unmistakably labelled illustrative.

### When a Request Conflicts With a Rule

Stop the affected change, name the conflict and its scope, and offer a compliant alternative. A request to reduce anxiety need not reveal the answer; it may justify additional support. A request for simpler reporting need not rename completion as mastery; it may justify a more literal activity summary.

If the human chooses a revision, record the authorized change or narrow release in their words. Preserve the earlier version and recheck affected states. Do not use one exception to disable unrelated rules. Do not invent an approval to keep the build moving.

### Independent Review Output

For every evaluated rule, return PASS, FAIL, or CANNOT-DETERMINE, with artifact version, screen/state, evidence location, and limit. Map this review vocabulary explicitly to any ledger field vocabulary. Not-run means a test was not performed; Cannot determine means the inspected evidence did not answer the question. Neither is a pass.

The reviewer must not edit the work it is evaluating or approve the release. Ground truth for planted defects is written before the review. Count true flags, false flags, misses, and unavailable cases without hiding small denominators behind percentages.

## Appendix E: Provenance and Evidence Templates

### E.1 Use the Existing Tooling

`PROVENANCE.md` and `tools/provenance/schema.json` define the actual ledger workflow. The agent runs the commands; the reader supplies intent, corrections, and reasons. The chapter JSON fragments are explanatory sketches, not files to paste over the live ledger.

Use `prov.py init` only for a new project, never to reset history. Record the actual actor, snapshot, intent, script, chapter, request count, and available check results. A human round requires the human's verbatim why. A released constraint needs the authorized release reason. Keep private file mappings outside the public ledger.

The local ledger helper and the live Figma snapshot/stamp route have different evidence status. Passing local tests does not prove a live API integration. Save the first actual run and any failure instead of replacing the distinction with "provenance works."

### E.2 Blank Round Card

| Field | Entry |
|---|---|
| Project alias / actual round ID / chapter | RUN |
| Actor / intent | RUN |
| Input contract and versions | RUN |
| Exact prompt and saved script | RUN |
| Snapshot scope and uncaptured properties | RUN |
| Screenshot or other observed evidence | RUN |
| Human diff and verbatim reason, if applicable | RUN |
| Constraints added, preserved, or released | RUN |
| Checks passed / failed / not run | RUN |
| Requests and actual visible cost evidence | RUN |
| Next action and unresolved limits | RUN |

Never fill the card with a hypothetical event and then export it as history. Illustrative cards belong in teaching material with an explicit label, not in the project ledger.

### E.3 Learner-Test Report Card

Record protocol and prototype versions, appropriate permission status, recruitment scope, actual participation, assistance, environment, delay, rubric, missingness, and limitations. Keep private identities and consent records separately. Report observations, interpretations, proposed repairs, and retest results in distinct fields.

If the test has not run, the report status is pending and every result field remains empty or RUN. An agent-generated persona, a prediction, or a walkthrough by the designer is not a participant. A pending test is an honest project dependency, not an invitation to fill the table with plausible numbers.

## Working References and Research Leads

### Local Source Texts Used for Drafting

1. Nik Bear Brown, *Experience Design for EdTech*, Chapter 3, "The Cognitive Machinery: Load, Difficulty, and Durable Learning." Working source: `../learning-experience-design-lxd/chapters/03-the-cognitive-machinery-load-difficulty-and-durable-learning.md`.
2. The same work, Chapters 1, 6, 9, 13, and 14: engagement versus learning, journey mapping, variability/accessibility, instrumentation, and evaluation. These are concept leads for this book's research phase.
3. Nik Bear Brown, *AI for Learning Experience Design*, Chapters 3, 6, 7, and 14: scaffolding, tutoring interactions, adaptive systems, and evaluation. Working directory: `../ai-for-learning-experience-design/chapters/`.
4. *Figma for Educational AI*, capability map and saved experiments, dated September 2026. Working directory: `../figma-for-educational-ai/`.
5. This project's `BLUEPRINT.md`, `PROVENANCE.md`, and `pantry/CHAPTER-TEMPLATE.md`: authoring plan and working method, not empirical evidence of product or learner behavior.

### Primary Learning-Science Leads Inherited From LXD Chapter 3

The following references are inherited research leads. Their scope and applicability to this manuscript have not been independently checked here. Do not interpret their inclusion as verification of every proposed screen rule.

- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257-285. [Publisher record](https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1202_4).
- Sweller, J., van Merrienboer, J. J. G., and Paas, F. (2019). Cognitive Architecture and Instructional Design: 20 Years Later. *Educational Psychology Review*, 31, 261-292. [Publisher record](https://link.springer.com/article/10.1007/s10648-019-09465-5).
- Kalyuga, S., Ayres, P., Chandler, P., and Sweller, J. (2003). The Expertise Reversal Effect. *Educational Psychologist*, 38(1), 23-31. [Publisher record](https://www.tandfonline.com/doi/abs/10.1207/S15326985EP3801_4).
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., and Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354-380. [Indexed record](https://pubmed.ncbi.nlm.nih.gov/16719566/).
- Roediger, H. L., and Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*, 17(3), 249-255. [Publisher record](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x).
- Karpicke, J. D., and Blunt, J. R. (2011). Retrieval Practice Produces More Learning than Elaborative Studying with Concept Mapping. *Science*, 331(6018), 772-775. [Publisher record](https://www.science.org/doi/10.1126/science.1199327).

### Still Needed Before Publication

Current official Figma tool/access documentation and live capability tests; current authoritative accessibility requirements and relevant platform patterns; selected LMS integration and export documentation; research notes for every chapter; content review of demonstration items; actual scripts and observed run records; appropriately permitted learner testing; and an author-edited, claim-checked bibliography.

The author review also needs to settle the remaining blueprint decisions: final audience and deployment format, imprint/series line, K-12 scope, and the strength of the central thesis after observing the baseline. The running LXD lesson is a provisional drafting choice, not a claim that every planning question has been resolved.

## About the Author

Nik Bear Brown is the named author of this project and its companion manuscripts. Additional biography, affiliations, acknowledgments, and publication details are intentionally left for the author's review rather than invented to complete the back matter.
