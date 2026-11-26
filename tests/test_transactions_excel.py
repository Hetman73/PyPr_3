import pandas as pd
from unittest.mock import patch
from src.transactions_excel import read_xlsx_to_dict


@patch('pandas.read_excel')
def test_read_excel_mock(mock_read_excel):
    # 1. Создаем подменный DataFrame (2 столбца, 2 строки)
    substitute_df = pd.DataFrame({
        'id': [1, 2],
        'amount': [100, 200]
    })

    # 2. При вызове возвращаем подменный df
    mock_read_excel.return_value = substitute_df

    # 3. Вызываем нашу функцию
    result = read_xlsx_to_dict()

    # 4. Проверяем результат
    assert len(result) == 2
    assert result[0]['id'] == 1
    assert result[1]['amount'] == 200