# === Stage 37: Add recommendations for the next useful action ===
# Project: FitnessJournal
def get_next_action(journal):
    """Suggest the next useful workout based on recent patterns."""
    if not journal.get('history'):
        return "Start your first workout routine."
    
    recent = journal['history'][-7:]
    if not recent:
        return "You haven't logged enough workouts yet."
    
    exercises_per_week = [sum(1 for d in recent if d.get('exercises')) for _ in range(1)]
    avg_per_week = sum(exercises_per_week) / len(recent)
    
    if avg_per_week < 3:
        return f"You've only done {avg_per_week:.1f} exercises this week. Consider adding a session to reach 3+ per week."
    
    last_exercise = recent[-1].get('exercises', [])
    if last_exercise:
        last_name = last_exercise[0].get('name', 'Unknown')
        return f"Last workout was {last_name}. Try a different exercise group next time to avoid overtraining."
    
    return "Consistent! Keep up the good work and aim for variety in your routines."
