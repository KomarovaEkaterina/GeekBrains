import functools


def factorial(n):
    my_list = range(1, n)
    for i in my_list:
        yield functools.reduce((lambda x, y: x * y), my_list[:i])


while True:
    try:
        num_of_factorial = int(input("Введите число, факториал которого хотите получить: "))
        count = 1
        for el in factorial(num_of_factorial + 1):
            print(f"{count}! = {el}")
            count += 1
        break
    except ValueError:
        print("Введен некорректный символ. Введите целое число.")
