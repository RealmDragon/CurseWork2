import pytest
from operations import get_last_operations, mask_card_number, mask_account_number, format_operation

def test_mask_card_number():
    assert mask_card_number('5058 7000 7912 3456') == 'XXXX XX** **** 3456'

def test_mask_account_number():
    assert mask_account_number('40817810981234567890') == '**7890'

def test_format_operation_card_to_card():
    operation = {
        'date': '2019-08-26T10:50:58.294Z',
        'description': 'Перевод организации',
        'operationAmount': {'amount': '82771.72', 'currency': 'руб.'},
        'from': 'Visa Platinum 7000 7912 3456',
        'to': 'Maestro 1234 5678 9012'
    }
    expected_output = """26.08.2019 Перевод организации
XXXX XX** **** 3456 -> XXXX XX** **** 9012
82771.72 руб."""
    assert format_operation(operation) == expected_output

def test_format_operation_card_to_account():
    operation = {
        'date': '2019-08-26T10:50:58.294Z',
        'description': 'Перевод на счет',
        'operationAmount': {'amount': '82771.72', 'currency': 'руб.'},
        'from': 'Visa Platinum 7000 7912 3456',
        'to': '40817810981234567890'
    }
    expected_output = """26.08.2019 Перевод на счет
XXXX XX** **** 3456 -> **7890
82771.72 руб."""
    assert format_operation(operation) == expected_output

def test_get_last_operations():
    last_operations = get_last_operations()
    assert len(last_operations) == 5
    assert last_operations[0].startswith('14.10.2018')
    assert last_operations[4].startswith('01.10.2018')

def test_get_last_operations_empty():
    with pytest.raises(FileNotFoundError):
        get_last_operations('nonexistent_file.json')