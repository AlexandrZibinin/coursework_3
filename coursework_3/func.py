import json


def get_dict_from_json(filename):
    """получаем данные из файла operation.json в виде списка словарей"""
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)


def get_executed(all_operations):
    """функция создает новый список словарей, включающих только операции типа EXECUTED"""
    operations = []
    for data in all_operations:
        if 'state' in data and data['state'] == 'EXECUTED':
            operations.append(data)
    return operations


def sort_operations(operations):
    """сортирует список по дате в порядке убывания"""
    return sorted(operations, key=lambda operation: operation['date'], reverse=True)


def five_operations(operations):
    """выводит 5 последний платежей"""
    return operations[:5]


def formatter_date(operations):
    date_lst = operations['date'].split('T')
    new_date = date_lst[0].split('-')
    return '.'.join(new_date[::-1])

# executed_operations = get_executed(get_dict_from_json(operations))
# sort_operation = sort_operations(executed_operations)
# # print(five_operations(sort_operation))
# for i in five_operations(sort_operation):
#     print(formatter_date(i))
#


#
# all_operations = get_dict_from_json(operations)
#
# get_executed(all_operations)
# получить словарь выполненных операций
# отсортировать словарь по дате
# вывести 5 последних операций
# - Операции разделены пустой строкой.
# - Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018).
# - Сверху списка находятся самые последние операции (по дате).
# - Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
# - Номер счета замаскирован и не отображается целиком в формате  **XXXX
# (видны только последние 4 цифры номера счета).
