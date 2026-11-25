import copy

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
    validate_records,
)

# Пустой список
records = []
validate_records(records)
assert find_records(records, "a") == []
assert statistics(records) == {
    "total": 0, "completed": 0, "not_completed": 0, "amount_sum": 0, "by_category": {},
}
assert delete_record(records, 1) is False
assert set_completed(records, 1, True) is False

# Добавление 
first = add_record(records, "  Python  ", "  учёба  ", 4)
assert first == {"id": 1, "title": "Python", "category": "учёба", "amount": 4, "completed": False}
assert len(records) == 1

# Повторяющиеся названия разрешены, id разные
second = add_record(records, "Python", "учёба", 2)
assert second["id"] == 2
assert [r["title"] for r in records] == ["Python", "Python"]

# Некорректные значения: список не меняется
bad_args = [
    ("", "учёба", 1),        # пустое название
    ("   ", "учёба", 1),     # название из пробелов
    ("А", "", 1),            # пустая категория
    ("А", "учёба", -1),      # отрицательное количество
    ("А", "учёба", "abc"),   # не число
    ("А", "учёба", True),    # bool вместо числа
    ("А", "учёба", 2.5),     # дробное
]
for title, category, amount in bad_args:
    try:
        add_record(records, title, category, amount)
        raise AssertionError(f"Ожидали ValueError для {(title, category, amount)}")
    except ValueError:
        pass
assert len(records) == 2

# ---------- Статус ----------
assert set_completed(records, 2, True) is True
assert records[1]["completed"] is True
assert set_completed(records, 99, True) is False       # неизвестный ID
assert records[0]["completed"] is False                # данные не изменились
try:
    set_completed(records, 1, "да")
    raise AssertionError("Ожидали ValueError для статуса-строки")
except ValueError:
    pass

# Статистика: два значения 4 и 2, вторая завершена 
stats = statistics(records)
assert stats["total"] == 2
assert stats["completed"] == 1
assert stats["not_completed"] == 1
assert stats["amount_sum"] == 6

# Поиск 
assert len(find_records(records, "PY")) == 2           # без учёта регистра
assert len(find_records(records, "  pyth  ")) == 2     # пробелы в запросе убираются
assert find_records(records, "java") == []
for query in ("", "   "):
    try:
        find_records(records, query)
        raise AssertionError("Ожидали ValueError для пустого запроса")
    except ValueError:
        pass

# Удаление и новые id
assert delete_record(records, 1) is True
assert [r["id"] for r in records] == [2]               # id 2 не перенумерован
assert delete_record(records, 1) is False              # повторное удаление
third = add_record(records, "Новая", "учёба", 1)
assert third["id"] == 3

# Статистика по двум категориям (проверка алфавита) 
plants = [
    {"id": 1, "title": "Томаты", "category": "огород", "amount": 12, "completed": False},
    {"id": 2, "title": "Яблони", "category": "сад", "amount": 3, "completed": True},
    {"id": 3, "title": "Морковь", "category": "огород", "amount": 40, "completed": False},
    {"id": 4, "title": "Смородина", "category": " сад ", "amount": 5, "completed": True},
]
stats = statistics(plants)
assert stats["amount_sum"] == 60
assert stats["by_category"] == {"огород": 52, "сад": 8}   # " сад " считается как "сад"
assert list(stats["by_category"]) == ["огород", "сад"]    # алфавитный порядок

# Поиск и статистика не меняют данные 
before = copy.deepcopy(plants)
find_records(plants, "то")
statistics(plants)
assert plants == before

# Строгие типы полей при проверке 
good = {"id": 1, "title": "А", "category": "Б", "amount": 0, "completed": False}
validate_records([good])

bad_records = [
    {"id": 1},                                    # не список
    [123],                                        # запись не словарь
    [{**good, "id": True}],                       # id - bool
    [{**good, "id": 0}],                          # id не положительный
    [{**good, "id": "1"}],                        # id - строка
    [{**good, "title": "   "}],                   # пустое название
    [{**good, "category": 5}],                    # категория не строка
    [{**good, "amount": -1}],                     # отрицательное количество
    [{**good, "amount": True}],                   # amount - bool
    [{**good, "amount": 1.5}],                    # amount - дробное
    [{**good, "completed": "false"}],             # completed - строка
    [{**good, "completed": 0}],                   # completed - число
    [good, {**good, "title": "В"}],               # повторный id
]
for data in bad_records:
    try:
        validate_records(data)
        raise AssertionError(f"Ожидали ValueError для {data}")
    except ValueError:
        pass

# Не хватает ключа
for key in good:
    broken = dict(good)
    del broken[key]
    try:
        validate_records([broken])
        raise AssertionError(f"Ожидали ValueError без ключа {key}")
    except ValueError:
        pass

# Дополнительные ключи допустимы
validate_records([{**good, "note": "что угодно"}])

print("test_logic: все проверки пройдены")
