import json


def get_dict_from_json(filename):
    """Получаем данные из файла operation.json в виде списка словарей"""
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)


def get_executed(all_operations):
    """Функция создает новый список словарей, включающих только операции типа EXECUTED"""
    operations = []
    for data in all_operations:
        if 'state' in data and data['state'] == 'EXECUTED' and 'from' in data:
            operations.append(data)
    return operations


def sort_operations(operations):
    """Сортирует список по дате в порядке убывания по дате"""
    return sorted(operations, key=lambda operation: operation['date'], reverse=True)


def five_operations(operations):
    """Выводит 5 последний платежей"""
    return operations[:5]


def formatter_date(operations):
    """Получает на вход дату в формате ГГГГ-ММ-ДДTЧЧ:ММ:СС.0000 и
    форматирует дату к виду ДД.ММ.ГГГГ"""
    date_lst = operations['date'].split('T')
    new_date = date_lst[0].split('-')
    return '.'.join(new_date[::-1])


def formatter_from(pay):
    """Маскирует отправителя платежа"""
    format_pay = pay.split()
    name = ' '.join(format_pay[:-1])
    number = ''.join(format_pay[-1])
    if len(format_pay[-1]) < 17:
        return f'{name} {number[0:4]} {number[4:6]}** **** {number[-5:-1]}'
    return f'{name} {'*' * 16}{number[-5:-1]}'


def formatter_to(pay):
    """Маскирует получателя платежа"""
    format_pay = pay.split()
    name = ' '.join(format_pay[:-1])
    number = ''.join(format_pay[-1])
    if len(format_pay[-1]) < 17:
        return f'{name} {number[0:4]} {number[4:6]}** **** {number[-5:-1]}'
    return f'{name} {'*' * 16}{number[-5:-1]}'
