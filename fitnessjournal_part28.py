# === Stage 28: Add overdue item detection based on due dates ===
# Project: FitnessJournal
def check_overdue_items(items, due_field='due_date'):
    """Return list of items whose due date has passed."""
    overdue = []
    for item in items:
        due = item.get(due_field)
        if due and due < datetime.now().date():
            overdue.append(item)
    return overdue
