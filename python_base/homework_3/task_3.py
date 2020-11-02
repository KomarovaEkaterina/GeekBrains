def my_func(num1, num2, num3):
    res = num1 + num2 + num3 - min(num1, num2, num3)
    return res


while True:
    try:
        a, b, c = [float(i) for i in input("Введите 3 числа через пробел: ").split()]
        print(f"Сумма двух максимальных чисел: {my_func(a, b, c)}")
        break
    except ValueError:
        print("Введен недопустимый символ. Повторите попытку.\n")
