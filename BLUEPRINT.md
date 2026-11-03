# Agentic Learning Experience Design with Figma
## Building Screens That Teach, Through the Figma MCP Server

**Working title:** Agentic Learning Experience Design with Figma — Building Screens That Teach, Through the Figma MCP Server
**Series:** Third volume alongside *Experience Design for EdTech* (`../learning-experience-design-lxd`) and *AI for Learning Experience Design* (`../ai-for-learning-experience-design`) [NEEDS HUMAN INPUT — Blueprint reasoning: the siblings say "Bear Brown & Company textbooks", the seeded README says "Bear Brown, LLC", and the Figma repos use "An independent series by Nik Bear Brown". Pick one series line and one publisher.]
**Author:** Nik Bear Brown
**Byline rule (inherited from `../figma-for-educational-ai/CLAUDE.md`):** an independent book, not affiliated with or endorsed by Figma. No Figma logo as a brand mark, and nothing styled to look like Figma's own material.
**Document:** Full TOC draft. Blueprint run in silent mode, written in the Teardown voice (`voices/teardown/VOICE.md`).
**Version:** 0.1
**Date:** 2026-11-03
**Status:** Pre-GATE 0. Nothing here is signed. Every `[NEEDS HUMAN INPUT]` is a decision only the author can make.
**Book directory:** `agentic-learning-experience-design-with-figma/`

---

## Document structure

1. Book Concept and Thesis
2. Learner Profile
3. Book Type and Deployment Specification
4. Field Positioning
5. Three-Act Learning Arc
6. Prerequisite Map
7. Assessment Structure
8. Chapter-by-Chapter TOC
9. Chapter Anatomy Template
10. Case Study Strategy
11. Hard Topics, Contested Claims, Aging Risk
12. Market Positioning
13. Feature List
14. Out of Scope
15. Adoption Risk Register
16. Open Questions

**Sources used for this draft.** Everything about what Figma and its MCP server can do comes from records in the sibling repos, not from memory:

- `../figma-for-educational-ai/CAPABILITIES.md` (checked against Figma's help pages 2026-09-26 and 2026-09-27)
- `../figma-for-educational-ai/experiments/log.csv` and `examples/`
- `../agentic-creative-direction/` (the checker-as-oracle pattern and the human-taste gate)
- `../brutalist-figma-claude/` (naming as an API contract, audits, token pipelines)
- `../learning-experience-design-lxd/BLUEPRINT.md` and `../ai-for-learning-experience-design/BLUEPRINT.md` (the learning science this book applies)

Every Figma fact in this file is a **lead for Phase 1 (Research)**, not a verified fact for this book. None has entered `facts/facts.json` yet. Figma changes monthly, and some of these rows are already six weeks old.

---

# PART 1 — BOOK CONCEPT AND THESIS

## Book concept summary

> This book teaches **agentic learning experience design: the capability to direct an AI agent, through the Figma MCP server, to build the screens of a learning experience (practice items, feedback, hints, worked examples that fade, review flows, progress views) so that the screens encode learning science instead of product-UX habits** — to **learning designers, instructional designers and educators who can already tell good learning design from bad but cannot yet build it at speed**, by **carrying one real lesson from learning objective to an agent-built, learner-tested Figma prototype, one MCP-driven build per chapter**. It fills the gap between the two Experience Design books (the learning science, deliberately tool-agnostic) and *Figma for Educational AI* (the Figma agent and MCP server in general, not learning design in particular). It succeeds if the reader can **hand an agent a learning objective and a learning-specific design system, get back a working prototype, and prove with a check and a learner that the screens make the learner do the thinking**.

**One-sentence logline:**
An agent will build you a beautiful quiz screen in ninety seconds. This book is about the five things it will get wrong, and how to make it stop.

## Central thesis

Here's what's actually happening when you ask an agent for "a quiz screen for chapter 3." It has seen far more product UI than learning UI. Product UI is optimized for one thing: the shortest path to task completion. Remove friction, show the answer, celebrate the click. Learning UI is often optimized for the opposite. Retrieval has to be effortful. The answer has to stay hidden until the learner commits. Support has to fade. Feedback has to explain, not just score. The LXD book calls this the engagement trap: what feels good and what teaches are separable.

So the thesis is:

"An agent building through the Figma MCP server defaults to product-UX patterns, because that is what its training and the default design systems reward. Learning design survives agentic production only when its rules live *inside the file the agent reads*: in component descriptions, variables and modes, annotations, and a rules file. The rules have to be checked by a machine and then by a learner. A learning designer's new craft is writing a design system the agent can't misuse."

**How I'll keep this honest.** The first half of the thesis, that agents default to product patterns, is a claim. It is not yet a finding. Chapter 1 tests it on a one-line prompt, in front of the reader, and reports what happened. If the agent gets it right, the chapter says so, and the thesis narrows to "you still need the rules to make it repeatable." [NEEDS HUMAN INPUT — Blueprint reasoning: decide now whether the book commits to the strong claim or the narrow one. The FEA repo has a measured precedent: film 07 ran component descriptions as agent rules in four conditions × 3 runs (`../figma-for-educational-ai/examples/film-07/`). Read its result before choosing.]

## Thesis test

The TOC reflects the thesis at every act:

- **Act One.** The reader watches the agent build a learning screen with no rules, tears it down against five learning-design checks, then learns how the agent actually reads a Figma file. The reader learns where rules can live before writing any. ✓
- **Act Two.** Every chapter builds one piece of a learning-specific design system (item types, feedback, fading, spacing, load, accessibility, progress), and each piece is written so the agent reads it. The reader can't finish a chapter without a rule the agent obeys and a check that catches it when it doesn't. ✓
- **Act Three.** The reader turns the pieces into a rules file and a review skill, then tests the prototype with learners for learning, not for pixel fidelity. The capstone is their own lesson, end to end. ✓

**Thesis test: PASS**, conditional on Chapter 1's experiment being run, not written from expectation.

---

# PART 2 — LEARNER PROFILE

## Primary reader

A working learning designer or instructional designer who has read, or could have written, the LXD book's argument. They know retrieval practice beats rereading. They know a hint ladder from a giveaway. What they lack is production speed: they hand a storyboard to a developer and wait three weeks, or they build in an authoring tool that can't express what they designed.

**Specific person:** [NEEDS HUMAN INPUT — Blueprint reasoning: the sibling books name a specific person (an MS student whose onboarding course "worked" by every metric except learning). This book needs its own. Is it a fellow at Humanitarians AI, a student in one of your Northeastern courses, a K-12 teacher? The answer moves the plan-tier decision in Part 3.]

**Secondary reader:** an engineer or product designer moving into EdTech, who can build fast but doesn't know why the learning screen should be slower than the product screen.

## Prior knowledge assumed

- The core learning-science vocabulary: retrieval practice, spacing, cognitive load, worked examples, feedback types, UDL. (This is Act One of the LXD book. This book cites it; it does not re-teach it.)
- Using a computer with confidence; never having opened a terminal is fine.
- Owning, or being able to get, a Figma account on the Education plan or a paid plan.

## Prior knowledge NOT assumed

- Figma beyond opening a file. Auto layout, components and variables are taught *when the agent needs them*, the same ordering as FEA (`PLAN.md`, "agent before basics").
- Claude Code or any CLI. Chapter 2 does the setup, and the AI+1 rule applies: the agent runs the commands.
- Programming. The agent writes the `use_figma` scripts; the reader learns to read and judge them.

## Prior misconceptions

1. **"The agent knows good learning design."** It knows good product design. Those disagree at exactly the points that matter: answer reveal, friction, feedback depth.
2. **"A prototype that looks right is right."** A learning screen is right when the learner does the thinking. You only find that out with a learner and a delayed check (Chapter 13).
3. **"Figma is for the visuals; the pedagogy lives in the storyboard."** In an agentic workflow, the agent reads only the file. A rule that lives only in a storyboard is a rule the agent never sees.
4. **"More MCP calls means more done."** On Education the server allows 200 calls a day and 10 a minute (FEA `CAPABILITIES.md`, 2026-09-26). A careless session burns a day's budget before lunch. Budgeting is part of the craft.
5. **"Light and dark are what modes are for."** Modes are a switch the agent can flip, and a support level is a switch too (Chapter 5).

## Motivation type

Utility, with a sharp edge: the reader is already being asked to "use AI" to produce course materials faster. They want speed without the engagement trap.

## Prerequisite map

| Prerequisite | Assumed? | Treatment |
|---|---|---|
| Learning-science vocabulary | Yes | Cited by chapter to the LXD book. A one-page "terms you'll need" box per chapter. |
| A Figma account with MCP access | Probably | Chapter 2, with the plan gates stated plainly |
| Claude Code installed | Probably | Chapter 2; the agent does the typing |
| Reading JavaScript | No | Taught by exposure: every `use_figma` script in the book is annotated line by line in Chapters 2–5 |
| A real lesson to redesign | Yes | Chosen in Chapter 4; it becomes the capstone |

Fewer than three hard "No" ratings, so no foundations chapter. Setup goes into Chapter 2.

---

# PART 3 — BOOK TYPE AND DEPLOYMENT SPECIFICATION

## Book type

A practitioner handbook built like a course: sequential chapters, each ending in a build the reader runs, with every chapter re-enterable as a task reference later ("how do I make a hint ladder the agent won't break?").

## Deployment specification

[NEEDS HUMAN INPUT — Blueprint reasoning: two defensible options.]

- **Option A, inferred from the siblings:** a 15-week graduate studio, the hands-on lab for *Experience Design for EdTech*. One chapter a week, with the LXD book's weekly topic matched to this book's build. The sibling TOCs use Weeks 1–15, and this TOC maps onto that calendar (Part 8). [INFERRED FROM: `../learning-experience-design-lxd/BLUEPRINT.md` Part 3]
- **Option B:** a self-paced handbook plus a workshop series, like FEA's 60–90 minute workshops (`../figma-for-educational-ai/workshops/`).

**Plan tier.** This decision changes every chapter.

| Tier | What it gets (per FEA `CAPABILITIES.md`, 2026-09-26) | Effect on this book |
|---|---|---|
| Higher-ed Education (Professional) | MCP server 200 calls/day; 3,000 AI credits/month; Figma agent; Make; one Site | Every chapter works |
| K-12 Education (Enterprise without AI) | MCP server yes; no Figma AI, Make or Sites | Core chapters work, because the MCP server runs on Claude's side, not Figma's credits. Chapter 14's Make section does not. |
| Paid Organization/Enterprise | Adds Code Connect and branching | Chapter 14 shows what these add; no chapter depends on them |

**Rule for every chapter:** tag it **all** or **HE**, and state the MCP call budget it was measured at. FEA already does this, and it's the only way a student can plan a week. The budgets get measured during drafting, not guessed now.

---

# PART 4 — FIELD POSITIONING

## The positioning statement, consolidated

The LXD books tell you what a learning screen should do and refuse to name a tool. Figma books tell you how to drive the tool and assume the screen's purpose is conversion or delight. This book is the join. It's the one place where "the answer stays hidden until the learner commits" is turned into a component description, a variable, a check and a learner test that an agent has to get through.

## Positioning by comparable

| Comparable | What it optimizes for | Where this book differs |
|---|---|---|
| *Experience Design for EdTech* (sibling) | Evidence discipline; tool-agnostic | This book is the build manual for its Act Two methods. It cites that book and doesn't re-argue it. |
| *AI for Learning Experience Design* (sibling) | AI *inside* the learning experience (tutors, guardrails) | This book is AI *building* the learning experience. Overlap: the tutor screens in Chapter 7 cite its guardrail patterns. |
| *Figma for Educational AI* (`../figma-for-educational-ai`) | Figma's AI and MCP for educators, engineers and non-designers | It teaches connection and the design basics (its modules 01–07). This book cites those and spends its pages on learning-specific components. |
| *Agentic Creative Direction* (`../agentic-creative-direction`) | Directing an agent to build brand and ad work | Same human-taste gate and checker-as-oracle pattern, applied to pedagogy instead of brand |
| *The Figma API* (`../brutalist-figma-claude`) | Getting design decisions out of Figma into production | Naming and audit chapters are reused. Its MCP chapter (13) is stale: see Part 11. |
| Commercial instructional-design and authoring-tool texts | [NEEDS HUMAN INPUT — Blueprint reasoning: no commercial comparables were researched for this draft. Phase 1 needs two or three named titles, such as an Articulate Storyline handbook or a general Figma-for-UX text, before the market claim in Part 12 can stand.] | |

---

# PART 5 — THREE-ACT LEARNING ARC

## The arc statement

The book takes the reader from *knowing what a good learning screen is* to *getting an agent to build one repeatably*. First the reader sees exactly how the agent fails without rules. Then they write the rules into the file one component at a time. Then they prove the result with a machine check and a learner.

## The pebble-in-the-pond opening

Chapter 1, page one. The reader types one sentence into Claude Code: "Build a five-question practice quiz for this lesson in my Figma file." They watch the canvas fill in. Then they score the result against five checks, one per learning-science principle:

1. Is the answer hidden until commit?
2. Does feedback explain?
3. Is there a hint that isn't the answer?
4. Is anything decorative competing for attention?
5. Does it work with a keyboard?

The whole book is the distance between that score and the capstone's score.

## Act One — Establish (Chapters 1–4, Weeks 1–4)

The reader sees the default and learns the machinery. By the end they know how the agent reads a frame (what `get_design_context` keeps and what it drops), where a rule can live so the agent sees it, and what learning objective their own screens serve.

## Act Two — Build (Chapters 5–11, Weeks 5–11)

This is the hard middle: the learning component library, one principle at a time. Each chapter ends with a component, a rule the agent reads and a check. The act's emotional center is Chapter 7 (feedback and hints). It's the first time the reader makes the agent *withhold* something, and every product-UX instinct pushes back.

## Act Three — Apply (Chapters 12–15, Weeks 12–15)

Integration. The rules become a rules file and a review skill, the prototype goes in front of learners, the design goes to a build, and the capstone redesigns the reader's own lesson under every rule at once.

## The studio thread across the arc

One lesson carries through the book.

- **The book's demonstration lesson (proposed):** one chapter of *Experience Design for EdTech* itself, Chapter 3, "The Cognitive Machinery: Load, Difficulty, and Durable Learning", turned into a practice unit. That dogfoods the series: the book teaching load is built under the load rules it teaches. [NEEDS HUMAN INPUT — Blueprint reasoning: FEA's running example is the Medhavy tutor study screen. Reusing it saves work but doubles the overlap. Using the LXD chapter keeps the books distinct. Your call.]
- **The reader's lesson:** chosen in Chapter 4 and rebuilt in Chapter 15.

---

# PART 6 — PREREQUISITE MAP

## The design system as upstream artifact

Every Act Two chapter adds to one Figma library file: the learning component library. Chapter 12 turns that library into a rules file. If a reader skips a chapter, the library has a hole, and the agent fills it with a product default. That's the dependency the reader will feel.

## Prerequisite chain

| Chapter | Needs |
|---|---|
| 1 | nothing (the agent is already connected in a lab, or Chapter 2 runs first; see Open Question 4) |
| 2 | a Figma account |
| 3 | 2 |
| 4 | 3 (the objective map is read back by `get_figjam`) |
| 5 | 3, 4 |
| 6 | 5 (item states are variables) |
| 7 | 6 |
| 8 | 6, 7 |
| 9 | 5, 6 |
| 10 | 6, 7, 9 |
| 11 | 4, 6 |
| 12 | 5–11 |
| 13 | any built prototype; best after 12 |
| 14 | 12 |
| 15 | all |

---

# PART 7 — ASSESSMENT STRUCTURE

The deliverable per chapter is a **build plus a check**. Every chapter's exercises include at least one Apply-level build in Figma through the agent, and one Evaluate-level critique of an agent-built screen.

| Assessment | Status | Applies to |
|---|---|---|
| Chapter build (a Figma file at an end state, link private by default) | needed | 2–15 |
| Teardown critique (score an agent's screen against the chapter's check and name the trade-off) | needed | 1, 3, 6–11 |
| Practice exercises (warm-up → challenge, per the Teardown `/write` structure) | needed | all |
| Chapter quizzes | desired | all |
| Flashcards / Anki | desired. The book about spacing should ship a spaced deck. | all |
| Learner test report | needed | 13, 15 |
| Capstone portfolio (lesson, library, rules file, test report) | needed | 15 |
| Canvas modules (`.imscc`) | [NEEDS HUMAN INPUT — needed only under Deployment Option A] | all |
| Certification rubric | out of scope here. FEA's draft `CERTIFICATION.md` covers Figma skill; this book could add a learning-design strand later. | — |

---

# PART 8 — CHAPTER-BY-CHAPTER TOC

15 chapters plus front and back matter, under the 18-chapter audit trigger.

Each chapter lists the MCP tools it leans on. The tool names come from Figma's saved tools page (`../figma-for-educational-ai/youtube/show-tell-what-a-day-costs/evidence/sources/tools-and-prompts.txt`, fetched 2026-09-27) and are re-checked in Phase 1. **Plan** tags are proposed; **budget** is measured at drafting.

## ACT ONE — ESTABLISH (Weeks 1–4)

### Chapter 1 — The Screen That Teaches Nothing
*What the agent builds when nobody tells it this is for learning.*

**Capability (DO):** critique an agent-built learning screen against five learning-design checks, and name which product-UX value each failure optimizes for.

**Outcomes:**
- Evaluate an agent-generated practice screen against the five Chapter 1 checks (Evaluate).
- Explain, for each failure, the product-UX goal it serves and the learning goal it costs (Understand).
- Predict which failures a one-line rule would fix and which need a component (Analyze).

**Opening case:** the one-sentence prompt, run live (the pebble, Part 5). The result is recorded as it happened, mistakes included. Nothing is staged.

**Machinery:** what happens between the prompt and the canvas. Claude plans, loads the `figma-use` skill, writes a `use_figma` script, and the script runs in your file with your sign-in. Why that last fact matters: the agent can edit anything you can, so work in a duplicate file (the sandbox pattern, FEA research notes).

**Design judgment:** the default screen is a philosophy, not an accident. It's what you get when the target is "done fast and feels good."

**Worked example:** the five-check teardown of the agent's quiz, item by item.

**Exercises:** (warm-up) score a provided agent-built screen; (application) run the prompt on your own content and score it; (synthesis) write one sentence of instruction that fixes the worst failure, rerun it, re-score, and report whether it held.

**Plan:** all · **Tools:** `use_figma`, `get_screenshot`

---

### Chapter 2 — Wiring the Agent to the Canvas
*Two hundred calls a day, and how not to spend them by lunch.*

**Capability:** connect Claude Code to the remote Figma MCP server, confirm the seat and tier the agent is acting under, and run a session against a call budget you planned.

**Outcomes:** configure the connection (Apply); interpret `whoami` output, including why Education shows as "Student tier" (Understand); plan a session ledger within 200 calls/day and 10/minute (Apply).

**Content blocks:**
1. Remote vs desktop server, and why this book uses remote: it runs on every seat and plan; the desktop server needs a paid Dev or Full seat (FEA `CAPABILITIES.md`).
2. The Claude Code plugin and the `figma-use` skill.
3. `whoami` first, every session (ACD rule).
4. The budget: which tools count against it and which don't (FEA's "what a day costs" film).
5. The sandbox duplicate and why branching isn't the answer on Education (not available on that plan).

**Cite, don't re-teach:** FEA modules 01–02.

**Worked example:** a full session ledger. Every call, what it cost, what it returned. FEA has per-call ledgers to model this on (`experiments/mcp-calls-*.csv`).

**Exercises:** connect and screenshot your `whoami`; budget a 20-call build before running it; post-mortem a session that blew its budget.

**Plan:** all · **Tools:** `whoami`, `create_new_file`, `get_screenshot`

---

### Chapter 3 — How the Agent Sees a Frame
*The agent reads your file, not your screen.*

**Capability:** predict what an agent will lose when it reads a frame, and restructure the frame so the learning intent survives the read.

**Outcomes:** compare `get_screenshot`, `get_metadata` and `get_design_context` output for the same frame (Analyze); explain why `get_design_context` returns React + Tailwind by default and what that implies (Understand); fix a frame so a second agent rebuilds it correctly (Apply).

**Machinery:** pixels vs structure. Layer names, auto layout and variables survive the read; visual grouping doesn't.

**Design judgment:** Figma optimized the MCP read for design-to-code handoff. That's why the output looks like a component tree for a web app, and why a learning rule has to be *in* the tree to survive.

**Where a rule can live (the chapter's map, used for the rest of the book):**

| Place | Survives the read? | Source |
|---|---|---|
| Layer and component names | yes | BFC ch4 "naming as an API contract" |
| Component descriptions | yes | FEA film-07 |
| Variables and modes | yes, via `get_variable_defs` | FEA film-06 |
| Annotations on frames and variants | yes. Dropped on component sets; FigJam refuses them. | FEA `CAPABILITIES.md`, 2026-09-27 |
| Comments, named versions, "Ready for dev" | not settable through MCP | same |
| A separate rules file | yes, if the agent is told to load it | Chapter 12 |

**Cite:** FEA module 03 and `examples/film-03/` (study card: screenshot vs design data).

**Exercises:** read one frame three ways and diff the results; rename a frame so a second agent's rebuild matches; find the annotation that vanished and explain why.

**Plan:** all · **Tools:** `get_metadata`, `get_design_context`, `get_screenshot`, `get_variable_defs`

---

### Chapter 4 — From Learning Objective to Screen Inventory
*Backward design, in a form the agent can read.*

**Capability:** turn a lesson's learning objectives into a screen inventory, where every screen names the evidence of learning it collects, and store it in a FigJam board the agent reads back correctly.

**Outcomes:** write objectives as observable performances (Apply); map each objective to the evidence a screen collects and the interaction that collects it (Analyze); structure a FigJam board so `get_figjam` returns it whole (Apply).

**Machinery:** a FigJam table reads back whole; a sticky returns only its first line (FEA `log.csv`). So the objective map is a table, not a wall of stickies, and a learning-design habit changes because of how the read works.

**Worked example:** the demonstration lesson's objectives → evidence → interaction → screens.

**Exercises:** inventory your own lesson; have the agent generate screens from the board and check that every screen traces to an objective; find a screen with no objective and cut it.

**Plan:** all · **Tools:** `get_figjam`, `use_figma` (FigJam), `generate_diagram`

---

## ACT TWO — BUILD (Weeks 5–11)

### Chapter 5 — Variables as Pedagogy: Support Levels as Modes
*Fading support is a switch, so make it one the agent can flip.*

**Capability:** build a variable collection whose modes are levels of instructional support (full worked example → partial → independent), and have the agent produce all three states of one screen from it.

**Outcomes:** explain the worked-example fading effect in design terms (Understand, cited to the LXD book); design a mode set for support levels (Create); verify each mode renders the intended support (Evaluate).

**Machinery:** what variable types and modes can hold, and what they can't. [Phase 1: verify which variable types (boolean, string, number, color) can drive layer visibility and text, and which need prototype logic.]

**Precedent to build on:** FEA E22/E23 built four tutor-uncertainty states from variables and a prototype in 13 calls and 0 credits (`examples/film-12/01-variables.js`, `02-component.js`, `03-prototype.js`).

**Design judgment:** using modes this way is a hack on a feature built for themes. The trade-off: one switch the agent understands, at the cost of a collection designers will find odd at first.

**Exercises:** add a fourth support level; have the agent build a new screen in all modes from one instruction; critique a fade that drops support too fast.

**Plan:** all

---

### Chapter 6 — Item Types the Agent Can't Break
*Question components whose descriptions are the rules.*

**Capability:** build a component set of assessment items (multiple choice, short answer, ordering, and one more of the reader's choice) whose descriptions state the item-writing rules, so the agent builds valid items from them.

**Outcomes:** write component descriptions as agent-readable rules (Create); apply item-writing rules (plausible distractors, no "all of the above", one correct key) through the agent (Apply); evaluate a batch of agent-built items against those rules (Evaluate).

**Precedent:** FEA film-07 (quiz-results screen; descriptions as agent rules, measured four conditions × 3 runs).

**Machinery:** component properties vs variants, and what `get_design_context` hands the next agent for each.

**Exercises:** write the description for a new item type; generate ten items and audit them; find the rule the agent broke and rewrite the description until it holds.

**Plan:** all · **Tools:** `use_figma`, `get_design_context`, `search_design_system`

---

### Chapter 7 — Feedback, Hints, and the Answer You Don't Show
*The first time you make the agent withhold something.*

**Capability:** prototype an item's full state machine (unanswered → committed → feedback → hint ladder → retry) so the answer stays hidden until commit and feedback explains instead of only scoring.

**Outcomes:** distinguish verification feedback from elaborated feedback and choose per objective (Analyze); build a hint ladder whose last rung still isn't the answer (Create); prototype the state machine with Figma's prototype logic (Apply).

**Design judgment:** every product instinct says show the answer. The trade-off named plainly: the learner's frustration in week one against retention in week four. The LXD book's desirable-difficulties chapter is the evidence; this chapter is the screen.

**Cross-reference:** the AI-tutor guardrail patterns in *AI for Learning Experience Design* when the hint comes from a model.

**Exercises:** build a three-rung hint ladder; have the agent add feedback to six items and grade whether it explains; red-team your own prototype for a path that leaks the answer.

**Plan:** all

---

### Chapter 8 — Retrieval and Spacing Flows
*Figma can draw the schedule. It can't run it.*

**Capability:** design and prototype a spaced-retrieval review flow (the states a learner sees on day 1, day 3 and day 10) and specify the scheduling logic as an annotation for whoever builds it.

**Outcomes:** explain spacing and retrieval in flow terms (Understand); prototype a multi-session flow (Apply); write a scheduling spec as annotations the next agent reads (Create).

**Honest limit:** a Figma prototype has no clock. The trade-off: prototype the states in Figma and annotate the logic, or build a working scheduler in Make. Make is HE-only, uses credits (FEA logged "about 30+" credits to change a font), and its Supabase backend gives key-value stores only. The chapter does both and compares them.

**Precedent:** FEA `examples/film-23/MAKE-BRIEF.md` (flashcard tool brief, not yet run). Running it is an opening.

**Exercises:** prototype a three-session flow; annotate the schedule; build the Make version and log its credit cost (HE).

**Plan:** all (Make section HE)

---

### Chapter 9 — Designing Under Cognitive Load
*Every decorative pixel is a claim on working memory.*

**Capability:** apply load rules (split attention, seductive details, reading level, minimum sizes, contrast in every mode) to agent-built screens, with an automated check that runs after every build.

**Outcomes:** identify load violations in an agent's screen (Analyze); encode load rules as tokens and descriptions (Create); run and interpret an automated check (Evaluate).

**Precedent:** ACD's `project/tools/design_check.py` checks contrast per mode, leading, minimum size, safe zones and overlaps. Adapt it for learning screens. FEA's `examples/film-24/SKILL.md` is a design-review skill to extend.

**Design judgment:** a machine can check contrast and size. It can't check whether the illustration is a seductive detail. Name which checks are machine-checkable and which stay human.

**Exercises:** run the check on Chapter 1's screen; fix it through the agent; write a load rule the check can't test and say how a human tests it.

**Plan:** all

---

### Chapter 10 — Accessible Learning Items
*An item a learner can't operate measures nothing.*

**Capability:** build assessment items that work with a keyboard and a screen reader, with alternatives for diagram-based items, and hand off the accessibility spec as annotations.

**Outcomes:** apply UDL and accessibility requirements to item design (Apply); annotate focus order, labels and alternatives (Create); evaluate what Figma can and can't verify about accessibility (Evaluate).

**Honest limit:** much of accessibility lives in the built code, not the canvas. The chapter separates what the file can carry (annotations, order, contrast per mode) from what only a build and a real screen reader can prove.

**Contested claim:** UDL's evidence base is contested (the LXD book's Risk 6). The chapter cites that and keeps the accessibility requirements, which stand on their own.

**Exercises:** annotate one item fully; have the agent build the high-contrast mode; list what still needs a test in the built version.

**Plan:** all

---

### Chapter 11 — Progress, Mastery, and the Dashboard Problem
*The easiest number to show is rarely the one that means learning.*

**Capability:** design a learner progress view and an instructor dashboard whose metrics are evidence of learning (mastery, retrieval success over time), not engagement (minutes, streaks), and annotate the data each element needs.

**Outcomes:** distinguish engagement metrics from learning evidence (Analyze, cited to the LXD book's thesis); design both views (Create); write the data spec as annotations [Phase 1: whether to frame it as xAPI statements].

**Design judgment:** streaks optimize for coming back, mastery views optimize for knowing what you know, and they can conflict.

**Exercises:** critique a streak-based progress screen; build a mastery view; annotate its data needs.

**Plan:** all

---

## ACT THREE — APPLY (Weeks 12–15)

### Chapter 12 — The Rules File: Teaching the Agent Your Learning Design System
*Everything the last seven chapters taught, in one place the agent always reads.*

**Capability:** compile the library's rules into a rules file and a review skill, so that a fresh agent with no chat history builds a compliant screen on the first try, and a second agent catches it when it doesn't.

**Outcomes:** generate and edit design-system rules (Create; Figma offers a `create_design_system_rules` prompt); write a review skill (Create); test the rules on a fresh session (Evaluate).

**Machinery:** why a rules file beats a long prompt: it's loaded every time, versioned, and reviewable.

**Precedent:** ACD's independent reviewer subagent (`.claude/agents/art-director-reviewer.md`) and its guard hook (`scripts/guard.py`); FEA's design-review skill.

**Exercises:** fresh-session test; adversarial prompt test (ask for a screen that breaks a rule); review-skill precision test (how many real violations it finds and how many false ones it raises).

**Plan:** all

---

### Chapter 13 — Testing With Learners, Not Pixels
*A prototype is a research instrument, so use it like one.*

**Capability:** run a small learner test on a Figma prototype that measures learning (a delayed retrieval check), not only usability, and report it honestly.

**Outcomes:** design a think-aloud plus a delayed check (Create); run it with three to five learners (Apply); report what the test can and can't show at that sample size (Evaluate).

**Opening:** FEA's protocol for the tutor-uncertainty states (`examples/film-22/PROTOCOL.md`) has been written and never run. This chapter runs a test like it and reports whatever happens.

**Rules:** no learner names or identifying data in the repo (FEA rule 6). Consent and institutional review are named as the reader's responsibility [NEEDS HUMAN INPUT — Blueprint reasoning: whether the book gives an IRB-exempt template, or only flags it, depends on deployment].

**Exercises:** write the protocol; run a pilot with one learner; revise the screen from what you saw, not from what the learner said they liked.

**Plan:** all

---

### Chapter 14 — Handoff: Code, Make, and the LMS
*Where the prototype stops and the product starts.*

**Capability:** choose a build path for a learning prototype (code from `get_design_context`, a Make app, or an LMS build) and hand it off with the rules intact.

**Outcomes:** compare the three paths on cost, plan tier and fidelity to the learning rules (Evaluate); produce a handoff package (Create).

**Honest limits, per FEA `CAPABILITIES.md`:** Code Connect and branching are not on Education, so the chapter shows what they add without depending on them. Make's GitHub flow is partly verified (film 23).

**Phase 1 research:** the LMS constraints (embedding, LTI, what a Canvas page can host) are not in any sibling repo and need sourcing.

**Exercises:** generate code for one screen and check that the rules survived; write a Make brief; list what an LMS build would lose.

**Plan:** all (Make HE)

---

### Chapter 15 — Capstone: One Lesson, Agent-Built, Learner-Tested
*Every rule at once, on your lesson.*

**Capability:** redesign the reader's own lesson end to end. Objectives → screen inventory → library → agent build → automated check → learner test → handoff. Report the Chapter 1 score against the final score.

**Deliverable:** the capstone portfolio (Part 7).

**Plan:** all

---

## Front and back matter

- **Front matter:** what this book is and isn't; the independent-book notice; how to read it alongside the two LXD volumes; the plan-tier table.
- **Appendix A:** the learning component library (the reference card for every component built).
- **Appendix B:** the call-budget ledger template.
- **Appendix C:** the MCP tool reference *as of the check date*, with the date on every row.
- **Appendix D:** the rules file, complete.

---

# PART 9 — CHAPTER ANATOMY TEMPLATE

Each chapter follows the Teardown `/write` structure (`voices/teardown/VOICE.md`), adapted to a build:

1. **Opening (400–600 words).** A real agent output and the problem it exposes, then objectives (action verbs), prerequisites and plan tag.
2. **The machinery.** What the MCP tools actually do here, from first principles. Every `use_figma` script shown is annotated.
3. **The design judgment.** What the default optimizes for, what the learning version optimizes for, and the trade-off named.
4. **The build.** Step by step through the agent: prompt, the agent's script, the result, *what the agent got wrong*, the fix.
5. **The check.** Machine check first, then the human check, and what each can't see.
6. **Graduated exercises.** Warm-up → application → synthesis → challenge, each naming its objective.
7. **Summary as capabilities.**
8. **Credit the AI.** What the agent did, what it got wrong, how the reader can check (FEA rule 8).
9. **Budget line.** MCP calls and AI credits the chapter's build used, as measured.

---

# PART 10 — CASE STUDY STRATEGY

## Coverage map

| Context | Chapters |
|---|---|
| Higher-ed course practice | 1, 4–8, 15 |
| AI tutor screens | 7 (cross-ref sibling), 11 |
| K-12 | [NEEDS HUMAN INPUT — Blueprint reasoning: K-12 learners have no Figma AI. If K-12 is in scope, one case per act should be a K-12 lesson built with the MCP server only.] |
| Corporate / workforce training | [NEEDS HUMAN INPUT] |

## Worked example format

Every worked example is a real run with a real agent output, recorded on the date it happened, including the failures. No reconstructed or idealized transcripts. A rerun that behaves differently is reported as a difference, not quietly replaced.

## Failure-case requirement

Every chapter shows at least one agent failure and its fix. The book's argument is the failures.

## Sourcing requirement

Figma capabilities: Figma's own help and developer pages, with fetch date. Learning science: cited through the sibling LXD books' sources, then checked at the primary source in Phase 4. No Figma feature described from memory (FEA rule 2).

---

# PART 11 — HARD TOPICS, CONTESTED CLAIMS, AGING RISK

## Contested claims

| Claim | Status | Handling |
|---|---|---|
| Agents default to product-UX patterns | Untested hypothesis | Chapter 1 tests it live; thesis narrows if it fails |
| Component descriptions steer agents reliably | Partly measured (FEA film-07) | Report FEA's measured result; replicate on learning items |
| UDL evidence base | Contested (LXD Risk 6) | Cite; keep accessibility requirements independent of it |
| "MCP calls don't use AI credits" | Cut as unsourced in FEA | Do not state until sourced |

## Hard chapters

- **Chapter 5.** Bending modes into support levels may hit limits in what variables can control. Phase 1 must confirm before drafting.
- **Chapter 8.** The honest answer may be "Figma isn't the tool for the logic", and the chapter has to say so without breaking the book's frame.
- **Chapter 13.** It depends on access to real learners.

## Aging risk

The highest in the series. The MCP server, its tool list, rate limits, the write beta ("free in beta… will become usage-based"), and Make/Weave/agent plan gating all changed within the six weeks the FEA records cover. Known stale material already: BFC Chapter 13 says the server "requires Dev Mode" and describes a local port-3845 server, which conflicts with the remote server being open on all seats. **Mitigations:**

- Date every tool claim.
- Keep tool specifics in Appendix C, so chapters teach the pattern ("where a rule can live") and survive renames.
- Re-check every Figma row at GATE 4.

---

# PART 12 — MARKET POSITIONING SUMMARY

[NEEDS HUMAN INPUT — Blueprint reasoning: no market research was done for this draft. What is established: the sibling series gives a built-in course pairing, and FEA's relationship with Figma's Education team (`../figma-for-educational-ai/FIGMA-RELATIONSHIP.md`) is a possible review channel. Sending anything to Figma is the author's decision. Audience size, price and comparables need Phase 1.]

---

# PART 13 — FEATURE LIST SUMMARY

| Feature | Priority |
|---|---|
| A learning component library file the reader can duplicate | must |
| Every build reproducible from annotated `use_figma` scripts in `examples/` | must |
| Plan tag and measured call budget per chapter | must |
| Rules file and review skill (Chapter 12) | must |
| Anki deck | should |
| Workshop kits per chapter (FEA format) | could |
| Videos | [NEEDS HUMAN INPUT — FEA already has a playlist; extend it or keep this book text-only?] |
| Canvas `.imscc` | depends on deployment |

---

# PART 14 — OUT OF SCOPE

- Teaching learning science from scratch (the LXD books do this).
- Figma fundamentals for their own sake (FEA modules 01–07).
- The Figma REST/Plugin API pipeline (BFC).
- Building the AI tutor itself (*AI for Learning Experience Design*).
- Authoring tools other than Figma (Storyline, Rise) except as a comparison in Chapter 14.
- Code Connect and branching as dependencies (not on Education).
- Publishing to Figma Community, Sites or YouTube. That's always the author's hand.

---

# PART 15 — ADOPTION RISK REGISTER

| # | Risk | Mitigation |
|---|---|---|
| 1 | Figma changes the MCP server mid-course and a chapter breaks | Dated Appendix C; teach patterns over tool names; GATE 4 re-check |
| 2 | Readers on K-12 or free plans hit gates | Plan tags; every core chapter works on MCP alone |
| 3 | Overlap with FEA makes this read as a repeat | Cite FEA's modules 01–07 instead of re-teaching them; different running example (Open Question 2) |
| 4 | Rate limits make a class lab impossible (200/day per person) | Measured budgets; batch calls; FEA's workshop ran at 6 calls per student |
| 5 | The core hypothesis (Chapter 1) doesn't hold | Narrow thesis already written (Part 1) |

---

# PART 16 — OPEN QUESTIONS

1. **Byline, series line and publisher** (Part 0 header).
2. **Running example:** the LXD Chapter 3 lesson (proposed) or FEA's Medhavy tutor screen?
3. **Deployment:** 15-week studio paired with the LXD course, or self-paced handbook plus workshops?
4. **Chapter 1 vs 2 order:** a reader can't run Chapter 1's live prompt before connecting. Either Chapter 1 uses a provided recording and the reader reruns it after Chapter 2, or setup moves first. Blueprint recommends the recording: the failure is the hook.
5. **Strong or narrow thesis** (Part 1), after reading FEA film-07's result.
6. **K-12 in scope?**
7. **Videos:** extend FEA's playlist, or none?
8. **Specific reader** (Part 2).
9. **Commercial comparables and market** (Parts 4, 12).
10. **The LXD book:** it lists Figma under "Prior knowledge NOT assumed… taught tool-agnostically" (`../learning-experience-design-lxd/BLUEPRINT.md:122`). Keep that line as it is, or point it at this book as the hands-on companion?

---

## GATE 0 — not signed

Per `conductor/00-blueprint/blueprint.md`:

- [ ] Every `[NEEDS HUMAN INPUT]` above is resolved.
- [ ] The chapter order does real work (Part 6).
- [ ] The assessment plan is stated (Part 7).
- [ ] The author has read this file and agrees it's the right book.

Next, after sign-off: `/scaffold` splits this file into `vision.md`, `architecture.md`, `chapters-spec.md` and `risks.md`, and Phase 1 (Research) starts with re-verifying every Figma fact listed here.
