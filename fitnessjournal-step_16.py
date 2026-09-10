# === Stage 16: Add argparse support for the most common commands ===
# Project: FitnessJournal
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="FitnessJournal CLI")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Add a workout")
    p_add.add_argument("routine", help="Routine name")
    p_add.add_argument("sets", nargs="+", help="Sets in format 'weight reps'")
    p_add.add_argument("--date", help="Date (YYYY-MM-DD)")
    p_add.add_argument("--note", help="Optional note")

    p_log = sub.add_parser("log", help="Log a workout")
    p_log.add_argument("routine", help="Routine name")
    p_log.add_argument("sets", nargs="+", help="Sets in format 'weight reps'")
    p_log.add_argument("--date", help="Date (YYYY-MM-DD)")

    p_summary = sub.add_parser("summary", help="Weekly summary")
    p_summary.add_argument("--week", help="ISO week number")

    p_records = sub.add_parser("records", help="Show personal records")
    p_records.add_argument("--routine", help="Filter by routine")

    return parser
