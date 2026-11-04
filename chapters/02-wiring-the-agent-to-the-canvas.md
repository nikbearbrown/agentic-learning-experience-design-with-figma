# Chapter 2 - Wiring the Agent to the Canvas
*A connection is useful only when you know where it can write.*

> **Rough draft - pre-research.** Tool and account leads come from `../figma-for-educational-ai` (FEA), principally `CAPABILITIES.md`, dated September 26-27, 2026, and need current checks `[VERIFY]`. Prompts below are instructions, not executed sessions. Every RUN slot remains empty until a real run.

## The concept

Before I ask an agent to improve a learning experience, I want to know which experience it is allowed to change. That sounds administrative. It is actually the first design constraint in the book. The same instruction can be harmless in a duplicate practice file and expensive in a shared course library. The screen does not tell you which situation you are in.

This chapter establishes a working connection between an agent and Figma, then makes that connection accountable. The deliverable is not a screenshot of a successful sign-in. It is a small, reversible edit in the intended sandbox, accompanied by a record of what the agent did and what the session cost.

### Three Pieces, Not One Feature

The workflow has three distinct pieces. Figma holds the document and applies permissions. The agent plans the work and chooses tools. The MCP connection exposes a particular set of operations between them. MCP is the connection protocol, not a design intelligence and not a guarantee that a tool behaves as the agent expects.

This distinction is useful when something fails. If the agent cannot find a tool, redrawing the screen will not help. If the tool can read a file but not write it, changing the prompt's tone will not grant edit access. If the agent identifies the wrong file, a successful write makes the problem worse.

FEA's capability map describes a remote server and a desktop server, with different access conditions. Its September notes use the remote route for the book's Education workflow. Treat that as the proposed route, not a current installation manual `[VERIFY: FEA CAPABILITIES.md, remote and desktop MCP rows]`. I do not want this chapter to fossilize a command that changes before the manuscript is published. The agent should consult the current official setup instructions and report which route it configured. Never construct a server URL by guessing.

The setup should not require you to type commands from the book. Tell the agent the intended connection. It handles configuration and tells you when a sign-in or permission decision requires your direct action. You should understand the permission decision even if you never see the configuration syntax.

### Identity Before Editing

The sibling project begins a session with `whoami`. It records an Education account reporting "Student tier" even for an educator `[VERIFY: FEA CAPABILITIES.md, E00]`. The point is not to memorize that label. The point is to distinguish account identity, team or workspace, plan label, seat type, and file permission. These are related but not interchangeable.

A person can belong to several teams. A suitable seat does not make every file editable. A readable file is not necessarily a safe one to edit. Ask the agent to state, in ordinary language, which account and environment it is using and which file you have designated. Do not publish the raw response if it contains personal identifiers.

I use a local alias such as `practice-unit` in the ledger. The real file key stays in the private connection context. The alias does not create security; it prevents the public design history from becoming an unnecessary account inventory.

### The Sandbox Is a Permission Boundary

Use a duplicate or a new disposable file. The blueprint uses duplication rather than depending on branching because the sibling capability notes place branching outside the Education path `[VERIFY: FEA CAPABILITIES.md, branching row]`. The principle survives that product detail: the first live experiment must not touch the only copy of important work.

Say what may change. "The open file" is weak if several files are open. "Only the frame I identify inside the practice-unit sandbox; no library publication, deletion, or changes elsewhere" gives the agent a boundary it can repeat before acting.

For the first edit, I want a single labelled frame, not five questions and an imported design system. A small test is easier to inspect, easier to undo, and better at isolating a broken connection. Once that works, complexity can increase for a reason.

### A Call Budget Is a Design Budget

FEA recorded daily and per-minute MCP allowances in September. Those numbers need rechecking before a live class `[VERIFY: FEA CAPABILITIES.md, rate-limits row]`. This draft therefore does not build the exercise around a promised quota. Start with a session allowance you can actually see, then allocate a smaller local budget within it.

There are three meters to distinguish: agent-provider usage, MCP requests, and Figma AI or Make credits. They may have different reset periods and pricing. Record each separately. If a tool response fails, record the request and the failure; whether it consumes a provider allowance is a separate question. Do not erase failed requests from the session history to make the budget look efficient.

A planned twenty-call session is a ceiling for the exercise, not a claim that twenty calls are required. I reserve room for an initial inspection, one build, one correction, read-back, and a diagnostic failure. If the connection is broken, the reserve buys diagnosis rather than blind retries. If the work finishes early, stop. An unused allowance is not unfinished work.

<!-- [TABLE: connection decision record showing identity, private file mapping, permissions, sandbox boundary, three cost meters, planned ceiling, and stop condition] -->

### Failure Recovery Is Part of the Connection

A useful connection test should also tell you how to stop. If the identity is wrong, do not try a write to see whether it works anyway. If the target is uncertain, ask for a read-only confirmation. If the write succeeds but the snapshot fails, preserve the write response and inspect the actual file before retrying. Repeating the whole script may create duplicates rather than repair the missing evidence.

This is why I want the agent to save its script before running it. After a partial failure, the script is evidence of what it attempted. A later explanation such as "I only added a frame" may omit a command that changed the current page or reused an existing node. Read the attempted operations and compare them with the observed result.

For the first session, write a stop card in plain language: wrong identity, uncertain target, unexpected deletion, constraint violation, missing critical evidence, or budget ceiling reached. Each condition should have an allowed next action. Stopping need not mean abandoning the project; it means changing from production to diagnosis without pretending nothing happened.

Also distinguish undo from recovery. Undoing a canvas edit may restore a visible state while leaving a ledger record, a duplicate file, or a consumed allowance. Deleting the evidence to make the history look clean is not recovery. Keep the failed attempt and append the corrective action.

The connection test ends with a short operational note: which route worked, what remained unsupported, where the private file mapping lives, and how the next session should confirm its target. That note makes a successful setup repeatable without publishing account details. A future session should still check identity rather than trust an old screenshot.

None of this needs to become ritual overhead on every tiny edit. The point is to establish a known safe pattern, then reuse it proportionately. Batch observations when that does not weaken them. Keep the checks whose absence would make a mistake invisible. Efficiency means fewer unnecessary operations, not fewer opportunities to notice that the agent is acting somewhere you did not intend.

Keep one distinction in your setup note: a permission you granted is not a test the agent passed. Record the grant, the action, and the observation separately. That small habit will matter throughout the book whenever an intended capability risks being mistaken for an observed result.

## What you'll be able to do

- **Configure** a connection using current official instructions, with the agent performing the setup work.
- **Distinguish** identity, seat, file access, and a designated editing boundary.
- **Plan and reconcile** a session budget that includes failed attempts and separates the three meters.
- **Demonstrate** one reversible edit and a read-back without claiming more than the test shows.

**Plan:** all, provisionally; current access must be checked. **MCP budget:** planning ceiling of 20 requests; actual use RUN. **Builds on:** Chapter 1's preview; no completed baseline required yet.

## Talking to Figma

### Before the First Write

Give the agent this instruction:

```text
Prepare the remote Figma MCP connection for this project using the current
official setup guidance. Do the configuration work yourself. Ask me only for
sign-in or permission decisions that require me. Do not expose credentials.

Before writing: report available tools, confirm identity and the intended team,
and identify the sandbox file using the local alias practice-unit. Explain any
missing access. Do not edit, publish, or delete anything yet.
```

The agent should report what is known and what is not. A browser sign-in completing is evidence of authentication, not proof that the canvas write route works. If the available tool names differ from this draft, retain the original name in the chapter record and record the current equivalent. Do not silently rewrite history.

> **RUN SLOT 2.0.** Record setup date, client and connection route, available tools, redacted identity summary, sandbox confirmation, and current allowance evidence. Keep authentication responses private. State whether any part of setup remains unresolved.

### Round 1: The Agent Draws a Connection Test

```text
In the designated practice-unit sandbox only, create one frame labelled
Connection test. Put the text "LXD practice unit: connection test" inside it.
Do not create quiz content yet. Save the exact write script before running it.

Initialize the provenance ledger if it does not exist. Never reinitialize an
existing ledger. Follow PROVENANCE.md: snapshot, check active constraints,
stamp, screenshot, and record. Stop if any required step fails; report which
evidence is missing rather than claiming a complete round.
```

This follows the same sequence as Chapter 1, but isolates the machinery. The proposed `snapshot.js` and `stamp.js` helpers are not live-verified in this manuscript. `PROVENANCE.md` explicitly says so. Their first successful use belongs here, with the response and the script saved, not with a sentence saying they should work.

A snapshot is a selected representation of the file. It is not a backup of every property. A stamp is a pointer to the ledger, not the ledger itself. A screenshot is visual evidence, not a complete state record. We keep all three because each answers a different question.

For example, a screenshot can show that text appeared. The snapshot can show which node contains it. The saved script can show how it was produced. The ledger can show the actor and intent. If one is missing, name the gap. Never make a ledger entry look fully evidenced merely because the canvas looks plausible.

> **RUN SLOT 2.1.** Save the exact script, tool responses, snapshot and stamp results, screenshot, ledger validation output, and request count. Mark the connection test complete only if the intended frame exists in the intended sandbox and can be read back.

### Your Turn in Figma

Change the test label by hand. Do not change everything. Replace "connection test" with "human correction recorded" and move the text a little within the frame. These are deliberately mundane edits. We are testing whether a human correction is detectable and preserved, not whether the agent can infer a whole pedagogy from one word.

Tell the agent:

```text
Done. Snapshot the same frame, compare it with the last recorded snapshot,
and describe my changes. Ask me for my reason before recording a human round.
Do not invent my reason or reuse an example reason from the book.
```

Give the real reason in one line. It may be as simple as testing that hand edits persist. This is your statement, not prose the agent is authorized to improve. A beautifully paraphrased reason can lose the distinction you intended to preserve.

The generated constraints may be too literal for later design work. That is fine in a connection test. Later chapters distinguish a node-level constraint from a general learning rule. Here the test is whether the next agent write respects the recorded human edit at all.

> **RUN SLOT 2.2.** Save the before/after diff, your verbatim reason, the created constraints, and any properties the snapshot did not capture. If the diff misses an edit, the helper needs diagnosis before it is trusted.

### Round 3: The Agent Redraws Under Constraint

```text
Read the active constraints. In the connection-test frame, add a second line
reading "Ready for Chapter 1 baseline" without changing my corrected label
or its recorded properties. Snapshot and run check-constraints before recording.
If a constraint fails, stop and report it. Do not override it yourself.
```

Check the result in the actual file. The agent may say it preserved the correction while rebuilding the text node, changing the identifier the constraint referred to. That is not the same evidence. Record how the constraint checker handles the situation. A checker that simply stops seeing the old node must not report a pass by omission.

If a human constraint makes the intended change impossible, ask for a narrow release and retain the author's words. Do not treat authorization to add a second line as authorization to discard all prior corrections.

> **RUN SLOT 2.3.** Save the final screenshot, constraint result, node continuity evidence, and ledger record. Report pass, fail, or not run for identity, sandbox, write, read-back, human diff, and constraint preservation separately.

### Reconcile the Budget

Create a row for every request. At minimum keep request order, tool, purpose, success or failure, whether a retry followed, and any displayed cost. Keep local processing separate from MCP requests. The ledger's round count and the request count will not be equal: a round can involve several requests.

| Work | Planned allowance | Actual requests | Cost evidence |
|---|---:|---|---|
| Identity and inspection | 3 | RUN | RUN |
| First draw and evidence | 5 | RUN | RUN |
| Human snapshot and diff | 2 | RUN | RUN |
| Constrained redraw and evidence | 5 | RUN | RUN |
| Diagnostic reserve | 5 | RUN | RUN |

These allocations sum to twenty. They are a planning example, not measured performance or a description of which requests count toward Figma's quota. If a batch can reduce overhead without weakening read-back, try it in a later run and compare actual evidence. Do not optimize away the very observation that would reveal a mistake.

The post-mortem should explain differences, not merely total them. Did the agent repeatedly inspect an unchanged frame? Did it request the wrong node? Did it retry a permission failure without changing the permission? Those are different causes and need different remedies.

## The provenance this chapter adds

```json
{
  "chapter": 2,
  "status": "RUN",
  "connection_route": "RUN",
  "sandbox_alias": "practice-unit",
  "rounds": [
    {"actor": "agent", "intent": "connection test", "evidence": "RUN"},
    {"actor": "human", "why": "RUN: verbatim human reason"},
    {"actor": "agent", "intent": "preserve correction", "checks": "RUN"}
  ],
  "mcp_requests": "RUN",
  "figma_credit_delta": "RUN",
  "agent_usage_observation": "RUN"
}
```

This is a reporting sketch, not a replacement for the schema enforced by `prov.py`. The record lets you distinguish a design problem from an access problem later. Keep detailed private connection information outside it.

## The check

**The machine half:** validate ledger structure, compare captured properties, count requests, and detect recorded constraint violations. A passing local test of `prov.py` does not validate the live snapshot and stamp helpers.

**The human half:** confirm that the sandbox is the one you intended, permission choices are acceptable, and the corrected text actually remained where you put it. Only you can authorize a release of your correction.

**What neither proves:** a successful write says nothing about learning, accessibility, or the cost of a larger session. This is a connection test. Keeping that claim small is its strength.

## Exercises

**Warm-up**

1. *(Low; distinguish access.)* List an identity fact, a seat fact, and a file-permission fact from your redacted setup record. Explain why none substitutes for the other two.
2. *(Low; plan a budget.)* Allocate a twelve-request session with room for one failure. Name the observation you would refuse to remove to save a call.

**Application**

3. *(Medium; demonstrate.)* Repeat the one-frame test in a second sandbox. Report whether the same setup assumptions held; do not copy the first run's results into the second.
4. *(Medium; diagnose.)* Inspect a failed request from your own record, or label an invented failure as illustrative. Classify it as connection, identity, permission, target, script, or evidence failure and name the next diagnostic action.
5. *(Medium; reconcile.)* Compare the planned and actual request ledger. Explain the largest difference and propose one change for a rerun.

**Synthesis**

6. *(High; preserve corrections.)* Design a test in which the agent replaces a corrected node with an identical-looking new node. Specify the evidence needed to distinguish preservation from disappearance of the constraint target.
7. *(High; distinguish meters.)* Write a budget report in which one meter is unavailable. Make it useful without turning the missing value into zero.

**Challenge**

8. *(Open; evaluate.)* Propose the smallest connection test that would catch a write landing in the wrong file. Explain what your test still could not detect.

## What you can now do

You can establish a bounded editing session, identify its evidence gaps, and distinguish a successful sign-in from a successful write/read-back cycle. You can also explain the cost of your test without pretending every meter measures the same thing.

## Credit the AI

**Planned agent contribution:** connection setup, bounded drawing, snapshots, diffs, and a budget ledger. **Observed mistakes:** RUN, to be filled from 2.0-2.3. **Verification:** inspect the actual sandbox, compare saved responses with the ledger, and preserve missing evidence as missing.

## Next

Return to Chapter 1 and collect the baseline if you have not done so. Then Chapter 3 asks a different connection question: not whether the agent can read the file, but what meaning survives when it does.
