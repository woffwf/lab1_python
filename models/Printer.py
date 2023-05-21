from abc import ABC, abstractmethod

class Printer(ABC):
    REQUIRED_COLOUR_PER_PAGE = 10

    def __init__(self, model, is_color, is_duplex, paper_tray_capacity, paper_count):
        self.model = model
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.paper_tray_capacity = paper_tray_capacity
        self.paper_count = paper_count

    @abstractmethod
    def print(self, pages):
        pass

    @abstractmethod
    def load_paper(self, count):
        pass

    @abstractmethod
    def get_remaining_pages_count(self):
        pass

    def __str__(self):
        return f"Model: {self.model}\nColor: {self.is_color}\nDuplex: {self.is_duplex}\n" \
               f"Paper Tray Capacity: {self.paper_tray_capacity}\nPaper Count: {self.paper_count}"
