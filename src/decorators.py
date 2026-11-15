"""Напишите декоратор
log
, который будет автоматически логировать начало и конец выполнения функции,
а также ее результаты или возникшие ошибки.
Декоратор должен принимать необязательный аргумент
filename
, который определяет, куда будут записываться логи (в файл или в консоль):

Если
filename
 задан, логи записываются в указанный файл.
Если
filename
 не задан, логи выводятся в консоль.
Логирование должно включать:

Имя функции и результат выполнения при успешной операции.
Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.

Пример использования декоратора

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

Ожидаемый вывод в лог-файл
mylog.txt
 при успешном выполнении:

my_function ok

Ожидаемый вывод при ошибке:

my_function error: тип ошибки. Inputs: (1, 2), {}

Где
тип ошибки
 заменяется на текст ошибки."""

import time
from functools import wraps


def log(filename=None):
    """Декоратор с параметром: логирует успех/ошибку функции.

    filename=None  -> вывод в консоль
    filename='.docs/mylog.txt' -> запись в файл (append)
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            try:
                result = func(*args, **kwargs)

            except Exception as e:
                elapsed = time.perf_counter() - start
                msg = f"{func.__name__} error: {type(e).__name__}. Inputs: args={args}, kwargs={kwargs}, Заняло {elapsed:.6f} секунд"
                _write(msg, filename)
                raise  # важно: ошибку не глотаем, а пробрасываем дальше
            else:
                elapsed = time.perf_counter() - start
                msg = f"{func.__name__} ok, Заняло {elapsed:.6f} секунд"
                _write(msg, filename)
                return result

        return wrapper

    return decorator


def _write(message, filename=None):
    """Вспомогательная функция записи лога в файл или консоль."""
    if filename is None:
        print(message)
    else:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")


@log()
# @log(filename="docs/mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
