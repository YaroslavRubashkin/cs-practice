import json

def csv_to_records(text: str) -> list[dict]:
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if not lines:
        return []
    
    headers = lines[0].split(',')
    records = []
    
    for line in lines[1:]:
        values = line.split(',')
        record = {}
        for i in range(len(headers)):
            if i < len(values):
                record[headers[i]] = values[i]
        records.append(record)
        
    return records


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None
    
    for line in lines:
        # Убираем пробелы справа и переводы строк
        line_raw = line.rstrip()
        if not line_raw:
            continue
            
        # Считаем отступ (количество пробелов в начале)
        indent = len(line_raw) - len(line_raw.lstrip())
        line_clean = line_raw.strip()
        
        # Проверяем и отбрасываем комментарии
        if line_clean.startswith('#'):
            continue
        if ' #' in line_raw:
            line_clean = line_raw.split(' #')[0].strip()
        elif '#' in line_clean and not line_clean.startswith('#'):
            # На случай, если комментарий прижат без пробела
            line_clean = line_clean.split('#')[0].strip()

        if not line_clean:
            continue

        # Обработка элементов списка (строка начинается с "- ")
        if line_clean.startswith('- '):
            if current_list_key and current_list_key in result:
                val = line_clean[2:].strip()
                # Приведение типов для элементов списка
                if val.isdigit():
                    val = int(val)
                elif val == 'true' or val == 'yes':
                    val = True
                elif val == 'false' or val == 'no':
                    val = False
                else:
                    try:
                        val = float(val)
                    except ValueError:
                        pass
                result[current_list_key].append(val)
            continue

        # Сбрасываем текущий список, если отступ равен 0 и это новая пара ключ-значение
        if indent == 0:
            current_list_key = None

        if ':' in line_clean:
            key, val = line_clean.split(':', 1)
            key = key.strip()
            val = val.strip()
            
            if not val:  # Это начало списка (например, "columns:")
                result[key] = []
                current_list_key = key
            else:
                # Приведение типов для обычных значений
                if val.isdigit():
                    val = int(val)
                elif val == 'true' or val == 'yes':
                    val = True
                elif val == 'false' or val == 'no':
                    val = False
                else:
                    try:
                        val = float(val)
                    except ValueError:
                        pass
                result[key] = val

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str) -> list[dict]:
    updated_rows = []
    for row in rows:
        new_row = row.copy()
        if key in new_row:
            lookup_val = str(new_row[key])
            if lookup_val in extra:
                extra_data = extra[lookup_val]
                for k, v in extra_data.items():
                    if k not in new_row:
                        new_row[k] = v
        updated_rows.append(new_row)
    return updated_rows


def records_to_json(records: list[dict]) -> str:
    # ensure_ascii=False сохраняет кириллицу как есть, indent=2 делает отступ в 2 пробела, sort_keys=True сортирует ключи
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
