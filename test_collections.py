from collections_lab import word_counts, common_topics, all_topics, totals_by_category, titles_in_category

records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
#Задание 1
assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
assert word_counts("!!!") == {}
assert word_counts("") == {}
assert word_counts(" sql  sql ") == {"sql": 2}

#Задание 2
first = ["python", "sql", "python"]
second = ["sql", "git"]
assert common_topics(first, second) == ["sql"]
assert all_topics(first, second) == ["git", "python"]
assert common_topics([], second) == []
assert all_topics([], ["b", "a", "a"]) == ["a", "b"]

#11 вариант
back = [record.copy() for record in records]

assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
assert titles_in_category(records, "основное") == ["A", "C"]
assert titles_in_category(records, "нет") == []
assert totals_by_category([]) == {}

print("Все проверки пройдены!")