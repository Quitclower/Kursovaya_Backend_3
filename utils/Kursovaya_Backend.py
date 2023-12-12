import json
from datetime import datetime


def read_json():
    """
    Выгрузка json файла
    """
    with open("operations.json", encoding="utf-8") as f:
        return json.load(f)


def filter_data(data):
    """
    Итерация по каждой операции оплат
    """
    data = [elem for elem in data if elem and elem["state"] == "EXECUTED"]
    return data


def sort_data(data):
    """
    Выведение и сортировка последних 5 выплат пользователя
    """
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:5]


def edit_data(data: str):
    """
    Функция переводит дату перевода
    """
    data = datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    data = datetime.strftime(data, "%d.%m.%Y")
    return data


def secret_number(numbers: str, to=False):
    """
    Функция скрытия номера карт
    """
    if not to:
        return f"{numbers[:4]} {numbers[4:6]}** **** {numbers[-4:]}"
    else:
        return f"** {numbers[:-4]}"


def print_operations(data) -> list:
    """
    Добавление счетов в список новых операции
    """
    operations = []
    for operations in data:
        if "from" in operations:
            data = edit_data(operations["date"])
            operations.append(...)
        else:
            pass
    return type[list]
