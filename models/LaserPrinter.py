from  models.printer import Printer

class LaserPrinter(Printer):
    def __init__(self, model, is_color, is_duplex, paper_tray_capacity, paper_count, toner_type, toner_level):
        super().__init__(model, is_color, is_duplex, paper_tray_capacity, paper_count)
        self.toner_type = toner_type
        self.toner_level = toner_level
        self.pages_printed = 0

    def print(self, pages):
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
        if self.paper_count + count > self.paper_tray_capacity:
            self.paper_count = self.paper_tray_capacity
            print(f"Paper tray is full. Loaded {self.paper_tray_capacity - self.paper_count} sheets of paper.")
        else:
            self.paper_count += count
            print(f"Loaded {count} sheets of paper. Total paper count: {self.paper_count}")

    def get_remaining_pages_count(self):
        return self.toner_level

    def __str__(self):
        return super().__str__() + f"\nToner Type: {self.toner_type}\nToner Level: {self.toner_level}\n" \
                                     f"Pages Printed: {self.pages_printed}"
