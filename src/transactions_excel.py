import pandas as pd


def read_xlsx_to_dict(path='data/transactions_excel.xlsx') -> dict:
    """ Функция для считывания финансовых операций из xlsx выдает
        список словарей с транзакциями. """

    excel_data = pd.read_excel(path)
    # Превращаем таблицу в список словарей
    # orient='records' -  каждая строка таблицы стала отдельным словарём,
    # а все эти словари положит в список
    return excel_data.to_dict(orient='records')


# if __name__ == '__main__':
#     data = read_xlsx_to_dict()
#     print(f"Количество записей: {len(data)}")
#     print(data[:2])  # Выведет первые 2 словаря