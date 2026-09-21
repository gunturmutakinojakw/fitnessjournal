# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: FitnessJournal
import unittest


class TestCreationHelpers(unittest.TestCase):
    def test_create_routine(self):
        from fitness_journal.core import Routine
        r = Routine(name="Push Day", exercises=[
            {"name": "Bench Press", "sets": [5, 5, 5, 5, 5]}
        ])
        self.assertEqual(r.name, "Push Day")
        self.assertEqual(len(r.exercises), 1)

    def test_validate_routine(self):
        from fitness_journal.core import Routine
        r = Routine(name="Test", exercises=[
            {"name": "X", "sets": [1, 2, 3]}
        ])
        self.assertTrue(r.validate())

    def test_validate_fail(self):
        from fitness_journal.core import Routine
        r = Routine(name="Bad", exercises=[
            {"name": "X", "sets": [1, 2, "three"]},
        ])
        self.assertFalse(r.validate())

    def test_create_set(self):
        from fitness_journal.core import Set
        s = Set(weight=10, reps=5)
        self.assertEqual(s.weight, 10)
        self.assertEqual(s.reps, 5)

    def test_validate_set(self):
        from fitness_journal.core import Set
        s = Set(weight=10, reps=5)
        self.assertTrue(s.validate())

    def test_validate_set_fail(self):
        from fitness_journal.core import Set
        s = Set(weight=10, reps=-1)
        self.assertFalse(s.validate())


if __name__ == "__main__":
    unittest.main()
