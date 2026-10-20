numbers = []
for part in input("Введите числа: ").split():
    numbers.append(int(part))
    
a = len(numbers)
b = sum(numbers)
if numbers:
    c = min(numbers)
    d = max(numbers)
    sred = b / a 
    
    print(f"Количество чисел: {a}")
    print(f"Сумма чисел: {b}")
    print(f"Минимум в списке: {c}")
    print(f"Максимум в списке: {d}")
    
    
else:
    print("Нет данных!")