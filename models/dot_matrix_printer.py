"""
module: models
"""
from models.printer import Printer


class DotMatrixPrinter(Printer):
    """
    Клас, що представляє точковий матричний принтер.
    """

    def __init__(self, model, is_color, is_duplex, paper_tray_capacity, paper_count, ribbon_color, ribbon_level):
        super().__init__(model, is_color, is_duplex, paper_tray_capacity, paper_count)
        self.ribbon_color = ribbon_color
        self.ribbon_level = ribbon_level
        self.data_set = {"data1", "data2"}  # Приклад значень для набору даних

    def print(self, pages):
        """
        Друкує вказану кількість сторінок.

        Arguments:
        - pages: кількість сторінок для друку.

        """
        if pages <= self.paper_count:
            if self.ribbon_level >= pages:
                self.paper_count -= pages
                self.ribbon_level -= pages
                print(f"Printing {pages} pages.")
            else:
                print("Not enough ribbon to print.")
        else:
            print("Not enough paper in the tray.")

    def load_paper(self, count):
        """
        Завантажує папір у принтер.

        Arguments:
        - count: кількість аркушів паперу для завантаження.

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
        - кількість залишених сторінок для друку.

        """
        return self.ribbon_level

    def __str__(self):
        """
        Повертає рядок, що представляє об'єкт класу DotMatrixPrinter.

        Returns:
        - рядок, що представляє об'єкт.

        """
        return super().__str__() + f"\nRibbon Color: {self.ribbon_color}\nRibbon Level: {self.ribbon_level}"
