# === Stage 14: Add file load support with fallback demo data ===
# Project: FitnessJournal
def load_journal(path="fitness_journal.json"):
    """Load workout data from JSON file; fall back to built-in demo data."""
    DEFAULT_DATA = {
        "routines": [
            {"id": 1, "name": "Push Day", "exercises": ["Bench Press", "Tricep Dips", "Overhead Press"], "sets": [3, 3, 3], "reps": [10, 10, 10], "weights": [60, 40, 30]},
            {"id": 2, "name": "Pull Day", "exercises": ["Bent Over Row", "Pull-ups", "Barbell Curl"], "sets": [3, 3, 3], "reps": [10, 10, 10], "weights": [50, 40, 25]},
        ],
        "records": [
            {"exercise": "Bench Press", "weight": 60, "date": "2025-06-01"},
            {"exercise": "Pull-ups", "weight": 40, "date": "2025-06-03"},
        ],
        "history": [
            {"routine_id": 1, "date": "2025-06-01", "sets_completed": 3, "total_kg": 150},
            {"routine_id": 2, "date": "2025-06-03", "sets_completed": 3, "total_kg": 115},
        ],
        "weekly_summary": {
            "week": "2025-W23",
            "total_workouts": 2,
            "total_sets": 6,
            "total_kg": 265,
        },
    }
    try:
        import json
        with open(path, "r") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_DATA
