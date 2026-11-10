# === Stage 67: Add a function that returns key project metrics ===
# Project: FitnessJournal
def get_project_metrics(journal):
    """Return key project metrics for the FitnessJournal.

    journal is a dict with keys 'routines', 'sets', 'records', 'weeks'
    where 'routines' is a list, 'sets' is a list of dicts with 'routine',
    'exercise', 'weight', 'reps', 'date', 'records' is a list of dicts with
    'exercise' and 'value', and 'weeks' is a list of week-summary dicts.
    """
    routines = journal.get('routines', [])
    sets = journal.get('sets', [])
    records = journal.get('records', [])
    weeks = journal.get('weeks', [])

    routine_names = [r.get('name', r) for r in routines]
    total_exercises = len(routines)
    total_sets_logged = len(sets)

    routine_set_counts = {}
    for s in sets:
        name = s.get('routine')
        if name in routine_names:
            routine_set_counts[name] = routine_set_counts.get(name, 0) + 1

    def exercise_total(exercise):
        return sum(
            s.get('weight', 0) * s.get('reps', 0)
            for s in sets
            if s.get('exercise') == exercise
        )

    total_volume = sum(exercise_total(e) for e in routine_names)

    pr_exercises = [r.get('exercise') for r in records]
    unique_prs = sorted(set(pr_exercises))
    pr_count = len(unique_prs)

    prs_by_exercise = {}
    for rec in records:
        ex = rec.get('exercise')
        val = rec.get('value', 0)
        prs_by_exercise[ex] = max(prs_by_exercise.get(ex, val), val)

    week_summaries = [w for w in weeks if isinstance(w, dict)]
    week_count = len(week_summaries)
    best_week_volume = max(
        (w.get('volume', 0) for w in week_summaries), default=0
    )

    metrics = {
        'total_routines': total_exercises,
        'total_sets_logged': total_sets_logged,
        'routine_set_counts': routine_set_counts,
        'total_volume': total_volume,
        'personal_records_count': pr_count,
        'records_by_exercise': prs_by_exercise,
        'weeks_tracked': week_count,
        'best_week_volume': best_week_volume,
    }
    return metrics
