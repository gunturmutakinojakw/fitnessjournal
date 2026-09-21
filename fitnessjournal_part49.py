# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: FitnessJournal
import pytest
from fitness_journal import WorkoutJournal


@pytest.mark.parametrize("routine_name,initial_sets,deleted_set", [
    ("BenchPress", [("50kg", 5), ("55kg", 5), ("60kg", 5)], "60kg"),
    ("Squat", [("80kg", 6), ("90kg", 6), ("100kg", 6)], "90kg"),
])
def test_delete_set(routine_name, initial_sets, deleted_set):
    journal = WorkoutJournal()
    for set_info in initial_sets:
        journal.add_set(routine_name, set_info)
    assert len(journal.get_sets(routine_name)) == 3
    journal.delete_set(routine_name, deleted_set)
    remaining = journal.get_sets(routine_name)
    assert len(remaining) == 2
    set_names = [s["weight"] for s in remaining]
    assert deleted_set not in set_names


@pytest.mark.parametrize("routine_name,initial_sets", [
    ("Pushups", [("20", 15), ("25", 15), ("30", 15)]),
    ("Pullups", [("10", 8), ("12", 8), ("14", 8)]),
])
def test_delete_all_sets(routine_name, initial_sets):
    journal = WorkoutJournal()
    for set_info in initial_sets:
        journal.add_set(routine_name, set_info)
    assert len(journal.get_sets(routine_name)) == 3
    for set_info in initial_sets:
        journal.delete_set(routine_name, set_info["reps"])
    assert len(journal.get_sets(routine_name)) == 0
    assert journal.get_sets(routine_name) == []


@pytest.mark.parametrize("routine_name,initial_sets", [
    ("Deadlift", [("100kg", 5), ("110kg", 5), ("120kg", 5)]),
    ("OverheadPress", [("40kg", 5), ("45kg", 5), ("50kg", 5)]),
])
def test_update_set(routine_name, initial_sets):
    journal = WorkoutJournal()
    for set_info in initial_sets:
        journal.add_set(routine_name, set_info)
    updated_set = ("120kg", 6)
    journal.update_set(routine_name, updated_set["reps"], updated_set["weight"])
    sets = journal.get_sets(routine_name)
    assert len(sets) == 3
    new_weight = [s["weight"] for s in sets if s["reps"] == 6]
    assert len(new_weight) == 1
    assert new_weight[0] == "120kg"


@pytest.mark.parametrize("routine_name,initial_sets", [
    ("Snatch", [("50kg", 3), ("55kg", 3), ("60kg", 3)]),
    ("CleanAndJerk", [("60kg", 4), ("65kg", 4), ("70kg", 4)]),
])
def test_delete_nonexistent_set_raises(routine_name, initial_sets):
    journal = WorkoutJournal()
    for set_info in initial_sets:
        journal.add_set(routine_name, set_info)
    with pytest.raises(ValueError, match="Set not found"):
        journal.delete_set(routine_name, "999kg")


@pytest.mark.parametrize("routine_name,initial_sets", [
    ("FrontSquat", [("50kg", 5), ("55kg", 5), ("60kg", 5)]),
    ("BackSquat", [("60kg", 5), ("65kg", 5), ("70kg", 5)]),
])
def test_update_nonexistent_set_raises(routine_name, initial_sets):
    journal = WorkoutJournal()
    for set_info in initial_sets:
        journal.add_set(routine_name, set_info)
    with pytest.raises(ValueError, match="Set not found"):
        journal.update_set(routine_name, "999kg", "80kg")
