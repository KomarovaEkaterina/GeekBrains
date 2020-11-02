# я не очень поняла идею с аналитикой, если честно.
# Там нужно было зановсить в списки по ключам только уникальные значения?
# Или нужно было сделать так, чтобы при совпадерии наименования товара суммировались цены и количества совпавших товаров?
# Сделала так, чтобы просто не добавлялись одинаковые значения в аналитику, если что переделаю.

num = 0  #  счетчик количества разных товаров
products = []  # список кортежей с товарами

while True:
    print("\n1 - ввести новый товар\n"
          "2 - получить аналитику по товарам\n"
          "3 - выйти из программы\n"
          "4 - вывести кортежи товаров")
    choice = int(input("Что хотите делать дольше? "))

    if choice == 3:
        break
    elif choice == 2:
        analytics = {'Название': [], 'Цена': [], 'Количество': [], 'ед': []}  # подозреваю, что нужно только проверять есть ли в списках такие же данные
        for itm in products:
            if itm[1].get('название') not in analytics.get('Название'):
                analytics['Название'].append(itm[1].get('название'))
            if itm[1].get('цена') not in analytics.get('Цена'):
                analytics['Цена'].append(itm[1].get('цена'))
            if itm[1].get('количество') not in analytics.get('Количество'):
                analytics['Количество'].append(itm[1].get('количество'))
            if itm[1].get('ед') not in analytics.get('ед'):
                analytics['ед'].append(itm[1].get('ед'))
        for key, value in analytics.items():
            print(key, ': ', value)

    elif choice == 1:
        name = input("\nВведите название товара: ")
        cost = float(input("Введите цену товара: "))
        amount = int(input("Введите количество товара: "))
        units = input("Введите единицы изменения товара: ")

        product = {"название": name, "цена": cost, "количество": amount, "ед": units}
        products.append((num + 1, product))

    elif choice == 4:
        print(f"\nВот такие товары внесены:")
        for prod in products:
            print(prod)

    else:
        print("Нужно ввести число с 1 до 3... Попробуйте заново!")
