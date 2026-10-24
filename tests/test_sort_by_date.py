import pytest
from src.processing import sort_by_date



def test_sort_by_date_raises():
    # Тестируем сценарий, когда в словаре нет ключа 'date'
    data = [{"id": 1, "state": "EXECUTED"}]

    # Используем with, чтобы поймать ожидаемую ошибку
    with pytest.raises(ValueError, match="В данной задаче словари должны содержать ключ 'date'"):
        sort_by_date(data)


def test_sort_by_date(sort_by_date_input):
    # Распаковываем кортеж из фикстуры
    input_data, expected_result = sort_by_date_input

    result = sort_by_date(input_data)

    # Проверяем результат
    assert result == expected_result
