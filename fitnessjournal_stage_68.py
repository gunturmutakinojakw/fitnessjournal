# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: FitnessJournal
def build_changelog(records, limit=15):
    """Build a compact changelog from activity records."""
    if not records:
        return "No activity recorded yet."
    lines = []
    for entry in records[-limit:]:
        date = entry.get("date", "unknown")
        action = entry.get("action", "activity")
        detail = entry.get("detail", "")
        if detail:
            lines.append(f"[{date}] {action}: {detail}")
        else:
            lines.append(f"[{date}] {action}")
    return "\n".join(lines)


def log_activity(log_file, entry):
    """Append a single activity entry to the log file."""
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def load_activity_log(log_file):
    """Load all activity entries from the log file."""
    entries = []
    if not os.path.exists(log_file):
        return entries
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def display_changelog(log_file, limit=15):
    """Display the compact changelog from the activity log."""
    print("=" * 40)
    print("CHANGELOG")
    print("=" * 40)
    entries = load_activity_log(log_file)
    if not entries:
        print("No activity recorded yet.")
        return
    print(build_changelog(entries, limit=limit))
