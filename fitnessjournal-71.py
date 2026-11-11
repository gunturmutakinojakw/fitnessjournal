# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: FitnessJournal
import datetime


def seed_demo_data(journal, seed=42):
    rng = random.Random(seed)
    today = datetime.date.today()
    routines = [
        Routine("Push Day", ["Bench Press", "Shoulder Press", "Triceps"]),
        Routine("Pull Day", ["Deadlift", "Row", "Biceps"]),
        Routine("Leg Day", ["Squat", "Lunge", "Calf Raise"]),
    ]
    for routine in routines:
        journal.add_routine(*routine)
    for day_offset in range(-13, 7):
        day = today + datetime.timedelta(days=day_offset)
        if day.weekday() >= 5:
            continue
        routine_name = routines[day.weekday() % len(routines)].name
        routine = next(r for r in routines if r.name == routine_name)
        for rep in range(rng.randint(3, 6)):
            sets = [
                ExerciseSet(
                    date=day,
                    exercise=routine.exercises[rep % len(routine.exercises)],
                    reps=rng.randint(5, 20),
                    weight=rng.randint(20, 120),
                )
                for _ in range(rng.randint(3, 5))
            ]
            journal.add_sets(*sets)
    for set_record in journal.all_sets():
        journal.record_pr(*set_record)
    return routines
