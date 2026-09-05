# === Stage 4: Implement create operations for the primary records ===
# Project: FitnessJournal
def add_set(routine, exercise, date, weight, reps, notes=""):
    """Add a single exercise set to a routine on a given date."""
    if routine not in _routines:
        _routines[routine] = {}
    if exercise not in _routines[routine]:
        _routines[routine][exercise] = []
    _routines[routine][exercise].append({
        "date": date,
        "weight": weight,
        "reps": reps,
        "notes": notes,
    })
    _save()
    return _routines[routine][exercise][-1]
