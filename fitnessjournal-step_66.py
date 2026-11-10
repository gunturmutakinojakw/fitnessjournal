# === Stage 66: Add export of a short status dashboard ===
# Project: FitnessJournal
def print_dashboard(records, routines, weeks):
    if not records:
        print("No workouts logged yet.")
        return
    today = records[-1].date
    total_volume = sum(set.weight * set.reps for r in records for set in r.sets)
    prs = [r for r in routines for s in r.sets if s.reps == s.best_reps]
    print("FitnessJournal Status")
    print("Latest:", today)
    print("Total Volume:", total_volume)
    print("Active Routines:", len(routines))
    print("Personal Records:", len(prs))
    for w in weeks[-3:]:
        print(w.week, "avg:", round(w.avg_volume, 1), "peak:", w.peak_volume)
