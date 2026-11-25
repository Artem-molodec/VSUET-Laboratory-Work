import json
from pathlib import Path
from analysis import validate_todos, completion_counts, top_users, leader_tasks, select_tasks

Out = Path(__file__).resolve().parent

def read_int(prompt, minimum=1):
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

def main():

    try:
        with open(Out / "todos.json", encoding="utf-8") as file:
            todos = json.load(file)
        validate_todos(todos)
        
        counts = completion_counts(todos)
        leaders = top_users(counts)
        selected = leader_tasks(todos, leaders)
        
    except FileNotFoundError:
        print("Ошибка: файл todos.json не найден")
        return
    except UnicodeDecodeError:
        print("Ошибка: файл не в кодировке UTF-8")
        return
    except json.JSONDecodeError as error:
        print(f"Ошибка JSON в {error.lineno}")
        return
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return

    #Выводим сводку
    print("Количество выполненных задач:")
    for user in counts:
        print(f"  Пользователь {user}: {counts[user]}")
    if len(leaders) == 0:
        print("Лидеров нет")
    else:
        print("Лидеры:", ", ".join(str(user) for user in leaders))

    user_id = read_int("Введите user_id: ")
    threshold = read_int("Введите порог id: ", minimum = 0)
    chosen = select_tasks(todos, user_id, threshold)    
    
    #Сохранение, сюда доходим только если ошибок не было
    try:
        with open(Out / "leaders.json", "w", encoding="utf-8") as file:
            json.dump(selected, file, ensure_ascii=False, indent=2)
        with open(Out / "selected.json", "w", encoding="utf-8") as file:
            json.dump(chosen, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"Не удалось сохранить результаты: {error}")
        return
    print("Результаты сохранены в leaders.json и selected.json")

if __name__ == "__main__":
    main()