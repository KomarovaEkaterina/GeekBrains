from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def count_cloth(self):
        pass


class Coat(Clothes):
    @property
    def count_cloth(self):
        print(f"Для пальто необходимо примерно {round(self.size/6.5 + 0.5, 3)}м ткани.")
        return self.size/6.5 + 0.5


class Costume(Clothes):
    @property
    def count_cloth(self):
        print(f"Для костюма необходимо примерно {round(2 * self.size + 0.3, 3)}м ткани.")
        return 2 * self.size + 0.3


while True:
    try:
        h = float(input("Введите высоту клиента в метрах: "))
        v = float(input("Введите европейский размер одежды клиента: "))

        print(f"Всего потребуется примерно {round(Coat(v).count_cloth + Costume(h).count_cloth,3)}м ткани для пошива пальто и костюма.")

        break

    except ValueError:
        print("На ввод допускаются только целые и дробные числа. Попробуйте снова.")

