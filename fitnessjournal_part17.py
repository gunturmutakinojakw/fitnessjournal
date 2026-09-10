# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: FitnessJournal
def dry_run(self, action: str, **kwargs) -> dict:
    """Simulate a mutating command and return a preview dict without changing state.

    Args:
        action: One of 'add_routine', 'add_set', 'set_pr', 'update_routine'.
        **kwargs: Arguments expected by the real command.

    Returns:
        A dict with keys 'dry_run', 'action', 'preview'.
    """
    preview = {
        'dry_run': True,
        'action': action,
        'preview': {},
    }
    if action == 'add_routine':
        preview['preview']['routine_name'] = kwargs.get('routine_name', '')
        preview['preview']['exercises'] = kwargs.get('exercises', [])
    elif action == 'add_set':
        preview['preview']['exercise'] = kwargs.get('exercise', '')
        preview['preview']['sets'] = kwargs.get('sets', [])
    elif action == 'set_pr':
        preview['preview']['exercise'] = kwargs.get('exercise', '')
        preview['preview']['new_pr'] = kwargs.get('new_pr', 0)
    elif action == 'update_routine':
        preview['preview']['exercise'] = kwargs.get('exercise', '')
        preview['preview']['new_sets'] = kwargs.get('new_sets', [])
    return preview
