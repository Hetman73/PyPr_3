
def get_mask_card_number(numbers: str) -> str:
    """Функция маскировки номера карты.

    Принимает  str.
    Возвращает строку в формате 'XXXX XX** **** XXXX'
    или 'номер карты не полный',или 'вы ничего не ввели'.
    """
    # Обработка пустого ввода.
    if numbers is None or numbers == "":
        return "вы ничего не ввели"

    # Преобразуем в строку и убираем пробелы,
    # если пользователь случайно передал строку с пробелами
    card_number = str(numbers).replace(" ", "")

    # Проверка на минимальную длину (в номере должно быть хотя бы 10 цифр
    # для формирования маски 4+2+4)
    if len(card_number) < 10:
        return 'номер карты не полный'

    else:


        slice_1 = card_number[0:4]
        slice_2 = card_number[4:6]
        slice_3 = card_number[-4:]

    # Финальный результат, применяем 'f' строку.
    return f"{slice_1} {slice_2}** **** {slice_3}"

if __name__ == "__main__":
    result = get_mask_card_number(input("Введите номер карты без пробела:"))
    print(result)


def get_mask_account(numbers: int) -> str:
    """Функция маскировки номера счета"""

    account_number = str(numbers)
    slice_1 = account_number[-4:]

    return f"**{slice_1}"


if __name__ == "__main__":
    result = get_mask_account(int(input("Введите номер счёта без пробела:")))
    print(result)
