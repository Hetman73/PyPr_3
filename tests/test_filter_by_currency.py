import pytest
from src.generators import filter_by_currency




@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776627256633335555",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 7565166738306028412",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812255158044991273",
            "to": "Счет 90792404730558650392",
        },
    ]


def test_usd_returns_two_transactions(transactions):
    """1.1: currency='USD' -> ровно 2 транзакции с id 939719570 и 142264268."""
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert [t["id"] for t in result] == [939719570, 142264268]


def test_rub_returns_one_transaction(transactions):
    """1.2: currency='RUB' -> ровно 1 транзакция с id 873106923."""
    result = list(filter_by_currency(transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["id"] == 873106923


def test_eur_returns_empty_iterator(transactions):
    """1.3: currency='EUR' -> пустой итератор, next() -> StopIteration."""
    result = filter_by_currency(transactions, "EUR")
    with pytest.raises(StopIteration):
        next(result)