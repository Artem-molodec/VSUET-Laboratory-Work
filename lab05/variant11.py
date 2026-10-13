text = input("Введите текст: ")
count = 0
for stre in text.split():
    word = stre.strip(".,!?;:").lower()
    
    if word == "":
        continue
    
    if 3 <= len(word) <= 5:
        print(word)
        count += 1
        
if count == 0:
    print("Нет совпадений =(")
print(count)