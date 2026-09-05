# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: FitnessJournal
import random

# In-memory state for FitnessJournal
workouts = []
records = {}
user = {"name": "Alex", "goals": ["strength", "endurance"]}

# Demo dataset
random.seed(42)
for day in range(5):
    date = f"2024-01-{day+1:02d}"
    routine = random.choice(["bench_press", "squats", "deadlift", "pull_ups", "pushups"])
    sets = random.randint(3, 5)
    reps = random.randint(8, 15)
    weight = random.randint(40, 100)
    workout = {"date": date, "routine": routine, "sets": sets, "reps": reps, "weight": weight}
    workouts.append(workout)
    key = (routine, reps)
    if key not in records:
        records[key] = workout["weight"]

# Quick summary
total_sets = sum(w["sets"] for w in workouts)
avg_weight = sum(w["weight"] for w in workouts) / len(workouts)
print(f"{user['name']}'s FitnessJournal: {len(workouts)} workouts, {total_sets} sets, avg weight {avg_weight:.0f}kg")
