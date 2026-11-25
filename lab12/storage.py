import json
import os

from logic import validate_records


def load_records(path):
    # Читает JSON-файл, проверяет весь набор и возвращает список записей.
    with open(path, encoding="utf-8") as file:
        records = json.load(file)
    validate_records(records)
    return records


def save_records(path, records):
    #Записывает список в JSON (UTF-8). Возвращает None при успехе

    validate_records(records)
    text = json.dumps(records, ensure_ascii=False, indent=2)
    temp_path = str(path) + ".tmp"
    try:
        with open(temp_path, "w", encoding="utf-8") as file:
            file.write(text)
        os.replace(temp_path, path)
    except OSError:
        try:
            os.remove(temp_path)
        except OSError:
            pass
        raise