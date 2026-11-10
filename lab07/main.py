from functions import sum_digits, average, normalize_text, select_numbers

value = int(input("Введите любое целое число: "))
result = sum_digits(value)
#sum_digits(value) - значение из value переходит в параметр number
print(f"Сумма цифр: {result}")

a = list(map(int,input("Введите числа: ").split()))
plan = average(a)
if plan != None:
    print(plan)
else:
    print("Нет данных")    
    
text = input("Текст: ")
aba = normalize_text(text)

print(aba)

threshold = int(input("Введите порог для списка: "))
selected = select_numbers(a, threshold)

print(selected)