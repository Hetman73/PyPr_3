import logging
from pathlib import Path

# ==========================================
# НАСТРОЙКА ЛОГИРОВАНИЯ ДЛЯ МОДУЛЯ MASKS
# ==========================================
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    base_dir = Path(__file__).resolve().parent.parent
    log_dir = base_dir / "logs"
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "app.log"

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)


# ==========================================
# ФУНКЦИИ МОДУЛЯ
# ==========================================


def get_mask_card_number(numbers: str) -> str:
    """Функция маскировки номера карты.

    Принимает  str.
    Возвращает строку в формате 'XXXX XX** **** XXXX'
    или 'номер карты не полный',или 'вы ничего не ввели'.
    """
    logger.debug(f"Вызвана get_mask_card_number с аргументом: {numbers}")

    # Обработка пустого ввода.
    if numbers is None or numbers == "":
        logger.error("Ошибка: введена пустая строка вместо номера карты")
        return "вы ничего не ввели"

    # Преобразуем в строку и убираем пробелы,
    # если пользователь случайно передал строку с пробелами
    card_number = str(numbers).replace(" ", "")

    # Проверка на минимальную длину (в номере должно быть хотя бы 10 цифр
    # для формирования маски 4+2+4)
    if len(card_number) < 10:
        logger.error(f"Ошибка: номер карты не полный ({card_number})")
        return "номер карты не полный"

    else:

        slice_1 = card_number[0:4]
        slice_2 = card_number[4:6]
        slice_3 = card_number[-4:]

    # Финальный результат, применяем 'f' строку.
    result = f"{slice_1} {slice_2}** **** {slice_3}"
    logger.info(f"Успешно замаскирован номер карты: {result}")
    return result


def get_mask_account(numbers: str) -> str:
    """Функция маскировки номера счета
       Принимает  str.
    Возвращает строку в формате '**XXXX'
    или 'номер счета не полный',или 'вы ничего не ввели'.
    """
    logger.debug(f"Вызвана get_mask_account с аргументом: {numbers}")

    # Обработка пустого ввода.
    if numbers is None or numbers == "":
        logger.error("Ошибка: введена пустая строка вместо номера счета")
        return "вы ничего не ввели"

    # Преобразуем в строку и убираем пробелы,
    # если пользователь случайно передал строку с пробелами

    account_number = str(numbers).replace(" ", "")

    slice_1 = account_number[-4:]

    # Проверка  длину (в номере должно быть  20 цифр)

    if len(account_number) < 20:
        logger.error(f"Ошибка: номер счета не полный ({account_number})")
        return "номер счета не полный"

    else:

        # Финальный результат, применяем 'f' строку.
        result = f"**{slice_1}"
        logger.info(f"Успешно замаскирован номер счета: {result}")
        return result


# if __name__ == "__main__":
#     result = get_mask_account(input("Введите номер счёта без пробела:"))
#     print(result)
