def user_info(first_name, last_name, year_of_birth, city, email, phone):
    print(f"\nИмя: {first_name}\nФамилия: {last_name}\nГод рождения: {year_of_birth}\nГород проживания: {city}\nЭл.Почта: {email}\nНомер телефона: {phone}")


name = input("Имя пользователя: ")
surname = input("Фамилия пользователя: ")
year = input("Год рождения пользователя: ")
cty = input("Город проживания пользователя: ")
mail = input("Электоронная почта пользователя: ")
phone_number = input("Номер телефона пользователя: ")

print(user_info(name, surname, year, cty, mail, phone_number))
