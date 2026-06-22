from unittest.mock import patch

from app.client import fetch_data


@patch("app.client.requests.get")
def test_fetch_data_success(mock_get):
    # Настраиваем mock-объект: что он должен вернуть
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"id": 1, "status": "ok"}

    # Вызываем нашу функцию
    result = fetch_data("https://fake-url.com")

    # Проверяем результат
    assert result["status"] == "ok"
    # Проверяем, что requests.get был вызван с нужным URL ровно 1 раз
    mock_get.assert_called_once_with("https://fake-url.com")
