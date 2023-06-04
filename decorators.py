"""
module: decorators
"""
import logging
from abc import ABC  # pylint: disable=import-error
import time
import functools
from models.printer import Printer  # pylint: disable=import-error


def method_logger(func):
    """
        Декоратор, що виводить в консоль повідомлення з назвою методу перед його викликом.
        """
    def wrapper(*args, **kwargs):
        """
        Функція-обгортка, яка виводить повідомлення перед викликом методу.

        Arguments:
        - *args: позиційні аргументи, передані методу.
        - **kwargs: іменовані аргументи, передані методу.

        Returns:
        - Результат виклику оригінального методу.
        """
        print(f"Виклик методу: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper

def measure_time(func):
    """
    Декоратор, що вимірює час виконання методу і виводить його в консоль.

    Args:
        func: Функція, до якої застосовується декоратор.

    Returns:
        Результат виклику функції `func`.

    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Обгортка над функцією `func`, що вимірює час виконання і виводить його в консоль.

        Args:
            *args: Позиційні аргументи для функції `func`.
            **kwargs: Ключові аргументи для функції `func`.

        Returns:
            Результат виклику функції `func`.

        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Метод {func.__name__} виконаний за {execution_time} секунд.")
        return result

    return wrapper
def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.exception(e)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.ERROR)
                    logging.exception(e)
        return wrapper
    return decorator