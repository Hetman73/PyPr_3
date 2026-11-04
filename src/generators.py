def filter_by_currency(transactions: list[dict], currency: str):
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор транзакций, где валюта операции == currency.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


# if __name__ == "__main__":
#     transactions = [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {"name": "USD", "code": "USD"},
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776627256633335555",
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {"name": "USD", "code": "USD"},
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 7565166738306028412",
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {"name": "руб.", "code": "RUB"},
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812255158044991273",
#             "to": "Счет 90792404730558650392",
#         },
#     ]
#
#     p = filter_by_currency(transactions, "USD")
#     print(next(p))   # транзакция id=939719570
#     print(next(p))   # транзакция id=142264268
#     # print(next(p))  # StopIteration — USD-транзакции закончились


def transaction_descriptions(transactions: list[dict]):
    """Принимает список словарей-транзакций.
    Возвращает итератор, который по очереди выдаёт описания операций.
    """
    for transaction in transactions:
        yield transaction["description"]


# if __name__ == "__main__":
#     transactions = [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {"name": "USD", "code": "USD"},
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776627256633335555",
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {"name": "USD", "code": "USD"},
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 7565166738306028412",
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {"name": "руб.", "code": "RUB"},
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812255158044991273",
#             "to": "Счет 90792404730558650392",
#         },
#     ]
#
#     descriptions = transaction_descriptions(transactions)
#     for _ in range(3):
#         print(next(descriptions))


def card_number_generator(start, end, width=16):
    """Генератор, который создаёт номера банковских карт в отформатированном виде:
    16 цифр, разбитых на 4 группы по 4 цифры через пробел (XXXX XXXX XXXX XXXX)."""
    for number in range(start, end + 1):
        digits = str(number).zfill(width)  # заполняем 0 слева с помощбю zero fill (строковый метод).
        formatted = " ".join(digits[i : i + 4] for i in range(0, width, 4))
        yield formatted


# if __name__ == "__main__":
#     card_generator = card_number_generator(1, 10, 16 )
#     for _ in range(10):
#         print(next(card_generator))
