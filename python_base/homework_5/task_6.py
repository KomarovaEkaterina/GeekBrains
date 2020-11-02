import re

dict_with_subj = {}
with open('task_6.txt', 'r', encoding='utf-8') as file:
    lines = [line.rstrip() for line in file.readlines()]
    for line in lines:
        lesson = re.split(r':', line, maxsplit=1)[0]
        hours = sum([int(el) for el in re.findall(r'\d+', line)])
        dict_with_subj[lesson] = hours
print(dict_with_subj)
