import json

def load_operations(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def mask_from(number_card):
    number_card = number_card.split(" ")
    mask_number_card = number_card[-1][:4]+" "+number_card[-1][4:6]+"** **** "+number_card[-1][12:16]
    return f"{' '.join(number_card[:-1])} {mask_number_card}"


def mask_to(number_card):
    number_card = number_card.split(" ")
    mask_number_card = "**"+number_card[-1][-4:]
    return f"{' '.join(number_card[:-1])} {mask_number_card}"


def change_format_data(data):
    data = data.split("T")[0].split("-")
    return f"{data[2]}.{data[1]}.{data[0]}"


def filter_sort_operation(operations):
    operations = [operation for operation in operations if operation.get("state") == "EXECUTED"]
    operations = sorted(operations, key=lambda operation: operation["date"], reverse=True)
    return operations
