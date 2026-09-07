# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: FitnessJournal
def format_set(set_name, weight, reps, pr=False):
    style = "bold" if pr else "normal"
    return f"  [{style}]{set_name}[/]: {weight}kg x {reps}"

def format_routine(routine):
    parts = []
    for s in routine.sets:
        parts.append(format_set(s.name, s.weight, s.reps, s.is_pr))
    return "\n".join(parts)

def format_weekly_summary(week):
    lines = [f"=== Week {week.year}-{week.week_num} ==="]
    for day in week.days:
        total = sum(s.weight * s.reps for s in day.sets)
        lines.append(f"  {day.day_name}: {len(day.sets)} sets, {total}kg total")
    return "\n".join(lines)
