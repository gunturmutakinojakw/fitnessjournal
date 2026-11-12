# === Stage 73: Add a lightweight HTML report export ===
# Project: FitnessJournal
def export_html_report(journal, output_path="fitness_report.html"):
    from datetime import datetime
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head><title>FitnessJournal Report</title>\n")
        f.write("<style>body{font-family:sans-serif;margin:2rem}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:6px;text-align:left}</style>\n")
        f.write("</head>\n<body>\n")
        f.write(f"<h1>Fitness Journal Report</h1>\n")
        f.write(f"<p>Generated: {datetime.now().isoformat()}</p>\n")
        f.write(f"<p>Total workouts logged: {len(journal['workouts'])}</p>\n")
        f.write("<h2>Routines</h2>\n")
        for routine in journal.get("routines", []):
            f.write(f"<h3>{routine['name']}</h3>\n")
            for exercise in routine.get("exercises", []):
                f.write(f"<p><strong>{exercise['name']}</strong> - {exercise.get('sets', 0)} sets</p>\n")
            f.write("<hr>\n")
        f.write("<h2>Personal Records</h2>\n")
        for record in journal.get("personal_records", []):
            f.write(f"<p>{record['exercise']} - {record['weight']} kg ({record['reps']} reps) on {record['date']}</p>\n")
        f.write("<h2>Recent Workouts</h2>\n")
        f.write("<table><tr><th>Date</th><th>Routine</th><th>Exercises</th></tr>\n")
        for workout in journal.get("workouts", [])[:10]:
            routine_name = workout.get("routine_name", "Unknown")
            exercise_list = ", ".join(e["name"] for e in workout.get("exercises", []))
            f.write(f"<tr><td>{workout['date']}</td><td>{routine_name}</td><td>{exercise_list}</td></tr>\n")
        f.write("</table>\n</body>\n</html>\n")
