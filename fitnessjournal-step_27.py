# === Stage 27: Add monthly summary calculations ===
# Project: FitnessJournal
from datetime import date

def monthly_summary(journal):
    """Return a dict with counts and totals per month."""
    monthly = {}
    for entry in journal:
        month_key = entry['date'].strftime('%Y-%m')
        if month_key not in monthly:
            monthly[month_key] = {
                'workouts': 0,
                'total_sets': 0,
                'total_kg': 0.0,
                'total_reps': 0,
                'new_prs': 0,
            }
        monthly[month_key]['workouts'] += 1
        monthly[month_key]['total_sets'] += len(entry['sets'])
        for s in entry['sets']:
            monthly[month_key]['total_kg'] += s['weight']
            monthly[month_key]['total_reps'] += s['reps']
        if any(s['weight'] == entry.get('pr', 0) for s in entry['sets']):
            monthly[month_key]['new_prs'] += 1
    return monthly
