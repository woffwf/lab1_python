"""
module:models
"""
from models.printer import Printer
from decorators.decorators import logged
from exception.printer_error_exception import PrinterError

class LaserPrinter(Printer):
    """
    Клас прінтер
    """
    def __init__(self, model, is_color, is_duplex, paper_tray_capacity, paper_count, toner_type, toner_level):
        """
        Ініціалізує об'єкт класу LaserPrinter.

        Arguments:
        - model: модель прінтера
        - is_color: прапорець, що вказує на кольоровість прінтера
        - is_duplex: прапорець, що вказує на підтримку двостороннього друку
        - paper_tray_capacity: ємність лотка для паперу
        - paper_count: кількість паперу у лотку
        - toner_type: тип тонера
        - toner_level: рівень тонера
        """
        super().__init__(model, is_color, is_duplex, paper_tray_capacity, paper_count)
        self.toner_type = toner_type
        self.toner_level = toner_level
        self.pages_printed = 0

    @logged(PrinterError, "console")
    def print(self, pages):
        """
        Виконує друк заданої кількості сторінок.

        Arguments:
        - pages: кількість сторінок

        Returns:
        - None
        """
        if pages <= self.paper_count:
            if self.toner_level >= pages:
                self.paper_count -= pages
                self.toner_level -= pages
                self.pages_printed += pages
                print(f"Printing {pages} pages.")
            else:
                print("Not enough toner to print.")
        else:
            print("Not enough paper in the tray.")

    def load_paper(self, count):
        """
        Завантажує задану кількість паперу у лоток.

        Arguments:
        - count: кількість аркушів паперу

        Returns:
        - None
        """
        if self.paper_count + count > self.paper_tray_capacity:
            self.paper_count = self.paper_tray_capacity
            print(f"Paper tray is full. Loaded {self.paper_tray_capacity - self.paper_count} sheets of paper.")
        else:
            self.paper_count += count
            print(f"Loaded {count} sheets of paper. Total paper count: {self.paper_count}")

    def get_remaining_pages_count(self):
        """
        Повертає кількість залишених сторінок для друку.

        Returns:
        - Кількість залишених сторінок
        """
        return self.toner_level

    def __str__(self):
        """
        Повертає рядкове представлення об'єкта.

        Returns:
        - Рядкове представлення об'єкта
        """
        return super().__str__() + f"\nToner Type: {self.toner_type}\nToner Level: {self.toner_level}\n" \
                                   f"Pages Printed: {self.pages_printed}"
