from managers.PrinterManager import PrinterManager
from models.InkjetPrinter import InkjetPrinter
from models.LaserPrinter import LaserPrinter
from models.DotMatrixPrinter import DotMatrixPrinter

def main():
     inkjet_printer = InkjetPrinter("Epson", True, False, 100, 50, "CMYK", 1000)
     laser_printer = LaserPrinter("HP ", False, True, 200, 100, "Black", 500)
     dot_matrix_printer = DotMatrixPrinter("Panasonic ", False, True, 80, 50, "Black", 3000)

     printer_manager = PrinterManager()
     printer_manager.add_printer(inkjet_printer)
     printer_manager.add_printer(laser_printer)
     printer_manager.add_printer(dot_matrix_printer)

     printer_manager.print_all(5)

if __name__ == "__main__":
     main()
