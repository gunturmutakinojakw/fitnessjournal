# === Stage 25: Add daily summary calculations ===
# Project: FitnessJournal
def daily_summary(records, date=None):
    """Return a dict of daily stats: total sets, total volume, exercises done."""
    if date is None:
        date = today()
    daily = {}
    for r in records:
        if r.date == date:
            sets = sum(set.count for set in r.sets)
            exercises = set(exercise.name for exercise in r.sets)
            if exercises:
                volume = sum(exercise.total_volume for exercise in r.sets)
                daily[date] = {
                    'total_sets': sets,
                    'total_volume': volume,
                    'exercises': len(exercises),
                    'exercises_done': exercises,
                }
    return daily
