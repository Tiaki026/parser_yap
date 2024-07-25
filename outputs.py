# outputs.py
from prettytable import PrettyTable


def control_output(results, cli_args):
    if cli_args.pretty:
        # Вывод в формате PrettyTable.
        pretty_output(results)
    else:
        # Вывод по умолчанию. 
        default_output(results)


def default_output(results):
    # Печатаем список results построчно.
    for row in results:
        print(*row)    


def pretty_output(results):
    # Инициализируем объект PrettyTable.
    table = PrettyTable()
    # В качестве заголовков устанавливаем первый элемент списка.
    table.field_names = results[0]
    # Выравниваем всю таблицу по левому краю.
    table.align = 'l'
    # Добавляем все строки, начиная со второй (с индексом 1).
    table.add_rows(results[1:])
    # Печатаем таблицу.
    print(table)
