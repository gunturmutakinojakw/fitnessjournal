# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: FitnessJournal
import sys, colorama as c

def colorize(text, color):
    return f"\033[{color}m{text}\033[0m"

def print_header(title):
    print(colorize(f"╔══════ {title} ═════╗", "1;36"))
    print(colorize("║", "36"))

def print_subheader(title):
    print(colorize(f"── {title} ──", "1;33"))

def print_row(label, value):
    print(f"{colorize(label, '1;32')}  {colorize(value, '1;36')}")

def print_summary(stats):
    print(colorize("══ Weekly Summary ══", "1;35"))
    for k, v in stats.items():
        print(f"{colorize(k, '1;32')}  {colorize(v, '1;36')}")
    print(colorize("── End of Report ──", "1;31"))

if __name__ == "__main__":
    print_header("Fitness Journal")
    print_subheader("Recent Routines")
    for r in routines:
        print_row(r["name"], f"{r['sets']} sets")
    print_summary({"total_sets": total_sets, "avg_weight": avg_weight})
