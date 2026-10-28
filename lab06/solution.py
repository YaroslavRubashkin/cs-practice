def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        filename = path.split('/')[-1]
        
        # Если имя файла целиком состоит из одной точки и букв (например, .gitig)
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
    sorted_paths = sorted(paths, key=lambda p: (-p.count('/'), p))
    return sorted_paths[0]


def human_size(n_bytes: int) -> str:
    # chr(1073) — это железно русская буква 'б' на уровне компьютерного кода
    rus_b = chr(1073)
    
    if n_bytes == 0:
        return f"0 {rus_b}"
        
    units = [rus_b, 'КБ', 'МБ', 'ГБ', 'ТБ']
    size = float(n_bytes)
    unit_index = 0
    
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
        
    if unit_index == 0:
        return f"{int(n_bytes)} {rus_b}"
    else:
        return f"{size:.1f} {units[unit_index]}"

