a = int(input("Введите начальное число: "))
b = int(input("Введите конечное число: "))


if a < b:
#Выводим по возрастанию(y - переменная счетчик, которая добавляет к a по 1)
    y = a
    while y <= b:
        print(y)
        y += 1
if a > b:
    y = a
    while y >= b:
        print(y)
        y -= 1
if a == b:
    print(a)