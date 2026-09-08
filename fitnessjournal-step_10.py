# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: FitnessJournal
def search_workouts(query, workouts=None):
    """Case-insensitive search across title, notes, and date strings."""
    if workouts is None:
        workouts = list(g_workouts.values())
    lowered = query.strip().lower()
    matches = []
    for uid, w in workouts:
        parts = [w["title"], w.get("notes", ""), w.get("date", "")]
        if any(lowered in p for p in parts):
            matches.append(w)
    return matches
