from table import row_sums, column_sums, diagonal_pattern, transform

try:
    #Запрашиваем размеры таблицы
    rows = int(input("Введите количество строк: "))
    columns = int(input("Введите количество столбцов: "))
    
    matrix = []
    #Создаем саму табличку
    for _ in range(rows):
        #Создаем строчку со своими значениями
        row = [int(number) for number in input("Строка таблицы: ").split()]
        #Проверяем что чисел в строке столько же сколько столбов
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел!")
            row = [int(number) for number in input("Строка таблицы: ").split()]
        matrix.append(row)
        
    print("Сумма каждой строки: ", row_sums(matrix))
    print("Сумма каждого столбца: ", column_sums(matrix))
    
    size = int(input("Введите размер: "))
    if size >= 1:
        #Перебираем каждую строчку и * распаковываем их и сразу выводим
        for line in diagonal_pattern(size):
            print(*line)
    else:
        print("Ввели размер меньше 1!")
    
    print("Исходная таблица: ")
    #Проверяем что таблица не пустая
    if matrix:
        for line in matrix:
            print(*line)
    else:
        print([])
        
    print("Преобразованная таблица: ")
    new_matrix = transform(matrix)
    if new_matrix:
        for line in new_matrix:
            print(*line)
    else:
        print([])
        
#Проверяем что ввели число а не буквы
except ValueError:
    print("Нужно ввести целое число!")