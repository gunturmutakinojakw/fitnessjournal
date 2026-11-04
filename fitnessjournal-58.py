# === Stage 58: Add bulk update behavior for selected records ===
# Project: FitnessJournal
def bulk_update_records(journal, record_ids, new_value):
    """Set a new_value on each journal record whose id is in record_ids."""
    updated = []
    for record in journal.records:
        if record.id in record_ids:
            record.value = new_value
            updated.append(record)
    return updated


def bulk_delete_records(journal, record_ids):
    """Remove records whose id is in record_ids and report how many were removed."""
    kept_ids = {r.id for r in journal.records if r.id not in record_ids}
    removed = [r for r in journal.records if r.id in record_ids]
    journal.records = [r for r in journal.records if r.id in kept_ids]
    return removed
