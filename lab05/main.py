import sys
from logstats import count_levels, top_errors, format_report

def main():
    filename = sys.stdin.readline().strip()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    total_lines = len([l for l in lines if l.strip()])
    counts = count_levels(lines)
    
    print(total_lines)
    print(counts["ERROR"])
    print(counts["BROKEN"])

    errors = top_errors(lines, 3)
    report_text = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)

if __name__ == "__main__":
    main()
