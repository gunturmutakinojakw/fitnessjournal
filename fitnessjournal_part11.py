# === Stage 11: Add JSON export for the current application state ===
# Project: FitnessJournal
import json

def export_state(journal):
    """Export current FitnessJournal state to a JSON string."""
    state = {
        "routines": journal._routines,
        "records": journal._records,
        "logs": journal._logs,
        "history": journal._history,
        "stats": journal._stats,
    }
    return json.dumps(state, indent=2)
