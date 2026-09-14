# === Stage 32: Add pagination helpers for long console output ===
# Project: FitnessJournal
def print_page(title, width=72):
    print("\n" + "=" * width)
    print(f" {title:^width}")
    print("=" * width)

def print_page_lines(lines, width=72):
    for line in lines:
        print(line)
    print()

def print_page_wrapped(text, width=72):
    print_page(text)
    print(text)
    print()

def print_page_table(headers, rows, width=72):
    print_page(f" {headers[0].upper()}")
    print(" | ".join(f"{h:^10}" for h in headers))
    print("-" * (width // 2))
    for row in rows:
        print(" | ".join(f"{str(c):^10}" for c in row))
    print()

def print_page_summary(title, stats):
    print_page(f" {title.upper()}")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print()
