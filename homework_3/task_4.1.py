def my_func(x, y):
    step = 1
    for i in range(abs(y)):
        step *= x
    res = 1 / step
    return res


while True:
    try:
        a = float(input("Введите действительное число: "))
        b = int(input("Введите целое отрицательное число: "))
        if b >= 0:
            print("Второе число обязательно должно быть отрицательным! Введите все заново.\n")
            continue
        print(f"{a} в степени {b} = : {my_func(a, b)}")
        break
    except ValueError:
        print("Введен недопустимый символ. Повторите попытку.\n")
