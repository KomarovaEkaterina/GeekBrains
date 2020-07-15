class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} начала двиение.")

    def stop(self):
        print(f"Машина {self.name} остановилась.")

    def turn(self, direction):
        print(f"Машина {self.name} повернула на{direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля: {self.speed}км/ч.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость {self.speed}км/ч. Привышение! Убавьте скорость!")
        else:
            print(f"Скорочть автомобиля {self.speed} - в пределах нормы.")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость {self.speed}км/ч. Привышение! Убавьте скорость!")
        else:
            print(f"Скорочть автомобиля {self.speed} - в пределах нормы.")


class PoliceCar(Car):
    pass


a = Car(60, 'red', 'Lada', False)
a.go()
a.turn('право')
a.stop()
print('\n')

b = TownCar(80, 'white', 'Subaru', False)
print(f"Машина {b.name}, цвета {b.color}")
b.go()
b.show_speed()
b.turn('лево')
print('\n')

c = WorkCar(50, 'black', 'Toyota', False)
print(f"Машина {c.name}, цвета {c.color}")
c.go()
c.show_speed()
c.stop()
print('\n')


