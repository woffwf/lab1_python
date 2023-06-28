"""
module:models
"""
from abc import ABC, abstractmethod


class Printer(ABC):
    """
    abstract class
    """
    REQUIRED_COLOUR_PER_PAGE = 10

    def __init__(self, model, is_color, is_duplex, paper_tray_capacity, paper_count):
        self.model = model
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.paper_tray_capacity = paper_tray_capacity
        self.paper_count = paper_count
        self.data_set = set()  # Додано нове поле для множини даних

    @abstractmethod
    def print(self, pages):
        """
          Абстрактний метод для друку сторінок.
        """

    @abstractmethod
    def load_paper(self, count):
        """
         Абстрактний метод для завантаження паперу.
         """

    @abstractmethod
    def get_remaining_pages_count(self):
        """
        Абстрактний метод для отримання кількості залишених сторінок.
        """

    def __str__(self):
        """
        Перевизначений метод __str__, щоб отримати рядкове представлення принтера.
        """
        return f"Model: {self.model}\nColor: {self.is_color}\nDuplex: {self.is_duplex}\n" \
               f"Paper Tray Capacity: {self.paper_tray_capacity}\nPaper Count: {self.paper_count}"

    def __iter__(self):
        """
        Перевизначений метод __iter__
        :return:
        """
        return iter(self.data_set)

    def print(self, pages):
        if pages <= 0:
            raise PrinterError("Неприпустима кількість сторінок для друку.")
