from itertools import cycle, count

my_count = count(3)
len_of_arr = 0
arr = []
while len_of_arr < 4:
    arr.append(next(my_count))
    len_of_arr += 1

my_cycle = cycle(arr)
count_cycles = 0
while count_cycles < 12:
    print(next(my_cycle))
    count_cycles += 1




