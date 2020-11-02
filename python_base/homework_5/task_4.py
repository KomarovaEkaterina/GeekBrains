from googletrans import Translator

translator = Translator()

with open('task_4.1.txt', 'r', encoding='utf-8') as start_file:
    with open('task_4.2.txt', 'w', encoding='utf-8') as new_file:
        lines = [line.rstrip() for line in start_file.readlines()]
        for line in lines:
            result = translator.translate(line, src='en', dest='ru')
            new_file.write(result.text + '\n')
