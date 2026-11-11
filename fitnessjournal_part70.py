# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: FitnessJournal
CLEAR_CONFIRMED = False


def confirm_clear():
    global CLEAR_CONFIRMED
    if input("Type 'yes' to clear all data, or 'no' to cancel: ").strip().lower() != "yes":
        CLEAR_CONFIRMED = False
        return
    CLEAR_CONFIRMED = True


def clear_state():
    global CLEAR_CONFIRMED
    if not CLEAR_CONFIRMED:
        print("Aborted: confirm before clearing.")
        return
    routines.clear()
    records.clear()
    weekly.clear()
    CLEAR_CONFIRMED = False
    print("All data cleared.")
