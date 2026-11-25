"""Консольная программа «План посадки растений»."""

import json
from pathlib import Path

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    sorted_records,
    statistics,
)
from storage import load_records, save_records

DATA_FILE = Path(__file__).resolve().parent / "data.json"

MENU = """
=== План посадки растений ===
1. Показать записи
2. Добавить запись
3. Найти записи
4. Изменить статус
5. Удалить запись
6. Показать статистику
7. Сохранить данные
8. Выйти"""


# ---------- Ввод ----------

def read_text(prompt):
    """Спрашивает строку, пока она не станет непустой. Возвращает строку без пробелов по краям."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Значение не должно быть пустым")


def read_int(prompt, minimum):
    """Спрашивает целое число не меньше minimum, пока ввод не станет верным."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Нужно целое число")
            continue
        if value < minimum:
            print(f"Число не может быть меньше {minimum}")
            continue
        return value


# ---------- Вывод ----------

def format_record(record):
    status = "посажено" if record["completed"] else "не посажено"
    return (f"{record['id']}. {record['title']} | {record['category']} | "
            f"{record['amount']} шт. | {status}")


def show_records(records):
    if not records:
        print("Нет записей")
        return
    for record in sorted_records(records):
        print(format_record(record))


def show_statistics(records):
    stats = statistics(records)
    print(f"Всего записей: {stats['total']}")
    print(f"Выполнено: {stats['completed']}")
    print(f"Не выполнено: {stats['not_completed']}")
    print(f"Сумма количества: {stats['amount_sum']} шт.")
    print("По категориям:")
    if not stats["by_category"]:
        print("  нет данных")
    for category, total in stats["by_category"].items():
        print(f"  {category}: {total} шт.")


# ---------- Действия меню ----------

def action_add(records):
    title = read_text("Название: ")
    category = read_text("Категория: ")
    amount = read_int("Количество растений: ", 0)
    record = add_record(records, title, category, amount)
    print(f"Добавлена запись с ID {record['id']}")


def action_find(records):
    query = input("Что искать в названии: ")
    try:
        found = find_records(records, query)
    except ValueError as error:
        print(error)
        return
    if not found:
        print("Ничего не найдено")
    for record in found:
        print(format_record(record))


def action_status(records):
    record_id = read_int("ID записи: ", 1)
    while True:
        choice = input("Новый статус (1 - выполнено, 2 - не выполнено): ").strip()
        if choice in ("1", "2"):
            break
        print("Введите 1 или 2")
    if set_completed(records, record_id, choice == "1"):
        print("Статус изменён")
    else:
        print("Запись с таким ID не найдена")


def action_delete(records):
    record_id = read_int("ID записи: ", 1)
    answer = input("Удалить запись? Введите «да» для подтверждения: ").strip().lower()
    if answer != "да":
        print("Удаление отменено")
        return
    if delete_record(records, record_id):
        print("Запись удалена")
    else:
        print("Запись с таким ID не найдена")


def save(records):
    """Сохраняет данные. Возвращает True только после успешной записи."""
    try:
        save_records(DATA_FILE, records)
    except (OSError, ValueError) as error:
        print(f"Не удалось сохранить: {error}")
        return False
    print("Данные сохранены в data.json")
    return True


def confirm_exit(records):
    """Спрашивает про сохранение. Возвращает True, если можно выходить."""
    while True:
        answer = input("Сохранить данные перед выходом? (да/нет): ").strip().lower()
        if answer == "да":
            return save(records)     # при ошибке записи вернём False и останемся в меню
        if answer == "нет":
            return True
        print("Ответьте «да» или «нет»")


# ---------- Запуск ----------

def load_start():
    """Загружает data.json. Возвращает список записей или None, если запуск нужно прекратить."""
    try:
        return load_records(DATA_FILE)
    except FileNotFoundError:
        print("Файл data.json не найден, начинаем с пустого списка")
        return []
    except UnicodeDecodeError:
        print("Ошибка: data.json не в кодировке UTF-8. Файл не изменён.")
    except json.JSONDecodeError as error:
        print(f"Ошибка JSON в data.json (строка {error.lineno}). Файл не изменён.")
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}. Файл не изменён.")
    except OSError as error:
        print(f"Ошибка доступа к data.json: {error}")
    return None


def main():
    records = load_start()
    if records is None:
        return

    while True:
        print(MENU)
        command = input("Команда: ").strip()
        if command == "1":
            show_records(records)
        elif command == "2":
            action_add(records)
        elif command == "3":
            action_find(records)
        elif command == "4":
            action_status(records)
        elif command == "5":
            action_delete(records)
        elif command == "6":
            show_statistics(records)
        elif command == "7":
            save(records)
        elif command == "8":
            if confirm_exit(records):
                break
        else:
            print("Неизвестная команда, выберите число от 1 до 8")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nВвод прерван, несохранённые данные потеряны")
