n = int(input("Введите n(n >= 1): "))
while n < 1:
    print("Ошибка: n должна быть не меньше 1.")
    n = int(input("Введите n(n >= 1): "))
#Первое число это n, которое мы сами ввели(n - это количество чисел)    
first_num = int(input("Введите 1-ое число: "))

total_sum = first_num
if first_num > 0:
    counter = 1
else:
    counter = 0
max_value = first_num

for i in range(2, n + 1):
    num = int(input(f"Введите {i}-ое число: "))

    total_sum += num
    if num > 0:
        counter += 1
    if num > max_value:
        max_value = num
        
print(f"Сумма: {total_sum}")
print(f"Количество положительных чисел: {counter}")
print(f"Максимальное число: {max_value}") 