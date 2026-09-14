# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: FitnessJournal
def upcoming_reminders(
    routines: dict,
    next_week: datetime.date,
    today: datetime.date,
) -> list[dict]:
    """Return a list of reminder dicts for any routine scheduled in the next seven days.

    Each dict contains 'routine', 'name', 'scheduled', 'reps', 'weight',
    'date' and 'due'.  'due' is the first day on or after today that matches
    the routine's schedule.

    Parameters
    ----------
    routines : dict
        Mapping of routine_id -> RoutineRecord.
    next_week : datetime.date
        The date seven days from today.
    today : datetime.date
        The current date.
    """
    reminders = []
    for rid, rec in routines.items():
        if rec.next is None:
            continue
        if rec.next < today:
            continue
        if rec.next > next_week:
            continue
        reminders.append(
            {
                "routine": rid,
                "name": rec.name,
                "scheduled": rec.next,
                "reps": rec.reps,
                "weight": rec.weight,
                "date": rec.next,
                "due": rec.next,
            }
        )
    return reminders
