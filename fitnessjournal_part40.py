# === Stage 40: Add plain text report export ===
# Project: FitnessJournal
import os

def export_report(journal, out_path):
    lines = []
    lines.append("FitnessJournal Report")
    lines.append("=" * 40)
    lines.append(f"Date: {journal['date']}")
    lines.append(f"Routines: {', '.join(journal['routines'])}")
    lines.append(f"Total exercises: {journal['total_exercises']}")
    lines.append(f"Sets completed: {journal['total_sets']}")
    lines.append(f"New PRs: {journal['new_prs']}")
    lines.append("-" * 40)
    if journal.get('weekly_summary'):
        lines.append(f"Weekly summary: {journal['weekly_summary']}")
    lines.append("-" * 40)
    for ex, data in journal['exercises'].items():
        sets_done = sum(1 for s in data['sets'] if s['completed'])
        pr = data.get('personal_record', 'N/A')
        lines.append(f"  {ex}: {sets_done} sets done, PR: {pr}")
    lines.append("=" * 40)
    lines.append("Done.")
    with open(out_path, 'w') as f:
        f.write('\n'.join(lines))
    print(f"Report saved to {out_path}")
