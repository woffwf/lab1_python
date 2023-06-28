"""
module: manager
"""
from abc import ABC

from models.printer import Printer


class PrinterManager(ABC):
    """
    Клас, що управляє принтерами.
    """

    def __init__(self):
        """
        Ініціалізує об'єкт класу PrinterManager.
        """
        self.printers = []

    def add_printer(self, printer):
        """
        Додає принтер до списку.

        Arguments:
        - printer: об'єкт принтера, який додається до списку.
        """
        self.printers.append(printer)

    def remove_printer(self, printer):
        """
        Видаляє принтер зі списку.

        Arguments:
        - printer: об'єкт принтера, який видаляється зі списку.
        """
        self.printers.remove(printer)

    def print_all(self, pages):
        """
        Друкує задану кількість сторінок на всіх принтерах у списку.

        Arguments:
        - pages: кількість сторінок, які необхідно роздрукувати.
        """
        for printer in self.printers:
            printer.print(pages)

    def __len__(self):
        """
        Повертає довжину списку принтерів.

        Returns:
        - довжина списку принтерів.
        """
        return len(self.printers)

    def __getitem__(self, index):
        """
        Повертає принтер за індексом.

        Arguments:
        - index: індекс принтера у списку.

        Returns:
        - об'єкт принтера за заданим індексом.
        """
        return self.printers[index]

    def __iter__(self):
        """
        Повертає ітератор для ітерації по списку принтерів.

        Returns:
        - ітератор по списку принтерів.
        """
        return iter(self.printers)

    def get_results(self):
        """
        Повертає список результатів виклику методу do_something() для всіх принтерів.

        Returns:
        - список результатів виклику методу do_something() для всіх принтерів.
        """
        return [printer.do_something() for printer in self.printers]

    def enumerate_objects(self):
        """
        Повертає список пар (порядковий номер, принтер) для всіх принтерів.

        Returns:
        - список пар (порядковий номер, принтер) для всіх принтерів.
        """
        return list(enumerate(self.printers))

    def zip_results(self):
        """
        Повертає список пар (принтер, результат) для всіх принтерів.

        Returns:
        - список пар (принтер, результат) для всіх принтерів.
        """
        return list(zip(self.printers, self.get_results()))

    def filter_attributes_by_type(self, attr_type):
        """
        Повертає словник з усіма ключами та значеннями атрибутів об'єкта.

        Arguments:
        - attr_type: тип атрибутів, які необхідно відфільтрувати.

        Returns:
        - словник з усіма ключами та значеннями атрибутів об'єкта, які є заданого типу.
        """
        return {key: value for key, value in self.printers[0].__dict__.items() if isinstance(value, attr_type)}

    def check_condition(self, condition):
        """
        Перевіряє, чи всі об'єкти зі списку задовольняють певну умову, і чи хоч один задовольняє цю умову.

        Arguments:
        - condition: умова, яку необхідно перевірити.

        Returns:
        - словник зі значеннями "all" та "any", що показують, чи всі або хоча б один об'єкт в списку задовольняють умову.
        """
        return {"all": all(condition(obj) for obj in self.printers), "any": any(condition(obj) for obj in self.printers)}
