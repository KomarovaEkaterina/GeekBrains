start_number = int(input("Введиде целое положительное число: "))
maximum = 0  # точно не будет числа меньше 0 - можно его использовать для начального значения максимума

while start_number % 10 > 0:
    number = start_number % 10
    start_number = start_number // 10
    if number > maximum:
        maximum = number

print(f"Максимальная цифра в числе: {maximum}")
