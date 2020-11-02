with open('task_1.txt', 'w', encoding='utf-8') as new_file:
    print("Вводите строки ниже. При вводе пустой строки запись закончится.")
    while True:
        new_str = input()
        if new_str == '':
            break
        else:
            new_file.write(new_str + '\n')
