from typing import Union
import re


def mask_account_card(arg: Union[str, int]) -> str:
    """Функция обрабатывать информацию о картах и счетах."""

    user_info = str(arg).replace(" ", " ").replace("-", "")

    user_text = "".join(re.findall(r"\D+", user_info))
    user_digits = "".join(re.findall(r"\d+", user_info))

    if len(user_digits) == 16:

        slice_1 = user_digits[0:4]
        slice_2 = user_digits[4:6]
        slice_3 = user_digits[-4:]

        return f"{user_text} {slice_1} {slice_2}** **** {slice_3}"

    elif len(user_digits) >= 20:

        return f"{user_text} **{user_digits[-4:]}"

    else:

        return ("Вы ошибл"
                "ись")


# if __name__ == "__main__":
#     result = mask_account_card(str(input("Ввод:")))
#     print(result)



def get_date(arg: str) -> str:
    """Функция отфильтровки даты "ДД.ММ.ГГГГ" """

    dates_list = re.findall(r"\d{4}-\d{2}-\d{2}", arg)
    dates_str = " ".join(dates_list)
    date_with_dots = dates_str.replace("-", ".")

        return date_with_dots

if __name__ == "__main__":
    result = get_date(str(input("Ввод:")))
    print(result)