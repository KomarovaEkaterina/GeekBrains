my_list = [7, 5, 3, 3, 2]
number = input("Введите натуральное число: ")

while number != '+':
    number = int(number)
    ind = -1

    for i in range(len(my_list)):
        if number > my_list[i]:
            ind = i
            break
        elif number == my_list[i]:
            ind = len(my_list) - 1 - my_list[::-1].index(number)

    if ind < 0:
        my_list.append(number)
    else:
        my_list.insert(ind, number)
        # my_list.insert(ind, float(number)) - для проверки

    print(f"Новый массив: {my_list}")

    number = input("Для завершения программы введите +\n"
                   "Чтобы продолжить, ведите элемент рейтинга (натуральное число): ")
