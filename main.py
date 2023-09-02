import os
from utils import load_operations, mask_to, mask_from, change_format_data, filter_sort_operation

def main():
    file_path = os.path.abspath("operations.json")
    operations = load_operations(file_path)
    operations = filter_sort_operation(operations)
    for operation in operations[:5]:
        print(f"{change_format_data(operation['date'])} {operation['description']}")
        print(f"{mask_from(operation['from']) if operation.get('from') else None} -> {mask_to(operation['to'])}")
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    main()

