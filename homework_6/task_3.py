class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        full_name = self.surname + " " + self.name
        print(f"Полное имя сотрудника: {full_name}")

    def get_total_income(self):
        total_income = sum(self._income.values())
        print(f"Ежемесячный доход с учетом премии: {total_income}")


while True:
    try:
        a = Position(input("Введите имя сотрудника: "),
                     input("Введите фамилию сотрудника: "),
                     input("Введите должность сотрудника: "),
                     float(input("Введите заработную плату сотрудника: ")),
                     float(input("Введите ежемесячный бонус сотрудника: ")))
        a.get_full_name()
        a.get_total_income()
        break
    except ValueError:
        print("Недопустимо вводить буквы в зп и премию сотрудника. Попробуйте снова.")
