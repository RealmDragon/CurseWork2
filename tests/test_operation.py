import pytest
from src.operation import Operation


@pytest.fixture
def example_data():
    return Operation(
        id=441945886,
        state="EXECUTED",
        date="019-08-26T10:50:58.294041",
        operationAmount={
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        description="Перевод организации",
        come_from="Maestro 1596837868705199",
        to="Счет 64686473678894779589",
    )


@pytest.fixture
def list_of_examples():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод организации",
            "come_from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "come_from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "come_from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "come_from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "come_from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 214024827,
            "state": "EXECUTED",
            "date": "2018-12-20T16:43:26.929246",
            "operationAmount": {
                "amount": "70946.18",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "come_from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        },
    ]


@pytest.fixture()
def list_of_operations():
    return [
        Operation(
            id=441945886,
            state="EXECUTED",
            date="2019-08-26T10:50:58.294041",
            operationAmount={
                "amount": "31957.58",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Перевод организации",
            to="Счет 64686473678894779589",
            come_from="Maestro 1596837868705199",
        ),
        Operation(
            id=41428829,
            state="EXECUTED",
            date="2019-07-03T18:35:29.512364",
            operationAmount={
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод организации",
            to="Счет 35383033474447895560",
            come_from="MasterCard 7158300734726758",
        ),
        Operation(
            id=939719570,
            state="EXECUTED",
            date="2018-06-30T02:08:58.425572",
            operationAmount={
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод организации",
            to="Счет 11776614605963066702",
            come_from="Счет 75106830613657916952",
        ),
        Operation(
            id=587085106,
            state="EXECUTED",
            date="2018-03-23T10:45:06.972075",
            operationAmount={
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Открытие вклада",
            to="Счет 41421565395219882431",
            come_from=None,
        ),
        Operation(
            id=142264268,
            state="EXECUTED",
            date="2019-04-04T23:20:05.206878",
            operationAmount={
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод со счета на счет",
            to="Счет 75651667383060284188",
            come_from="Счет 19708645243227258542",
        ),
        Operation(
            id=873106923,
            state="EXECUTED",
            date="2019-03-23T01:09:46.296404",
            operationAmount={
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            description="Перевод со счета на счет",
            to="Счет 74489636417521191160",
            come_from="Счет 44812258784861134719",
        ),
        Operation(
            id=214024827,
            state="EXECUTED",
            date="2018-12-20T16:43:26.929246",
            operationAmount={
                "amount": "70946.18",
                "currency": {"name": "USD", "code": "USD"},
            },
            description="Перевод организации",
            to="Счет 21969751544412966366",
            come_from="Счет 10848359769870775355",
        ),
    ]


def test_field_access(example_data):
    operation = example_data
    assert operation.id == 441945886
    assert operation.state == "EXECUTED"
    assert operation.date == "019-08-26T10:50:58.294041"
    assert operation.operationAmount == {
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "RUB"},
    }
    assert operation.description == "Перевод организации"
    assert operation.come_from == "Maestro 1596837868705199"
    assert operation.to == "Счет 64686473678894779589"


def test_from_list(list_of_examples, list_of_operations):
    assert Operation.from_dict(list_of_examples) == list_of_operations


def test_equality(example_data):
    operation_1 = example_data
    operation_2 = example_data
    assert operation_1 == operation_2


def test_inequality(list_of_examples):
    operation_1 = Operation(**list_of_examples[0])
    operation_2 = Operation(**list_of_examples[1])
    assert operation_1 != operation_2


def test_identity(example_data):
    operation_1 = example_data
    operation_2 = example_data
    assert operation_1 is operation_2


def test_hide_card_numbers(example_data):
    operation = example_data
    assert operation.hide_card_numbers(operation.come_from) == "Maestro 1596 83** **** 5199"


def test_hide_account_number(example_data):
    operation = example_data
    assert operation.hide_account_numbers(operation.to) == "Счет **9589"