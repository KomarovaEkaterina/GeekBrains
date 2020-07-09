from sys import argv


def count_salary(production, rate, bonus):
    salary = (production * rate) + bonus
    return salary


try:
    print(f"Зарплата сотрудника: {count_salary(float(argv[1]), float(argv[2]), float(argv[3]))}")
except ValueError:
    print("Вы ввели некорректный аргумент. Допускаются только целые и дробные числа.")
except IndexError:
    print("При выполнении данного скрипта необходимо указать 3 аргумента. ")

