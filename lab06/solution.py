def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        filename = path.split('/')[-1]
        
        # Обработка файлов без расширения или скрытых типа .gitig
        if filename.startswith('.') and filename.count('.') == 1:
            ext = ""
        elif '.' in filename:
            ext = filename.split('.')[-1].lower()
        else:
            ext = ""
            
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    # Сортируем по вложенности и алфавиту
    sorted_paths = sorted(paths, key=lambda p: (-p.count('/'), p))
    return sorted_paths


def human_size(n_bytes: int) -> str:
    if n_bytes == 0:
        return "0 Б"
        
    # Все единицы измерения теперь строго заглавными буквами
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    size = float(n_bytes)
    unit_index = 0
    
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
        
    if unit_index == 0:
        return f"{int(n_bytes)} Б"
    else:
        return f"{size:.1f} {units[unit_index]}"

