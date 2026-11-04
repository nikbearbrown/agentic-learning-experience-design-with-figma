# Chapter 14 - Handoff: Code, Make, and the LMS
*The prototype ends. Its obligations should not.*

> **Rough draft - pre-research.** Figma/Make leads: FEA `CAPABILITIES.md`, `examples/film-23/MAKE-BRIEF.md`, and the tested read paths from earlier chapters `[VERIFY]`. LMS, embedding, LTI, packaging, and grade/reporting claims require current primary-source research for the selected platform. No export, integration, or release is claimed here.

## The concept

Suppose the prototype is correct. The learner drafts a response, commits, receives an explanation, and requests a new case. Then an implementation agent turns it into a web page where selecting an option immediately reveals the key. The result may look almost identical. The learning contract has not survived.

This is the real handoff problem. Passing a screenshot is easy. Passing the reason for a delayed reveal, the distinction between support and independence, the meaning of a missing response, and the tests that verify those distinctions is harder.

We will compare three routes: a code implementation informed by design context, a Make implementation where available, and an LMS-hosted or LMS-integrated route. The right choice depends on the required behavior, current access, data responsibility, and the delivery environment. There is no universal winner and no automatic route from design fidelity to learning fidelity.

### Handoff the Contract, Not Just the Canvas

The package needs the objective map, component contracts, item content and reviewed keys, state machine, support model, scheduling policy if used, access requirements, evidence model, rules file, provenance, known limits, and acceptance tests. A screenshot index helps the implementer locate states. It cannot replace those contracts.

Name the authoritative version of each artifact. An implementation agent receiving three rules files must not decide by whichever one appears last in its context. Define conflict handling: stop, identify the contradictory requirements, and ask the author or designated owner. Do not silently loosen a learning rule because an implementation route makes it inconvenient.

Separate authoring data from learner-facing data. A hidden answer layer in Figma is useful for authoring, not a security design. A real application may need to control when answer information is delivered and where scoring occurs according to its threat model and purpose. Do not promise assessment security from client-side hiding. For low-stakes practice, some exposure risks may be acceptable; state the decision rather than pretending they do not exist.

### Route One: Code From the Design Evidence

Design-context output can provide a useful starting representation, but generated code is not automatically the product. The build still needs the reviewed state logic, semantic controls, persistence, error handling, privacy decisions, and tests.

The sibling project records design-context examples and a framework-shaped response `[VERIFY: FEA film-03 and film-07 saved contexts]`. Use the actual current response for the selected target. Do not assume that a code-looking output contains the requirements missing from the source file.

This route can offer direct control over tests and data flow, depending on the chosen stack and team. It also transfers maintenance responsibility to the project. An agent can help implement but cannot make that responsibility disappear. Before choosing it, identify who will fix a broken dependency, rotate a credential, or respond to a failed save after the book exercise ends.

### Route Two: Make, If Available

The blueprint's Make route is optional and provisionally HE-tagged. FEA's dated capability notes and pending flashcard brief are research leads, not a current access guarantee or a completed evaluation `[VERIFY]`.

A Make brief should name the same contracts as a code brief. It should not become "make this interactive" with an image attached. Ask for a bounded slice: one item, its states, a synthetic attempt record, and the tests that matter. Observe actual credit use, export behavior, persistence, and code ownership where relevant. Do not assume an integration advertised elsewhere is enabled for this account.

The benefit may be speed of getting an executable sample. The cost may include opaque changes, limited control, access restrictions, or a backend arrangement that does not fit the institution. Those are questions to test, not conclusions to invent. If the route cannot preserve a required behavior, keep the requirement and reconsider the route.

### Route Three: The LMS

"Put it in the LMS" can mean a native quiz, a content page, an embedded application, a packaged module, or an integration using a supported standard. These are different architectures. Each may impose different restrictions on scripts, authentication, data storage, accessibility, grading, and navigation.

This book has not researched the current constraints for a specific LMS. The handoff should therefore contain a platform discovery step, not confident generic instructions. Ask the platform owner what is allowed, inspect current official documentation, and test in a nonproduction course. Do not assume a Figma embed becomes an assessment, a package imports every interaction, or a score reaches the gradebook merely because the page loads.

Likewise, a package format and an integration standard solve different problems. Do not use their acronyms as synonyms for compatibility. Record the exact required outcome: launch, identity, response persistence, completion reporting, grading, or return navigation. Then test that outcome in the selected environment.

### Choose by a Required Slice

Use a decision matrix with current evidence:

| Requirement | Code route | Make route | LMS route |
|---|---|---|---|
| Pre-commit reveal boundary | Test in build | Test in build | Test selected interaction |
| Assistance-aware attempts | Implement/test | Verify/implement/test | Verify supported data path |
| Persistent schedule | Implement/test | Verify backend and policy | Verify platform or external service |
| Access contract | Build/manual tests | Build/manual tests | Platform plus content tests |
| Ownership and maintenance | Named project owner | Current terms/export/owner | Named institutional owner |
| Actual cost/access | RUN | RUN | RUN |

This is a research and test matrix, not a comparative product rating. The blank evidence is the work to do. Choose the smallest route that satisfies the nonnegotiable requirements and has an owner who can maintain it.

<!-- [TABLE: handoff package manifest with artifact version, authoritative owner, acceptance test, and route-specific unresolved questions] -->

### Content Migration Can Break the Learning Contract

An export may flatten variants, drop annotations, transform text, or separate assets from their descriptions. The exact behavior must be tested for the selected route. The general handoff risk is that material survives visually while its relation to the objective or state disappears.

Create an export inventory. For each item, identify the content version, key or rubric location, feedback, alternatives, support metadata, and state references. After import or generation, compare the inventory rather than checking only that the first screen opens. A missing hint rationale or stale alternative can matter as much as a missing image.

If the target platform cannot express a required field, do not discard it silently. Keep it in the handoff as an unresolved mapping and decide whether the behavior can be implemented elsewhere or the product scope must change. A documented loss is a decision. An undocumented loss is a future surprise.

### Authentication Is Not an Authorization Test

A built sample that lets one test user sign in does not prove that users can see only their own responses or that an instructor can see only permitted records. The required roles and data boundaries need explicit tests if the product stores real learner information.

For the book's first slice, use synthetic data and the smallest approved environment. If a later project adds real identities, involve the responsible institutional owner and security/privacy process. Do not let the agent create a production data service merely because it knows how to add a sign-in screen.

The same caution applies to secrets. An application that works with a key embedded in client code has not established a safe configuration. Follow the project's secure configuration path and inspect the actual data flow. A screenshot of a successful request is not evidence that the credential was handled appropriately.

### Define Who Can Approve a Substitution

Some substitutions are implementation details: a different layout mechanism that preserves behavior and access may not need an author-level decision. Others change the learning task: replacing explanation with recognition, dropping a delayed check, or revealing the answer early to fit a native widget.

Write a change-classification rule in the handoff. The implementer can propose changes, but the responsible human should decide substitutions that alter the objective, evidence, information boundary, privacy boundary, or accessibility route. The agent should identify those changes before making them, not report them as incidental cleanup afterward.

### Keep a Release Checklist Separate From the Book Rubric

The capstone rubric evaluates the design work. A real release may also require operational monitoring, backup and recovery, support ownership, performance checks, content rights, and platform approval. Those are not automatically satisfied because the chapter exercises are complete.

This book deliberately stops short of issuing a production certificate. The handoff should give the next owner a clear list of what was tested, what failed, and what remains. That is more useful than a broad "ready to ship" sentence whose meaning changes depending on who reads it. The final release authority belongs to the responsible people and processes for the actual deployment.

### Reproducibility Needs a Starting Point

Save enough environment information for another authorized implementer to repeat the acceptance slice: relevant tool versions, dependency or export versions, setup assumptions, synthetic data, and exact test steps. Keep secrets and private account mappings out of that record. A reproducible test is not the same as a publicly reproducible production account.

For an agent-generated build, retain the actual prompts and patches or export artifacts that produced the tested version. A later rerun may generate a different implementation. That difference is worth inspecting, not a reason to replace the record with whichever version looks best.

If a platform update changes the behavior, preserve the earlier tested result with its date and create a new result for the current environment. Do not call the old test false merely because it no longer describes the product. This dated evidence is especially important in a book about changing agent tools. The enduring lesson is the contract and method; the operational details need a visible maintenance history.

## What you'll be able to do

- **Choose** a delivery route using required behavior and observed constraints.
- **Package** the learning contract with versions, owners, and acceptance tests.
- **Test** one end-to-end slice rather than claiming compatibility from appearance.
- **Report** losses, substitutions, and unimplemented requirements without silently changing the objective.

**Plan:** all for package/specification work; optional Make HE, provisional. **MCP budget:** package/read-back planning ceiling 20 requests; actual RUN. **Build/integration costs:** separate and RUN. **Builds on:** Chapters 10-13.

## Talking to Figma

### Round 1: Assemble the Handoff Manifest

```text
Assemble a manifest for the approved lesson. Include objective map, item and
component contracts, support states, feedback/state machine, scheduling policy,
access contract, evidence model, rules, provenance, known limits, and tests.
Use exact versions and source paths. Identify missing or conflicting artifacts.

Separate public teaching material, private authoring keys, credentials, and
participant material. Do not copy private data into the handoff or publish it.
Read back the required design annotations and report what the build agent will
actually receive. Do not start implementation until route blockers are clear.
```

The manifest should expose an uncomfortable truth if one exists. A complete-looking prototype may have no defined save-error behavior or no rubric for short answers. That is a handoff defect worth finding now. Do not paper over it by writing a plausible default without recording the decision.

> **RUN SLOT 14.1.** Save manifest, versions, read-back evidence, missing requirements, and ownership questions. Keep secrets and private identifiers out of the committed record.

### Define One Acceptance Slice

Choose one item and one meaningful user journey. For this book, the slice can be:

1. Open a new case in the intended delivery environment.
2. Draft a response without seeing correctness information.
3. Request a hint, then return with the draft intact.
4. Commit exactly one attempt with assistance recorded.
5. Receive the reviewed explanation through the supported access route.
6. Return later and see the persisted attempt interpreted under the declared policy.

The slice crosses visual, behavioral, data, and access boundaries. It is small enough to test but substantial enough to reveal whether the route fits. If persistence is outside the intended product, remove it deliberately and state the resulting limit. Do not claim it from a prototype history.

Write expected results before implementation. For example, repeated activation must not create two accepted attempts under the chosen contract. A failed save must not be reported as an incorrect response. The display must say assisted if the hint was used, even after it closes.

### Your Turn: Choose and Bound the Route

Review the matrix with the person responsible for delivery. Pick a route based on current evidence and unresolved risks, not the ease of taking a screenshot. If a platform cannot support a nonnegotiable behavior, choose another route or explicitly revise the product scope.

A scope revision is an author decision. Replacing an explanation task with a native choice quiz may be acceptable for a different objective; it is not an invisible technical substitution. Record the learning consequence and your reason in the design history.

> **RUN SLOT 14.2.** Save the route decision, evidence used, blockers, authorized scope changes, and human reason. A decision made before implementation remains provisional until the slice passes.

### Round 3: A Fresh Agent Implements the Slice

```text
Using only the approved handoff package, implement the bounded acceptance slice
in the selected sandbox route. State the contract you recovered before writing.
Do not consult the earlier design conversation as hidden context. List missing
requirements rather than inventing them. Use established libraries and platform
patterns for domain logic and access behavior where appropriate.

Do not publish, connect real learner records, or alter a production course.
Save the code/export provenance and actual tests. Report every requirement as
passed, failed, not implemented, or not tested, with evidence.
```

This is Chapter 12's fresh-session test applied to implementation. It measures whether the package can carry intent, not whether the same agent remembers what it meant yesterday.

> **RUN SLOT 14.3.** Save the fresh-session inputs, recovered contract, implementation artifacts, environment, tests, costs, and unresolved questions. If the route is unavailable, record that and retain the package; do not manufacture a build result.

### Round 4: Compare Learning Fidelity, Not Only Pixels

Compare the built slice against the prototype and the contract. Use separate verdicts for visual correspondence, state behavior, evidence interpretation, access behavior, and persistence. A small visual difference can be acceptable. A premature reveal with perfect typography is not.

```text
Audit the built slice independently of its implementation narrative. Trace one
attempt from input to displayed evidence. Test the defined unhappy paths.
For each difference from the design, state whether it is visual, behavioral,
instructional, data-related, or access-related. Do not approve the release.
Return findings and remaining tests for human review.
```

For an LMS route, include actual launch and return behavior in the test environment. If grading or identity exchange is required, test it under the institution's approved process. A local browser pass does not establish platform integration.

> **RUN SLOT 14.4.** Save the fidelity report, observed defects, repairs, and unrun integration tests. The result is a tested slice with limits, not a blanket production-readiness certificate.

## The provenance this chapter adds

```json
{
  "chapter": 14,
  "handoff_manifest": "RUN",
  "route_decision": "RUN: evidence and human reason",
  "fresh_agent_recovery": "RUN",
  "acceptance_slice_results": "RUN",
  "integration_results": "RUN or not-run",
  "publication_or_production_release": "not-authorized-by-this-chapter"
}
```

The record links a delivered behavior to the design requirement and author decision behind it. It also preserves where the delivery route could not carry the original contract.

## The check

**The machine half:** package completeness, version references, implemented acceptance tests, data-field integrity, and automated checks suited to the actual build. It cannot establish platform compatibility without running in the relevant environment.

**The human half:** choose acceptable trade-offs, confirm institutional delivery requirements, judge instructional substitutions, inspect manual access tests, and authorize any release separately.

**What neither proves:** long-term maintainability, universal compatibility, or learning effectiveness. A successful slice narrows the implementation risk; it does not remove every operational or instructional uncertainty.

## Exercises

**Warm-up**

1. *(Low; package.)* List three requirements a screenshot cannot hand off by itself and the artifact that should carry each.
2. *(Low; choose.)* Define the exact meaning of "in the LMS" for your project without using compatibility as an unexplained label.

**Application**

3. *(Medium; package.)* Assemble a manifest with versions and owners. Mark missing artifacts rather than silently drafting them as approved.
4. *(Medium; test.)* Write a six-step acceptance slice with at least two failure paths and a clear evidence interpretation.
5. *(Medium; choose.)* Compare two routes using current evidence. Include access, data responsibility, maintenance, and unrun tests.

**Synthesis**

6. *(High; report.)* A native platform interaction cannot collect the required explanation. Propose an alternative and state whether the objective changes.
7. *(High; test.)* Ask a fresh agent to recover the contract from the package alone. Report missing context separately from implementation defects.

**Challenge**

8. *(Open; evaluate.)* A build matches every screenshot and fails one information-boundary test. Write the release recommendation and the minimum repair/retest evidence needed to reconsider it.

## What you can now do

You can choose and test a delivery path without treating a design export as a finished learning product. You can preserve the contract, record losses, and keep the release decision with its responsible human owner.

## Credit the AI

**Planned contribution:** manifest, route investigation, bounded implementation, and independent fidelity audit. **Observed errors and cost:** RUN. **Verification:** actual environment tests, raw acceptance evidence, and human decisions about scope and release.

## Next

Chapter 15 repeats the full chain on your own lesson. The purpose is not to demonstrate every feature in the book. It is to produce one defensible learning experience whose design, evidence, and limits you can explain end to end.
