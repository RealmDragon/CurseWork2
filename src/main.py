from src.operation import Operation
from src import utils as u


def main():
    # Extract data from json file.
    list_operations = u.get_operations()
    # Editing file for class creation.
    operations_edited = u.edit_operations(list_operations)
    # Sorting operations by date.
    sorted_operations = u.sort_operations(operations_edited)
    # Extract specified number of operations.
    last_operations = u.show_last_operation(sorted_operations, 5)
    # Class creation from list.
    operations = Operation.from_dict(last_operations)
    return [x for x in operations]


if __name__ == "__main__":
    transactions = main()
    for operation in transactions:
        print(
            f"{operation.edit_date()} {operation.description} \n"
            f"{operation.hide_card_numbers(operation.come_from)} -> {operation.hide_account_numbers(operation.to)}\n"
            f"{operation.operationAmount['amount']} {operation.operationAmount['currency']['name']}\n"
        )