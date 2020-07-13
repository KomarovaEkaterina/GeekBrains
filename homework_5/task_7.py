import json

with open('task_7.1.txt', 'r', encoding='utf-8') as file:
    companies = [line.rstrip() for line in file.readlines()]
    all_com_with_profit = 0
    all_profit_without_damages = 0
    result_dict = {}
    result_profit_dict = {}
    result_list = []
    try:
        for i in range(len(companies)):
            company = companies[i].split()
            revenue = float(company[2])
            costs = float(company[3])
            profit = revenue - costs
            if profit >= 0:
                all_com_with_profit += 1
                all_profit_without_damages += profit
            result_dict[company[0]] = profit
        result_list.append(result_dict)
        result_profit_dict['average_profit'] = round(all_profit_without_damages / all_com_with_profit, 3)
        result_list.append(result_profit_dict)
        with open('task_7.2.json', 'w', encoding='utf-8') as new_file:
            print(json.dumps(result_list, indent=4))
            new_file.write(json.dumps(result_list, indent=4))
    except ValueError:
        print('Исходный файл с компаниями заполнен некорректно!')


