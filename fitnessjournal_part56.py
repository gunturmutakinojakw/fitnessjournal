# === Stage 56: Add compact error classes for domain failures ===
# Project: FitnessJournal
class FitnessError(Exception):
    pass

class RoutineNotFoundError(FitnessError):
    pass

class InvalidWeightError(FitnessError):
    pass

class InvalidRepError(FitnessError):
    pass

class RecordNotFoundError(FitnessError):
    pass

class InvalidDateError(FitnessError):
    pass

class InsufficientRecordsError(FitnessError):
    pass

class DuplicateRoutineError(FitnessError):
    pass

class DuplicateSetError(FitnessError):
    pass

class InvalidWeeklyRangeError(FitnessError):
    pass
