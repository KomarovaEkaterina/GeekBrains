from abc import ABC, abstractmethod


class MenuErr(ValueError):
    def __init__(self, txt):
        self.txt = txt


class Stock:
    def __init__(self):
        self.tools = {'Бугалтерия': {}, 'Разработка': {}, 'HR': {}}

    def show_products(self):
        for key, value in self.tools.items():
            print(f"Подразделение: {key}.")
            for tool, disc in value.items():
                print(f"\tУстройство: {tool}  Цена за штуку:{disc['price per one']}  На складе сейчас {disc['Amount in stock']}шт")

    def add_products(self, tool, amount, part):
        ky = f"{tool.brand} {tool.model}".lower()
        if ky in self.tools[part].keys():
            self.tools[part][ky]['Amount in stock'] += amount
        else:
            self.tools[part].update({ky: {'price per one': tool.price, 'Amount in stock': amount}})

    def del_products(self, name, amount, part):
        ky = f"{name}".lower()
        if self.tools[part][ky]['Amount in stock'] - amount <= 0:
            self.tools[part].pop(ky)
        else:
            self.tools[part][ky]['Amount in stock'] -= amount

    def moove_to_other_part(self, from_part, to_part, amount, name):
        ky = f"{name}".lower()
        if self.tools[from_part][ky]['Amount in stock'] - amount <= 0:
            deleted = self.tools[from_part].pop(ky)
        else:
            pr = self.tools[from_part][ky]['price per one']
            amnt = self.tools[from_part][ky]['Amount in stock']
            deleted = self.tools[from_part].pop(ky)
            self.tools[from_part].update({ky: {'price per one': pr, 'Amount in stock': (amnt - amount)}})
        if ky in self.tools[to_part].keys():
            self.tools[to_part][ky]['Amount in stock'] += amount
        else:
            self.tools[to_part].update({ky: deleted})
            self.tools[to_part][ky]['Amount in stock'] = amount


class OfficeEquipment(ABC):
    def __init__(self, brand, model, price):
        self.brand = brand
        self.price = price
        self.model = model

    @abstractmethod
    def get_pages(self, *smth):
        pass

    @abstractmethod
    def print_txt(self, *smth):
        pass


# печатает из эл. формата в бумажный
class Printer(OfficeEquipment):
    @staticmethod
    def get_pages(file):
        with open(file, 'r', encoding='utf-8') as new_file:
            lines = [line.rstrip() for line in new_file.readlines()]
        return lines

    def print_txt(self, file):
        lines = self.get_pages(file)
        for line in lines:
            print(line)
        print(f"Данный текст был распечатан устройством {self.brand} модели {self.model} из файла {file}\n")


# печатает из бумажного формата в электронный
class Scanner(OfficeEquipment):
    @staticmethod
    def get_pages():
        text = ''
        print("Введите текст, который хотите перевести в эл.формат. Для прекращения ввода нажмите 'Enter' на пустой строке.")
        while True:
            line = input()
            if line == '':
                break
            text += line + '\n'
        return text

    def print_txt(self, file):
        with open(file, 'w', encoding='utf-8') as new_file:
            new_file.write(self.get_pages())
        print(f"Введенный вами текст был сканирован устройством {self.brand} модели {self.model} и записан в файл {file}\n")


# печатает из бумажного формата в бумажный
class Xerox(OfficeEquipment):
    @staticmethod
    def get_pages():
        text = ''
        print("Введите текст, который хотите размножить. Для прекращения ввода нажмите 'Enter' на пустой строке.")
        while True:
            line = input()
            if line == '':
                break
            text += line + '\n'
        return text

    def print_txt(self, copies):
        text = self.get_pages()
        for i in range(copies):
            print(f"{i + 1}. {text}")

        print(f"Введенный вами текст был размножен на устройсте {self.brand} модели {self.model} {copies} раз(а)")


def input_all_stuff():
    new_brand = input("Введите бренд: ")
    new_model = input("Введите модель: ")
    while True:
        try:
            new_price = float(input("Введите цену за 1 единицу: "))
            break
        except ValueError:
            print("Цена вводится целыми или дробными числами. Попробуйте снова.")
    while True:
        try:
            new_amount = int(input("Введите количество устройств, которые добавляете: "))
            break
        except ValueError:
            print("Количество - это целое число. Попробуйте снова.")
    while True:
        try:
            is_checking = int(input("Введите 1, если хотете проверить устройство и 2, если желаете внести на склад без проверки: "))
            if is_checking < 1 or is_checking > 2:
                raise MenuErr("Выберете один из 2 вариантов: ")
            break
        except MenuErr as er:
            print(er)
        except ValueError:
            print("Допустимы только целые числа из предлоденных вариантов. Попробуйте ввод заново. ")
    return new_brand, new_model, new_price, new_amount, is_checking


def choose_part(text):
    while True:
        try:
            variant = int(input(f"{text}:\n"
                                "1 - Бугалтерия\n"
                                "2 - Разработка\n"
                                "3 - HR\n"))
            if variant < 1 or variant > 3:
                raise MenuErr("Доступны всего 3 подразделения! Выберете одно из них.")
        except MenuErr as oops:
            print(oops)
        except ValueError:
            print("На ввод доступны только целые числа представленные в меню.")
        else:
            if variant == 1:
                prt = 'Бугалтерия'
            elif variant == 2:
                prt = 'Разработка'
            else:
                prt = 'HR'
            return prt


my_stock = Stock()
while True:
    print("\nВведите номер меню для совершения действия.\n"
          "1 - добавить принтер на склад\n"
          "2 - добавить сканер на склад\n"
          "3 - добавить ксерокс на склад\n"
          "4 - удалить технику со склада\n"
          "5 - просмотреть технику на складе\n"
          "6 - перенести технику из одного подразделения в другое\n"
          "7 - выйти из склада")
    try:
        choose = int(input())
        if choose < 1 or choose > 7:
            raise MenuErr("Выберите число от 1 до 7 из вариантов меню!")
    except MenuErr as err:
        print(err)
    except ValueError:
        print("Выберите один из целочисленных вариантов меню!")
    else:
        if choose == 1:
            brnd, mdl, prc, am, chck = input_all_stuff()
            part = choose_part('Выберете подразделение для добавления устройтва')
            new_printer = Printer(brnd, mdl, prc)
            if chck == 1:
                while True:
                    try:
                        file_name = input("Введите название текстового файла из которого будем печатать без расширения (пример: my_file): ")
                        new_printer.print_txt(file_name + '.txt')
                        break
                    except FileExistsError:
                        print("Такого файла не существует! Попробуйте снова.")
            my_stock.add_products(new_printer, am, part)
            print("Принтер внесен на склад!")

        elif choose == 2:
            brnd, mdl, prc, am, chck = input_all_stuff()
            part = choose_part('Выберете подразделение для добавления устройтва')
            new_scanner = Scanner(brnd, mdl, prc)
            if chck == 1:
                file_name = input("Введите название файла, в который положим скан без расширения (пример: my_file): ")
                new_scanner.print_txt(file_name + '.txt')
            my_stock.add_products(new_scanner, am, part)
            print("Сканер внесен на склад!")

        elif choose == 3:
            brnd, mdl, prc, am, chck = input_all_stuff()
            part = choose_part('Выберете подразделение для добавления устройтва')
            new_xerox = Xerox(brnd, mdl, prc)
            if chck == 1:
                while True:
                    try:
                        count_copies = int(input("Введите количество копий: "))
                        new_xerox.print_txt(count_copies)
                        break
                    except ValueError:
                        print("Количество толжно быть целым числом! Попробуйте снова.")
            my_stock.add_products(new_xerox, am, part)
            print("Ксерокс внесен на склад!")

        elif choose == 4:
            while True:
                part = choose_part('Выберете подразделение для удаления устройтва')
                st = ''
                for nam, nm in my_stock.tools[part].items():
                    st += str(nam) + ' (' + str(nm['Amount in stock']) + '), '
                print(f"В этом подразделении находятся: {st[:-2]}")
                br_md = input("Введите бренд и модель устройства, которые хотите удалить со склада: ")
                if br_md == '':
                    break
                elif br_md not in my_stock.tools[part].keys():
                    print("Такого устройства в этом подразделении нет. Выберете другое подразделение.")
                else:
                    print("Внимание! Если вы введете число, превышающее количесво устройств этого типа на складе, то наименование полностью удалится!")
                    while True:
                        try:
                            num = int(input("Введите количество устройств, которые хотите удалить: "))
                            break
                        except ValueError:
                            print("Количество - это целое число больше 0. Попробуйте снова.")
                    my_stock.del_products(br_md, num, part)
                    print("Устройство успешно удалено со склада.")
                    break
        elif choose == 5:
            my_stock.show_products()
        elif choose == 6:
            while True:
                f_part = choose_part('Выберете подразделение из которого желаете перенести устройство')
                st = ''
                for nam, nm in my_stock.tools[f_part].items():
                    st += str(nam) + ' (' + str(nm['Amount in stock']) + '), '
                print(f"В этом подразделении находятся: {st[:-2]}")
                t_part = choose_part('Выберете подразделение в которое желаете перенести устройство')
                br_md = input("Введите бренд и модель устройства, которые хотите  перенести: ")
                if br_md == '':
                    break
                elif br_md not in my_stock.tools[f_part].keys():
                    print("Такого устройства в этом подразделении нет. Выберете другое подразделение.")
                else:
                    print(
                        "Внимание! Если вы введете число, превышающее количесво устройств этого типа в данном подразделении, то наименование полностью удалится!")
                    while True:
                        try:
                            number = int(input("Введите количество устройств, которые хотите перенести: "))
                            break
                        except ValueError:
                            print("Количество - это целое число больше 0. Попробуйте снова.")
                    my_stock.moove_to_other_part(f_part, t_part, number, br_md)
                    print("Устройство успешно перенесено!")
                    break
        elif choose == 7:
            break
