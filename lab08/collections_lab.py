text = input("Введите текст: ")

def word_counts(text):
    words = text.lower().split()
    
    counts = {}
    
    for word in words:
        word = word.strip(".,!?;:")
        #Проверяем что слово не пустое
        if word:
            #Перебираем слова и считаем повторения этих слов, а [word] это ключ
            counts[word] = counts.get(word, 0) + 1
            
    return counts 
counts = word_counts(text)   
print(counts)
#выводим пары по алфавиту
def word_pair(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")
#вызываем функцию для работы        
word_pair(counts)

first = input("Введите первый список строк: ").split()
second = input("Введите второй список строк: ").split()
#Проверка что списки в нижнем регистре
if all(text == text.lower() for text in first) and all(text == text.lower() for text in second):
    def common_topics(first, second):
        #Преврашаем списки во множества
        first_set = set(first)
        second_set = set(second)
        #Получаем новое множетсво из общих элементов
        total_set = first_set & second_set
        
        return sorted(total_set)
        
    def all_topics(first, second):
        #Преврашаем списки во множества
        first_set = set(first)
        second_set = set(second)
        #Получаем новое множество из уникальных элементов
        total_set = first_set | second_set
        
        return sorted(total_set)
    
    print(f"Общие строки из списков: {common_topics(first, second)}")
    print(f"Все уникальные строки: {all_topics(first, second)}")
else:
    print("Один из списков не в нижнем регистре!")


a = input("Введите название учебного предмета: ")
b = int(input("Введите количество часов: "))
#Создали словарь    
study = {
    "title": a,
    "hours": b
}
#меняем кол-во часов на новое
study["hours"] = int(input("Введите новое количество часов: "))
#Добавляем новый ключ completed
study["completed"] = False
#Создаем кортеж и распаковываем его в переменные
result = (study["title"], study["hours"])
title, hours = result

print(f"Название: {title}")
print(f"Часы: {hours}")

#Создаем свой список словарей с названиями
records = []
#Запрашиваем количество словарей в списке
n = int(input("Введите количество растений: "))

for i in range(n):
    title = input("Введите названия растения: ")
    category = input("Введите названия категории: ")
    amount = int(input("Введите количество: "))
    #Добавляем в список словарь с ключами и значениями из переменных
    records.append({
        "title": title,
        "category": category,
        "amount": amount
    })
    
def totals_by_category(records):
    #Создаем словарь
    totals = {}
    #Запускаем цикл по всем словарям
    for record in records:
        #Обращаемся к ключам словаря который щас выбран
        category = record["category"]
        amount = record["amount"]
        #Добавляем в словарь категорию и их числа эмоунт
        totals[category] = totals.get(category, 0) + amount
        
    return totals
#Вызываем функцию и выводим результат
totals = totals_by_category(records)
print(sorted(totals))

def titles_in_category(records, category):
    #Создаем новый список
    result = []
    
    for record in records:
        #Проверяем совпадает ли текущая категория с той, которую ищем
        if record["category"] == category:
            #Добавляем название/титул в список
            result.append(record["title"])
    
    return result

category = input("Введите категорию для поиска: ")

result = titles_in_category(records, category)
print(f"Найденные растения:  {result}")