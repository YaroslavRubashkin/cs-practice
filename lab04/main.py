import sys
from stats import average_by_city, parse_record, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    valid_count, error_count = 0, 0
    valid_records = []
   
    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        try:
            record = parse_record(cleaned_line)
            valid_records.append(record)
            valid_count += 1
        except ValueError:
            error_count += 1

    warmest = warmest_city(valid_records)
    averages = average_by_city(valid_records)
    warmest_temp = averages.get(warmest, 0.0)

    print(valid_count)
    print(error_count)
    print(f"{warmest_temp:.1f}")

if __name__ == "__main__":
    main()

