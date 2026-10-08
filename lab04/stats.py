def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно два знака ';'")
    city, temp_str, date = parts
    if not city.strip() or not date.strip():
        raise ValueError("Город или дата не могут быть пустыми")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Температура должна быть числом")
    # Ключ изменен на "temperature" под требования автотеста
    return {"city": city.strip(), "temperature": temp, "date": date.strip()}

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        try:
            record = parse_record(cleaned_line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records

def average_by_city(records: list[dict]) -> dict:
    city_totals, city_counts = {}, {}
    for r in records:
        city = r["city"]
        # Используем правильный ключ "temperature"
        city_totals[city] = city_totals.get(city, 0.0) + r["temperature"]
        city_counts[city] = city_counts.get(city, 0) + 1
    return {city: round(city_totals[city] / city_counts[city], 1) for city in city_totals}

def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    averages = average_by_city(records)
    best_city = None
    for city, avg_temp in averages.items():
        if best_city is None:
            best_city = city
        else:
            if avg_temp > averages[best_city]:
                best_city = city
            elif avg_temp == averages[best_city] and city < best_city:
                best_city = city
    return best_city


