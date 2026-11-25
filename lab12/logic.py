KEYS = ("id", "title", "category", "amount", "completed")

def validate_records(records):
    
    if not isinstance(records, list):
        raise ValueError("Корень должен быть списком")

    seen_ids = set()
    for number, item in enumerate(records, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Запись {number}: должна быть объектом")
        for key in KEYS:
            if key not in item:
                raise ValueError(f"Запись {number}: нет поля {key}")

        if type(item["id"]) is not int or item["id"] <= 0:
            raise ValueError(f"Запись {number}: id должен быть положительным целым")
        if item["id"] in seen_ids:
            raise ValueError(f"Повторяющийся id: {item['id']}")
        seen_ids.add(item["id"])

        for key in ("title", "category"):
            value = item[key]
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"Запись {number}: {key} должен быть непустой строкой")

        if type(item["amount"]) is not int or item["amount"] < 0:
            raise ValueError(f"Запись {number}: amount должен быть целым числом не меньше 0")
        if type(item["completed"]) is not bool:
            raise ValueError(f"Запись {number}: completed должен быть true или false")


def sorted_records(records):
    """Возвращает НОВЫЙ список записей по возрастанию id. Исходный список не меняется."""
    return sorted(records, key=lambda record: record["id"])


def add_record(records, title, category, amount):
    #Добавляет запись В КОНЕЦ СПИСКА records (список изменяется)

    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название не должно быть пустым")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Категория не должна быть пустой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество должно быть целым числом не меньше 0")

    new_id = 1
    for record in records:
        if record["id"] >= new_id:
            new_id = record["id"] + 1

    record = {
        "id": new_id,
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record


def find_records(records, query):
    #Ищет записи, в названии которых есть подстрока query (без учёта регистра)

    if not isinstance(query, str) or not query.strip():
        raise ValueError("Поисковый запрос не должен быть пустым")
    needle = query.strip().casefold()
    found = []
    for record in sorted_records(records):
        if needle in record["title"].casefold():
            found.append(record)
    return found


def set_completed(records, record_id, completed):
    #Устанавливает статус записи с данным id (список изменяется).

    if type(completed) is not bool:
        raise ValueError("Статус должен быть True или False")
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    #Удаляет запись с данным id (список изменяется). Остальные id не меняются.

    for index, record in enumerate(records):
        if record["id"] == record_id:
            del records[index]
            return True
    return False


def statistics(records):
    #Считает статистику. Исходный список НЕ меняется
    completed = 0
    amount_sum = 0
    sums = {}
    for record in records:
        if record["completed"]:
            completed += 1
        amount_sum += record["amount"]
        category = record["category"].strip()
        sums[category] = sums.get(category, 0) + record["amount"]

    by_category = {}
    for category in sorted(sums):
        by_category[category] = sums[category]

    return {
        "total": len(records),
        "completed": completed,
        "not_completed": len(records) - completed,
        "amount_sum": amount_sum,
        "by_category": by_category,
    }