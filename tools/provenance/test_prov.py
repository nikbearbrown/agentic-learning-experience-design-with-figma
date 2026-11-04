#!/usr/bin/env python3
"""test_prov.py: checks prov.py against fixture snapshots of one practice item.

The story in fixtures/: the agent draws an item (r1); the human hides the answer, moves the hint
button up and rewrites the feedback (r2); then the agent redraws twice, once undoing the hidden
answer (r3-agent-reverts) and once keeping every correction (r3-agent-keeps).
Nothing touches Figma. Run: python3 -I tools/provenance/test_prov.py
"""
import json, os, shutil, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
PROV = os.path.join(HERE, "prov.py")
FIX = os.path.join(HERE, "fixtures")


def run(*args, cwd):
    return subprocess.run([sys.executable, "-I", PROV, *args], cwd=cwd, capture_output=True, text=True)


class ProvenanceLoop(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.d, "snapshots"))
        for f in os.listdir(FIX):
            shutil.copy(os.path.join(FIX, f), os.path.join(self.d, "snapshots", f))
        r = run("init", "--project", "test", "--lesson", "LXD Ch 3 practice unit", "--file-ref", "practice-unit",
                cwd=self.d)
        self.assertEqual(r.returncode, 0, r.stderr)

    def tearDown(self):
        shutil.rmtree(self.d)

    def ledger(self):
        with open(os.path.join(self.d, "provenance.json")) as f:
            return json.load(f)

    def record_r1_r2(self):
        r = run("record", "--actor", "agent", "--snapshot", "snapshots/r1-agent.json", "--intent", "first draw",
                "--prompt", "Build a practice item for this lesson.", "--calls", "3", cwd=self.d)
        self.assertEqual(r.returncode, 0, r.stderr)
        r = run("record", "--actor", "human", "--snapshot", "snapshots/r2-human.json", "--intent", "correct the draw",
                "--why", "The answer was on screen before the learner tried. Feedback has to explain.", cwd=self.d)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_diff_sees_the_human_edits_and_ignores_stamp_churn(self):
        r = run("diff", "snapshots/r1-agent.json", "snapshots/r2-human.json", "--json", cwd=self.d)
        kinds = sorted((c["name"], c["change"]) for c in json.loads(r.stdout))
        self.assertEqual(kinds, [("Answer", "visible"), ("Feedback", "text"), ("Hint button", "moved")])

    def test_subpixel_change_is_not_a_move(self):
        r = run("diff", "snapshots/r2-human.json", "snapshots/r3-agent-keeps.json", "--json", cwd=self.d)
        kinds = [(c["name"], c["change"]) for c in json.loads(r.stdout)]
        self.assertEqual(kinds, [("Commit button", "added")])

    def test_human_round_needs_a_why(self):
        run("record", "--actor", "agent", "--snapshot", "snapshots/r1-agent.json", "--intent", "draw", cwd=self.d)
        r = run("record", "--actor", "human", "--snapshot", "snapshots/r2-human.json", "--intent", "fix", cwd=self.d)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("--why", r.stderr)
        self.assertEqual(len(self.ledger()["rounds"]), 1)

    def test_human_edits_become_constraints(self):
        self.record_r1_r2()
        cons = {(c["name"], c["property"]) for c in self.ledger()["constraints"]}
        self.assertEqual(cons, {("Answer", "visible"), ("Feedback", "text"), ("Hint button", "position")})

    def test_agent_revert_is_caught_and_refused(self):
        self.record_r1_r2()
        r = run("check-constraints", "snapshots/r3-agent-reverts.json", cwd=self.d)
        self.assertEqual(r.returncode, 1)
        self.assertIn("Answer", r.stdout)
        r = run("record", "--actor", "agent", "--snapshot", "snapshots/r3-agent-reverts.json", "--intent", "redraw",
                cwd=self.d)
        self.assertEqual(r.returncode, 2)
        self.assertEqual(len(self.ledger()["rounds"]), 2)

    def test_override_needs_the_humans_words_and_is_kept(self):
        self.record_r1_r2()
        r = run("record", "--actor", "agent", "--snapshot", "snapshots/r3-agent-reverts.json", "--intent", "redraw",
                "--override-why", "Show the answer on this one; it's a worked example, not a test.", cwd=self.d)
        self.assertEqual(r.returncode, 0, r.stderr)
        last = self.ledger()["rounds"][-1]
        self.assertEqual(len(last["violations_overridden"]), 1)
        self.assertTrue(last["override_why"])

    def test_agent_round_that_keeps_corrections_records(self):
        self.record_r1_r2()
        r = run("record", "--actor", "agent", "--snapshot", "snapshots/r3-agent-keeps.json", "--intent", "add commit",
                "--check", "answer-hidden-until-commit=pass", "--check", "keyboard=not-run", cwd=self.d)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(run("validate", cwd=self.d).returncode, 0)

    def test_release_lets_a_constraint_go(self):
        self.record_r1_r2()
        cid = next(c["id"] for c in self.ledger()["constraints"] if c["name"] == "Answer")
        r = run("record", "--actor", "human", "--snapshot", "snapshots/r2-human.json", "--intent", "release",
                "--release", cid, "--why", "This screen is now the worked example.", "--free", cwd=self.d)
        self.assertEqual(r.returncode, 0, r.stderr)
        r = run("check-constraints", "snapshots/r3-agent-reverts.json", cwd=self.d)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_log_and_stamp(self):
        self.record_r1_r2()
        log = run("log", cwd=self.d).stdout
        self.assertIn("| r2 | human |", log)
        stamp = run("stamp-text", cwd=self.d).stdout.strip()
        self.assertTrue(stamp.startswith("Provenance · r2 · human ·"), stamp)
        self.assertIn("3 human corrections held", stamp)

    def test_validate_rejects_a_broken_ledger(self):
        self.record_r1_r2()
        data = self.ledger()
        data["rounds"][1]["why"] = ""
        data["rounds"][0]["actor"] = "robot"
        with open(os.path.join(self.d, "provenance.json"), "w") as f:
            json.dump(data, f)
        r = run("validate", cwd=self.d)
        self.assertEqual(r.returncode, 1)
        self.assertIn("robot", r.stdout)
        self.assertIn("needs the human's 'why'", r.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
