# src/main.py
import logging
from pathlib import Path

# Импортируем ваши функции из других модулей
from utils import get_transactions_dict, save_transactions_dict
from exporters.csv_exporter import save_as_csv
from processing import filter_transactions  # если у вас есть фильтрация


# ... другие импорты

def main():
    """Главная функция запуска проекта."""

    print("--- Запуск программы ---")

    # 1. Загружаем данные
    transactions = get_transactions_dict('operations.json')

    if not transactions:
        print("Нет данных для обработки. Проверьте файл operations.json и логи.")
        return

    print(f"Загружено транзакций: {len(transactions)}")

    # 2. Обрабатываем данные (если нужно)
    # Например, фильтруем выполненные транзакции
    # filtered = filter_transactions(transactions)

    # 3. Сохраняем результаты
    # JSON для визуализации
    saved_json = save_transactions_dict(transactions, 'transactions_output.json')
    if saved_json:
        print(f"JSON сохранён в: {saved_json.resolve()}")

    # CSV для Excel
    # Обратите внимание: путь строится относительно текущей папки,
    # если запускать из корня проекта, файл попадет в корень.
    # Лучше использовать абсолютный путь через Path.
    csv_path = Path("data") / "transactions.csv"

    # Убедимся, что папка data существует
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    save_as_csv(transactions, str(csv_path))
    print(f"CSV сохранён в: {csv_path.resolve()}")

    print("--- Программа завершена ---")


if __name__ == "__main__":
    main()