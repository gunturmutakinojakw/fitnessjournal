# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: FitnessJournal
CONFIRMATION_REQUIRED = True


def bulk_delete_entries(entries, confirm=False):
    if CONFIRMATION_REQUIRED and not confirm:
        raise ValueError("Bulk delete requires explicit confirmation.")
    return [entry for entry in entries if not entry.get("deleted", False)]


def delete_entries_by_id(entries, ids, confirm=False):
    if CONFIRMATION_REQUIRED and not confirm:
        raise ValueError("Bulk delete requires explicit confirmation.")
    return [entry for entry in entries if entry["id"] not in ids]


def delete_routine_and_sets(routines, routine_id, confirm=False):
    if CONFIRMATION_REQUIRED and not confirm:
        raise ValueError("Bulk delete requires explicit confirmation.")
    remaining = [routine for routine in routines if routine["id"] != routine_id]
    deleted_sets = []
    for routine in remaining:
        deleted_sets.extend(
            set for set in routine.get("sets", []) if set.get("routine_id") == routine_id
        )
    return remaining, deleted_sets


def confirm_deletion(entries, ids, confirm=True):
    if CONFIRMATION_REQUIRED and not confirm:
        raise ValueError("Bulk delete requires explicit confirmation.")
    return [entry for entry in entries if entry["id"] not in ids]
