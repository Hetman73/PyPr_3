import pytest

from src.widget import get_date
from tests.conftest import get_date_input


def test_get_date_simple():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-01-01T00:00:00") == "01.01.2024"
    assert get_date("2024-12-31T23:59:59") == "31.12.2024"
    assert get_date("") == "пустой ввод"
    assert get_date("   2024-05-01T12:00:00   ") == "01.05.2024"
    assert get_date("not a date") == ".."


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-01-01T00:00:00", "01.01.2024"),
        ("2024-12-31T23:59:59", "31.12.2024"),
        ("", "пустой ввод"),
        ("not a date", ".."),
    ],
)
def test_get_date_parametrized(string, expected_result):
    assert get_date(string) == expected_result


@pytest.mark.parametrize(["string", "expected_result"], get_date_input())
def test_get_date_function(string, expected_result):
    assert get_date(string) == expected_result
