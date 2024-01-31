import json
import os

operations = os.path.abspath('../operations.json')


def get_dict_from_json(filename):
    """получаем данные из файла по пути filename в виде списка словарей"""
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)

