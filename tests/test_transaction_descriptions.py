import pytest
from src.generators import transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"},
        {"id": 3, "description": "Перевод с карты на карту"},
    ]


def test_returns_descriptions_in_order(transactions):
    """Выдаёт описания всех транзакций по порядку."""
    result = list(transaction_descriptions(transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_returns_iterator(transactions):
    """Возвращает именно итератор, а не список."""
    result = transaction_descriptions(transactions)
    assert iter(result) is result
    assert not isinstance(result, list)


def test_empty_input():
    """Для пустого списка итератор сразу исчерпан."""
    result = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(result)