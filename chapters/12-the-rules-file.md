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
