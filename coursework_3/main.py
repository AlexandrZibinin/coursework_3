import os
from func import *


def main():
    filename = os.path.abspath('../operations.json')

    operations = get_dict_from_json(filename)

    operations = get_executed(operations)
    operations = sort_operations(operations)
    operations = five_operations(operations)

    for operation in operations:
        print(formatter_date(operation), operation['description'])
        print(f'{formatter_from(operation['from'])} -> {formatter_to(operation['to'])}')
        print(operation['operationAmount']['amount'], operation['operationAmount']['currency']['name'])
        print()


if __name__ == '__main__':
    main()
