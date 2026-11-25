from unittest.mock import patch, mock_open
from src.transactions_csv import read_csv_to_dict


# ТЕСТ 1: Проверяем, что функция возвращает список
# Мы "подсовываем" фейковый файл с одной строчкой данных
@patch('builtins.open', new_callable=mock_open, read_data="id;amount\n1;100\n")
def test_returns_list(mock_file):
    result = read_csv_to_dict()

    # Проверяем, что результат — это список
    assert isinstance(result, list)
    # Проверяем, что в нем 1 элемент
    assert len(result) == 1


# ТЕСТ 2: Проверяем, что данные читаются правильно (через точку с запятой)
@patch('builtins.open', new_callable=mock_open, read_data="id;state\n1;EXECUTED\n2;CANCELED\n")
def test_parses_data_correctly(mock_file):
    result = read_csv_to_dict()

    # Проверяем, что первый элемент — это словарь с правильными ключами
    assert result[0]['id'] == '1'
    assert result[0]['state'] == 'EXECUTED'


# ТЕСТ 3: Проверяем, что пустые строки игнорируются
@patch('builtins.open', new_callable=mock_open, read_data="id;amount\n1;100\n;\n3;300\n")
def test_ignores_empty_rows(mock_file):
    result = read_csv_to_dict()

    # В файле 3 строки, но одна пустая (;), поэтому должно остаться 2
    assert len(result) == 2