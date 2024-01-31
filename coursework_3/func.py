import json
import os

operations = os.path.abspath('../operations.json')


def get_dict_from_json(filename):
    """получаем данные из файла operation.json в виде списка словарей"""
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)


def get_executed(all_operations):
    """функция создает новый список словарей, включающих только перации типа EXECUTED"""
    for data in all_operations:
        if 'state' in data and data['state'] == 'EXECUTED':
            print(data)


#
# all_operations = get_dict_from_json(operations)
#
# get_executed(all_operations)