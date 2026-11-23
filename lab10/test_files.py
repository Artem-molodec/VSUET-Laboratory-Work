from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix

with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"
    
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]

    #1. Проверка таблицы 1х1 с 0
    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]
    
    #2. Пустой файл
    path.write_text("", encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError:
        pass #Пропуск ошибки для дальнешей работы
    else:
        assert False, "Ошибка не обнаружена"
    
    #3. Заголовок 0 3
    path.write_text('0 3', encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"
        
    #4. Заголвок 1 2, строка 1
    path.write_text("1 2\n1\n", encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError as error:
        assert "Строка 2" in str(error)
    else:
        assert False, "Ошибка не обнаружена"
        
    #5. Заголовок 1 2, строка 1 x
    path.write_text("1 2\n1 x\n", encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError as error:
        assert "Строка 2" in str(error)
    else:
        assert False, "Ошибка не обнаружена"
    
    #6. Заголовок 1 1, две строки данных
    path.write_text("1 1\n0\n0\n", encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"
        
    #7. Отсутствующий путь
    missing = Path(directory) / "net_file.txt"
    try:
        read_matrix(missing)
    except FileNotFoundError:
        pass
    else:
        assert False, "Ошибка не обнаружена"
        
print("Все проверки пройдены!")