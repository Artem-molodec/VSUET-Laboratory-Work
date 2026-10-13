word = input("Введите слово с пробелами: ")

word_prodel = word.split()
normalized = " ".join(word_prodel)

print(len(word))
print(len(normalized))
print(normalized)
print(len(word_prodel))