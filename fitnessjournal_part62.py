# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: FitnessJournal
def recommend_next(exercises, history):
    """Exercises: list of dicts with keys 'name' and 'last_date'.
    history: dict mapping exercise name to a list of recent weights (last first)."""
    today = "2024-06-01"
    scores = {}
    for ex in exercises:
        name = ex["name"]
        last = ex["last_date"]
        days_since = (today - last).days
        recent = history.get(name, [])
        last_weight = recent[0] if recent else 0
        if days_since <= 3:
            priority = "skip"
        elif days_since <= 7:
            priority = "low"
        elif days_since <= 14:
            priority = "medium"
        else:
            priority = "high"
        if recent and last_weight > 0:
            added = 2 * (last_weight / 100.0)
        else:
            added = 0
        scores[name] = (priority, days_since, added)
    ranked = sorted(scores.values(), key=lambda x: (x[0], x[1], x[2]), reverse=True)
    order = [name for _, _, _ in ranked]
    return order
