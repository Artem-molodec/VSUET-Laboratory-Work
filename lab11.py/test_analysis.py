import json
import tempfile
from pathlib import Path

from analysis import validate_todos, completion_counts, top_users, leader_tasks, select_tasks
TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]

counts = completion_counts(TODOS)
assert counts == {5: 2, 10: 2}
assert top_users(counts) == [5, 10]
tasks = leader_tasks(TODOS, top_users(counts))
assert [t["id"] for t in tasks] == [1, 3, 4, 5]

# Пустой список
assert completion_counts([]) == {}
assert top_users({}) == []

# Только незавершённые задачи
only_false = [{"id": 1, "userId": 5, "title": "А", "completed": False}]
counts = completion_counts(only_false)
assert counts == {5: 0}
assert top_users(counts) == []
assert leader_tasks(only_false, []) == []

# Один лидер и несколько лидеров
assert top_users({5: 2, 10: 3}) == [10]
assert top_users({1: 3, 2: 3, 3: 1}) == [1, 2]

assert [t["id"] for t in select_tasks(TODOS, 5, 2)] == [5]
# Граница: id=5 не больше порога 5
assert select_tasks(TODOS, 5, 5) == []
assert [t["id"] for t in select_tasks(TODOS, 5, 4)] == [5]
# Неизвестный пользователь
assert select_tasks(TODOS, 99, 2) == []
# Пользователь есть, но совпадений нет
assert select_tasks(TODOS, 10, 4) == []

#Ошибки структуры 
bad_data = [
    {"id": 1},                                                      # не список
    [{"id": 1, "userId": 5, "title": "А", "completed": True},
     {"id": 1, "userId": 6, "title": "Б", "completed": True}],      # повторный id
    [{"id": 1, "title": "А", "completed": True}],                   # нет userId
    [{"id": 1, "userId": 5, "title": "А", "completed": "false"}],   # completed - строка
    [{"id": True, "userId": 5, "title": "А", "completed": True}],   # id - bool
]
for data in bad_data:
    try:
        validate_todos(data)
        raise AssertionError(f"Ожидали ValueError для {data}")
    except ValueError:
        pass

chosen = select_tasks(TODOS, 5, 2)
with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "selected.json"
    with open(path, "w", encoding="utf-8") as file:
        json.dump(chosen, file, ensure_ascii=False, indent=2)
    with open(path, encoding="utf-8") as file:
        restored = json.load(file)
assert restored == chosen

print("Все тесты пройдены")