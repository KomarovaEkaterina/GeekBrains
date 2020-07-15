class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self, mass_for_one=25, height=5):
        general_mass = self._length * self._width * mass_for_one * height / 1000
        print(f"Масса асфальта ровна {general_mass}т")


while True:
    try:
        a = Road(float(input(f"Введите длину дорожного полотна в метрах: ")), float(input(f"Введите ширину дорожного полотна в метрах: ")))
        a.count_mass()
        break
    except ValueError:
        print('На ввод допустимы только числа. Попробуйсте заново.')
