"""Реализуйте функцию, которая принимает на вход путь до JSON-файла и
возвращает список словарей с данными о финансовых транзакциях.
Если файл пустой, содержит не список или не найден,
функция возвращает пустой список."""

import json
import logging
from pathlib import Path

# ==========================================
# 1. НАСТРОЙКА ЛОГИРОВАНИЯ (перед функцией)
# ==========================================
# Создаем отдельный логгер для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG) # Уровень не меньше DEBUG

# Создаем обработчик файла (file_handler)
file_handler = logging.FileHandler("utils.log", mode="a", encoding="utf-8")

# Создаем форматер (file_formatter)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Устанавливаем форматер для обработчика и добавляем его к логгеру
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# ==========================================
# 2. САМА ФУНКЦИЯ
# ==========================================
def get_transactions_dict(input_file: str, base_dir: Path | None = None) -> list[dict]:
    """
    Загружает список транзакций из JSON-файла.

    """
    if base_dir is None:
        base_dir = Path(__file__).resolve().parent.parent

    input_path = base_dir / "data" / input_file
    logger.info(f"Попытка загрузить файл: {input_path}")

    if not input_path.is_file():
        logger.error(f"Файл не найден: {input_path}")
        return []

    try:
        with open(input_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
    except (OSError, UnicodeDecodeError) as e:
        logger.error(f"Ошибка чтения файла {input_path}: {e}")
        return []

    if not content:
        logger.warning(f"Файл пустой: {input_path}")
        return []

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON в файле {input_path}: {e}")
        return []

    if not isinstance(data, list):
        logger.error(f"Данные в файле {input_path} не являются списком (тип: {type(data).__name__})")
        return []

    logger.info(f"Успешно загружено {len(data)} транзакций из {input_path}")
    return data

if __name__ == "__main__":
    result = get_transactions_dict('operations.json')
    print(f"Загружено транзакций: {len(result)}")

    # Сохраняем результат в отдельный файл для визуализации
    output_path = Path("transactions_output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

    print(f"Результат сохранён в: {output_path.resolve()}")

