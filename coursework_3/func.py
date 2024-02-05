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
        if 'state' in data and data['state'] == 'EXECUTED' and 'from' in data:
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

def formatter_from(from_pay):
    format_from = from_pay.split()
    name = ' '.join(format_from[:-1])
    number = ''.join(format_from[-1])
    if len(format_from[-1]) < 17:
        return f'{name} {number[0:4]} {number[4:6]}** **** {number[-5:-1]}'
    return f'{name} {'*'* 16}{number[-5:-1]}'
