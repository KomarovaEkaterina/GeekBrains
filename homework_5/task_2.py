try:
    with open('task_2.txt', 'r', encoding='utf-8') as new_file:
        strings = [line.rstrip() for line in new_file.readlines()]
        print(f"Всего в файле {len(strings)} строк.")
        for i in range(len(strings)):
            print(f"В строке №{i + 1} - {len(strings[i].split())} слов(а)")
except IOError:
    print('Указанного файла не существует.')
