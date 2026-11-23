from pathlib import Path

from files_lab import read_matrix, selected_sum
from table import row_sums, column_sums, diagonal_pattern

def read_positive_integer():
    while True:
        try:
            number = int(input("Введите целое положительное число: "))
        except ValueError:
            print("Ввели не целое число!")
            continue
        if number <= 0:
            print("Введеное число должно быть больше 0!")
            continue
        return number

print(read_positive_integer())

def main():
    folder = Path(__file__).resolve().parent
    source = folder / "matrix.txt"
    report = folder / "report.txt"
    
    try:
        matrix = read_matrix(source)
        
        row_text = " ".join(map(str, row_sums(matrix)))
        column_text = " ".join(map(str, column_sums(matrix)))
        report_text = (
            f"Суммы строк: {row_text}\n"
            f"Суммы столбцов: {column_text}\n"
            f"Результат варианта: {selected_sum(matrix)}\n"
        )
        with open(report, "w", encoding="utf-8") as file:
            file.write(report_text)
    except FileNotFoundError:
        print(f"Файл {source.name} не найден!")
    except UnicodeError:
        print("Файл не читается в кодировке UTF-8!")
    except ValueError as error:
        print(f"Ошибка формата {error}")
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
    else:
        print(f"Отчет записан в {report.name}")
        
        size = read_positive_integer()
        for line in diagonal_pattern(size):
            print(*line)
            
if __name__ == "__main__":
    main()