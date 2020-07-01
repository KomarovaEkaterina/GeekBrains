seasons = {'Зима': [12, 1, 2],
           'Весна': [3, 4, 5],
           'Лето': [6, 7, 8],
           'Осень': [9, 10, 11]}

month = int(input("Введите месяц целым числом: "))
while month > 12 or month < 1:
    month = int(input("Месяцев всего 12. Введите месяц целым числом с 1 до 12: "))

for key, value in seasons.items():
    if month in value:
        print(f"{month}-й месяц - это {key}")
