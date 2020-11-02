my_list = [2, True, 'test', 3.5, None, (2, 3), {2: 1, 3: 4}, complex(7, 8), tuple('вася'), [1, 2, 3], b'text']

for num, el in enumerate(my_list):
    print(f"Элемент №{num + 1}: {type(el)}")  # делаю + 1 к номеру элемента, чтобы при выводе не было 0 индекса.

