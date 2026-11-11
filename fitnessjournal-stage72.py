# === Stage 72: Add Markdown report export ===
# Project: FitnessJournal
def export_markdown(journal, path="fitness_journal_report.md"):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# FitnessJournal Report\n\n")
        for routine in journal["routines"]:
            f.write(f"## {routine['name']}\n\n")
            for exercise in routine["exercises"]:
                f.write(f"### {exercise['name']}\n\n")
                f.write("| Date | Sets | Reps | Weight |\n")
                f.write("|------|------|------|--------|\n")
                for entry in exercise["entries"]:
                    f.write(
                        f"| {entry['date']} | {entry['sets']} | "
                        f"{entry['reps']} | {entry['weight']} |\n"
                    )
                prs = [e["weight"] for e in exercise["entries"] if e["weight"]]
                f.write(f"\n**Personal Record:** {max(prs) if prs else 'N/A'}\n\n")
            weekly = summarize_week(routine, exercise)
            if weekly:
                f.write(f"### Weekly Summary\n\n")
                f.write(
                    f"**Total Volume:** {weekly['volume']} | "
                    f"**Sessions:** {weekly['sessions']}\n\n"
                )
