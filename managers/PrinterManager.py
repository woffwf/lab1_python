from printer import Printer

class PrinterManager:
    def __init__(self):
        self.printers = []

    def add_printer(self, printer):
        self.printers.append(printer)

    def remove_printer(self, printer):
        self.printers.remove(printer)

    def print_documents(self, pages):
        for printer in self.printers:
            printer.print(pages)

    def get_remaining_pages(self):
        remaining_pages = {}
        for printer in self.printers:
            remaining_pages[printer.model] = printer.get_remaining_pages_count()
        return remaining_pages
