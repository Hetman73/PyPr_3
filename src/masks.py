def get_mask_card_number(numbers: int) -> str:
    """Функция маскировки номера краты"""

    card_number = str(numbers)

    slice_1 = card_number[0:4]
    slice_2 = card_number[4:6]
    slice_3 = card_number[-4:]

    return f"{slice_1} {slice_2}** **** {slice_3}"


if __name__ == "__main__":
    result = get_mask_card_number(int(input("Введите номер карты без пробела:")))
    print(result)


def get_mask_account(numbers: int) -> str:
    """Функция маскировки номера счета"""

    account_number = str(numbers)
    slice_1 = account_number[-4:]

    return f"**{slice_1}"


if __name__ == "__main__":
    result = get_mask_account(int(input("Введите номер счёта без пробела:")))
    print(result)
