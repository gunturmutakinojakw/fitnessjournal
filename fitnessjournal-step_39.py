# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: FitnessJournal
def repair_journal(journal):
    """Fix common data integrity issues in the FitnessJournal."""
    if not journal:
        return journal

    # Fix missing workout dates
    for i in range(len(journal)):
        if journal[i].get('date') is None:
            journal[i]['date'] = datetime.now().strftime('%Y-%m-%d')

    # Fix missing sets
    for i in range(len(journal)):
        if journal[i].get('sets') is None:
            journal[i]['sets'] = []

    # Fix missing total volume
    for i in range(len(journal)):
        if journal[i].get('total_volume') is None:
            journal[i]['total_volume'] = sum(set['weight'] * set['reps'] for set in journal[i].get('sets', []))

    # Fix missing weight or reps in sets
    for i in range(len(journal)):
        for j in range(len(journal[i].get('sets', []))):
            if journal[i]['sets'][j].get('weight') is None:
                journal[i]['sets'][j]['weight'] = 0
            if journal[i]['sets'][j].get('reps') is None:
                journal[i]['sets'][j]['reps'] = 0

    return journal
