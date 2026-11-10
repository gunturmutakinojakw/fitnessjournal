# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: FitnessJournal
def reset_demo_data(journal):
    journal['routines'] = [
        {'id': 1, 'name': 'Push Day', 'exercises': ['Bench Press', 'Shoulder Press', 'Triceps']},
        {'id': 2, 'name': 'Pull Day', 'exercises': ['Deadlift', 'Rows', 'Biceps']},
        {'id': 3, 'name': 'Leg Day', 'exercises': ['Squat', 'Lunges', 'Calves']},
    ]
    today = datetime.date.today().isoformat()
    week_start = today - timedelta(days=today.weekday())
    week_label = week_start.strftime('%B %d')
    journal['sets'] = [
        {'id': 1, 'routine_id': 1, 'exercise': 'Bench Press', 'date': today, 'reps': 10, 'weight': 60},
        {'id': 2, 'routine_id': 1, 'exercise': 'Bench Press', 'date': today, 'reps': 8, 'weight': 70},
        {'id': 3, 'routine_id': 1, 'exercise': 'Bench Press', 'date': today, 'reps': 6, 'weight': 80},
        {'id': 4, 'routine_id': 2, 'exercise': 'Deadlift', 'date': today, 'reps': 5, 'weight': 120},
        {'id': 5, 'routine_id': 3, 'exercise': 'Squat', 'date': today, 'reps': 8, 'weight': 80},
    ]
    journal['records'] = [
        {'id': 1, 'exercise': 'Bench Press', 'reps': 10, 'weight': 60, 'date': today},
        {'id': 2, 'exercise': 'Deadlift', 'reps': 5, 'weight': 120, 'date': today},
        {'id': 3, 'exercise': 'Squat', 'reps': 8, 'weight': 80, 'date': today},
    ]
    journal['summaries'] = [
        {'id': 1, 'week': week_label, 'total_sets': 5, 'total_volume': 4320, 'exercises_done': 5},
    ]
