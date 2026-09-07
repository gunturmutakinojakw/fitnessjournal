# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: FitnessJournal
def sort_workouts(key=None, reverse=False):
    """Sort workouts by title, date, priority, or last update time.

    Args:
        key: A string indicating the sort field: 'title', 'date', 'priority',
             or 'last_update'. Defaults to 'title'.
        reverse: If True, sort in descending order. Defaults to False.

    Returns:
        A sorted list of workout dictionaries.
    """
    if key is None:
        key = 'title'

    def sort_key(workout):
        value = workout.get(key, '')
        if key == 'date':
            return workout.get('date', '')
        elif key == 'priority':
            try:
                return int(value)
            except (ValueError, TypeError):
                return 0
        elif key == 'last_update':
            return workout.get('last_update', '')
        else:
            return str(value).lower()

    return sorted(workouts, key=sort_key, reverse=reverse)
