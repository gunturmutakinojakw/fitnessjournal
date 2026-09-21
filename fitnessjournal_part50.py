# === Stage 50: Add unit tests for import and export behavior ===
# Project: FitnessJournal
import json, os, tempfile
from unittest import TestCase
from fitness_journal import FitnessJournal, Routine, Workout, Set, PersonalRecord


class TestImportExport(TestCase):
    def setUp(self):
        self.journal = FitnessJournal()
        self.routine = Routine("Push Day", ["Bench Press", "Shoulder Press"])
        self.workout = Workout("2024-01-15", self.routine, [
            Set("Bench Press", 10, 80, 1.0),
            Set("Bench Press", 8, 90, 1.0),
            Set("Shoulder Press", 10, 40, 1.0),
        ], PersonalRecord("Bench Press", 90))
        self.journal.add_workout(self.workout)

    def test_import_from_json(self):
        path = os.path.join(tempfile.gettempdir(), "test_import.json")
        data = self.journal.export()
        with open(path, "w") as f:
            json.dump(data, f)
        self.assertTrue(os.path.exists(path))

    def test_export_round_trip(self):
        exported = self.journal.export()
        self.assertEqual(len(exported["workouts"]), 1)
        self.assertEqual(exported["workouts"][0]["date"], "2024-01-15")
        self.assertEqual(exported["workouts"][0]["routine"]["name"], "Push Day")
        self.assertEqual(len(exported["workouts"][0]["sets"]), 3)
        self.assertEqual(exported["workouts"][0]["personal_records"][0]["exercise"], "Bench Press")
