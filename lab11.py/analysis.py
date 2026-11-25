
def validate_todos(data):
    #Проверка корня
    if not isinstance(data, list):
        raise ValueError("Корень должен быть списком!")
    
    unique_id = set()
    
    for i, item in enumerate(data):
        #Проверка что запись-словарь
        if not isinstance(item, dict):
            raise ValueError(f"Запись {i} не является объектом!")
        
        for key in ("id", "userId"):
            value = item.get(key)
            if type(value) is not int or value <= 0:
                raise ValueError(f"Запись {i}: поле {key} должно быть положительным числом")
        #Проверка на пустую строку title    
        title = item.get("title")
        if not isinstance(title, str) or not title.strip():
            raise ValueError(f"Запись {i}: title должен быть непустой строкой")
        #Проверка что completed логична
        mean = item.get("completed")
        if type(mean) is not bool:
            raise ValueError(f"Запись {i}: comleted должен быть логичным")
        #Проверка на уникальный id
        if item["id"] in unique_id: #Проверяем что он не встречался раньше
            raise ValueError(f"Повтроряющийся id: {item['id']}")
        unique_id.add(item["id"]) #Запоминаем для след проверкипо
        
def completion_counts(todos):
    counts = {}
    for todo in todos:
        user = todo["userId"]
        if user not in counts:
            counts.setdefault(user, 0)
        if todo["completed"]:
            counts[user] += 1
    return counts

def top_users(counts):
    if not counts:
        return []
    best = 0
    for user in counts:
        if counts[user] > best:
            best = counts[user]

    if best == 0:
        return []

    leaders = []
    for user in counts:
        if counts[user] == best:
            leaders.append(user)

    leaders.sort()
    return leaders


def leader_tasks(todos, leaders):
    result = []
    for todo in todos:
        if todo["userId"] in leaders and todo["completed"] == True:
            result.append(todo)
    return result

def select_tasks(todos, user_id, parameter=None):

    if parameter is None:

        raise ValueError("Для варианта 11 нужен числовой порог")

    result = []                          
    for todo in todos:                   
        if todo["userId"] != user_id:   
            continue                   
        if not todo["completed"]:        
            continue                    
        if todo["id"] <= parameter:     
            continue                     
        result.append(todo)              
    return result                        