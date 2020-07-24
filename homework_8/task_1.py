from datetime import datetime


class Data:
    def __init__(self, date_as_string):
        self.date_as_string = date_as_string

    @classmethod
    def get_numbers(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if cls.check_number(day, 'day') != 0:
            print('Валидация числа не пройдена. Изменено на 30.')
            day = 30
        if cls.check_number(month, 'month') != 0:
            print('Валидация месяца не пройдена. Изменено на 12.')
            month = 12
        if cls.check_number(year, 'year') != 0:
            print(f'Валидация года не пройдена. Изменено на {datetime.now().year}.')
            year = datetime.now().year
        data = cls(f'{day:02}-{month:02}-{year:04}')
        return data


    @staticmethod
    def check_number(number, tp):
        if tp == 'day':
            if number > 30 or number < 1:
                return 1
        elif tp == 'year':
            if number > datetime.now().year or number < 1:
                return 1
        elif tp == 'month':
            if number > 12 or number < 1 or number == 2:
                return 1
        return 0


print("Данная программа валидирует даты.\n"
      "Пропускаются даты начиная с 01-01-0001 и до 30.12 текущего года.\n"
      "Недопустимы 31 числа каждого месяца - они не пройдут валидацию.\n"
      "Февраль тоже никто не любит, поэтому он также считается недопустимым месяцем.\n"
      "В случае непрохождения валидации введенная вами дата изменится на 30.12 текущего года.\n")
while True:
    try:
        d = int(input('Введите день: '))
        m = int(input('Введите месяц: '))
        y = int(input('Введите год: '))
    except ValueError:
        print('На вход допускаются только целые числа.')
    else:
        dt = Data.get_numbers(f'{d}-{m}-{y}')
        print(f'\nПосле прохождения валидации ваша дата выглядит так: {dt.date_as_string}')
        break




