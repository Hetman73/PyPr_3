"""Реализуйте функцию, которая принимает на вход транзакцию и возвращает сумму
транзакции (
amount
) в рублях, тип данных —
float
. Если транзакция была в
USD
 или
EUR
, происходит обращение к внешнему API для получения текущего курса валют и
конвертации суммы операции в рубли. Для конвертации валюты воспользуйтесь
Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.(данная ссылка на работает)"""

import os
from typing import Any

import requests


def get_transaction_amount_in_rub(transaction: dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях.
    Для USD/EUR запрашивает курс через Exchange Rates Data API.
    """
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    # Если уже рубли — просто возвращаем сумму
    if currency == "RUB":
        return float(amount)

    # Получаем ключ из переменной окружения (безопасный способ)
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("Не задан API_KEY в переменных окружения")

    # Правильный эндпоинт для конвертации (https://apilayer.com/exchangerates_data-api
    # не найден)
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": api_key}
    params = {"from": currency, "to": "RUB", "amount": amount}

    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()  # выбросит исключение при 4xx/5xx

    data = response.json()
    return float(data["result"])


# if __name__ == "__main__":
#     from dotenv import load_dotenv
#
#     load_dotenv()  # Читаем API_KEY из файла .env
#
#     test_transaction = {
#         "amount": 100.0,
#         "currency": "USD"
#     }
#
#     try:
#         result = get_transaction_amount_in_rub(test_transaction)
#         print(f"Сумма в рублях: {result:.2f}")
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
