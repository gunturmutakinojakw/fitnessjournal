# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: FitnessJournal
def get_weekly_summary(records: list[dict]) -> dict:
    """Return a dictionary with weekly workout statistics.

    Args:
        records: a list of workout records, each containing
            'date', 'routine', 'sets', and optionally 'weight',
            'reps', or 'duration'.

    Returns:
        A dictionary with keys:
            'total_workouts', 'total_sets', 'total_weight',
            'total_reps', 'total_duration', 'week_start', 'week_end'.
    """
    if not records:
        return {
            'total_workouts': 0,
            'total_sets': 0,
            'total_weight': 0.0,
            'total_reps': 0,
            'total_duration': 0.0,
            'week_start': None,
            'week_end': None,
        }
    week_start = min(r['date'] for r in records)
    week_end = max(r['date'] for r in records)
    total_workouts = len(records)
    total_sets = sum(r.get('sets', 0) for r in records)
    total_weight = sum(r.get('weight', 0.0) for r in records)
    total_reps = sum(r.get('reps', 0) for r in records)
    total_duration = sum(r.get('duration', 0.0) for r in records)
    return {
        'total_workouts': total_workouts,
        'total_sets': total_sets,
        'total_weight': round(total_weight, 1),
        'total_reps': total_reps,
        'total_duration': round(total_duration, 1),
        'week_start': week_start,
        'week_end': week_end,
    }
