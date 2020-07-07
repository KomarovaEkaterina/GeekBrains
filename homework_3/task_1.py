def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Ошибка! Деление на 0 невозможно."


while True:
    try:
        dividend = float(input("Введите делимое: "))
        divider = float(input("Введите делитель: "))
        print(f"Результат выполнения функции: {division(dividend, divider)}")
        break
    except ValueError:
        print("Введены недопустимые символы, попробуйте снова.\n")


