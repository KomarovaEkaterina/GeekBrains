class MyOwnZero(Exception):
    def __init__(self, err_message):
        self.err_message = err_message


while True:
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        if b == 0:
            raise MyOwnZero("Деление на 0 невозможно!")
    except ValueError:
        print("На вход допускаются только числа. Плпробуйте ввести снова.")
    except MyOwnZero as err:
        print(f"{err}\nДелитель должен быть отличен от 0. Попробуйте снова.")
    else:
        print(f"Результат деления: {(a / b):.2}")
        break
