from table import row_sums, column_sums, diagonal_pattern, transform

a = [[1, 2, 3], [4, 5, 6]]
b = [[1], [-1], [0]]
c = [[-2, 0, 3], [4, -5, 6]]

assert row_sums(a) == [6, 15]
assert column_sums(a) == [5, 7, 9]

assert row_sums(b) == [1, -1, 0]
assert column_sums(b) == [0]

assert row_sums([]) == []
assert column_sums([]) == []

assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]

assert diagonal_pattern(1) == [[0]]
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

#Создаем копию таблицы по строкам, а не внешний(c.copy())
original_copy = [row.copy() for row in c]
transformed = transform(c)
assert transformed == [[-1, 0, 3], [2, -5, 3]]
assert c == original_copy

transformed[0][0] = 12345
assert c == original_copy

print("Все проверки пройдены!")