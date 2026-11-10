def sum_digits(number):
    c = abs(number)
    n = 0
    while c > 0:
        a = c % 10
        c //= 10
        n += a
    return n

def average(numbers):
    if numbers:
        a = len(numbers)
        sum_ = sum(numbers)
        b = sum_ / a
        return b   
    return None

def normalize_text(text):
    cleaned = text.lower().split()
    a = " ".join(cleaned)
    return a

def select_numbers(numbers, threshold):
    filtered = []
    for num in numbers:
        if abs(num) == threshold:
            filtered.append(num)
    return filtered