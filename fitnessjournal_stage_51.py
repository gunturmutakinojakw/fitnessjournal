# === Stage 51: Add unit tests for search and filter behavior ===
# Project: FitnessJournal
import sys
sys.path.insert(0, '..')
from fitness_journal import WorkoutJournal

journal = WorkoutJournal()

# --- Search tests ---
journal.add_workout("Push Day", "2024-01-01", {"bench press": {"sets": [5, 5, 3], "weight": [80, 80, 80]}}, {"bench press": 80})
journal.add_workout("Pull Day", "2024-01-02", {"rows": {"sets": [4, 4], "weight": [60, 60]}}, {"rows": 60})
journal.add_workout("Push Day", "2024-01-03", {"bench press": {"sets": [5, 5, 5], "weight": [85, 85, 85]}}, {"bench press": 85})

# Search by date
results = journal.search_workouts("2024-01-01")
assert len(results) == 1 and results[0].name == "Push Day"

# Search by exercise
results = journal.search_workouts(exercise="bench press")
assert len(results) == 2

# Search by date range
results = journal.search_workouts(start="2024-01-01", end="2024-01-02")
assert len(results) == 2

# Search by muscle group
results = journal.search_workouts(muscle="chest")
assert len(results) == 2

# --- Filter tests ---
# Filter by minimum reps
results = journal.filter_workouts(min_reps=10)
assert len(results) == 3

# Filter by maximum weight
results = journal.filter_workouts(max_weight=70)
assert len(results) == 0

# Filter by minimum weight
results = journal.filter_workouts(min_weight=80)
assert len(results) == 3

# Filter by workout name
results = journal.filter_workouts(name="Push Day")
assert len(results) == 2

# Filter by date range
results = journal.filter_workouts(start="2024-01-01", end="2024-01-02")
assert len(results) == 2

print("All search and filter tests passed.")
