def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")
        
    parts = line.split(" ", 2)
    
    if len(parts) < 2:
        raise ValueError("Некорректный формат строки")
        
    time = parts[0]
    level = parts[1]
    
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError("Неизвестный уровень логирования")
        
    message = parts[2] if len(parts) == 3 else ""
        
    return {"time": time, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            
    return counts


def top_errors(lines, n: int) -> list:
    error_counts = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue
            
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    
    return [list(item) for item in sorted_errors[:n]]


def format_report(counts: dict, errors: list) -> str:
    lines = ["Отчёт по журналу", ""]
    
    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")
        
    lines.append("")
    lines.append("Частые ошибки:")
    
    if not errors:
        lines.append("Ошибок не обнаружено.")
    else:
        for msg, count in errors:
            lines.append(f"- {msg} — {count}")
            
    return "\n".join(lines) + "\n"



