from managers.printer_manager import PrinterManager
from models.inkjet_printer import InkjetPrinter
from models.laser_printer import LaserPrinter
from models.color_laser_printer import ColorLaserPrinter
from models.dot_matrix_printer import DotMatrixPrinter

def main():
    inkjet_printer = InkjetPrinter("Epson Inkjet", True, False, 100, 50, "CMYK", 1000)
    laser_printer = LaserPrinter("HP LaserJet", False, True, 200, 100, "Black", 500)
    color_laser_printer = ColorLaserPrinter("Canon Color Laser", True, False, 150, 75, "CMYK", 2000)
    dot_matrix_printer = DotMatrixPrinter("Panasonic Dot Matrix", False, True, 80, 50, "Black", 3000)

    printer_manager = PrinterManager()
    printer_manager.add_printer(inkjet_printer)
    printer_manager.add_printer(laser_printer)
    printer_manager.add_printer(color_laser_printer)
    printer_manager.add_printer(dot_matrix_printer)

    printer_manager.print_all(5)

if __name__ == "__main__":
    main()
