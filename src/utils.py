""" Реализуйте функцию, которая принимает на вход путь до JSON-файла и
возвращает список словарей с данными о финансовых транзакциях.
Если файл пустой, содержит не список или не найден,
функция возвращает пустой список.  """

from pathlib import Path
import json


def get_transactions_dict(input_file: str) -> list[dict]:
    """
    Загружает список транзакций из JSON-файла.

    Возвращает пустой список, если:
    - файл не найден;
    - файл пустой;
    - содержимое не является списком;
    - JSON некорректен.

    Args:
        input_file: имя файла в директории data/

    Returns:
        list[dict]: список транзакций или [] при ошибке
    """
    # Путь к корню проекта: utils.py -> src -> PythonProject_3
    base_dir = Path(__file__).resolve().parent.parent
    input_path = base_dir / 'data' / input_file

    # 1. Файл не найден
    if not input_path.is_file():
        return []

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
    except (OSError, UnicodeDecodeError):
        return []

    # 2. Файл пустой (или содержит только пробелы)
    if not content:
        return []

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        # 4. Некорректный JSON — тоже возвращаем []
        return []

    # 3. Содержимое не список
    if not isinstance(data, list):
        return []

    return data


if __name__ == "__main__":
    result = get_transactions_dict('operations.json')
    print(f"Загружено транзакций: {len(result)}")
    print(result)