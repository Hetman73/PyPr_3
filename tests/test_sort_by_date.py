from src.processing import sort_by_date


def test_sort_by_date(sort_by_date_input):
    # Распаковываем кортеж из фикстуры
    input_data, expected_result = sort_by_date_input

    result = sort_by_date(input_data)

    # Проверяем результат
    assert result == expected_result
