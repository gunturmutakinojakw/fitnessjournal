# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: FitnessJournal
from dataclasses import dataclass, field
from datetime import date

@dataclass
class Set:
    weight: float
    reps: int
    notes: str = ""

@dataclass
class Exercise:
    name: str
    sets: list[Set] = field(default_factory=list)

@dataclass
class Workout:
    date: date
    exercises: list[Exercise] = field(default_factory=list)

@dataclass
class PersonalRecord:
    exercise: str
    value: float
    date: date
    note: str = ""
