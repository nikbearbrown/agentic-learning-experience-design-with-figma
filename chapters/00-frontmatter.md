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
