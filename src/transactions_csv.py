import csv


def read_csv_to_dict(path='data/transactions.csv') -> dict:
    """ Функция для считывания финансовых операций из CSV выдает
        список словарей с транзакциями. """
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        # Превращаем reader в список словарей, пропуская полностью пустые строки
        return [row for row in reader if any(row.values())]


# if __name__ == '__main__':
#     data = read_csv_to_dict()
#
#     # 1. Проверяем, что это список
#     print("Тип данных:", type(data))
#
#     # 2. Проверяем, сколько всего транзакций прочиталось
#     print("Всего транзакций:", len(data))
#
#     # 3. Выводим первый элемент (первую транзакцию), чтобы посмотреть структуру
#     print("Первая транзакция:", data[0])