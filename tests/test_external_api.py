from unittest.mock import patch, Mock
from src.external_api import get_transaction_amount_in_rub


def test_rub_transaction_returns_amount():
    """1. Если валюта RUB, API не вызывается, возвращается просто amount."""
    transaction = {"amount": 100.50, "currency": "RUB"}

    result = get_transaction_amount_in_rub(transaction)

    assert result == 100.50


@patch('os.getenv')  # Подменяем получение ключа
@patch('requests.get')  # Подменяем сам запрос к API
def test_usd_transaction_uses_api(mock_get, mock_getenv):
    """2. Если валюта USD, вызывается API (подменяем через Mock)."""

    # Настраиваем, что вернет os.getenv
    mock_getenv.return_value = "fake_api_key"

    # Создаем фейковый ответ от API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9000.0}
    mock_response.raise_for_status.return_value = None  # Чтобы не было ошибок

    # Настраиваем, что вернет requests.get
    mock_get.return_value = mock_response

    transaction = {"amount": 100.0, "currency": "USD"}
    result = get_transaction_amount_in_rub(transaction)

    assert result == 9000.0

    # Бонус: можно проверить, что запрос действительно был отправлен
    mock_get.assert_called_once()


@patch('os.getenv')
@patch('requests.get')
def test_eur_transaction_uses_api(mock_get, mock_getenv):
    """3. Если валюта EUR, тоже идет запрос к API."""

    mock_getenv.return_value = "fake_api_key"

    mock_response = Mock()
    mock_response.json.return_value = {"result": 9800.0}
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    transaction = {"amount": 100.0, "currency": "EUR"}
    result = get_transaction_amount_in_rub(transaction)

    assert result == 9800.0