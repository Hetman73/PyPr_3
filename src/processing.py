from typing import Any, Dict, List


def filter_by_state(executed: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция фильтрует словари по заданному ключу.
    Функция filter_by_state, принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только
     те словари, у которых ключ state соответствует указанному значению."""

    new_list = []  # сюда складываем отфильтрованные позиции
    target_state = state.lower()  # всё приводим к нижнему регистру, один раз

    for item in executed:
        # "state" in item защита от полного отсутвия такого ключа.
        if "state" in item and item["state"].lower() == target_state:
            new_list.append(item)

    return new_list


# if __name__ == "__main__":
#     result = filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
#     print(result)


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортировки по дате.
    Функция sort_by_date, принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция возвращает новый
    список, отсортированный по дате (date)."""

    for item in data:
        if "date" not in item:
            raise ValueError("В данной задаче словари должны содержать ключ 'date'")

    return sorted(data, key=lambda x: x["date"], reverse=reverse)


# if __name__ == "__main__":
#     result = sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
#
#     print(result)
