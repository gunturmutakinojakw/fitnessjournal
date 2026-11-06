# === Stage 64: Add validation for relationship references ===
# Project: FitnessJournal
def validate_references(data):
    routines = {r["id"]: r for r in data.get("routines", [])}
    workouts = {w["id"]: w for w in data.get("workouts", [])}
    sets = {s["id"]: s for s in data.get("sets", [])}
    messages = data.get("errors", [])
    seen = {}

    for w in data.get("workouts", []):
        if w.get("routine_id") not in routines:
            key = ("workout", w.get("id"))
            if key not in seen:
                seen[key] = "routine_id does not reference a known routine"
                messages.append(seen[key])
        for s in w.get("sets", []):
            if s.get("workout_id") != w.get("id"):
                messages.append("set workout_id does not match its parent workout")
            if s.get("exercise_id") not in routines:
                key = ("set", s.get("id"))
                if key not in seen:
                    seen[key] = "exercise_id does not reference a known routine"
                    messages.append(seen[key])

    for p in data.get("personal_records", []):
        if p.get("exercise_id") not in routines:
            key = ("personal_record", p.get("id"))
            if key not in seen:
                seen[key] = "exercise_id does not reference a known routine"
                messages.append(seen[key])
        if p.get("workout_id") not in workouts:
            key = ("personal_record", p.get("id"))
            if key not in seen:
                seen[key] = "workout_id does not reference a known workout"
                messages.append(seen[key])
        if p.get("set_id") not in sets:
            key = ("personal_record", p.get("id"))
            if key not in seen:
                seen[key] = "set_id does not reference a known set"
                messages.append(seen[key])

    if not messages:
        return True, []
    return False, messages
