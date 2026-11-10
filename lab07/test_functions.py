from functions import average, normalize_text, sum_digits, select_numbers
# Проверка sum_digits
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
# Проверка average
assert average([]) is None
assert average([2, 4, 6]) == 4
# Проверка normalize_text
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
# Проверка select_numbers (11 вариант)
assert select_numbers([2, -2, 2, 5], 2) == [2, -2, 2]
assert select_numbers([], 2) == []
assert select_numbers([1, 2, -1, -2, 3], 2) == [2, -2]
# Проверка, что список не изменится
numbers = [-5, 0, 2, 5]
original = numbers.copy()

select_numbers(numbers, 2)

assert numbers == original

print("Базовые проверки пройдены")