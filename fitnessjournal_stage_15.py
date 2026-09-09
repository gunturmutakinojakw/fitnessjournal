# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: FitnessJournal
def dispatch_command(command, args):
    """Simple command dispatcher for text-based commands."""
    cmd = command.lower().strip()
    if cmd == "add":
        return {"action": "add", "routine": args.get("routine", "")}
    elif cmd == "log":
        return {"action": "log", "exercise": args.get("exercise", ""), "sets": args.get("sets", 0), "weight": args.get("weight", 0)}
    elif cmd == "pr":
        return {"action": "personal_record", "exercise": args.get("exercise", ""), "weight": args.get("weight", 0)}
    elif cmd == "summary":
        return {"action": "weekly_summary"}
    elif cmd == "help":
        return {"action": "help", "message": "Available commands: add, log, pr, summary, help"}
    elif cmd == "quit":
        return {"action": "quit"}
    else:
        return {"action": "unknown", "message": f"Unknown command: {command}"}
