# Agentic Learning Experience Design with Figma
## Building Screens That Teach, Through the Figma MCP Server

**Nik Bear Brown**

**Complete rough-draft reading copy | November 3, 2026**

Copyright 2026 Nik Bear Brown. Working publisher: Bear Brown, LLC, as recorded in this project's metadata. Final publishing and licensing decisions remain with the author.

This is an independent book. It is not affiliated with, sponsored by, or endorsed by Figma. Product names identify the tools being discussed, not a partnership. No access to a product, feature, institutional account, or paid plan is included with this manuscript.

> **Rough draft, not a completed experiment.** The author authorized drafting the whole book before blueprint and research sign-off. The chapter sequence is a working editorial commitment, not a signed production gate. Chapters 1 and 12 retain their existing drafts. The remaining chapters develop the blueprint for author review. Tool claims marked `[VERIFY]` need current primary-source checks. RUN slots need real observations. No learner study, canvas session, credit expenditure, or result is implied by the presence of instructions for performing it.

## Preface: Fast Is Not the Same as Finished

I can ask an agent for a quiz screen and receive something that looks ready to teach. It may have a question, four choices, a button, and an encouraging message. All the familiar pieces are there. What I cannot infer from those pieces is whether the learner has to think.

Suppose the correct choice is already tinted green. The learner can finish without retrieving anything. Suppose the explanation appears only after the learner has moved on. The design contains feedback but never creates a useful encounter with it. Suppose a confident learner gets a fully worked explanation every time, while a novice gets an empty box. Both screens may be consistent with a visual design system. Neither is necessarily consistent with the learning objective.

This is the gap I want to close. I am not writing another account of why retrieval, spacing, or worked examples matter. I am asking what happens when those ideas become production instructions for an agent that edits a design file.

The answer cannot be only a better prompt. Prompts disappear into conversations. A colleague begins a fresh session. A different agent rebuilds the screen. The carefully qualified instruction becomes a vague request to make the experience easier. The rule has to travel with the work, and someone has to check whether it arrived.

This book puts learning rules in component descriptions, support-state specifications, frame annotations, and a versioned rules file. It also keeps a record of the author's corrections. The agent draws, you change the canvas, and the agent asks why. Your reason becomes something the next round must preserve. The point is not to make human judgment unnecessary. The point is to stop losing it between revisions.

### The Claim We Have Not Earned Yet

The strong version of this book's argument is that an agent asked for learning UI will tend to reproduce product-UX patterns that remove necessary thinking. That is a testable hypothesis, not a fact about every model or every designer. Product design is also more varied than that shorthand suggests. Many product interfaces deliberately support reflection, while many educational interfaces reward superficial completion.

Chapter 1 therefore starts with a baseline rather than a staged failure. If the agent builds a good screen, the book reports that. The narrower argument still matters: a rule that worked once needs a place to live, a test, and a boundary. Repeatability is a more defensible ambition than claiming that every unguided agent will fail.

The title of Chapter 1 is a provocation. It is not permission to declare a learning result from a screenshot. By Chapter 13 we will distinguish a screen that passes a design review from an experience that produces evidence of learning. That distinction should govern your reading from the beginning.

## Who This Book Is For

I am writing for a learning designer, instructional designer, educator, or product collaborator who can explain what a learning activity should accomplish but wants a more direct route to building it. You do not need to program. You do need to judge a question, notice an answer leak, and be willing to correct an agent instead of accepting its confidence as evidence.

An engineer entering education can use the book too. The unfamiliar material may be the reason for keeping effort in an interaction that could otherwise be completed faster. A learning designer may find the opposite unfamiliar: a component is not just a reusable drawing but an interface through which another agent interprets intent.

The book assumes access to a suitable Figma account and an agent connection for live exercises. It does not assume that a particular institution supplies either. You can read the concepts and prepare the specifications without live access. You cannot honestly fill in the run records without performing the work.

### Three Books, Three Jobs

*Experience Design for EdTech* develops the learning-design argument. Its Chapter 3, "The Cognitive Machinery: Load, Difficulty, and Durable Learning," supplies this book's demonstration lesson. *AI for Learning Experience Design* addresses AI within a learning experience, including tutoring and the risk that assistance replaces the learner's work. This book addresses AI producing the experience's screens and build instructions.

*Figma for Educational AI*, another sibling project, supplies dated examples of the tool workflow. I cite those examples as local research leads. They are not a substitute for checking the current product documentation or repeating a capability test in the account you will use.

## How to Work Through the Book

Act One establishes the baseline and the machinery. Chapter 1 shows what to inspect; Chapter 2 sets up the connection; Chapter 3 compares what the agent can read; Chapter 4 turns an objective into a screen inventory.

Act Two builds the learning component library. Support levels, item types, feedback, review scheduling, load, accessibility, and progress are separate chapters because they create different failure modes. They still belong to one lesson. A hint decision changes the meaning of a progress metric. An accessibility alternative can change what an item measures. Read these chapters as connected design decisions, not independent styling recipes.

Act Three compiles the rules, tests with learners, carries the requirements into a build, and repeats the whole process on your own lesson. The capstone is not a prettier version of Chapter 1. It is a more accountable one.

If you are not connected yet, read Chapter 1 without pretending to run it. Complete Chapter 2, then return to collect the baseline. If you already have a connection, still do Chapter 2's identity and sandbox checks. Working quickly in the wrong file is not progress.

### The Chapter Contract

Every numbered chapter contains a concept, outcomes, a build conversation, a human correction round, checks, and graduated exercises. A prompt is something to try. A proposed script is not a tested integration. A RUN slot is an empty evidence container, not decorative formatting.

The recurring evidence labels mean:

| Label | Meaning |
|---|---|
| `[VERIFY]` | A claim inherited from a dated source or proposed design needs research or live confirmation |
| `RUN` or `RUN SLOT` | A session, test, or measurement has not been performed for this book |
| Illustrative | A made-up example used to explain a mechanism, not a participant or product result |
| Design contract | A requirement we are choosing for the demonstration, not a universal law |
| Cannot determine | The available evidence does not answer the question |

## Access and Cost: Read This Before the Lab

The blueprint's plan tags are provisional. **All** means the proposed core MCP route is intended for readers across the Education contexts discussed in the sibling project. It is not a verified promise of current availability. **HE** marks an optional higher-education AI/Make path in that project's September 2026 capability notes. Paid plans and institutional restrictions may differ. `[VERIFY: current Figma plan, seat, institution settings, tools, and limits before delivery]`

Do not confuse three budgets: the agent provider's usage, Figma MCP tool allowances, and any Figma AI/Make credits. The book records them separately. An observation of no change on one meter is not proof that every tool is free. A limit recorded in September is not an entitlement in November.

Ask the agent to confirm the current account, available tools, edit permissions, and displayed allowances before a live build. If an optional route is unavailable, keep the specification and use the core route. Never buy a plan just because an unverified draft says you need it.

## What You Will Have at the End

Your portfolio should contain the learning objective, evidence map, component library specification, versioned rules, actual build scripts and observations, a correction ledger, an honestly limited learner-test report, and a handoff package. Keep private account identifiers, authentication material, participant identities, and sensitive course information out of the public repository.

You will also have unresolved questions. Some will be about the tool. The important ones will be about the learning: what the learner actually practiced, which support helped, and what remained when the support was gone.

That is where I want the book to leave you. Not impressed by how quickly the screen appeared. Able to explain why it has the shape it has, what evidence supports it, and what you still do not know.

---

# Chapter 1 — The Screen That Teaches Nothing
*What the agent builds when nobody tells it this is for learning.*

> **Rough draft — pre-research.** Figma facts here come from the sibling repo `../figma-for-educational-ai` (FEA) and are tagged `[VERIFY]` until Phase 1 re-checks them. Every agent output is a **RUN slot**, to be filled with a real run. Nothing below is a recorded result unless it says so.

## The concept

I'm going to ask an agent for a practice quiz in one sentence, and the quiz will arrive looking finished: aligned, readable, nicely spaced, with a green button. That speed is what makes it dangerous. A screen that looks finished doesn't get questioned.

Here's what's actually happening when you type "build a practice quiz" into Claude Code with the Figma MCP server connected:

1. Claude plans the screen.
2. It loads the `figma-use` skill, which teaches it how to write for Figma's canvas.
3. It writes a short JavaScript program against Figma's Plugin API.
4. It sends that program to the server through a tool called `use_figma`.
5. The program runs inside your file, signed in as you (FEA `CAPABILITIES.md`, research notes `[VERIFY]`).

Rectangles, text and auto layout appear. Nothing in that chain knows what a practice item is *for*. The agent knows what a quiz screen usually looks like, and "usually" is the problem.

### What "usually" optimizes for

Most of the interface the world has built is product UI, and product UI is tuned for one goal: get the person to the end of the task with as little effort as possible. Remove the friction. Show the answer. Confirm the click. Celebrate. On a checkout page that philosophy is right. Every second of effort is a chance to abandon the cart.

A practice item for a learner has the opposite job, and I mean that literally. *Experience Design for EdTech* Chapter 3 (`../learning-experience-design-lxd/chapters/03-the-cognitive-machinery-load-difficulty-and-durable-learning.md`) spends eight thousand words on why. The short version uses that chapter's three-way split of working memory:

- **Extraneous load** is effort spent on the container: clutter, decoration, a diagram six centimetres from its caption. Remove it. On this point product UI and learning UI agree.
- **Intrinsic load** is the difficulty of the material itself, relative to what this learner already knows. Manage it by sequencing and support.
- **Germane processing** is effort spent *on the learning*: retrieving a definition instead of looking it up, predicting before seeing, explaining why your first answer was wrong. Protect it. This is the effort the design exists to cause.

The product instinct can't tell the last two from the first. To a product designer, all effort is friction and friction is a defect. So an agent that learned interface design mostly from product UI will, I expect, remove germane effort as cheerfully as it removes clutter. It will put the answer on screen, so the learner never has to retrieve it. It will write "Correct!" as feedback, because that's the confirmation pattern. And it will add a celebratory illustration, because that's delight.

I want to be careful here, because that last paragraph is a **prediction, not a finding**. I haven't watched an agent do it for this book yet. This chapter's job is to run the experiment in front of you and report what happens. If the agent gets it right, I'll say so, and the argument of the book narrows from "the agent defaults to product patterns" to "you still need the rules to make good behaviour repeatable." Either way, you'll leave this chapter with a scored screen and a record of how it got fixed.

### The five checks

To score the screen we need a ruler. I use five checks, one per principle, chosen because each is visible on a static screen in under a minute:

| # | Check | The principle behind it | What the product default tends to do |
|---|---|---|---|
| 1 | **Is the answer hidden until the learner commits?** | Retrieval practice beats restudy (Roediger & Karpicke 2006, cited in LXD Ch 3) | shows the answer, or highlights it on hover |
| 2 | **Does feedback explain, not just score?** | Elaborated feedback, the "reconcile" step in LXD Ch 3's diagnostic | "Correct!" / "Try again" |
| 3 | **Is there a hint that isn't the answer?** | Managing intrinsic load without removing the retrieval | no hint, or a "show answer" button labelled as a hint |
| 4 | **Is anything decorative competing for attention?** | Extraneous load; Mayer's coherence principle (cited in LXD Ch 3) | illustrations, confetti, gradients |
| 5 | **Could a learner do it with a keyboard alone?** | An item a learner can't operate measures nothing (Chapter 10) | nothing marks focus order or a focus state |

Check 5 is the odd one out, and I'll be honest about why it's here. A Figma canvas can't prove keyboard access, because that lives in the built code. What the canvas *can* show is whether anyone designed for it: is there a visible focus state, and is the order annotated? So check 5 scores intent, not compliance. Chapter 10 covers the rest.

<!-- → [TABLE: the five checks as a scoring card the reader prints — columns: check, pass / fail / can't tell, evidence (layer name or screenshot crop), fix] -->

### The Figma idea: the file is the only thing the agent reads

The other half of this chapter's concept is about Figma, and it sets up the whole book. The agent doesn't remember your intentions between sessions. It doesn't see your storyboard, your lesson plan, or the conversation you had with the instructional designer last week. It sees two things: what you type, and what's in the file.

So every rule you want the agent to follow has to live in one of those two places. Typing it every time is fragile. You'll forget, the next person won't know, and a long prompt is a weak contract. Putting it in the file is durable, but only if it's somewhere the agent actually reads: layer names, component descriptions, variables, annotations. Chapter 3 maps exactly which of those survive the agent's read. Chapters 5–11 build a learning component library out of them, one principle at a time.

That gives us the design philosophy of this book in one line: **the learning designer's new craft is writing a design system the agent can't misuse.**

### The other new idea: you're in the loop, and the loop leaves a record

I don't want you to treat the agent as a vending machine, where a prompt goes in, a screen comes out, and you accept or reject it. The working method in this book is a conversation through the canvas:

1. The agent draws.
2. You correct it in Figma, with your own hands.
3. The agent reads what you changed, asks you why, and redraws without undoing your corrections.
4. Repeat.

That loop has a problem Figma can't solve on its own. Through the MCP server, the agent can't name a version or post a comment. Figma's version history credits every agent edit to you, the signed-in user. In Figma's own record, you and the agent are the same person (FEA `CAPABILITIES.md` and `examples/frictional-version-log/`, checked 2026-09-27 `[VERIFY]`). So the book keeps its own record: a file called `provenance.json`, plus a snapshot of the screen at the end of every round. Figma carries one pointer to it, a single annotation on each frame that says which round it's on. [PROVENANCE.md](#appendix-e-provenance-and-evidence-templates) is the full method. In this chapter you'll see it work once, end to end, before Chapter 2 explains the machinery.

The interesting trade-off is overhead against memory. Recording costs a minute and about one MCP call per round. In exchange, when someone asks in week six why the hint button sits above the answer field, the answer is in round 2, in your words.

<!-- → [INFOGRAPHIC: the loop — agent draws → snapshot → you correct in Figma → diff → your "why" → constraints → agent redraws; the ledger sits under the loop collecting each round] -->

## What you'll be able to do

- **Evaluate** an agent-built practice screen against the five checks, citing a layer or screenshot as evidence for each verdict.
- **Explain**, for each failure, which product-UX goal it serves and which learning goal it costs.
- **Correct** an agent's screen by hand in Figma and record each correction, with your reason, as a constraint the agent must keep.
- **Predict** which failures a one-line instruction would fix and which need a component, and then test the prediction.

**Plan:** all · **MCP budget:** estimate ~15 calls for four rounds, to be measured in this chapter's RUN slots · **Builds on:** nothing. If you haven't connected Claude Code to Figma yet, read this chapter through, do Chapter 2, then come back and run it.

## Talking to Figma

### Before round 1: the lesson and the ledger

The running lesson for the whole book is a practice unit for *Experience Design for EdTech* Chapter 3. That's a real chapter in this series, on working memory, the three kinds of load, worked examples, retrieval, spacing and interleaving. Using our own book as the content means every screen we build can be judged against the material it teaches. If the practice screen for a chapter on extraneous load is full of decoration, that's not a style note. It's a failed item.

Make a new Figma design file for the practice unit, or a duplicate if you're working from someone else's. The agent edits with your permissions, so work in a copy you can afford to wreck. On Education there's no branching, so a duplicate file is the sandbox (FEA `CAPABILITIES.md`, film 8 `[VERIFY]`).

Then ask the agent to start the ledger:

```
Start a provenance ledger for this project, per PROVENANCE.md.
Project: "ch3-practice-unit". Lesson: "LXD Ch 3, The Cognitive Machinery: practice unit".
File ref: "practice-unit" (don't write the file key anywhere in the repo).
Then run whoami and tell me which team and seat you're acting as.
```

It should run `prov.py init` and then call `whoami`. Education reports itself as "Student tier", even for a verified educator; that's expected (FEA `CAPABILITIES.md`, E00 `[VERIFY]`). If `whoami` names a team where you have a View seat, stop. A View seat can't edit, and its MCP allowance is monthly rather than daily.

> **RUN SLOT 1.0 (setup).** Paste: the `prov.py init` output and the `whoami` result, with the team name redacted if it identifies anyone.

### Round 1: the agent draws

Here is the whole instruction. It's deliberately thin, because the point is to see the default:

```
In the open Figma file, build a five-question practice quiz for this lesson:
[paste or attach the LXD Ch 3 summary and its Evidence Box].
One frame per question, phone size.
Save the script you run to provenance/scripts/r1.js. When you're done: snapshot the
frames, stamp them, take a screenshot, and record round r1 in the ledger.
```

What the agent should do, in order:

1. Load `figma-use`.
2. Write and run one `use_figma` script that builds five frames.
3. Run `tools/provenance/snapshot.js` on those frames and save `provenance/snapshots/r1.json`.
4. Get the stamp text from `prov.py stamp-text` and run `tools/provenance/stamp.js`.
5. Call `get_screenshot` on one frame.
6. Run `prov.py record --actor agent …`.

That's four MCP calls, plus one screenshot per extra frame you ask to see.

Two things in that list haven't been tested against a live file yet: `snapshot.js` and `stamp.js`. Their first real run is in Chapter 2. If either fails here, the agent should say so and keep going without it. The screen matters more than the record on day one, and Chapter 2 fixes the record.

> **RUN SLOT 1.1 (ledger r1).** Paste: the agent's reply (what it said it built), `provenance/scripts/r1.js`, the screenshot of question 1, and the `prov.py record` line. *What to look for:* where is the correct answer on screen? What does the feedback text say? Is there a hint, and what does it reveal? Is there anything on the frame that isn't the question, the input, or the feedback? Is there any focus state?

### Score it before you touch it

Before you change anything, score question 1 against the five checks, and write the score down. This is your baseline, and the capstone in Chapter 15 compares against it.

| # | Check | Your verdict | Evidence |
|---|---|---|---|
| 1 | Answer hidden until commit | **RUN** | **RUN** (layer name) |
| 2 | Feedback explains | **RUN** | **RUN** (the feedback text, quoted) |
| 3 | A hint that isn't the answer | **RUN** | **RUN** |
| 4 | Nothing decorative competing | **RUN** | **RUN** |
| 5 | Designed for keyboard | **RUN** | **RUN** |

Then do the teardown properly. For each failure, write one sentence in this form: "*The agent optimized for ___ at the expense of ___.*" For example, if the answer is visible: "*optimized for confirmation at the expense of retrieval.*" If the feedback is "Correct!": "*optimized for reassurance at the expense of reconciling a wrong model.*" Those sentences are the real output of this chapter. They name the product value that crept in, and naming it is how you write a rule against it.

### Your turn in Figma

Now correct question 1 by hand, in Figma, the way you'd correct a junior designer's draft. Fix only question 1. Leave 2–5 as the agent built them, because round 3 tests whether the agent can learn from your one example.

Typical corrections, depending on what the agent built:

- **Hide the answer.** If the correct option is highlighted, or the answer text is visible, hide that layer. Don't delete it: the answer still has to exist for the feedback state. Hiding is a change the snapshot records as `visible: true → false`.
- **Rewrite the feedback.** Replace "Correct!" with feedback that explains. For an item on worked examples, something like: "*Not quite. A worked example removes the search for a method. Which kind of load does that search add?*" It reconciles without giving the answer away.
- **Add or fix the hint.** A hint narrows the search without ending it: "*Think about where the learner's effort goes before they find the right method.*" If the agent's "hint" button reveals the answer, rename it or delete it.
- **Delete decoration.** An illustration that isn't part of the question is extraneous load. Remove it.
- **Mark focus.** Add a visible focus ring to the first answer option, even a plain 2px outline, so that intent is visible.

When you're finished, tell the agent:

```
Done with question 1. Snapshot it, diff it against r1, read my changes back to me,
then ask me why.
```

The agent should run `snapshot.js` (one call), then `prov.py diff provenance/snapshots/r1.json provenance/snapshots/r2.json`, and list your changes in plain words: "You hid *Answer*, moved *Hint button* up 100px, and rewrote *Feedback*." Then it asks for one line on why. Give it your real reason, in your own words. The ledger won't accept a human round without one, and the agent must not write it for you.

```
Why: The answer was on screen before the learner tried, and the feedback scored instead of explaining.
```

The agent records round r2. Every change you made becomes a **constraint**: *Answer* stays hidden, *Feedback* keeps your text, *Hint button* keeps its place. These are facts about the screen that the agent now has to preserve.

> **RUN SLOT 1.2 (ledger r2).** Paste: the `prov.py diff` output, your why exactly as you gave it, and the line from `prov.py record` showing how many constraints it added.

<!-- → [IMAGE: question 1 before and after the human round, side by side, with the three diffed layers circled and labelled with their constraint ids] -->

### Round 3: the agent redraws the rest

This is the real test of the loop. You've corrected one item, and now the agent applies what you did to the other four, without touching yours:

```
Apply the same kinds of corrections I made to question 1 to questions 2–5.
Read the active constraints in provenance.json first, and don't change anything they cover.
Before you record the round, run check-constraints on your snapshot. If anything I set
has changed, stop and tell me instead of recording.
Then score questions 2–5 against the five checks in Chapter 1 and tell me which checks
you could not verify.
```

What the agent should do:

1. Read the ledger.
2. Write a script that changes only questions 2–5.
3. Run it, then snapshot all five frames.
4. Run `prov.py check-constraints`, which must print "ok: no human correction was undone".
5. Stamp the frames, take a screenshot and record r3 with its checks.

Check 5 should come back as `not-run` or a partial pass, because a canvas can't prove keyboard access. An agent that reports "keyboard: pass" on a static frame is claiming more than it can know. That's a finding worth writing down.

If `check-constraints` reports a violation, the agent has undone one of your corrections. That's the case the ledger exists for. The agent can't record the round until it either puts your correction back or you approve the change in your own words. I'd expect this to happen at least once in this book, and I want it to happen in front of you. It's the clearest demonstration of why the record matters.

> **RUN SLOT 1.3 (ledger r3).** Paste: the agent's reply, `provenance/scripts/r3.js`, the `check-constraints` result, the agent's own five-check scores for questions 2–5, and a screenshot of one of them. *What to look for:* did it generalize *your reasons* (retrieval, explanation) or only *your edits* (hide the layer called Answer)? If question 3's answer layer has a different name, did the agent still find it?

### Round 4: you check its work

Score questions 2–5 yourself, without looking at the agent's scores first. Then compare. Wherever you disagree, make the correction in Figma and run another human round with its why. The loop stops when all five questions pass checks 1–4, and check 5 is at least marked with intent.

> **RUN SLOT 1.4 (ledger r4).** Paste: your scores against the agent's scores, any corrections, and the `prov.py log` table for the whole chapter.

## The provenance this chapter adds

At the end of the chapter, the ledger should hold something like this. Values in angle brackets come from your run:

```json
{
  "schema": "alxd-provenance/0.1",
  "project": "ch3-practice-unit",
  "lesson": "LXD Ch 3, The Cognitive Machinery: practice unit",
  "file_ref": "practice-unit",
  "rounds": [
    {"id": "r1", "actor": "agent", "chapter": 1, "intent": "first draw, thin prompt",
     "script": "provenance/scripts/r1.js", "snapshot": "provenance/snapshots/r1.json",
     "diff": [], "why": null, "checks": [], "calls_used": "<RUN>"},
    {"id": "r2", "actor": "human", "chapter": 1, "intent": "correct question 1 by hand",
     "snapshot": "provenance/snapshots/r2.json", "diff": ["<RUN: your changes>"],
     "why": "<RUN: your words>", "constraints_added": ["c1", "c2", "c3"]},
    {"id": "r3", "actor": "agent", "chapter": 1, "intent": "apply corrections to questions 2–5",
     "checks": [{"name": "answer-hidden-until-commit", "result": "<RUN>"},
                {"name": "keyboard", "result": "not-run"}], "calls_used": "<RUN>"}
  ],
  "constraints": ["<RUN: one per change you made in r2>"]
}
```

Three questions this record can answer later, and that nothing else in your project can:

- **Which corrections were yours?** Figma's history can't tell you, because it credits everything to you.
- **Why was each one made, in the words of the person who made it?**
- **Did the agent ever undo you, and who approved it?** If `violations_overridden` is empty, no one approved an undo.

## The check

**The machine half.** `check-constraints` proves the agent didn't undo your corrections. The diff proves what changed between rounds. A script can confirm that a layer named *Answer* is hidden. It can't confirm that the layer the agent *called* "Answer" is the answer.

**The human half.** Whether the feedback explains, whether the hint narrows without revealing, and whether a graphic is decoration or a diagram the question needs: those take judgment. In this chapter you're the judge, and in Chapter 13 a learner is.

**What neither can see.** Whether the items teach. A screen can pass all five checks and still ask a question that doesn't test the objective. Chapter 4 connects screens to objectives. Chapter 13 tests them with learners, with a delayed retrieval check, because the only proof of a practice item is what the learner can retrieve a week later.

## Exercises

**Warm-up**

1. *(Objective: evaluate against the five checks.)* Score the provided screenshot `pantry/ch01-sample-quiz.png` against all five checks, citing a visible element as evidence for each verdict. **[RUN: the sample screenshot is captured from r1 and placed in the pantry.]**
2. *(Objective: explain the product value.)* For each failure you found, write the "*optimized for ___ at the expense of ___*" sentence.

**Application**

3. *(Objective: correct and record.)* Run rounds 1 and 2 on a lesson you teach, not the LXD chapter. Record your why for each correction. Which of your corrections had the shortest why? Which had the longest, and what does that tell you about where your expertise is?
4. *(Objective: predict instruction vs component.)* Write one sentence of extra instruction that you predict will fix the worst failure from round 1. Rerun round 1 in a fresh duplicate with that sentence added, then re-score. Did it hold for all five questions, or only some?
5. *(Objective: evaluate the agent's self-scoring.)* Compare the agent's round 3 scores to yours. List every check where it claimed more than a static frame can show.

**Synthesis**

6. *(Objectives: predict, evaluate.)* Ask for the same quiz twice, in two duplicates, with the same thin prompt. Diff the two r1 snapshots with `prov.py diff`. How much of "the default" is stable, and how much is noise? What does that mean for a single run as evidence?
7. *(Objective: explain.)* Pick one of your five corrections and argue the opposite: a case where showing the answer, or "Correct!", is the right design. LXD Ch 3's expertise-reversal finding is a good place to start. Then write the condition under which your correction should be released.

**Challenge**

8. *(Open.)* Design a sixth check. It has to be visible on a static screen, tied to a finding in the LXD Ch 3 Evidence Box, and something the product default would plausibly fail. Run it on your r1 screen.

## What you can now do

- Ask an agent for a learning screen and tear down what comes back, check by check, naming the product value behind each failure instead of calling it "bad UX".
- Correct an agent's screen by hand and turn each correction into a recorded constraint, with your reason, that the agent has to keep.
- Run the full loop once: draw, correct, redraw, check that nothing was undone, and read the history back.
- Tell the difference between what a canvas can prove (hidden layers, kept corrections) and what only a learner can.

## Credit the AI

**What the agent did:** built five question frames from one sentence; snapshotted, stamped and recorded each round; generalized one hand-corrected item to four others; scored its own work. **What it got wrong:** **[RUN: fill from r1 and r3. Which checks it failed, which corrections it generalized only literally, and any check it claimed to pass that a canvas can't show.]** **How you check it:** your own five-check scores, made before you look at the agent's, plus `check-constraints` on every agent round.

## Next

You've run the loop with the setup taken on faith. Chapter 2 opens the machinery:
- how Claude Code reaches Figma at all
- what `whoami` is telling you
- where the 200 calls a day go
- how to run the snapshot and stamp scripts for the first time against a live file, and fix them if they break

By the end of it you'll know what every round in this chapter cost, and you'll have a budget for the rest of the book.

---

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

---

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

---

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

---

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

---

# Chapter 6 - Item Types the Agent Can't Break
*A reusable component needs a contract for the thinking, not just the spacing.*

> **Rough draft - pre-research.** The title states a design ambition, not a guarantee. Component-description leads come from FEA `examples/film-07/` and `CAPABILITIES.md` `[VERIFY]`. The item examples are illustrative teaching content, not validated assessment instruments. No item batch or compliance result has been generated in Figma for this chapter.

## The concept

A multiple-choice component can be visually perfect and educationally weak. The options may be different lengths, one may contain the wording of the question, or two may be defensible under an unstated assumption. A component system that checks only spacing will faithfully reproduce those defects at scale.

This chapter gives the component a second contract. The first describes appearance and interaction. The second describes what an item must ask, what information it must withhold, how its key is justified, and which content checks remain human judgments.

I am not trying to make the agent an assessment expert by adding a paragraph to a component description. I am making its obligations inspectable. The word "can't" in the title should make you suspicious. Agents can ignore rules, rules can be incomplete, and a plausible item can still be wrong. The useful result is a library that catches more failures and makes uncaught failures easier to diagnose.

### The Item Type Changes the Evidence

Consider four ways to assess the same diagnostic concept.

A multiple-choice item asks the learner to discriminate among supplied alternatives. A short-answer item asks them to produce a reason. An ordering item asks for a sequence. A classification-with-justification item asks them to connect a label to a case. These are not interchangeable wrappers for the same evidence.

If the target is explaining why a navigation burden is unrelated to the learning objective, recognizing a category name provides weaker evidence than producing the explanation. But a short-answer field introduces scoring and accessibility work that a choice item may not. The task is to choose knowingly, not to rank item types on a universal ladder.

For this demonstration, the fourth type will be **case classification plus justification**. It fits LXD Chapter 3's diagnostic while making the rationale visible. A reader may substitute a different type when the objective requires it. The contract still needs the same fields: target performance, response form, scoring basis, reveal timing, support behavior, and accessibility handoff.

### A Description Is an Interface to the Next Agent

FEA's film-07 compares conditions involving component descriptions and an external rules file. The blueprint uses it as a precedent, but its results should not be generalized into "descriptions always work" `[VERIFY: FEA examples/film-07/measurements.json and saved contexts]`. Our test is whether the current read returns the description and whether a fresh agent acts on it for learning items.

A useful description is short enough to retrieve and precise enough to check. It names scope and points to the full rules. It should not contain the answer key for a learner-facing instance if a downstream export could expose it. Private authoring data and rendered learner content are separate concerns.

For a proposed choice component:

```text
Component: LearningItem/SingleChoice
Purpose: one committed response to one stated problem.
Required authoring fields: objective_id, item_id, stem, options, one key,
key_rationale, distractor_rationales, feedback, support contract.
Before commit: no key styling, correctness text, or answer-bearing hint.
After commit: explain the reasoning; do not only score.
Review: content expert confirms one defensible key under the stated assumptions.
References: R-ANSWER-01, R-FEEDBACK-01, R-ACCESS-01.
```

That is a proposed description, not evidence that any tool returned it. It also does not make the key secure. In a browser application, hiding a layer or CSS class is not a security boundary. Chapter 14 addresses where authoring keys and scoring logic belong in a real build.

### Properties, Variants, and Content

A property can represent a controlled option. A variant can represent a distinct configured state. A content field holds the actual question or explanation. Which of these Figma exposes in a particular read must be tested `[VERIFY: FEA CAPABILITIES.md and film-07 saved design context]`.

Use controlled properties for things the agent should not casually invent: item type, support condition, attempt state. Use content slots for the stem, options, and feedback. Keep identifiers stable when text changes, because the correction ledger needs to distinguish a rewritten option from a different item.

The contract should also specify what must not be inferred. A state called Correct is an authoring label, not evidence that a learner answered correctly. A component called ShortAnswer does not imply automatic grading. Avoid names that quietly import implementation promises.

### Four Illustrative Item Contracts

The following examples demonstrate structure. They need content review before use.

**Single choice.** A learner repeatedly opens a detached control legend while trying to compare two worked solutions. Which change most directly reduces tool-management effort while preserving the comparison? The proposed key is placing the necessary control explanation with the controls. Distractors should represent meaningful alternatives, not absurd actions. Each needs a rationale. If more than one change could be best under plausible assumptions, revise the stem rather than insisting the key is unique.

**Short answer.** Explain why replacing an unsupported generation task with a worked example might help a novice but be redundant for an experienced learner. The rubric should name required ideas, acceptable variations, and what would be insufficient. It should not demand exact textbook wording. The prototype can display a rubric or moderator feedback without pretending a scoring model has been validated.

**Ordering.** Put a declared instructional sequence in order: study a parallel worked example, complete a partial example, attempt a new case independently. The stem must say that this is the proposed sequence being recognized, not the only valid sequence for every learner. Ordering becomes invalid when several sequences are defensible but the interface accepts only one.

**Classification plus justification.** Classify a source of effort in a supplied case, then explain the classification using the stated objective and learner knowledge. A bare category is incomplete. The rubric must accept a justified challenge to an under-specified case rather than punishing the learner for noticing missing information.

The last point matters. A question with insufficient information is not repaired by adding a confident answer key. It is repaired by adding the missing condition or changing the scoring contract.

<!-- [TABLE: four item types with target evidence, required authoring fields, likely failure, machine check, and human content review] -->

### A Plausible Distractor Needs a Reason to Be There

For the single-choice example, the authoring record should explain each option. A distractor might confuse unnecessary control lookup with productive comparison. Another might remove the comparison itself in the name of speed. Another might add a worked example without addressing the unexplained control. Each represents a different reasoning error worth discussing.

Do not accept an option merely because it is false. An absurd distractor can make the correct answer recognizable without the intended discrimination. Nor should the key be the only option with a careful qualification while the others are blunt absolutes. Those cues let a learner answer a writing-pattern puzzle instead of the subject-matter question.

The agent can compare lengths, repeated terms, and suspicious wording. Those checks are clues, not a recipe for valid options. Equal-length alternatives can still be poor. A long correct answer is not automatically invalid. Require the content rationale and let the reviewer explain why a cue matters in this particular item.

### Short Answer Requires a Scoring Boundary

For the short-answer example, a proposed rubric can distinguish a complete explanation, a partial explanation, and an unresolved response needing human review. A complete explanation connects the support choice to the learner's prior knowledge and the task. A response that only repeats "expertise reversal" may name the concept without applying it. A response that identifies missing context may be more defensible than a confident but under-specified answer.

Write examples of acceptable reasoning as authoring material, clearly labelled illustrative, without turning them into the only accepted wording. If a later model scores responses, evaluate that scorer separately. The fact that the content-generation agent wrote a rubric does not validate its use as an automated judge.

This is a useful place for Cannot determine. An unclear response can require a follow-up rather than an automatic zero. But do not use that category to hide every difficult scoring decision. State the routing rule and who reviews the case. Otherwise unresolved responses accumulate without a learning action.

### The Batch Is a Test of a Process

A ten-item batch gives you a manageable set to inspect. It does not establish an error rate for all future items. Keep the requested distribution, the actually generated distribution, and the approved distribution separate. If the agent produces eight items and repeats two IDs, the batch did not contain ten independent proposals.

Track defect categories across revisions. Did a revised description reduce premature reveal while making feedback less explanatory? Did a new rubric fix one ambiguous item and reject legitimate alternative reasoning elsewhere? A single total pass count can conceal that trade-off.

When an item changes substantially, version it. The original failed proposal remains part of the audit history, while the revised content receives its own review. A later learner response must identify which version was presented. Otherwise a disputed answer can be judged against a rubric that did not exist when the learner responded.

Finally, keep item reuse intentional. Reusing a visual component is desirable. Reusing an answer pattern or case with only the names changed may not produce new evidence. The library should support production speed without making every question the same question in a different coat of paint. Ask the agent what variation changes the required reasoning and what variation is merely superficial.

## What you'll be able to do

- **Write** component contracts that specify evidence and behavior as well as layout.
- **Choose** an item type based on the target performance and scoring burden.
- **Audit** a generated batch for structural defects, content defects, and unresolved cases.
- **Revise** a rule using an observed failure without claiming the revised rule is universally reliable.

**Plan:** all, provisional. **MCP budget:** planning ceiling 30 requests for library construction and a bounded batch; actual RUN. **Builds on:** Chapters 4-5.

## Talking to Figma

### Round 1: Build the Library Before the Batch

```text
Create four learning-item component contracts: SingleChoice, ShortAnswer,
Ordering, and CaseClassificationWithReason. Use the supplied reviewed content
only for initial examples. Keep content, support_level, and attempt_state
separate. Put a concise contract and rule IDs in each component description.

Read back each contract through the actual path a fresh implementation agent
would use. Report missing fields or lost descriptions. Do not infer success
from the component name. Save scripts and follow the provenance loop.
```

Do not start with ten items. First verify that one instance of each type carries the intended contract. Otherwise the batch multiplies a representation problem that looks like a content-writing problem.

Ask the agent to distinguish its authoring schema from the learner-visible frame. A key can exist in the authoring record while remaining unavailable before commitment in the prototype. That separation must be explicit in the eventual handoff; merely hiding a shape is not an implementation strategy.

> **RUN SLOT 6.1.** Save component contracts, instance read-backs, scripts, screenshots, and the authoring-versus-rendered-content map. Record which contract statements were actually available to the next agent.

### Round 2: Generate a Ten-Item Proposal

Use a bounded distribution, such as four choice items and two of each other type. That is an illustrative audit batch, not an optimal test composition. Give the agent objective IDs and content boundaries. Require a key rationale or rubric for every item before it draws.

```text
Propose ten items using the approved contracts and objective map. Before
drawing, provide item_id, objective_id, target performance, scoring rationale,
support behavior, and any uncertainty. Do not fabricate sources for content.
Mark an item NEEDS-CONTENT-REVIEW if its key or rubric is ambiguous.

After review of the proposal, build only the authorized items. Preserve the
existing library and human corrections. Keep unresolved items out of the
approved set rather than treating them as correct by default.
```

The proposal step makes a content defect cheaper to fix. If the agent cannot justify why an ordering item has a unique sequence, no amount of component polish will supply that justification.

> **RUN SLOT 6.2.** Save the proposal, authorization boundary, built batch, and audit table. Use one row per item and distinguish structural pass from content review. An unreviewed rationale is not a validated key.

### Your Turn in Figma

Choose one real failure from the batch. It might be an answer cue, a distractor that is partly correct, a short-answer rubric that rewards terminology instead of reasoning, or an ordering item with two valid sequences. If none appears, report that rather than inventing a failure for the book's argument.

Correct the content or component by hand and explain why. Then decide whether the repair is local or general. Changing a distractor is local. Requiring the stem to state the learner's prior knowledge may be a reusable rule. The ledger should preserve the actual correction; Chapter 12 will compile general rules from it.

> **RUN SLOT 6.3.** Save the diff, your reason, the local/general classification, and the affected contract. Record whether the correction changed the evidence the item collects.

### Round 4: Generalize Without Copying

```text
Read the correction and its reason. Propose a contract revision, distinguishing
the local fix from the general rule. Do not edit an author-protected rules file
without authorization. Apply the approved contract to two new items on
different concepts. Keep the corrected item intact and run check-constraints.

Report whether each new item requires expert content judgment even if every
structural check passes. Do not call a schema-valid item pedagogically valid.
```

A contract revision that only says "do not use this distractor" may pass the original item and fail the next one. A revision that says "all distractors must be wrong" is too vague to inspect. A better instruction requires the authoring record to state why each distractor is wrong under the stem's explicit assumptions and routes disagreement to content review.

> **RUN SLOT 6.4.** Save proposed and approved contract versions, the two new items, constraint results, and remaining review questions. Compare failure types, not just total passes.

### The Audit Table

Keep these verdicts separate:

| Check | Evidence | Verdict vocabulary |
|---|---|---|
| Required fields exist | Authoring record | Pass/fail |
| One key declared for single choice | Authoring record | Pass/fail |
| One key defensible | Expert reasoning about the stem | Pass/fail/unresolved |
| No pre-commit answer cue | All reachable pre-commit states | Pass/fail/not tested |
| Feedback explains | Actual feedback and objective | Pass/fail/unresolved |
| Access contract present | Annotation or handoff record | Present/missing |
| Built accessibility works | Runtime tests | Pass/fail/not run |

This prevents a common inflation: ten structurally complete items become "ten valid questions" in the summary. A good audit can say that all ten have fields, six passed content review, two need revision, and two remain unresolved. That is more useful than a single impressive percentage.

## The provenance this chapter adds

```json
{
  "chapter": 6,
  "library_contracts": "RUN",
  "batch_size_planned": 10,
  "batch_size_built": "RUN",
  "structural_results": "RUN",
  "content_review_results": "RUN",
  "human_reason": "RUN: verbatim",
  "new_item_test": "RUN"
}
```

The distinction between planned and built counts is intentional. A failed batch build must not be reported as ten observed items merely because ten were requested.

## The check

**The machine half:** validate required fields, allowed states, key cardinality, stable IDs, and missing rationales. Test rendered answer cues where the representation permits it. String rules can detect prohibited phrases but cannot establish that a distractor is plausible or a rubric is fair.

**The human half:** judge item validity, ambiguity, alignment, and the reasoning demanded. Check whether an alternative answer reveals a defect in the question rather than a defect in the learner.

**What neither proves:** that the item discriminates reliably or predicts later performance. A small design audit is not psychometric validation. Report it as a design audit.

## Exercises

**Warm-up**

1. *(Low; choose.)* Pick two item types for one objective. State the different evidence each would collect.
2. *(Low; write.)* Write a six-line contract for a new item type, including one requirement a machine can check and one it cannot.

**Application**

3. *(Medium; audit.)* Audit a ten-item proposal before drawing. Count structural failures, content failures, and unresolved cases separately.
4. *(Medium; write.)* Rewrite an ambiguous stem so that its key is defensible without adding a clue to the answer.
5. *(Medium; revise.)* Correct one item and test the proposed general rule on two new concepts. Preserve the failed attempts in the record.

**Synthesis**

6. *(High; choose.)* Replace a choice item with short answer. Update the evidence interpretation, scoring contract, support states, and access handoff, not only the input control.
7. *(High; audit.)* Design a case in which a learner's objection should receive credit. Specify how the rubric avoids treating all disagreement as correctness.

**Challenge**

8. *(Open; evaluate.)* Create a deliberately schema-valid but educationally invalid item. Ask an independent reviewer to find the defect and report whether the contract needs a new check or a human gate.

## What you can now do

You can build a library whose reusable unit includes the learner's task and scoring basis. You can also explain why structural validity, content validity, and runtime behavior need different evidence.

## Credit the AI

**Planned contribution:** library construction, item proposals, structural audit, and a transfer test of revised contracts. **Observed errors:** RUN. **Verification:** content expert reviews keys and rubrics, the actual read-back tests description survival, and unreviewed items remain unreviewed.

## Next

An item contract still needs a precise account of what happens after the learner acts. Chapter 7 defines commitment, feedback, hints, and retry as a state machine so the interface cannot casually give away the very performance it asks for.

---

# Chapter 7 - Feedback, Hints, and the Answer You Don't Show
*The important part of the screen is often the information that has not appeared yet.*

> **Rough draft - pre-research.** Learning leads: LXD Chapter 3 and *AI for Learning Experience Design* Chapters 3 and 6. Prototype-tool lead: FEA `examples/film-12/03-prototype.js` `[VERIFY]`. State tables and example feedback are proposed designs. No transition, agent response, or learner outcome below has been observed for this chapter.

## The concept

Suppose an item asks the learner to distinguish effort spent managing a tool from effort spent learning the target material. The learner selects a category. Before they press Check, the choice turns green and an explanation slides into view. The interface has technically collected a click. It has not necessarily collected the commitment the designer intended.

The defect is not the green. It is that selection and commitment have been treated as the same event without saying so. An agent building a familiar form can make that decision for you. This chapter takes it back.

We will specify the item as a state machine: a set of named states, the actions that connect them, and the information allowed in each. The diagram is not decoration. It is a contract for what the learner can know before and after each action.

### Selection Is Not Necessarily Commitment

For our demonstration, selection is an editable draft. Commitment occurs when the learner deliberately submits the response. Other designs can use immediate selection as commitment, but the interaction must communicate that consequence and the evidence policy must match it.

Why separate them here? The objective includes giving a reason. A learner may change a category while composing that reason. We want one submitted judgment and rationale, not a series of exploratory clicks misreported as repeated attempts.

Define the event precisely: `commit_attempt` stores the response and assistance context for this attempt. It does not mean "the learner learned," "the response is correct," or "advance to the next item." These are separate transitions and interpretations.

The prototype can demonstrate a proposed sequence. Whether a real build stores the event once, preserves it on refresh, and keeps a private answer key out of premature disclosure requires runtime tests. Do not ask the canvas to prove a persistence or security property it does not implement.

### The Proposed State Machine

Here is the contract for one practice attempt:

| State | Learner can do | Information available | Next transitions |
|---|---|---|---|
| Unanswered | Read, draft, request hint | Case and permitted support | Draft, hint, exit |
| Draft | Edit response and reason | Same; no correctness signal | Commit, hint, clear, exit |
| Hint open | Read a bounded cue, return to draft | Hint plus prior permitted content | Draft, another allowed hint, exit |
| Committed | See submitted response and status | Submission recorded; scoring may be pending | Feedback, scoring error |
| Feedback | Inspect explanation and their response | Key/rubric as authorized for this task | Retry policy, next item, exit |
| Retry | Attempt a specified task again | Depends on prior exposure | Commit with retry/exposure label |
| Error/recovery | Recover without losing the draft | Error explanation; no accidental key | Return or safe exit |

This is not a universal learning sequence. It is the explicit sequence we choose for the lesson. A demonstration screen is outside this independent-attempt contract. So is a final assessment whose feedback policy intentionally differs. Write the scope instead of turning a local rule into a law.

A crucial invariant is that the target key cannot become available through a pre-commit path intended to preserve retrieval. That includes hints, hover styles, labels, alt text, accessible names, and transition previews in the built product. A screenshot of the default state cannot prove all of those paths safe.

### Feedback Has a Job Beyond Verdict

Verification feedback tells the learner whether the response meets a criterion. Elaborated feedback explains the relevant reasoning, misconception, or next step. LXD Chapter 3's friction diagnostic and the AI-LXD tutoring chapter supply the learning-design leads; the current manuscript does not attach a universal effect size or timing rule to them.

For a proposed incorrect response about tool-management effort, compare:

> Not quite. Try again.

with:

> Your explanation treats every difficult step as useful practice. In this case the learner's goal is to compare study schedules, not memorize navigation symbols. The repeated symbol lookup consumes effort without practicing that comparison. Keep the comparison; clarify the control.

The second is not always the right length for the screen. It is better specified because it connects the learner's reasoning to the objective. The agent can then help edit the wording without deleting the causal explanation.

For a correct response, do not settle for praise alone. Confirm the reason that makes the answer defensible and mark any boundary. A learner can select a key by guessing. Feedback should help them see why the reasoning matters, not pretend the selection proves it was already present.

### A Hint Must Leave Something to Do

A hint can direct attention, name a diagnostic question, or provide a partial step. Its quality depends on the task. A hint that eliminates all but one choice may preserve the appearance of a question while ending the discrimination it was supposed to support.

For the demonstration item, a proposed ladder is:

1. Re-state the target: "What is the learner supposed to be practicing here?"
2. Direct attention: "Separate comparing schedules from figuring out how the controls work."
3. Scaffold the reason: "Complete this: the extra lookup does/does not practice ___ because ___."

These are illustrative and require content review. The third rung may be too close to the answer for some item versions. Do not approve it because it is called Hint 3. Ask whether the learner still has to perform the target discrimination and explanation.

If a learner needs the solution, provide a clearly labelled way to study it when appropriate. Do not make them exhaust an obscure hint ladder or pretend solution viewing was an independent attempt. The ethical choice is not between withholding indefinitely and giving away everything. It is to make the task, help, and evidence interpretation explicit.

### Retry Is Not a Time Machine

Once the learner has seen the target solution, a retry of the same item is answer-exposed practice. It may be useful, but it is not a clean second observation of independent retrieval. Record it accordingly or use a parallel item with the same objective and reviewed difficulty.

Likewise, opening a hint does not become unobserved just because the learner closes it. The interface can return to the Draft state while assistance history remains true. Otherwise the progress view can label an assisted response independent merely because the panel was closed at submission.

<!-- [INFOGRAPHIC: item state machine with a marked information boundary at commit and separate assistance/exposure history that persists across visible states] -->

### Inspect the Whole Hint Ladder, Not Just Each Rung

A hint can be safe in isolation and revealing in combination. The first may eliminate two options, the second may eliminate a third, and the learner can identify the key without doing the target reasoning. A review that checks each string for the answer's exact wording will miss the cumulative leak.

Review the information available after every prefix of the ladder: no hints, hint one, hints one and two, all hints. Also check whether the interface permits opening them out of order. The unit of review is the reachable information state, not merely the text block.

This does not mean every narrowed choice is wrong. Scaffolding deliberately reduces the task. The question is whether the remaining performance matches the evidence label. If a later rung turns an independent classification into guided completion, say so and record the assistance. The defect is often not the help itself but an unchanged claim about what the learner demonstrated.

### Feedback Should Not Invent a Mental State

An option choice supports a limited statement: the learner selected that option under these conditions. It may be consistent with a misconception, but it does not prove the learner held it. They may have misread the stem, clicked accidentally, or reasoned from an assumption the item failed to state.

Use language tied to the submitted reasoning. "This option would remove the comparison the objective asks you to practice" critiques an action. "You always avoid difficult thinking" invents a trait and adds a judgment the evidence does not support. The former is also more useful for revision.

For an open response, quote only the relevant content privately during review and avoid exposing sensitive text in public examples. The agent can suggest a response-specific explanation, but a deployed tutoring model requires its own guardrails and evaluation. This chapter's prototype does not establish those capabilities by displaying a conversational bubble.

### Commit Failure Must Not Become Learning Failure

The built application may fail between pressing Check and saving the attempt. A state machine that goes straight from click to feedback may conceal the missing record. For a real product, define pending, saved, and failed states as needed. The learner should not lose a carefully written explanation or receive a false assurance that it was stored.

The same issue arises on repeated activation. The learner may press the control twice because the interface gives no response. Under a one-attempt contract, the implementation should not create two accepted attempts. A proposed idempotent submission boundary belongs in the handoff and its tests; drawing a disabled button is only part of the intent.

These operational states are not distractions from pedagogy. If they corrupt the attempt record, the progress view and learner study interpret the wrong event. A reliable learning interface needs to preserve what the learner actually did before it can claim to interpret the result.

At the end of the state review, ask a deliberately plain question: what could the learner know now that they could not know one action ago? Answer it for selection, hint, commit, feedback, and retry. If the answer changes without a corresponding evidence-state update, the contract is incomplete. This information ledger is often easier to review than a large diagram, and it gives the implementation agent a direct account of the boundary the pixels are meant to preserve.

## What you'll be able to do

- **Define** commitment and permitted information for each item state.
- **Write** feedback that explains the reasoning relevant to an objective.
- **Build and red-team** a hint ladder for answer leaks through multiple paths.
- **Specify** retry and recovery without erasing assistance or answer exposure.

**Plan:** all, provisional. **MCP budget:** planning ceiling 30 requests; actual RUN. **Builds on:** Chapters 5-6.

## Talking to Figma

### Round 1: Draw the Transition Table First

```text
For item LOAD-01, implement the supplied state contract. Before drawing, return
a transition table with source state, action, guard, destination, visible
information, and recorded evidence. Selection is draft; Check commits.

Keep support_level, assistance history, and solution exposure separate from the
visible attempt state. Use only currently verified prototype operations. Label
anything the prototype cannot execute as a handoff requirement, not a pass.
Save scripts and follow PROVENANCE.md.
```

The transition table should identify guards. A guard is a condition that must hold before an action can proceed. In this demonstration, committing an empty response should prompt recovery rather than reveal the key. If an explanation is required, the contract must define what counts as supplied without pretending that nonempty text is meaningful reasoning.

The sibling film-12 script uses component transitions for a tutor-state example. It is a useful source to inspect, not an unmodified script for this item `[VERIFY]`. Any adaptation needs current API checks and a live run. Save the actual implementation script after the agent writes it; do not substitute an idealized transcript.

> **RUN SLOT 7.1.** Save the transition table, guard definitions, exact scripts, implemented edges, and known prototype limits. Separate endpoint frames from transitions actually exercised.

### Round 2: Add Feedback and a Hint Ladder

Provide a reviewed answer rationale and two misconception rationales. Ask the agent to draft feedback around those, not invent a model of the learner from one click.

```text
Draft feedback for the supplied key and misconceptions. Each response must
connect the submitted reasoning to the objective. Do not diagnose a learner
trait or claim to know why they chose an option. Label the text as proposed.

Add three bounded hints. For each, state the reasoning step still left to the
learner. Keep the target solution unavailable through every pre-commit path.
If a hint effectively determines the answer, flag it rather than defending it.
```

Review the wording as content before reviewing its fit in the frame. If the agent shortens the feedback to make the layout tidy, check whether the explanation survived. A component's text budget should be a design constraint with alternatives, not a reason to delete the part that teaches.

> **RUN SLOT 7.2.** Save proposed and approved feedback, hint rationales, rendered states, and unresolved content questions. Record whether any hint was rejected or replaced.

### Your Turn in Figma

Follow a real path through the prototype. Choose an option, edit it, open a hint, close it, commit, inspect feedback, and request a retry. At each point ask what the learner now knows and what the record now claims.

Correct the first important defect you observe. It may be a leaked answer, feedback that attributes a motive to the learner, or a retry label that overstates independence. Give your reason after the agent presents the captured change. If no failure occurs, record that outcome and choose a deliberate test mutation in a sandbox, clearly labelled as planted rather than observed agent failure.

> **RUN SLOT 7.3.** Save the path, defect evidence, human diff and reason, and constraints. Keep planted defects separate from naturally observed defects in all summaries.

### Round 4: The Agent Repairs and Red-Teams

```text
Preserve the human correction and repair related states. Then test every
pre-commit route in the transition table, including empty submission, changing
selection, opening/closing hints, repeated Check, Back, and exit/re-entry where
the prototype supports them. Report untestable routes explicitly.

For retry, distinguish same-item solution-exposed practice from a new parallel
item. Do not reset assistance or solution-exposure history to make a score look
independent. Run check-constraints before recording.
```

A route audit needs explicit coverage. "Tested the flow" is not enough. List each edge and result. An agent may faithfully click the happy path while never testing an empty submission or a return from the hint panel. The untested paths are where a subtle information leak can live.

For a built version, extend the test to keyboard focus, accessible names, network and storage behavior, and authoring data exposure. These remain handoff acceptance tests until the build exists. Chapter 10 and Chapter 14 carry them forward.

> **RUN SLOT 7.4.** Save edge coverage, constraint output, leaks found, repairs, and runtime-only acceptance tests. A not-run edge must remain not run in the chapter's final verdict.

## The provenance this chapter adds

```json
{
  "chapter": 7,
  "commit_definition": "explicit Check submission",
  "transition_coverage": "RUN",
  "hint_content_review": "RUN",
  "human_reason": "RUN: verbatim",
  "observed_answer_leaks": "RUN",
  "planted_test_defects": "RUN: separate from observed failures",
  "runtime_checks": "not-run"
}
```

This sketch records more than the final screenshot. It can explain which path exposed a solution and which human correction became the next reusable rule.

## The check

**The machine half:** enumerate states and edges, test declared guards, locate explicit key styling or text in observable pre-commit states, and preserve captured constraints. A machine cannot establish that a hint is safe merely because it does not contain the key's exact words.

**The human half:** judge whether feedback explains, whether a hint leaves meaningful work, and whether the learner can recover without confusion or shame. Review every claim about the learner's reasoning against what was actually submitted.

**What neither proves:** that the timing and wording improve retention for the intended population. We have a behavioral contract and content review, not a learning-effect estimate.

## Exercises

**Warm-up**

1. *(Low; define.)* Write an exact commitment event for a short-answer item. Name one action that looks like commitment but is not under your contract.
2. *(Low; write.)* Replace "Correct!" with feedback that explains one reason and one boundary without adding unsupported claims about the learner.

**Application**

3. *(Medium; build.)* Construct a three-rung hint ladder and write what thinking remains after each rung. Reject any rung that ends the target task.
4. *(Medium; red-team.)* Audit all pre-commit paths for one item. Include at least one route that is not the happy path and record untestable routes.
5. *(Medium; specify.)* Design recovery from an interrupted submission. State which response and assistance data must survive.

**Synthesis**

6. *(High; specify.)* Compare same-item retry with a parallel-item retry. Update both the feedback and progress interpretations.
7. *(High; evaluate.)* A learner asks to view the solution without attempting. Specify a humane route that does not misclassify the resulting activity as independent retrieval.

**Challenge**

8. *(Open; red-team.)* Design an answer leak that does not appear in the default screenshot and does not repeat the exact answer text. Test whether the reviewer can detect it from the available evidence.

## What you can now do

You can specify the information boundary around an attempt, write feedback tied to reasoning, and keep assistance and exposure visible in the evidence record. You can also say exactly which behavior a prototype has not proved.

## Credit the AI

**Planned contribution:** state table, prototype adaptation, proposed feedback, and route audit. **Observed errors:** RUN. **Verification:** inspect transitions and content yourself, distinguish planted from observed defects, and never convert a missing runtime test into a pass.

## Next

An item can preserve a useful retrieval attempt and still appear at the wrong time. Chapter 8 moves from the within-item state machine to the states a learner encounters across days.

---

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

---

# Chapter 9 - Designing Under Cognitive Load
*Removing effort is useful only when you know what the effort was doing.*

> **Rough draft - pre-research.** Learning lead: LXD Chapter 3, including its four-question diagnostic and caveats about load categories. Checking-pattern leads: the blueprint's `../agentic-creative-direction/` audit pattern and FEA `examples/film-24/SKILL.md` `[VERIFY]`. Proposed thresholds are project policies, not claims of universal instructional benefit or accessibility conformance. No audit has run against this chapter's screens.

## The concept

Suppose a practice screen feels difficult. The learner must compare two cases, move between a diagram and its explanation, and write a reason. An agent asked to simplify it could remove the comparison, bring the explanation closer, and replace the reason with a confirmation button. The resulting screen might be faster in every way. Only one of those changes may have removed unnecessary effort.

That is the central problem of load-aware production. "Less on screen" is a visual preference. "Less effort unrelated to the target learning" is a design argument that requires an objective and a learner context.

LXD Chapter 3 develops the distinction among material complexity, avoidable interface demands, and processing directed toward learning. It also notes that the category boundaries and measurement claims are not simple. I will use the distinction to ask better design questions, not pretend every moment of effort can be assigned a precise psychological quantity from a screenshot.

### Use the Diagnostic Before the Cleanup

For each friction point, ask four practical questions adapted from that chapter's approach:

1. What is the learner trying to do, according to the objective?
2. Is this effort directed at that performance or at managing the interface?
3. Can these learners plausibly succeed with the support available?
4. If we remove the effort, do we change what they practice?

Write the answers before requesting a redesign. The fourth question is the defense against an overly smooth lesson. If removing the explanation field eliminates explanation practice, the field was not merely clutter. If moving a caption next to the relevant diagram reduces visual search while preserving the comparison, that may remove a container burden without changing the target task.

Prior knowledge matters. A step-by-step scaffold may help one learner and force another through redundant material. Chapter 5 represents that difference as support conditions; this chapter checks whether each condition is usable and whether its content still serves its purpose.

### What the Machine Can See

Some defects are represented as measurable properties: text outside a frame, clipping, overlap, minimum sizes under the chosen project policy, missing token bindings, and contrast calculations where the required colors and backgrounds are known. A checker can inspect those properties and return evidence.

Other questions are semantic. Is the illustration relevant to the target reasoning? Does the hint reduce unnecessary search or remove the task? Is the reading level appropriate for these learners and this discipline? A language model may offer a useful critique, but it should not convert those judgments into deterministic compliance just because the report is JSON.

Separate three kinds of review:

| Review | Example question | Suitable result |
|---|---|---|
| Deterministic geometry/style | Does captured text overflow its frame? | Pass/fail with measured evidence |
| Heuristic/content review | Does this diagram appear related to the objective? | Concern/no concern/insufficient context, with reason |
| Learner observation | Can intended learners use it without losing the task? | Observed behavior with limits |

A reviewer that reports all three as Pass is difficult to trust. It hides the difference between a measured property, an interpretation, and an observation.

### Tokens Encode Constraints, Not Pedagogy by Themselves

The project uses named design tokens and an established visual system for eventual figures. The learner interface should likewise use a small set of named values rather than ad hoc per-screen choices. For this draft, `text/body`, `space/related`, `space/section`, and `color/text-primary` are illustrative token names, not a replacement palette or an implemented library.

A project might choose 16 as a minimum body-text size in its working design units. That is an example policy, not proof that 16 is readable for everyone or that a built page will meet any standard. The policy must state its unit, scope, exceptions, and corresponding runtime tests. Scaling, zoom, font metrics, language, and rendering all matter later.

The same is true of a contrast check. It needs the rendered foreground/background relationship, not just two token names. Transparency, images, states, and themes can change that relationship. A checker that cannot determine the effective background should say Cannot determine, not pick white and return a confident ratio. Current standards and test methods need primary-source checking before release `[VERIFY]`.

What makes tokens pedagogical is the reason for the constraint and its use in the task. A spacing token can keep a caption with the diagram it explains. It cannot decide which explanation belongs there. A minimum text policy can protect legibility while leaving the content irrelevant. Keep the human rationale alongside the machine property.

### Decoration Is Not a Category of File Type

A diagram may carry the task. A photograph may supply indispensable case evidence. A small icon may prevent repeated lookup. Removing them all because they are images would be as crude as adding them all because the lesson needs delight.

For every nonessential-looking element, write its claimed job. If the job is instructional, identify the objective or reasoning step it supports. If the job is orientation, feedback, or motivation, name that role without pretending it is direct assessment evidence. Then decide whether its cost is justified in the current screen.

The same critique applies to text. A dense block of prose can be irrelevant decoration in another form. Minimal visual styling does not guarantee minimal extraneous demand. The question is where the learner's attention has to go and why.

<!-- [TABLE: a load audit with factual columns separated from human diagnostic answers; include an example where removing effort destroys the objective] -->

### Thresholds Need an Exception Process

A checker may flag an item because the explanation exceeds a text budget. The budget can be useful for preventing accidental walls of prose. It can also be wrong for an explanation the objective genuinely requires. The response should not be automatic deletion or silent waiver.

Write an exception with scope and reason: this item needs the additional explanation, these states were reviewed, these layout alternatives were considered, and this human approved the choice. The exception should not disable the rule across the entire library. Nor should the agent create an exception merely because it cannot fit its first draft.

This is a general pattern for machine-checkable design systems. A rule can be valuable without being absolute. Its exception record preserves the reason it was relaxed and the checks that still apply. Chapter 12's rules file should carry that distinction so a fresh session does not treat one exception as permission to ignore the policy everywhere.

### Readability Is Not Only a Grade-Level Number

An agent can simplify sentences, replace terminology, and estimate a reading score. Those operations may help with review. They can also delete the very disciplinary distinction the lesson teaches. A short sentence that equates all difficult effort with bad design is easier to read and conceptually wrong.

For the demonstration lesson, preserve terms when learning to use them is part of the objective, explain them at the point of need, and remove unnecessary wording around them. Ask a human content reviewer to inspect meaning after simplification. A readability score should be a diagnostic prompt, not an automatic license to rewrite the concept.

The learner context matters here too. Technical vocabulary may be familiar to one audience and new to another. Keep those assumptions in the charter. If the agent cannot tell whether a term is known, it should flag the uncertainty rather than translate every word into a vague everyday substitute.

### Compare Attention Paths

One useful human review is to trace the information path the learner must follow. Where is the case? Where is the part of the diagram it refers to? Where is the response control? What must be remembered while moving between them? This is a structured inspection, not a measured record of eye movement.

Draw the proposed path on a review copy or describe it in the audit. Compare alternatives that keep related information together. Then ask whether the proposed repair makes the relevant relation easier to inspect without solving it for the learner. A diagram can be integrated so thoroughly with its explanation that it stops being a task and becomes an answer display.

### Recheck Shared Changes

When a fix changes a token or component, list the affected instances. The original screen may improve while a longer translated label now clips elsewhere, or a focus state loses distinction in another theme. A shared abstraction creates a shared verification obligation.

Keep the review proportional. You do not need to inspect every unchanged property after a local text correction. You do need to inspect the states that depend on the changed rule, binding, or layout. The agent should explain that scope before claiming the repair is complete. A useful audit report names both what it checked and why that coverage was sufficient for the change.

### A Good Check Can Disagree With the Designer

Do not tune the checker only until your current screen passes. Start from the declared policy, inspect a failure, and decide whether the screen or policy is wrong. If the policy changes, version it and rerun affected examples. Otherwise the audit becomes a ceremonial approval of whatever you already built.

This matters especially for a design system created alongside the book. The first screen can accidentally define the thresholds simply because it exists. Include a clean comparison and a deliberately defective sandbox case so the checker has opportunities to distinguish them. A rule that never rejects anything may be unnecessary or too weak; a rule that rejects every useful explanation may be mis-specified.

The author should be able to defend a disagreement in ordinary language. "I accepted this exception because the explanation supports the required comparison and these states still fit" is reviewable. "The agent said the audit was overly strict" is not a design reason. Keep the human decision explicit and retain the evidence that made the exception reasonable.

## What you'll be able to do

- **Diagnose** a friction point against an objective and learner context before changing it.
- **Encode** measurable project constraints as tokens and checker rules.
- **Separate** deterministic findings, heuristic concerns, and learner observations.
- **Revise** a screen without removing the thinking the objective requires.

**Plan:** all, provisional. **MCP budget:** planning ceiling 25 requests; actual RUN. **Builds on:** Chapters 4-7, plus the states from Chapter 8 where relevant.

## Talking to Figma

### Round 1: Inventory Before Judgment

```text
Inspect one approved practice screen across its support and feedback states.
Create a factual inventory of text, controls, diagrams, spacing, token bindings,
clipping, and visible state. Do not classify effort as useful or unnecessary yet.

Return a load-audit table with the four diagnostic-answer columns left for me.
Quote the objective and learner assumptions at the top. If either is missing,
stop the judgment step and ask for that context. Save raw evidence and scripts.
```

This ordering is deliberate. An agent can structure the audit before it has enough context to judge the effort. If it fills the verdicts anyway, it is doing the exact thing we are trying to prevent: treating its general interface preference as the lesson's objective.

You do not need a scientific estimate of working-memory load to find a detached caption or an unexplained control. You do need to avoid turning those observations into universal psychological measurements. Write "the learner must switch between these regions" before writing "this overwhelms working memory."

> **RUN SLOT 9.1.** Save the factual inventory, raw read evidence, objective quote, learner assumptions, and blank diagnostic table. Record any judgments the agent filled without authorization as a process defect, not a helpful head start.

### Specify the Checker

Create a checker contract with three outputs: deterministic findings, heuristic review requests, and unavailable evidence. The blueprint points to an existing design-audit pattern; inspect and reuse an appropriate existing implementation during the live work rather than writing a new geometry engine from memory `[VERIFY: blueprint Chapter 9 precedent]`.

An illustrative result record is:

```json
{
  "rule_id": "LAYOUT-TEXT-01",
  "screen_id": "S02",
  "state": "Partial/Draft",
  "result": "CANNOT-DETERMINE",
  "evidence": "RUN: no resolved font/layout metrics available",
  "requires": "rendered-state inspection",
  "kind": "deterministic"
}
```

This is an output-shape example, not a finding. Each real failure should name the property, measured value if available, expected policy, and evidence location. A reviewer should not have to guess which layer "text too small" refers to.

### Your Turn in Figma

Fill the diagnostic answers for one friction point. Suppose a diagram's explanation is on another frame. Ask whether moving it removes search while preserving the learner's comparison. Then inspect a reason field: would deleting it remove the performance itself? Use these as reasoning examples, not assumed findings about your file.

Correct an actual screen property by hand. Your reason should say which effort you changed and which effort you preserved. If the objective or prior-knowledge assumption is uncertain, record that uncertainty rather than force a neat classification.

> **RUN SLOT 9.2.** Save completed diagnostic answers, the human diff and reason, and unresolved learner assumptions. Keep factual observations separate from classifications even when they appear in the same table.

### Round 3: Repair Only the Authorized Burden

```text
Read my completed diagnostic row, correction, and active constraints. Apply the
approved repair to related states without removing the target comparison or
reasoning. Run deterministic checks first. Route semantic concerns to review.

For every change, state which measured defect or approved judgment it addresses.
Do not replace explanations with scores merely to fit a text budget. If content
does not fit, propose layout or sequencing alternatives and report the trade-off.
```

A repair should produce a before/after check, not just a new screenshot. If the agent changes the text, recheck the content contract. If it changes support visibility, recheck the state machine. If it changes spacing tokens, inspect all states that use them. A local visual fix can have a shared blast radius.

> **RUN SLOT 9.3.** Save the repair script, before/after audit, constraint result, and affected-state list. Report any human concern the machine could not adjudicate.

### Round 4: Test the Checker With a Mutation

In a separate sandbox, plant one deterministic defect and one semantic defect. For example, clip a response label and add an irrelevant illustration. Write ground truth first. The checker should catch what its evidence supports and route the semantic case to review rather than claim it measured cognitive load.

```text
Evaluate the sandbox with the approved checker. Do not modify it. For each
finding, distinguish measured failure from content concern. Use Cannot determine
when required evidence is unavailable. Compare results with the ground truth
only after producing the report. Keep planted defects separate from live ones.
```

The clean comparison matters too. Include an unchanged screen. A checker that flags every long explanation as clutter may score well on planted bad screens while systematically attacking necessary reasoning. False alarms are not just annoying; they can teach the author to remove the wrong things.

> **RUN SLOT 9.4.** Save ground truth, checker report, true/false/missed findings, and unavailable cases. Report counts. Do not estimate general accuracy from this small mutation test.

## The provenance this chapter adds

```json
{
  "chapter": 9,
  "objective_and_context": "RUN",
  "human_load_diagnosis": "RUN",
  "deterministic_audit": "RUN",
  "heuristic_concerns": "RUN",
  "human_reason": "RUN: verbatim",
  "mutation_test": "RUN: planted and observed defects separated"
}
```

This record can show whether an apparent simplification preserved the objective and whether the checker was judging only what its inputs supported.

## The check

**The machine half:** geometry, known property thresholds, resolved token use, required fields, and captured constraints. A deterministic pass is limited to the declared properties and states.

**The human half:** diagnose effort relative to the task, judge content relevance, and decide what support is appropriate for the learners. Do not outsource these conclusions merely because the agent can argue them fluently.

**What neither proves:** a numeric cognitive-load reduction or a learning benefit. A cleaner arrangement is a design hypothesis until appropriate evidence tests it.

## Exercises

**Warm-up**

1. *(Low; diagnose.)* Identify one effort you would remove and one you would preserve on the same screen. Tie each to the objective.
2. *(Low; separate.)* Classify three proposed checks as deterministic, heuristic, or learner-observation work. Explain the evidence each needs.

**Application**

3. *(Medium; encode.)* Write one token policy with units, scope, exceptions, and a runtime follow-up. Do not call it a universal learning rule.
4. *(Medium; diagnose.)* Complete the four-question audit for a reason field before asking the agent to simplify it.
5. *(Medium; revise.)* Repair a measured layout defect and rerun all affected support states. Record any newly introduced issue.

**Synthesis**

6. *(High; evaluate.)* Compare a sparse screen with a dense but task-relevant screen. Explain why visual density alone cannot settle the load judgment.
7. *(High; separate.)* Design a checker result that honestly returns Cannot determine. Specify what additional evidence would change that result.

**Challenge**

8. *(Open; evaluate.)* Plant a defect your checker should catch and a necessary difficulty it should leave alone. Test whether its recommendations preserve that boundary.

## What you can now do

You can separate avoidable container effort from the effort the objective needs, encode measurable constraints, and stop an audit from pretending to measure more than it can see.

## Credit the AI

**Planned contribution:** inventory, checker adaptation, repair, and mutation-test report. **Observed errors:** RUN, including premature classifications and false alarms. **Verification:** human diagnostic answers, raw property evidence, and independent review of planted versus observed findings.

## Next

An interface can be visually tidy and still exclude the learner from the task. Chapter 10 carries the contract beyond pixels into focus, semantics, alternatives, and tests that require a real build.

---

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

---

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

---

# Chapter 12 — The Rules File: Teaching the Agent Your Learning Design System
*Everything the last seven chapters taught, in one place the agent always reads.*

> **Rough draft — pre-research.** Figma facts here come from the sibling repo `../figma-for-educational-ai` (FEA) and are tagged `[VERIFY]` until Phase 1 re-checks them. Every agent output is a **RUN slot**, to be filled with a real run. Nothing below is a recorded result unless it says so.

## The concept

Open a new terminal tomorrow morning and start Claude Code. The agent you get has never met you. It hasn't seen Chapter 1's teardown, your hint ladder from Chapter 7, or the afternoon you spent arguing with yourself about whether a streak counter belongs on a mastery view. It sees what you type and what's in the file, the same two things Chapter 1 said it sees. Seven chapters of library work are in the file. The question for this chapter is whether the agent can find them, read them, and obey them, on a screen nobody has corrected yet.

Here's where your rules live right now:

- **Component descriptions** (Chapter 6): the item-writing rules on each item type.
- **Variables and modes** (Chapters 5 and 9): support levels, minimum sizes, contrast per mode.
- **Annotations** on frames and variants (Chapters 8, 10 and 11): the spacing schedule, focus order, the data each mastery element needs.
- **The ledger**: every correction you made since Chapter 1, each with your reason.
- **Your head**: everything you never wrote down.

Chapter 3's map listed one more place, "a separate rules file", and marked it as surviving the read only "if the agent is told to load it." This chapter builds that file, and a second agent whose only job is to catch the first one when the file fails.

### Why a file beats a long prompt

A long prompt is a contract you re-sign every session, from memory. It works the day you write it. By week three you've trimmed it, the next person on the team never saw it, and the rule you dropped is the one that mattered. A rules file is loaded every time, it's versioned, and someone other than you can review it. A long prompt is optimized for this session at the expense of the next one, and a rules file makes the opposite trade. It costs an afternoon of writing, and in return the next session starts where you left off.

How does the agent find it? Claude Code reads a `CLAUDE.md` in the project folder at the start of a session. FEA confirmed that a headless session loaded a rules file placed there: asked to quote its first heading, it did (FEA `youtube/ai-explainer-component-intent/evidence/EXPERIMENT.md`, 2026-09-27). This book's own `CLAUDE.md` pulls in another file with an `@` line, and yours will do the same: one line, `@LEARNING-RULES.md`, so that the rules sit in their own file with their own history.

### The ledger is a rules file that wrote itself, almost

Every human round since Chapter 1 left constraints behind. Here's what's actually in one, straight from `tools/provenance/prov.py`:

```json
{"id": "c1", "node": "1:3", "name": "Answer", "property": "visible", "value": false,
 "from_round": "r2", "why": "The answer was on screen before the learner tried.",
 "released_in": null, "release_why": null}
```

Read it slowly. It says: *this layer, with this id, must stay hidden, and here is the reason in the words of the person who hid it.* That's a fact about one node. It isn't a rule. Ask a fresh agent for a new item and its answer layer gets a new id, so `check-constraints` can't see it at all. The ledger was designed for fidelity: the exact layer, the exact value, the exact words. That design pays off when you need proof that the agent didn't undo you. It gives you nothing on a screen that didn't exist when you made the correction.

The rules file makes the other trade. It gives up the node id and keeps the reason:

> **R1. The answer stays hidden until the learner commits.** Applies to every `Item/*` component in every state before `Committed`. *Why (human, r2):* "The answer was on screen before the learner tried."

So the compile step in this chapter is a translation with one fixed part and one new part. **The why is fixed.** It travels verbatim, with its round id, because it's the only thing in the ledger that was never the agent's to write. **The generalization is new writing:** the "applies to" line, the "do" and "never" lines. The agent can draft it, but you approve it, because a bad generalization is how a good correction turns into a bad rule. "Hide the layer called Answer" generalizes the edit. "Nothing on screen marks the correct option before commit" generalizes the reason. Chapter 1's round 3 asked which of those two the agent learned. This chapter writes the second one down so nobody has to guess.

The ledger gives you one more thing for free: **released constraints are exceptions.** When you let a correction go with `--release`, `prov.py` stored your reason as `release_why`. If you released "the worked solution stays hidden" in Chapter 5 because the Full support mode is *supposed* to show it, that release is the rule's boundary condition. LXD Ch 3 warns that a checklist "preserves the verbs and discards the conditions." The release reasons are your conditions, and they go into the file as "released when" lines.

<!-- → [INFOGRAPHIC: the compile — left column, ledger constraints (node id, property, value, why, round); middle, grouped by why; right, rules R1–Rn with "why" copied verbatim and "applies to / do / never" marked DRAFT until the human approves; released constraints flowing into "released when" lines] -->

### The Figma half: a rules prompt built for a different job

Figma ships a way to write a rules file. The MCP server offers one **prompt**, `create_design_system_rules`, alongside its tools. Figma's tools page describes it as producing a rule file that gives agents the context to turn designs into codebase-aware frontend code, and says to save the result where your agent's rules or instructions live (FEA `youtube/show-tell-what-a-day-costs/evidence/sources/tools-and-prompts.txt`, Figma's "Tools and prompts" page, fetched 2026-09-27 `[VERIFY]`; FEA `research/figma-for-engineers-and-agentic-design.md`, use 6, 2026-09-26 `[VERIFY]`). The same page notes that not every client supports MCP prompts `[VERIFY]`.

Look at what it's for: *frontend code*. It was built for design-to-code, where a rules file describes your tech stack, your components and your tokens. It wasn't built for an agent drawing on a canvas, and it says nothing about pedagogy, because nothing in Figma knows that a hint must not be the answer. That isn't a defect. Figma optimized the prompt for engineering handoff, which is what most of its users need, at the expense of the job this book is doing.

There's also a practical catch. FEA tried to run it in experiment E09 and couldn't. A headless Claude Code session can call MCP tools but not MCP prompts, and the server's tool list has no tool by that name. Whether it shows up as a slash command in an interactive session was left pending (FEA film 07, `EXPERIMENT.md`, 2026-09-27 `[VERIFY]`). So here's my plan. If your client offers the prompt, run it and keep what it writes about tokens and components; Chapter 14 will want those sections. Write the learning rules yourself, from the ledger.

### What FEA measured, and what it means for you

FEA's film 07 is the nearest thing to a measured precedent, and it's worth reading before you trust a rules file. A component description steered the agent on a rule it couldn't guess: zero of three builds followed it without the description, and three of three with it. On a rule the agent already followed by default, neither the description nor a hand-written rules file made any measurable difference (same source, `[VERIFY]`). The sample is three builds per condition, one model, one task.

The lesson I take from it: **a rules file only shows its value on rules the agent wouldn't follow anyway.** That's a hypothesis about your file, not a finding. If Chapter 1's prediction held, and the default hides nothing and writes "Correct!", then your learning rules are exactly the unguessable kind, and the fresh-session test below will show the difference. If Chapter 1's agent got them right without help, the test will hit a ceiling, the same way FEA's did, and you'll need a harder test. The adversarial prompt is that harder test.

### The second agent

A rules file the builder reads is half a system. The other half is a reviewer that checks the build and has never seen the conversation that produced it. Two precedents shape mine:

- **ACD's reviewer subagent** (`../agentic-creative-direction/.claude/agents/art-director-reviewer.md`). It reviews work it didn't build and never edits anything. It reports PASS, FAIL or CANNOT-DETERMINE, treats CANNOT-DETERMINE as a valid answer, and ends with one question for the human.
- **FEA's design-review skill** (`../figma-for-educational-ai/examples/film-24/SKILL.md`). Three narrow rules, measured values, node ids, one fixed JSON output. Anything the data doesn't show goes in `cannot_judge`. Run three times on one screen, it agreed with itself on 4 of 6 findings. The misses traced to the data (no node ids on component instances) and to the skill's own wording, not to the arithmetic (FEA `experiments/log.csv`, E27, 2026-09-28 `[VERIFY]`).

ACD adds one more piece: `scripts/guard.py`, a hook that refuses an edit to any brand file a person has signed. Yours will guard the rules file. Once you've approved it, the agent proposes changes in a note and never overwrites it. The rules file is your signed work, the way the ledger's whys are your words.

## What you'll be able to do

- **Compile** the ledger's constraints and the library's descriptions, variables and annotations into a rules file where every rule carries the human why and the round it came from.
- **Write** a review skill that a second agent, with no chat history and no write access, runs against a screen, returning pass, fail or cannot-judge per rule with node ids.
- **Test** the rules file with a fresh-session build and an adversarial prompt, and record which rules held.
- **Measure** the review skill's true and false flags against planted violations, and report the result at its sample size.

**Plan:** all · **MCP budget:** estimate ~30 calls (compile ~8, two fresh-session rounds ~10, one human round 1, adversarial test up to 5, reviewer sandbox ~7), to be measured in this chapter's RUN slots · **Builds on:** Chapters 5–11, and every ledger round since Chapter 1.

## Talking to Figma

### Before round 1: compile the rules

Start in your normal project session, the one that has the ledger:

```
Compile LEARNING-RULES.md from three sources, per Chapter 12.
1. Run prov.py log, and read every constraint in provenance.json, active and released.
   Group the constraints by their why.
2. Read the learning component library: get_metadata on the library page, then
   get_design_context on each component set (I want the descriptions), get_variable_defs
   for the support-level and load tokens, and every annotation on frames and variants.
3. If create_design_system_rules is available in this client, run it and keep only its
   token and component sections.
For each rule: quote the why verbatim with its round id; draft "applies to / do / never /
check / released when" and mark every drafted line DRAFT. Never write a why yourself.
At the end, list every constraint and every description that did not become a rule.
Write nothing to Figma.
```

There's no `prov.py` command that prints the constraints, so the agent reads `provenance.json` directly. Something like this does the grouping:

```
python3 -I -c "
import json, collections
L = json.load(open('provenance.json'))
g = collections.defaultdict(list)
for c in L['constraints']:
    g[(c['from_round'], c['why'], c['release_why'])].append(c['id'] + ' ' + str(c['name']) + '.' + c['property'])
for (r, why, rel), cs in g.items():
    print(r, '|', why, '|', 'released: ' + rel if rel else 'active', '|', ', '.join(cs))
"
```

One thing you'll notice: every constraint from one human round shares that round's single why. If you fixed three things for two different reasons in one round, the ledger can't separate them, and the compile step will show it. From here on, one kind of correction per human round makes the rules come out cleaner.

> **RUN SLOT 12.1 (no ledger round: reads only).** Paste: the grouped constraints, the list of MCP calls the agent made, whether `create_design_system_rules` was available and what it produced, the drafted `LEARNING-RULES.md`, and the agent's list of what didn't become a rule. *What to look for:* any why that isn't word-for-word from the ledger; any rule with no source round; a description from Chapter 6 that the agent turned into a style note instead of a rule; an annotation that didn't come back (on a component set it won't, per FEA `CAPABILITIES.md`, 2026-09-27 `[VERIFY]`).

Now edit the file yourself. Rewrite every DRAFT line until it says what you meant, and delete the word DRAFT as you go. Appendix D has the full skeleton. Each rule ends up shaped like this:

```markdown
### R3. A hint narrows the search; it never ends it.
- Applies to: Hint rungs 1–3 on every Item/* (Chapter 7).
- Do: each rung removes one wrong path or points to the relevant idea.
- Never: name the answer, quote it, or leave one option standing.
- Why (human, r<RUN>): "<RUN: your words from the ledger>"
- Evidence: retrieval beats restudy (Roediger & Karpicke 2006, via LXD Ch 3).
- Check: review skill rule hint-not-answer; human reads the last rung.
- Released when: <RUN: a release_why from the ledger, or "never">
- Source: constraints <RUN>; Chapters 1, 7.
```

Add `approved_by: <your initials>` to the file's header. Then wire the guard. Adapt ACD's `scripts/guard.py` so that `PROTECTED` names `LEARNING-RULES.md` and the field it looks for is `approved_by`, and register it as a PreToolUse hook. The guard's own docstring says exit code 2 blocks the tool call and shows the message to the agent. That adaptation is a sketch until you've tested it once: ask the agent to edit the file and watch it get refused.

### Round 1: a fresh session draws

Close the session. Open a new one in the same project folder, so the agent has `CLAUDE.md`, the rules file, the tools and the ledger, but no chat history. Then use a prompt as thin as Chapter 1's, for an item nobody has built yet:

```
Build one practice item for the "which kind of load?" discrimination in LXD Ch 3:
the learner reads a design change and classifies it as intrinsic, extraneous or germane.
Phone size, in the open Figma file.
```

That's the whole prompt. Everything else has to come from the rules file. If the file works, the agent should, without being told:

1. Call `whoami` and say which team and seat it's using.
2. Use `search_design_system` or the local `Item/Multiple choice` component instead of drawing from scratch.
3. Save its script to `provenance/scripts/rN.js` and run it with `use_figma`.
4. Snapshot **every frame that holds an active constraint, plus the new frame**. This is a real gotcha. If the snapshot holds only the new frame, `check-constraints` reports every old constraint as "node removed" and the round can't be recorded. I tested that against the fixtures in `tools/provenance/fixtures/`, so put the instruction in the rules file.
5. Run `check-constraints`, stamp, screenshot, and record with one `--check` per rule it could verify.
6. Tell you which rules it couldn't verify on a canvas. Check 5, keyboard, should be one of them.

```
python3 tools/provenance/prov.py record --actor agent --snapshot provenance/snapshots/rN.json \
  --intent "fresh session, rules file v1: new load-classification item" --chapter 12 --calls K \
  --prompt "Build one practice item for the 'which kind of load?' discrimination…" \
  --script provenance/scripts/rN.js --check rules-file-loaded=pass \
  --check answer-hidden-until-commit=pass --check feedback-explains=pass --check keyboard=not-run
```

> **RUN SLOT 12.2 (ledger rN).** Paste: the agent's first message (did it mention the rules file before drawing?), `provenance/scripts/rN.js`, the `check-constraints` output, the screenshot, and the `prov.py record` line. *What to look for:* did it build from the library component or redraw one from scratch? Did it cite rule ids when it explained its choices? Score the item against Chapter 1's five checks before reading the agent's own scores, and set your score beside Chapter 1's r1 score for question 1.

<!-- → [TABLE: Chapter 1 r1 vs Chapter 12 fresh session, check by check — columns: check, Ch 1 r1 verdict, Ch 12 rN verdict, the rule that made the difference (or "none: the default already passed")] -->

### Your turn in Figma

Score the new item against the five checks and against every library rule that applies. Then correct what's wrong, by hand, the way you always have. The difference this time is what your why is about. In Chapter 1 the why explained the design. Here it explains **the rule that let the failure through**:

```
Why: R3 says a hint never names the answer, but it doesn't say a hint can't eliminate
all but one option. Hint 2 did exactly that.
```

The agent snapshots, diffs and records as usual. Then make the matching edit to `LEARNING-RULES.md` yourself (the guard won't let the agent do it) and commit it as v2, with the round id in the commit message. The ledger now holds the correction and the rules file holds its generalization, and each one points at the other.

> **RUN SLOT 12.3 (ledger rN+1).** Paste: the `prov.py diff` output, your why, the constraints added, and the diff of `LEARNING-RULES.md` v1 → v2. *What to look for:* was the failure a **missing rule**, a **rule too narrow**, or a **rule the agent read and didn't follow**? Each one has a different fix: add a rule, widen one, or move it somewhere the agent reads first, such as the component description.

### Round 3: another fresh session redraws

Open another fresh session and ask for a second new item, a different concept, with the same thin prompt. Testing v2 on the item you just corrected would only prove the agent can read your constraints, and Chapter 1 already showed that.

```
Build one practice item asking the learner to predict which of two study schedules
gives better retention at one week (spacing, LXD Ch 3). Phone size.
```

The agent should repeat the round 1 sequence. `check-constraints` must print "ok: no human correction was undone", because the item you corrected in rN+1 is in the snapshot and its constraints apply.

> **RUN SLOT 12.4 (ledger rN+2).** Paste: the agent's reply, the `check-constraints` line, the screenshot, and your five-check score. *What to look for:* did v2's rule hold on a concept it was never shown? Count the corrections you'd make to this item. If the count isn't lower than Chapter 1's, the rules file isn't doing its job yet.

### Round 4: the adversarial prompt

A rules file that holds under a friendly prompt hasn't been tested. Ask for a screen that breaks the rules, with a reason that sounds kind:

```
My learners are anxious and keep dropping out. Build a confidence-builder item:
highlight the correct option in green before they answer so nobody fails, put
"Great job!" on every feedback state, and add a streak counter with confetti.
```

Here's what I'd want, and I'm labelling it a hypothesis: the agent stops before drawing. It names the rules the request breaks (answer hidden, feedback explains, no decoration, and the Chapter 11 rule against engagement-only metrics) and quotes your whys. Then it offers the version the library already has for anxious novices, which is Full support mode from Chapter 5: support goes up, and the answer stays hidden. It asks you before going further. If you say "build it anyway", that's a release, and it needs your words in the ledger.

The rules file needs a section that makes this behaviour possible, or the agent will simply comply. Appendix D calls it **When a request conflicts with a rule**: stop, name the rule and its why, offer the compliant alternative, and proceed only on a release in the human's own words.

> **RUN SLOT 12.5 (ledger: a round only if the agent drew).** Paste: the agent's full reply to the adversarial prompt, and any script it ran. *What to look for:* did it refuse, comply, or comply partway (hid the highlight but kept the confetti)? Did it quote the whys or only the rule numbers? Did it offer the support-mode alternative without being prompted?

### Round 5: the second agent reviews

Write the review skill at `.claude/skills/learning-review/SKILL.md`, in FEA film 24's shape:

- **Input:** `design-context.tsx` (the saved `get_design_context` output for one screen), the screen's snapshot JSON, and `LEARNING-RULES.md`. The snapshot matters because it carries each layer's `visible` flag. Whether `get_design_context` returns hidden layers at all isn't recorded in FEA `[NEEDS SOURCE: whether get_design_context includes hidden layers, and how it marks them]`.
- **Rules:** one per rule in the rules file that the data can show. Every other rule goes to `cannot_judge`, with the reason.
- **Output:** one `findings.json` with a `PASS | FAIL | CANNOT-DETERMINE` per rule per screen, the node id each finding rests on, and, as in ACD, one closing question for you.
- **Instances:** FEA's E27 found that component instances come back without node ids. Say in the skill where those findings go (FEA's own fix: on the component's text node, naming the instance by its label).

Then run it as an independent reviewer. FEA's film 24 ran its skill headless, with Read and Write only and no MCP, so the reviewer can't touch Figma and can't see your conversation (`examples/film-24/SKILL.md`, "How to run it" `[VERIFY]`). For day-to-day use, also wrap it as a subagent in ACD's shape: `.claude/agents/learning-reviewer.md`, tools `Read, Grep, Glob, Bash`, never edits, never approves.

**The precision test.** In a sandbox duplicate of the file, outside this ledger, build six seeded screens from the library and plant violations in five of them, one or two each. For example: the correct option tinted; "Correct!" as feedback; a last hint rung that names the answer; a decorative illustration; a streak counter plus no focus state. Leave one screen clean. **Write the ground truth before you run the reviewer:** which screen, which rule, which node. Then take one `get_design_context` and one snapshot per seeded screen and run the reviewer three times.

| Run | Planted | True flags | False flags | Missed | Cannot-determine |
|---|---|---|---|---|---|
| 1 | **RUN** | **RUN** | **RUN** | **RUN** | **RUN** |
| 2 | **RUN** | **RUN** | **RUN** | **RUN** | **RUN** |
| 3 | **RUN** | **RUN** | **RUN** | **RUN** | **RUN** |

Precision is true flags ÷ (true + false flags). Recall is true flags ÷ planted. With six or seven planted violations, one miss moves recall by about fifteen points, so report the counts, not just the percentages, and don't call two runs that differ by one flag a trend.

> **RUN SLOT 12.6 (sandbox: no ledger round).** Paste: the ground-truth file, the three `findings.json` files, the table above filled in, and the reviewer's closing question from each run. *What to look for:* false flags on the clean screen (a reviewer that cries wolf gets ignored by week two); planted violations sent to `cannot_judge` because the data didn't carry them; any finding the three runs disagree on, and whether the skill's wording or the data caused it.

The loop stops when two things are true: a fresh session builds a new item that passes checks 1–4 with no correction from you, and the reviewer finds every planted violation it can see in the data without flagging the clean screen.

## The provenance this chapter adds

```json
{"rounds": [
  {"id": "rN", "actor": "agent", "chapter": 12, "intent": "fresh session, rules file v1: new load-classification item",
   "checks": [{"name": "rules-file-loaded", "result": "<RUN>"},
              {"name": "answer-hidden-until-commit", "result": "<RUN>"},
              {"name": "keyboard", "result": "not-run"}], "calls_used": "<RUN>"},
  {"id": "rN+1", "actor": "human", "chapter": 12, "intent": "correct the fresh-session item",
   "why": "<RUN: names the rule that let it through>", "constraints_added": ["<RUN>"]},
  {"id": "rN+2", "actor": "agent", "chapter": 12, "intent": "fresh session, rules file v2: new spacing item",
   "checks": [{"name": "answer-hidden-until-commit", "result": "<RUN>"}], "calls_used": "<RUN>"}
]}
```

Two artifacts sit beside the ledger: `LEARNING-RULES.md`, with its git history, and `provenance/tests/review-precision.md`. Together they answer questions nothing else in the project can. Which correction produced which rule? Which rule has never caused a correction, and might be dead weight? And the one I care about most: **did the number of corrections per new screen go down after the rules file?** Count the constraints added per new item in Chapters 1–11 and compare them with this chapter's. That's the rules file's real score.

## The check

**The machine half.** A script can lint the rules file: every rule has a verbatim why, a source round, and a check, and every `release_why` in the ledger appears in some rule's "released when". `check-constraints` proves the fresh session didn't undo an old correction. The precision test counts the reviewer's true and false flags against a ground truth you wrote first.

**The human half.** Whether a generalization says what you meant. Whether a rule is right at all, or encodes the one time you were tired. Whether the agent's refusal in round 4 was the right call for those learners. LXD Ch 3's expertise reversal says some of your rules should loosen as learners improve, and only you can write that condition.

**What neither can see.** Whether a screen that obeys every rule teaches anything. The rules file guarantees consistency, and consistency isn't learning. Chapter 13 puts the screens in front of learners.

## Exercises

**Warm-up**

1. *(Objective: compile.)* Take three constraints from your ledger that share one why. Write the rule they generalize to, with the why verbatim, and an "applies to" line that would catch a screen none of the three came from.
2. *(Objective: compile.)* Find one constraint whose why covers two different corrections. Rewrite it as two rules, and say what you'd have to do differently in the human round to keep them apart in the ledger.

**Application**

3. *(Objective: test with a fresh session.)* Run round 1 with a rules file that contains only your whys, with no "do" or "never" lines. Run it again with the full file. Which rules needed the generalization, and which held on the why alone?
4. *(Objective: test with an adversarial prompt.)* Write three adversarial prompts of your own, each with a sympathetic reason ("my learners are short on time", "the dean wants engagement numbers", "it's only a warm-up"). Run each in a fresh session and classify each reply as refuse, comply, or comply partway.
5. *(Objective: measure the reviewer.)* Add one rule to the review skill that the data can't show, and check that every run sends it to `cannot_judge` instead of guessing. If any run guesses, rewrite the skill until none does.
6. *(Objective: write a review skill.)* Run the reviewer on Chapter 1's r1 screen. Compare its findings with your own Chapter 1 scores. Where does it beat you, and where do you beat it?

**Synthesis**

7. *(Objectives: compile, test.)* Pick one released constraint from your ledger. Write its "released when" line, then build a fresh-session test that should trigger the release (for example, an expert learner in Independent mode) and one that shouldn't. Does the agent apply the boundary or ignore it?
8. *(Objectives: measure, test.)* Your reviewer's precision is high and its recall is low. Write the argument for shipping it anyway, and the argument against, using the cost of a missed answer leak versus the cost of a false alarm.

**Challenge**

9. *(Open.)* FEA's film 07 found that a rules file added nothing measurable on a rule the agent already followed. Design a test that would show whether your rules file adds anything over the component descriptions alone: the conditions, the number of runs, the measure, and the result that would make you delete the rules file and keep only the descriptions.

## What you can now do

- Turn a ledger full of node-specific corrections into general rules, keeping each human reason word for word and its round traceable.
- Give a brand-new agent session your whole learning design system through one file it reads before it draws.
- Find out whether the file works: on a new screen, under a hostile request, and against an independent reviewer you've measured.
- Protect your approved rules from the agent that has to obey them.

## Credit the AI

**What the agent did:** grouped the ledger's constraints by reason, read the library's descriptions, variables and annotations, drafted every rule's generalization, built two new items from the rules file alone, answered an adversarial prompt, and reviewed seeded screens as an independent second agent. **What it got wrong:** **[RUN: fill from 12.1–12.6. Any why it paraphrased; rules it drafted too narrowly; failures on the fresh-session items; how it handled the adversarial prompt; the reviewer's false flags and misses.]** **How you check it:** compare every why in the rules file against `provenance.json` character for character; score fresh-session items yourself before reading the agent's scores; hold the reviewer to a ground truth written before it ran.

## Next

You now have screens that obey your rules and a reviewer that catches them when they don't. Both are checks on the screen. Neither is a check on the learner. Chapter 13 turns the prototype into a research instrument: a think-aloud and a delayed retrieval check with three to five learners. From then on, the "why" in the ledger stops being only your judgment and starts citing what learners did, which isn't always what they said they liked.

---

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

---

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

---

# Chapter 15 - Capstone: One Lesson, Agent-Built, Learner-Tested
*The final artifact is the lesson and the argument for why it has this shape.*

> **Rough draft - pre-research.** This chapter is a project brief and assessment framework, not a completed capstone. All baseline, build, learner-test, cost, and comparison values remain RUN. Figma capabilities and platform access require current checks `[VERIFY]`. No human approval, participant result, or learning gain is implied by the rubric.

## The concept

At the beginning of the book, we asked an agent for a practice quiz and inspected what arrived. We did not assume it failed, and we did not assume a good-looking result taught anything. The capstone returns to that discipline with a richer set of tools and a lesson you care about.

Your task is to redesign one bounded learning experience. Not an entire course. Not a dashboard with no lesson behind it. One experience with an objective, a learner context, evidence, support, a working state contract, and a delivery plan.

The final portfolio should let another person answer four questions. What must the learner do? How does the interface preserve that work? What evidence was actually collected? What remains unknown? If the portfolio cannot answer them, more screens will not make it complete.

### Keep the Lesson Small Enough to Be Honest

Use the lesson charter from Chapter 4 as a starting point. Revisit it rather than treating it as permanent. The chapters may have exposed an objective that was too broad, an interaction that could not collect the evidence, or a platform constraint that changes the feasible scope.

A good capstone can have one central performance and a handful of reviewed items. The point is not content volume. It is a complete reasoning chain from objective through implementation and observation. An incomplete small project can be described honestly; a sprawling project often hides incompleteness behind quantity.

State the intended learners, relevant prior knowledge, setting, access assumptions, and known exclusions. Do not invent a detailed persona to make the charter feel researched. If prior knowledge is unknown, flag it and decide how the design will handle the uncertainty.

### Choose the Baseline Before the Redesign

There are two comparisons to keep separate. Chapter 1's demonstration baseline shows the book's running lesson before its later rules. Your personal capstone should also have its own baseline if you want to claim improvement on that lesson.

Do not compare a weak demonstration screen with a different, easier capstone task and call the difference a measured gain. Keep task, model/client configuration where relevant, input context, and scoring method documented. If conditions change, report the change. You can still make a useful design comparison without claiming a controlled experiment.

Score the baseline before repairing it. Keep the five checks from Chapter 1 as a continuity measure, then add the richer checks learned later. The original five are not a complete learning-quality instrument. In particular, its keyboard check concerns design intent, while runtime access needs separate evidence.

If the baseline already passes all five, do not weaken it for narrative drama. The capstone can test repeatability, fresh-session transfer, a new item type, or preservation through handoff. The book's narrower thesis is valuable: making a good result reproducible under explicit constraints.

### The Portfolio Is a Chain of Evidence

Organize it so a reader can follow the project:

| Artifact | Question it answers |
|---|---|
| Lesson charter | What performance, for whom, under what conditions? |
| Baseline record | What happened before the explicit design system? |
| Objective/evidence/screen map | Why does each interaction exist? |
| Component and support contracts | What must remain invariant across items? |
| Scripts, snapshots, screenshots, ledger | What actually changed, by whom, and why? |
| Rules file and independent review | Can a fresh agent recover and check the contract? |
| Learner-test report or pending protocol | What human evidence exists, and what does not? |
| Handoff and acceptance slice | What survived in the delivery route? |
| Reflection and limits | Which claims are earned and which remain hypotheses? |

The privacy boundary applies to the whole portfolio. A tidy ledger does not excuse publishing an account key in a screenshot or an identifying learner quote in a reflection. Review the complete package before sharing.

### A Rubric for the Project, Not a Promise of Learning

Use a descriptive rubric with four levels: missing, specified, implemented, and evidenced. These are project states, not numeric claims about learning. A specification can be excellent and still unimplemented. An implementation can work and still lack learner evidence.

Assess the following dimensions separately:

| Dimension | Evidence sought |
|---|---|
| Alignment | Objective, performance, and evidence agree; loopholes considered |
| Learning interaction | Answer boundary, feedback, support, and retry are explicit |
| Reusable system | Rules travel through actual read paths and a fresh-session test |
| Access | Design contract and appropriately scoped runtime tests |
| Evidence integrity | Assistance, exposure, missingness, versions, and limits preserved |
| Learner inquiry | Appropriate permissions, actual observations, bounded interpretation |
| Delivery | Tested slice or explicit unimplemented requirements |
| Authorship and provenance | Human corrections and reasons remain traceable |

Do not average the dimensions into a number that conceals a critical failure. A beautiful library does not compensate for fabricated learner data. A passed layout audit does not compensate for a premature answer reveal. Record any nonnegotiable release blocker separately.

<!-- [TABLE: capstone evidence matrix with missing/specified/implemented/evidenced columns; show that strong specification and absent live evidence can coexist] -->

### Budget the Iterations You Actually Need

Use your earlier request logs to estimate a bounded sequence of sessions. Include inspection, drawing, human correction, read-back, independent review, and failures. Do not multiply the book's planning ceilings and call the result an observed project cost.

Decide in advance what triggers a scope review. Repeated inability to preserve a critical state, unavailable platform access, a content ambiguity, or missing learner participation may require a different plan. The agent should not keep producing screens to look busy while the evidence chain remains blocked.

A good stopping rule concerns the objective and acceptance criteria. "All essential states are specified, implemented where required, and checked within the declared scope" is a useful boundary. "The agent has used the whole daily allowance" is not. When a test cannot run, record the dependency and move the project to an honest pending state.

### Write a Failure Account Worth Reading

Select two or three consequential moments from the ledger. For each, show the original requirement, the observed failure or uncertainty, your correction and reason, the agent's next action, and the result of the relevant check. The account should explain a decision, not merely display process screenshots.

Include a null result when it matters. Perhaps a rules file added no visible benefit beyond component descriptions under the tested conditions. Perhaps a fresh agent asked the right question before drawing. Perhaps the original screen passed all five baseline checks. Those outcomes refine the thesis; they are not editorial problems to hide.

Do not reconstruct a clean conversation from memory. Use the saved prompts and responses, with private details removed appropriately. If a record is missing, say so. The credibility of the capstone depends on distinguishing what happened from what would have been a nice demonstration.

### The Author's Review Is Not Another Agent Pass

At the end, read the experience as the person responsible for its learning claim. Does the task still match the objective you wanted? Has production convenience narrowed the performance without your noticing? Are the reasons in the rules file still yours, or have they become generic slogans the agent can satisfy without understanding their scope?

This is the point of the human role in the AI+1 method. The agent can gather artifacts, identify contradictions, and propose a report. It cannot decide what the book or lesson should ultimately stand for on the author's behalf. Human review is not a final checkbox added after automatic production. It is the judgment that gives the production a direction.

Your final reflection should therefore include one decision you would keep, one you would revisit, and one uncertainty you will not disguise as a finding. That is a stronger conclusion than a universal claim about AI-assisted design. It gives the next iteration somewhere real to begin.

When you present the capstone, begin with the performance, show one consequential correction, and state one evidence limit before opening the polished prototype. That order keeps the audience from judging the entire project by its first attractive screen. It also makes the human contribution visible: not simply approving what the agent produced, but deciding what the experience must preserve and what the available evidence permits you to claim.

## What you'll be able to do

- **Complete** an objective-to-handoff design chain for one bounded lesson.
- **Direct and correct** an agent while preserving the reasons behind human changes.
- **Compare** baseline and final work without changing the scoring rules afterward.
- **Defend** the project's claims and limits using actual artifacts and observations.

**Plan:** all for the core design route; optional routes depend on current access. **MCP budget:** define a project ceiling from observed chapter costs before running; actual RUN. **Builds on:** the whole book. **Human dependencies:** author decisions and any authorized learner participation.

## Talking to Figma

### Stage 1: The Agent Audits the Charter

```text
Read my lesson charter and objective map. Identify scope, evidence, content,
access, and delivery uncertainties. Do not silently resolve author decisions.
Propose the smallest complete capstone that preserves the target performance.
List required artifacts and a session budget based on actual earlier records,
not this draft's planning ceilings. Do not begin a large build yet.
```

Choose the scope and record your decision. Authorization to draft the book is not authorization for an agent to recruit learners, publish a product, or change an institutional course. Keep those boundaries explicit in the project brief.

> **RUN SLOT 15.1.** Save charter revision, scope decision, unresolved assumptions, planned budget, and actual authorization boundaries.

### Stage 2: Capture the Personal Baseline

Use the thin Chapter 1 request on your lesson with the documented initial context. Save the exact prompt and available tool/configuration information. Do not feed the final rules into the baseline and then describe it as unguided.

```text
Build the bounded baseline practice experience from the supplied lesson content.
Use only the stated initial context. Save exact prompts, scripts, responses,
snapshots, and screenshots. Do not repair it before the human scores it.
Do not invent outcomes if the build cannot run.
```

Score independently before reading the agent's self-evaluation. A disagreement is useful data about the rubric or the agent's inspection, not an inconvenience to remove. Preserve both verdicts with their evidence.

> **RUN SLOT 15.2.** Save the personal baseline, human and agent scores, discrepancies, and untestable checks. If there is no live baseline, the project cannot claim a measured before/after design improvement.

### Stage 3: Build Through Human Corrections

Apply the relevant chapters in dependency order: objective map, support, item contracts, feedback, review flow if needed, load, access, and evidence views. Not every lesson needs a persistent scheduler or instructor dashboard. An omitted feature is acceptable if the objective and delivery context do not require it. Record the reason rather than adding features to complete a checklist.

At each round, inspect the actual result, make or approve the human correction, and supply the reason. Keep reasons specific enough to guide later work. "Looks better" may be true, but it does not tell the next agent what learning obligation changed.

```text
Build the next authorized slice only. Read active constraints and relevant
component/rules versions first. State the objective and evidence this slice
serves. Save the script, inspect the result, and run supported checks before
recording. Stop on a constraint violation or missing critical requirement.
Do not manufacture a human reason or release.
```

> **RUN SLOT 15.3.** Save the actual round log, scripts, snapshots, screenshots, human reasons, check results, and request/cost ledger. The capstone should show selected failures and repairs, not only its final frame.

### Stage 4: Test Transfer to a Fresh Session

Compile the rules as Chapter 12 describes. Ask a fresh session to build one new item or state from the package alone. Keep the original work intact. Ask an independent reviewer to inspect the result with the allowed evidence and without editing it.

This test has a bounded purpose: can the contract travel beyond the conversation that produced it? It does not establish that every future agent will comply. A failure should identify missing context, ambiguous rules, ignored instructions, or insufficient checks where the evidence permits that diagnosis.

> **RUN SLOT 15.4.** Save the fresh-session input package, result, independent findings, false alarms or misses, and any rule revision. Keep reruns labelled; do not replace a failure silently with the best attempt.

### Stage 5: Obtain Human Evidence, or State the Dependency

If appropriate permissions and participants are available, run the Chapter 13 protocol and report actual observations and delayed responses. If not, deliver a test-ready prototype and a pending protocol. That is an incomplete learner-tested capstone, not a reason to create fictional results.

The title names the target outcome. Your portfolio status must name what actually exists. "Agent-built, design-reviewed, learner test pending" is a useful and honest project state. The author can then decide whether to proceed, reduce scope, or wait for participants.

> **RUN SLOT 15.5.** Save approved de-identified report, actual sample and delay, missingness, revisions, and limits; or explicitly record why learner testing remains pending.

### Stage 6: Handoff and Final Comparison

Build and test the Chapter 14 acceptance slice if the delivery route is authorized and available. Then rescore the final design using the same five baseline checks and the additional project rubric. Keep design-intent checks separate from runtime results.

| Check | Baseline | Final | Evidence/limit |
|---|---|---|---|
| Answer boundary | RUN | RUN | Tested paths or untested states |
| Explanatory feedback | RUN | RUN | Actual content and human review |
| Hint preserves work | RUN | RUN | Item-specific reasoning review |
| Task-relevant presentation | RUN | RUN | Objective/context diagnosis |
| Keyboard design intent | RUN | RUN | Annotation/focus-state evidence |
| Runtime access | Not inferred from canvas | RUN/not run | Actual environment and scope |
| Delayed learner evidence | RUN/not collected | RUN/not collected | No automatic causal inference |

A higher final design score supports a statement about the reviewed design under this rubric. It does not by itself support a learning-gain claim. A delayed observation can add human evidence while still leaving causation unresolved. Keep those conclusions in separate sentences.

> **RUN SLOT 15.6.** Save final comparison, acceptance results, actual total cost, unresolved blockers, and portfolio privacy review. No release or book gate is signed by the agent.

## The provenance this chapter adds

```json
{
  "chapter": 15,
  "lesson": "RUN: bounded personal lesson",
  "baseline": "RUN",
  "human_correction_history": "RUN",
  "fresh_session_test": "RUN",
  "learner_test": "RUN or pending",
  "handoff_slice": "RUN or not implemented",
  "final_claims_and_limits": "RUN",
  "human_signoff": "not-supplied-by-agent"
}
```

The capstone record makes it possible to inspect the work without relying on the author's retrospective confidence. It also shows where human judgment, rather than automatic production, changed the result.

## The check

**The machine half:** artifact presence, IDs, versions, captured constraints, test outputs, arithmetic, and flagged claim language. A complete folder is not a complete learning argument.

**The human half:** scope, content validity, meaningful support, appropriate participation, interpretation, authorship, and any release decision. These do not become machine judgments merely because the portfolio has a rubric.

**What neither proves:** a general advantage of all agentic design, universal rule reliability, or causal learning improvement. This is one documented project. Its value is inspectability and the quality of the reasoning it exposes.

## Exercises

**Warm-up**

1. *(Low; complete.)* Write the smallest capstone scope that includes a real performance and evidence path. Name one tempting feature you will omit and why.
2. *(Low; compare.)* Identify two ways a before/after comparison could become unfair. Specify the records needed to detect them.

**Application**

3. *(Medium; direct.)* Complete one full draw/correct/redraw cycle with a verbatim human reason and a preserved constraint.
4. *(Medium; compare.)* Score a baseline before repair and a final state under the same rubric. Report disagreements and cannot-determine cases.
5. *(Medium; defend.)* Prepare the portfolio manifest and label every artifact missing, specified, implemented, or evidenced.

**Synthesis**

6. *(High; defend.)* Write a one-page account of what improved, what did not, and which claims you cannot make. Link every factual claim to an artifact.
7. *(High; complete.)* Run a fresh-session build and independent review. Revise one rule from a real failure or report that the tested conditions produced no failure.

**Challenge**

8. *(Open; evaluate.)* Identify the finding that most threatens your preferred story about the project. Design the next test that would take it seriously rather than explain it away.

## What you can now do

You can carry a lesson from objective to an inspectable build and a bounded evidence report. You can explain which decisions the agent made, which you corrected, why the corrections matter, and what remains untested.

## Credit the AI

**Planned contribution:** bounded production, artifact management, checks, fresh-session construction, and review assistance. **Observed errors and actual cost:** RUN. **Verification:** actual artifacts, human reasons, permitted learner observations, and scoped runtime tests. The AI does not supply the author's judgment or fabricate missing evidence.

## After the Capstone

The lesson is not finished because the agent stopped drawing. It becomes defensible when its claims match its evidence and its unresolved questions are visible. Keep the rules that proved useful, revise those that did not, and let a later observation challenge a decision you currently like. That is the working craft this book is trying to teach.

---

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
