import pytest

from src.widget import mask_account_card
from tests.conftest import account_card


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Счет 736541084301358743") == "номер счета не полный"


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 736541084301358743", "номер счета не полный"),
    ],
)
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result


@pytest.mark.parametrize(["string", "expected_result"], account_card())
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result
