
import pytest
from src.generators import card_number_generator


@pytest.mark.parametrize("start, end, expected", [
    (1, 4, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
    ]),
    (0, 0, ["0000 0000 0000 0000"]),
])
def test_returns_number_card(start, end, expected):
    assert list(card_number_generator(start, end)) == expected