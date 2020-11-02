len_of_list = int(input("Введите целое количество элементов в списке: "))

while len_of_list <= 0:
    len_of_list = int(input("Необходимо ввести целое число больше 0. Попробуйте снова: "))

my_list = []  # создадим пустой лист, чтобы потом его заполнить значениями
for num in range(len_of_list):
    new_el = input(f"Введите значение элеманта №{num + 1} ")
    my_list.append(new_el)

a = 0  # переменная для хранения текущего этемента списка при измененеии мест
for i in range(1, len_of_list, 2):  # вы вроде на вебинаре говорили, что можно пользоваться range
    a = my_list[i]
    my_list[i] = my_list[i - 1]
    my_list[i - 1] = a


print(f"После выполнения программы список стал выглядеть так: {my_list}")
