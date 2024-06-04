import json
from datetime import datetime


=======


def mask_card_number(card_number):
    """Маскирует номер карты."""
    return f"XXXX XX** **** {card_number[-4:]}"

def mask_account_number(account_number):
    """Маскирует номер счета."""
    return f"**{account_number[-4:]}"

def format_operation(operation):
    """Форматирует данные об операции для вывода."""

    date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%d.%m.%Y')
    amount, currency = operation['operationAmount']['amount'], operation['operationAmount']['currency']['code']
=======
    date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d.%m.%Y')
    amount, currency = operation['operationAmount']['amount'], operation['operationAmount']['currency']


    if 'from' in operation:
        from_value = mask_card_number(operation['from']) if 'card' in operation['from'] else mask_account_number(
            operation['from'])
    else:
        from_value = 'Неизвестно'

    to_value = mask_card_number(operation['to']) if 'card' in operation['to'] else mask_account_number(operation['to'])

    return f"""{date} {operation['description']}
{from_value} -> {to_value}
{amount} {currency}"""


def get_last_operations(operations):
    """Возвращает список из 5 последних выполненных операций."""
    executed_operations = []
    for op in operations:
        if op['state'] == 'EXECUTED':
            executed_operations.append(op)
=======
def get_last_operations(filename='operations.json'):
    """Возвращает список из 5 последних выполненных операций."""
    with open(filename, 'r', encoding='utf-8') as f:
        operations = json.load(f)

    executed_operations = []
    for op in operations:
        try:
            if op['state'] == 'EXECUTED':
                executed_operations.append(op)
        except KeyError:
            print(f"Ошибка: Отсутствует ключ 'state' в операции {op['id']}")

    executed_operations.sort(key=lambda x: x['date'], reverse=True)
    return [format_operation(op) for op in executed_operations[:5]]

if __name__ == '__main__':

    operations = [
        # ... (Your operations data)
    ]
    for operation in get_last_operations(operations):
        print(operation)
        print()
=======
    for operation in get_last_operations():
        print(operation)
        print()