string = input("Введите строку: ")

list_of_words = string.split()
for num, word in enumerate(list_of_words):
    if len(word) > 10:
        print(f"{num + 1}: {word[:10]}")
    else:
        print(f"{num + 1}: {word}")
