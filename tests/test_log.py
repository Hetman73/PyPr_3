import re
import pytest
from src.decorators import log


def test_log_success_to_console(capsys): # capture system output — «захват системного вывода, признак консоли».
    """Успех: логирует в консоль."""
    @log(filename=None)
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)

    assert result == 3  # функция вернула правильный результат
    captured = capsys.readouterr()
    # время непредсказуемо — проверяем через регулярку
    assert re.match(
        r"^my_function ok, Заняло \d+\.\d+ секунд\n$",
        captured.out
    )


def test_log_success_to_file(tmp_path):
    """Успех: логирует в файл."""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert re.match(
        r"^my_function ok, Заняло \d+\.\d+ секунд\n$",
        content
    )


def test_log_error_to_console(capsys):
    """Ошибка: логирует и пробрасывает исключение."""
    @log(filename=None)
    def my_function(x, y):
        return x + y

    with pytest.raises(TypeError):
        my_function(1, "2")  # 1 + "2" → TypeError

    captured = capsys.readouterr()
    assert "my_function error: TypeError" in captured.out
    assert "Inputs: args=(1, '2'), kwargs={}" in captured.out


def test_log_error_to_file(tmp_path):
    """Ошибка: пишет в файл и пробрасывает исключение."""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    with pytest.raises(TypeError):
        my_function(1, "2")

    content = log_file.read_text(encoding="utf-8")
    assert "my_function error: TypeError" in content