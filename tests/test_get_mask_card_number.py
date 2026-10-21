import pytest

from src.masks import get_mask_card_number
from tests.conftest import card_numbers


def test_get_mask_card_number():
    assert get_mask_card_number("2363985678548965") == "2363 98** **** 8965"
    assert get_mask_card_number("") == "вы ничего не ввели"
    assert get_mask_card_number("2363 9856 7854 8965") == "2363 98** **** 8965"
    assert get_mask_card_number("23639856") == "номер карты не полный"


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("2363985678548965", "2363 98** **** 8965"),
        ("", "вы ничего не ввели"),
        ("2363 9856 7854 8965", "2363 98** **** 8965"),
        ("23639856", "номер карты не полный"),
    ],
)
def test_get_mask_card_number(string, expected_result):
    assert get_mask_card_number(string) == expected_result


# @pytest.mark.parametrize("string, expected_result", card_numbers())
# def test_get_mask_card_number(string, expected_result):
#     assert get_mask_card_number(string) == expected_result
