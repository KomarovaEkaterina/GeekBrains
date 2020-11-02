base = int(input("Введите время в секундах: "))

hours = base // 3600
ost_sec = base % 3600
minutes = ost_sec // 60
seconds = ost_sec % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")


