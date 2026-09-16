# === Stage 38: Add data integrity checks for broken references ===
# Project: FitnessJournal
def _broken_ref(self, ref_type, ref_value):
    """Validate and return a dict describing broken references."""
    errors = []
    if ref_type == "routine":
        routine = self._routines.get(ref_value)
        if not routine:
            errors.append(f"Routine '{ref_value}' not found.")
        else:
            sets = self._sets
            for s in sets.values():
                if s.get("routine") == ref_value:
                    errors.append(f"Routine '{ref_value}' has orphaned sets.")
    elif ref_type == "set":
        sets = self._sets
        if ref_value not in sets:
            errors.append(f"Set '{ref_value}' not found.")
        else:
            if sets[ref_value].get("routine") not in self._routines:
                errors.append(f"Set '{ref_value}' references missing routine.")
    elif ref_type == "record":
        records = self._records
        if ref_value not in records:
            errors.append(f"Record '{ref_value}' not found.")
        else:
            if records[ref_value].get("routine") not in self._routines:
                errors.append(f"Record '{ref_value}' references missing routine.")
    elif ref_type == "week":
        weeks = self._weekly_summaries
        if ref_value not in weeks:
            errors.append(f"Week '{ref_value}' not found.")
    return errors
