# === Stage 18: Add an activity log with timestamps and action names ===
# Project: FitnessJournal
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, timestamp=None):
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now()
        self.entries.append({"action": action, "timestamp": timestamp})

    def get_log(self):
        return self.entries

    def __str__(self):
        lines = [f"Activity Log ({len(self.entries)} entries):"]
        for i, entry in enumerate(self.entries, 1):
            lines.append(f"  {i}. [{entry['timestamp']}] {entry['action']}")
        return "\n".join(lines)
