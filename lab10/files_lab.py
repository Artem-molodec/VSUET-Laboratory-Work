def read_matrix(path):
    with open(path, 'r', encoding="utf-8") as file:
        text = file.read()
        if text.endswith("\n"): #Если текст заканчивается переводом строки, отрезаем последнюю часть
            text = text[:-1]
        if text == "": #Проверяем что файл пустой и реагируем на ошибку
            raise ValueError("файл пустой!")
        #Режем текст по \n
        lines = text.split("\n")
        header = lines[0].split() #Берем заголовок из lines и режем пробелом
        if len(header) != 2:
            raise ValueError("Строка 1: нужно 2 числа(строки и столбцы)")
        
        try: #Проверяем что размеры это целые числа
            rows, columns = int(header[0]), int(header[1])
        except ValueError:
            raise ValueError("Строка 1: размеры должны быть целыми числами!") from None
        if rows <= 0 or columns <= 0:
            raise ValueError("Строка 1: размеры должны быть положительными!") from None
        #Обрезаем все, кроме загаловка
        texts = lines[1:]
        #Проверяем что количество чисел в строке равно ведденым
        if len(texts) < rows:
            raise ValueError(f"Ожидалось чисел: {rows}, Получено: {len(texts)}")
        if len(texts) > rows:
            raise ValueError(f"Ввели лишние числа!")
        
        matrix = []
        #Перебираем пары строка и ее номер
        for number, line in enumerate(texts, start = 2):
            #Режем строку на список подстрок
            parts = line.split()
            if len(parts) != columns:
                raise ValueError(f"Строка {number}: Ожидалось чисел: {columns}, Полученно чисел: {len(parts)}")
        #Проверяем что числа целые
            try:
                row = [int(part) for part in parts]
            except ValueError:
                raise ValueError(f"Строка {number}: найдено не целое число")
            matrix.append(row)    
            
        return matrix
#Считаем сумму значений последнего столбца
def selected_sum(matrix):
    total = 0
    for row in matrix:
        total += row[-1]
    return total
      