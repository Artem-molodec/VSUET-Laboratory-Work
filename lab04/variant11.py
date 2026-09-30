n = int(input("Введите n (n >= 0): "))
a = 0
while n < 0:
    print("Ошибка: n должна быть не меньше 0.")
    n = int(input("Введите n (n >= 0): "))

total_sum = 0

for i in range(1, n + 1):
    num = int(input(f"Введите {i}-ое число: "))
    
    if abs(num) <= 3:
        a += 1
        total_sum += num
        
print(f"Количество значений подходящих под условие: {a}")
print(f"Сумма значений: {total_sum}")