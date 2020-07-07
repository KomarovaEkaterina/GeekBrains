def int_func(word):
    return word.title()


while True:
    str_of_words = input("\nВведите слово или строку из слов в маленьком регистре латинскими буквами: ")
    arr_of_words = str_of_words.split()
    res = ''
    flag = 0
    for word in arr_of_words:
        for letter in word:
            if ord(letter) > 122 or ord(letter) < 97:
                print(f"Ошибка! В слове '{word}' есть недопустимые символы или заглавные буквы. "
                      f"На вход допускаются только латинские буквы в нижнем регистре. Попробуйте снова.")
                flag += 1
                break
        if flag > 0:
            continue
        else:
            res += int_func(word) + ' '
    if flag == 0:
        print(f"\nИтоговая строка: {res}")
        break

