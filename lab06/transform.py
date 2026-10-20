start = []
for item in input("Введите отрицательные числа: ").split():
    start.append(int(item))
    
end = []
for a in start:
    end.append(abs(a))
        
print(f"Исходный список: {start}")
print(f"Конечный список: {end}")