from models.Printer import Printer


class InkjetPrinter(Printer):
    def __init__(self, model, is_color, is_duplex, paper_tray_capacity, paper_count, ink_type, ink_level):
        super().__init__(model, is_color, is_duplex, paper_tray_capacity, paper_count)
        self.ink_type = ink_type
        self.ink_level = ink_level

    def print(self, pages):
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
        if self.paper_count + count > self.paper_tray_capacity:
            self.paper_count = self.paper_tray_capacity
            print(f"Paper tray is full. Loaded {self.paper_tray_capacity - self.paper_count} sheets of paper.")
        else:
            self.paper_count += count
            print(f"Loaded {count} sheets of paper. Total paper count: {self.paper_count}")

    def get_remaining_pages_count(self):
        return self.ink_level

    def __str__(self):
        return super().__str__() + f"\nInk Type: {self.ink_type}\nInk Level: {self.ink_level}"
