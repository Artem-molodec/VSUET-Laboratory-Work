import json
import tempfile
from pathlib import Path

from storage import load_records, save_records

RECORDS = [
    {"id": 1, "title": "Томаты", "category": "огород", "amount": 12, "completed": False},
    {"id": 3, "title": "Яблони", "category": "сад", "amount": 3, "completed": True},
]

with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "data.json"

    # ---------- Сохранение и повторное чтение ----------
    save_records(path, RECORDS)
    assert load_records(path) == RECORDS
    text = path.read_text(encoding="utf-8")
    assert "Томаты" in text                      # кириллица читаема, без \u0422

    # Пустой список
    save_records(path, [])
    assert load_records(path) == []

    # ---------- Файла нет ----------
    try:
        load_records(Path(folder) / "нет_такого.json")
        raise AssertionError("Ожидали FileNotFoundError")
    except FileNotFoundError:
        pass

    # ---------- Повреждённый JSON ----------
    broken = Path(folder) / "broken.json"
    broken.write_text("[{'id': 1}]", encoding="utf-8")        # одинарные кавычки
    try:
        load_records(broken)
        raise AssertionError("Ожидали JSONDecodeError")
    except json.JSONDecodeError:
        pass
    assert broken.read_text(encoding="utf-8") == "[{'id': 1}]"   # файл не изменён

    # ---------- Неправильная кодировка ----------
    wrong = Path(folder) / "cp1251.json"
    wrong.write_bytes('[{"title": "Томаты"}]'.encode("cp1251"))
    try:
        load_records(wrong)
        raise AssertionError("Ожидали UnicodeDecodeError")
    except UnicodeDecodeError:
        pass

    # ---------- Повторный id и неправильная структура ----------
    duplicate = Path(folder) / "duplicate.json"
    duplicate.write_text(json.dumps(RECORDS + [RECORDS[0]]), encoding="utf-8")
    try:
        load_records(duplicate)
        raise AssertionError("Ожидали ValueError для повторного id")
    except ValueError:
        pass

    not_list = Path(folder) / "object.json"
    not_list.write_text('{"id": 1}', encoding="utf-8")
    try:
        load_records(not_list)
        raise AssertionError("Ожидали ValueError для объекта вместо списка")
    except ValueError:
        pass

    # ---------- Плохие данные не затирают прежний файл ----------
    save_records(path, RECORDS)
    try:
        save_records(path, [{"id": 1}])
        raise AssertionError("Ожидали ValueError при сохранении")
    except ValueError:
        pass
    assert load_records(path) == RECORDS
    assert not Path(str(path) + ".tmp").exists()

    # ---------- Ошибка записи (папки не существует) ----------
    try:
        save_records(Path(folder) / "нет_папки" / "data.json", RECORDS)
        raise AssertionError("Ожидали OSError")
    except OSError:
        pass

print("test_storage: все проверки пройдены")
