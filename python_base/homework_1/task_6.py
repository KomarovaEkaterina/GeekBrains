start = float(input("Введите начальные показатели спортсмена: "))
end = float(input("Введите желаемый конечный результат: "))

day = 1
print(f"{day}-й день: {start:.2f}")
while start < end:
    day += 1
    start = start + start * 0.1
    print(f"{day}-й день: {start:.2f}")

print(f"Ответ: на {day}-й день спортсмен достигнет результатов. ")
