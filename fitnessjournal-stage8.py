# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: FitnessJournal
def filter_workouts(workouts, **kwargs):
    """Filter workouts by status, category, owner, or tag.
    
    Supports any combination of these filters:
    - status: active, completed, paused
    - category: strength, cardio, flexibility, mixed
    - owner: string or list of strings
    - tag: string or list of strings
    
    Returns a new list containing only matching workouts.
    """
    if not kwargs:
        return list(workouts)
    
    result = []
    for workout in workouts:
        match = True
        if 'status' in kwargs:
            if workout.status not in kwargs['status']:
                match = False
        if 'category' in kwargs:
            if workout.category not in kwargs['category']:
                match = False
        if 'owner' in kwargs:
            owners = kwargs['owner']
            if isinstance(owners, str):
                owners = [owners]
            if workout.owner not in owners:
                match = False
        if 'tag' in kwargs:
            tags = kwargs['tag']
            if isinstance(tags, str):
                tags = [tags]
            if workout.tag not in tags:
                match = False
        if match:
            result.append(workout)
    return result
