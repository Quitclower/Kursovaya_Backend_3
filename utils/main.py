import json
from Kursovaya_Backend import read_json, filter_data, sort_data, edit_data, secret_number, print_operations

with open("operations.json", encoding="utf-8") as f:
    data = json.load(f)


def print_operations1(data) -> list:
    last_operations = data[:5]  # Получаем последние 5 операций
    for operation in last_operations:
        date = operation['date']
        description = operation['description']
        from_account = operation['from']
        to_account = operation['to']
        amount = operation['amount']
        currency = operation['currency']
        print(f'{date} {description}')
        print(f'{from_account} -> {to_account}')
        print(f'{amount} {currency}')
        print()


read_json()

print_operations1(data)
