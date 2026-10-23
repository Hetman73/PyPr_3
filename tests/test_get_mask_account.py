import pytest

from src.masks import get_mask_account
from tests.conftest import account_numbers


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("") == "вы ничего не ввели"
    assert get_mask_account("7365 4108 4301 3587 4305") == "**4305"
    assert get_mask_account("7365410843013587") == "номер счета не полный"


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("73654108430135874305", "**4305"),
        ("", "вы ничего не ввели"),
        ("7365 4108 4301 3587 4305", "**4305"),
        ("7365410843013587", "номер счета не полный"),
    ],
)
def test_get_mask_account(string, expected_result):
    assert get_mask_account(string) == expected_result


@pytest.mark.parametrize("string, expected_result", account_numbers())
def test_get_mask_account(string, expected_result):
    assert get_mask_account(string) == expected_result
