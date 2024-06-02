import json
from datetime import datetime


def mask_card_number(card_number):
    """Маскирует номер карты."""
    return f"XXXX XX** **** {card_number[-4:]}"


def format_operation(operation):
    """Форматирует данные об операции для вывода."""
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