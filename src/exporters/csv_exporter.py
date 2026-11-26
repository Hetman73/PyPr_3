# import csv
# import logging
# from typing import Any
#
# logger = logging.getLogger("utils")
#
# def _flatten_dict(d: dict, parent_key: str = '', sep: str = '_') -> dict:
#     """Вспомогательная функция для 'разглаживания' вложенных словарей."""
#     items = []
#     for k, v in d.items():
#         new_key = f"{parent_key}{sep}{k}" if parent_key else k
#         if isinstance(v, dict):
#             items.extend(_flatten_dict(v, new_key, sep=sep).items())
#         else:
#             items.append((new_key, v))
#     return dict(items)
#
# def save_as_csv(transactions: list[dict], output_file: str = "transactions.csv") -> None:
#     """Плоское представление транзакций — удобно открыть в Excel."""
#     if not transactions:
#         logger.warning("save_as_csv: список транзакций пуст, файл не создан")
#         return
#
#     # 1. Разглаживаем каждую транзакцию
#     flattened_txs = [_flatten_dict(tx) for tx in transactions]
#
#     # 2. Собираем все возможные колонки (вдруг в каких-то транзакциях есть уникальные поля)
#     fieldnames = sorted({key for tx in flattened_txs for key in tx.keys()})
#
#     logger.info(f"save_as_csv: сохраняем {len(transactions)} записей в {output_file}")
#
#     try:
#         # 3. Записываем в файл
#         with open(output_file, "w", encoding="utf-8", newline="") as f:
#             # restval="" гарантирует, что если у транзакции нет какого-то поля,
#             # ячейка останется пустой, а не вызовет ошибку
#             writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
#             writer.writeheader()
#             writer.writerows(flattened_txs)
#     except OSError as e:
#         logger.error(f"save_as_csv: ошибка записи {output_file}: {e}")
#         return
#
#     logger.info(f"save_as_csv: успешно сохранено в {output_file}")