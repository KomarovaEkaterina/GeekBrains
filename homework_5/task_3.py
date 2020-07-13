with open('task_3.txt', 'r', encoding='utf-8') as new_file:
    persons = [line.rstrip() for line in new_file.readlines()]
    surnames = ''
    all_sal = 0
    try:
        for i in range(len(persons)):
            person = persons[i].split()
            salary = float(person[1])
            all_sal += salary
            if salary < 20000:
                surnames += person[0] + ' '
        print(f'Средняя зарплата сотрудников: {round(all_sal / len(persons), 3)}')
        print(f'Сотрудники, получающие меньше 20тыс: {surnames}')
    except ValueError:
        print('Исходный файл сотрудников заполнен некорректно!')




