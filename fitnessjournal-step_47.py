# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: FitnessJournal
def demo():
    routines = {
        "Push Day": ["Bench Press", "Overhead Press", "Tricep Dips"],
        "Pull Day": ["Deadlift", "Bent Over Row", "Pull Ups"],
    }
    records = {
        "Bench Press": 115,
        "Overhead Press": 75,
        "Deadlift": 275,
    }
    weekly_log = {
        "Push Day": [
            {"exercise": "Bench Press", "sets": [85, 90, 95]},
            {"exercise": "Overhead Press", "sets": [60, 65, 65]},
        ],
        "Pull Day": [
            {"exercise": "Deadlift", "sets": [225, 245, 265]},
            {"exercise": "Bent Over Row", "sets": [90, 95, 100]},
        ],
    }
    print("Welcome to FitnessJournal!")
    print(f"Active routines: {list(routines.keys())}")
    print(f"Personal records: {records}")
    print(f"Recent weekly sessions: {list(weekly_log.keys())}")
    for day, sessions in weekly_log.items():
        for s in sessions:
            max_set = max(s["sets"])
            pr = records.get(s["exercise"], 0)
            status = "NEW PR!" if max_set > pr else "within range"
            print(f"  {day} -> {s['exercise']}: {s['sets']} ({status})")
