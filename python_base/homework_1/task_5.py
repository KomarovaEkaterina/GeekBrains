income = int(input("Введите доходы фирмы: "))
expenses = int(input("Введите расходы фирмы: "))

if expenses > income:
    print("Фирма работает в убыток - издержки больше, чем доходы.")
elif expenses == income:
    print("Фирма работает в 0 - издержки ровны доходам.")
else:
    revenue = (income - expenses) / income
    print("Фирма работает с прибылью - издержки меньше, чем доходы. ")
    print(f"Рентабельность выручки ровна {revenue:.3f}")

    persons = int(input("Сколько человек работает в фирме? "))
    profit_for_person = (income - expenses) / persons
    print(f"Прибыль фирмы на одного сотрудника ровна {profit_for_person:.3f}")
