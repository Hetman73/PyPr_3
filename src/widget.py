
from typing import Union
import re


def mask_account_card(arg: Union[str, int]) -> str:
    """Функция обрабатывать информацию о картах и счетах."""

    user_info = str(arg).replace(" ", "").replace("-", "")

    user_text = "".join(re.findall(r"\D+", user_info))
    user_digits = "".join(re.findall(r"\d+", user_info))


    slice_1 = user_digits[0:4]
    slice_2 = user_digits[4:6]
    slice_3 = user_digits[-4:]


    return f"{user_text} {slice_1} {slice_2}** **** {slice_3}"

if __name__ == "__main__":
        result = mask_account_card(str(input("Ввод:")))
        print(result)



