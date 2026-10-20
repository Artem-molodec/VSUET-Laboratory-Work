numbers = []
for item in input("Числа в список: ").split():
    numbers.append(int(item))


if numbers:
    maximum = max(numbers)
    
    for i, number in enumerate(numbers):
        if number == maximum:
            print(i)
else:
    print("Нет данных!")