# === Stage 24: Add grouped summaries by category or status ===
# Project: FitnessJournal
def grouped_summaries(records, group_by="category"):
    groups = {}
    for r in records:
        key = getattr(r, group_by, "default")
        groups.setdefault(key, []).append(r)
    summaries = []
    for key, items in sorted(groups.items()):
        total_sets = sum(getattr(i, "total_sets", 0) for i in items)
        avg_reps = sum(getattr(i, "avg_reps", 0) for i in items) / max(len(items), 1)
        max_weight = max(getattr(i, "max_weight", 0) for i in items)
        summaries.append({
            "category": key,
            "count": len(items),
            "total_sets": total_sets,
            "avg_reps": round(avg_reps, 1),
            "max_weight": max_weight,
        })
    return summaries
