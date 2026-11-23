import json
from pathlib import Path

from src.utils import get_transactions_dict


def test_loads_valid_transactions(tmp_path):
    """Корректный JSON со списком транзакций → возвращается этот список."""
    (tmp_path / 'data').mkdir()
    transactions = [{"id": 1, "amount": 100.0}]
    (tmp_path / 'data' / 'operations.json').write_text(
        json.dumps(transactions), encoding='utf-8'
    )

    result = get_transactions_dict('operations.json', base_dir=tmp_path)

    assert result == transactions


def test_missing_file_returns_empty_list(tmp_path):
    """Файла нет → пустой список."""
    (tmp_path / 'data').mkdir()

    result = get_transactions_dict('missing.json', base_dir=tmp_path)

    assert result == []


def test_not_a_list_returns_empty_list(tmp_path):
    """В JSON лежит объект, а не список → пустой список."""
    (tmp_path / 'data').mkdir()
    (tmp_path / 'data' / 'operations.json').write_text(
        '{"id": 1}', encoding='utf-8'
    )

    result = get_transactions_dict('operations.json', base_dir=tmp_path)

    assert result == []