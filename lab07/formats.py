import json

def csv_to_records(text: str) -> list[dict]:
    # Делим на строки и убираем пустые
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if not lines:
        return []
    
    # Очищаем заголовки от пробелов по краям
    headers = [h.strip() for h in lines[0].split(',')]
    records = []
    
    for line in lines[1:]:
        # Очищаем каждое значение от пробелов по краям
        values = [v.strip() for v in line.split(',')]
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
        # По правилу: всё после знака # отбрасывается
        if '#' in line:
            line = line.split('#')[0]
            
        line_raw = line.rstrip()
        if not line_raw.strip():
            continue
            
        # Считаем отступ для списков
        indent = len(line_raw) - len(line_raw.lstrip())
        line_clean = line_raw.strip()
        
        # Если это элемент списка
        if line_clean.startswith('- '):
            if current_list_key and current_list_key in result:
                val = line_clean[2:].strip()
                if val.isdigit():
                    val = int(val)
                elif val.lower() in ['true', 'yes']:
                    val = True
                elif val.lower() in ['false', 'no']:
                    val = False
                else:
                    try:
                        val = float(val)
                    except ValueError:
                        pass
                result[current_list_key].append(val)
            continue
            
        if indent == 0:
            current_list_key = None
            
        if ':' in line_clean:
            key, val = line_clean.split(':', 1)
            key = key.strip()
            val = val.strip()
            
            if not val:
                result[key] = []
                current_list_key = key
            else:
                if val.isdigit():
                    val = int(val)
                elif val.lower() in ['true', 'yes']:
                    val = True
                elif val.lower() in ['false', 'no']:
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
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
