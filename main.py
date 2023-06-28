"""
module: main
"""
from exception.printer_error_exception import PrinterError
from managers.printer_manager import PrinterManager
from models.inkjet_printer import InkjetPrinter
from models.laser_printer import LaserPrinter
from models.dot_matrix_printer import DotMatrixPrinter

def main():
    """
    Головна функція програми.
    """
    inkjet_printer = InkjetPrinter("Epson", True, False, 100, 50, "CMYK", 1000)
    laser_printer = LaserPrinter("HP", False, True, 200, 100, "Black", 500)
    dot_matrix_printer = DotMatrixPrinter("Panasonic", False, True, 80, 50, "Black", 3000)

    printer_manager = PrinterManager()
    printer_manager.add_printer(inkjet_printer)
    printer_manager.add_printer(laser_printer)
    printer_manager.add_printer(dot_matrix_printer)
    printer_manager.print_all(5)

    try:
        printer_manager.print_all(5)
    except PrinterError as e:
        print(f"Сталася помилка принтера: {e.message}")


if __name__ == "__main__":
    main()
