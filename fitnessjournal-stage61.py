# === Stage 61: Add performance timing for core list and search operations ===
# Project: FitnessJournal
import time

def _timeit(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed

def _search_by_name(items, name):
    start = time.perf_counter()
    matches = [item for item in items if name.lower() in item.get('name', '').lower()]
    elapsed = time.perf_counter() - start
    return matches, elapsed

def _summarize_week(sets_by_date):
    start = time.perf_counter()
    total_exercises = sum(len(ex) for ex in sets_by_date.values())
    total_volume = sum(
        sum(set.get('weight', 0) * set.get('reps', 0) for set in exercises)
        for exercises in sets_by_date.values()
    )
    elapsed = time.perf_counter() - start
    return {'exercises': total_exercises, 'volume': total_volume}, elapsed

def _find_prs(records):
    start = time.perf_counter()
    prs = [record for record in records if record.get('is_pr', False)]
    elapsed = time.perf_counter() - start
    return prs, elapsed
