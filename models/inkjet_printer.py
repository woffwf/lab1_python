"""
module:models
"""
from models.printer import Printer


class InkjetPrinter(Printer):
    """
       Клас, що представляє Inkjet принтерів.
       """
    def __init__(self, model, is_color, is_duplex, paper_tray_capacity, paper_count,ink_type, ink_level):
        """
        Ініціалізує об'єкт класу Printer з заданими параметрами.

        :param model: Модель принтера.
        :param is_color: Прапорець, що вказує на кольоровість принтера.
        :param is_duplex: Прапорець, що вказує на наявність двостороннього друку.
        :param paper_tray_capacity: Вмістимість лотка для паперу.
        :param paper_count: Кількість паперу в принтері.
        :param ink_type: Тип чорнила принтера.
        :param ink_level: Рівень чорнила принтера.
        """
        super().__init__(model, is_color, is_duplex, paper_tray_capacity, paper_count)
        self.ink_type = ink_type
        self.ink_level = ink_level
        self.paper_count = 0  # Оголошення атрибуту paper_count
        self.data_set = {"data3", "data4"}  # Приклад значень для множини даних

    def print(self, pages):
        """
        Друкує вказану кількість сторінок.

        :param pages: Кількість сторінок для друку.
        """
        if pages <= self.paper_count:
            if self.ink_level >= pages * Printer.REQUIRED_COLOUR_PER_PAGE:
                self.paper_count -= pages
                self.ink_level -= pages * Printer.REQUIRED_COLOUR_PER_PAGE
                print(f"Printing {pages} pages.")
            else:
                print("Not enough ink to print.")
        else:
            print("Not enough paper in the tray.")

    def load_paper(self, count):
        """
        Завантажує задану кількість аркушів паперу в принтер.

        :param count: Кількість аркушів паперу для завантаження.
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

        :return: Кількість залишених сторінок.
        """
        return self.ink_level

    def __str__(self):
        """
        Повертає рядкове представлення принтера.

        :return: Рядкове представлення принтера.
        """
        return super().__str__() + f"\nInk Type: {self.ink_type}\nInk Level: {self.ink_level}"
