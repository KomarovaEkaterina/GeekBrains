def summa(res, flag):
    a = [i for i in input("Введите числа через пробел (для выхода введите q): ").split()]
    for i in range(len(a)):
        if a[i] != 'q':
            res += float(a[i])
        else:
            flag = False
    return res, flag


fl = True
sm = 0
while fl:
    try:
        sm, fl = summa(sm, fl)
        print(f"Сумма чисел ровна: {sm}")
    except ValueError:
        print("Введен недопустимый символ. Начните ввод строки заново.\n")

