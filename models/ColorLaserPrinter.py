from  models.laser_printer import LaserPrinter

class ColorLaserPrinter(LaserPrinter):
    def __init__(self, model, is_color, is_duplex, paper_tray_capacity, paper_count, toner_type, toner_level):
        super().__init__(model, is_color, is_duplex, paper_tray_capacity, paper_count, toner_type, toner_level)

    def print(self, pages):
        if self.is_color:
            super().print(pages)
        else:
            print("This printer does not support color printing.")

    def __str__(self):
        return super().__str__() + "\nColor Printing Supported: Yes"
