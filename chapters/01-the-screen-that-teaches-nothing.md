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

That loop has a problem Figma can't solve on its own. Through the MCP server, the agent can't name a version or post a comment. Figma's version history credits every agent edit to you, the signed-in user. In Figma's own record, you and the agent are the same person (FEA `CAPABILITIES.md` and `examples/frictional-version-log/`, checked 2026-09-27 `[VERIFY]`). So the book keeps its own record: a file called `provenance.json`, plus a snapshot of the screen at the end of every round. Figma carries one pointer to it, a single annotation on each frame that says which round it's on. [PROVENANCE.md](../PROVENANCE.md) is the full method. In this chapter you'll see it work once, end to end, before Chapter 2 explains the machinery.

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
