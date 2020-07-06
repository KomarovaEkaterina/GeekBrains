# Решение через списки

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]  # это можно и не задавать, на него все равно проверки нет, очень определяю по статочному принципу

month = int(input("Введите месяц целым числом: "))
while month > 12 or month < 1:
    month = int(input("Месяцев всего 12. Введите месяц целым числом с 1 до 12: "))

if month in winter:
    print(f"{month}-й месяц - это зима")
elif month in spring:
    print(f"{month}-й месяц - это весна")
elif month in summer:
    print(f"{month}-й месяц - это лето")
else:
    print(f"{month}-й месяц - это осень")
