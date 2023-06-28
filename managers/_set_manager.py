"""
module: manager
"""
from models.printer import Printer


from models.printer import Printer

class SetManager:
    """
    Клас, що управляє наборами даних.
    """

    def __init__(self, manager):
        """
        Ініціалізує об'єкт класу SetManager.

        Arguments:
        - manager: об'єкт менеджера, що містить набори даних.
        """
        self.manager = manager
        self.current_data_set = None
        self.current_data_set_iterator = None

    def __iter__(self):
        """
        Повертає ітератор для ітерації по наборам даних.

        Returns:
        - ітератор по наборам даних.
        """
        self.current_data_set = iter(self.manager)
        self.current_data_set_iterator = None
        return self

    def __len__(self):
        """
        Повертає загальну кількість елементів у всіх наборах даних.

        Returns:
        - загальна кількість елементів у всіх наборах даних.
        """
        return sum(len(obj.data_set) for obj in self.manager)

    def __getitem__(self, index):
        """
        Повертає елемент за заданим індексом.

        Arguments:
        - index: індекс елемента.

        Returns:
        - елемент за заданим індексом.

        Raises:
        - IndexError: якщо індекс виходить за межі доступних елементів.
        """
        count = 0
        for obj in self.manager:
            if count <= index < count + len(obj.data_set):
                return list(obj.data_set)[index - count]
            count += len(obj.data_set)
        raise IndexError("Index out of range")

    def __next__(self):
        """
        Повертає наступний елемент для ітерації.

        Returns:
        - наступний елемент.

        Raises:
        - StopIteration: якщо закінчилися елементи для ітерації.
        """
        if self.current_data_set is None:
            self.current_data_set = iter(self.manager)
            self.current_data_set_iterator = iter(next(self.current_data_set).data_set)

        try:
            return next(self.current_data_set_iterator)
        except StopIteration:
            self.current_data_set_iterator = iter(next(self.current_data_set).data_set)
            return next(self.current_data_set_iterator)

        raise StopIteration
