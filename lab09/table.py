def row_sums(matrix):
    if not matrix:
        return []
    else:
        sums = []
        for row in matrix:
            a = 0
            for value in row:
                a += value
            sums.append(a)
        return sums

def column_sums(matrix):
    if not matrix:
        return []
    else:
        sums = []
        #Перебираем столбцы через длину первой строчки
        for column in range(len(matrix[0])):
            a = 0
            for row in matrix:
                a += row[column]
            sums.append(a)
        return sums

def diagonal_pattern(size):
    matrix = []
    for row in range(size):
        a = []
        for column in range(size):
            if row == column:
                a.append(0)
            elif row < column:
                a.append(1)
            else:
                a.append(2)
        matrix.append(a)
    return matrix

def transform(matrix):
    result = []
    #Перебираем строки в матрице
    for row in matrix:
        new_row = []
        #Перебираем значения в данной строке
        for value in row:
            if value % 2 == 0:
                new_row.append(value // 2)
            else:
                new_row.append(value)
        result.append(new_row)
    return result