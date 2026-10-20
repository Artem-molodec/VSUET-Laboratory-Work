start = []
for item in input("Введите числа: ").split():
    number = int(item)
    if abs(number) <= 3:
        start.append(number)
    
    
print(f"Список в исходном порядке: {start}")
print(f"Количество чисел в списке: {len(start)}")
print(f"Сумма чисел: {sum(start)}")
print(f"Отсортированная копия: {sorted(start)}")        