my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"Исходный список: {my_list}")
print(f"Результат: {[el for el in my_list if my_list.count(el) == 1]}")
