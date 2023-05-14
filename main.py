class Printer:
    def __init__(self, model, type, isColor, isDuplex, paperTrayCapacity, paperCount):
        self.model = model
        self.type = type
        self.isColor = isColor
        self.isDuplex = isDuplex
        self.paperTrayCapacity = paperTrayCapacity
        self.paperCount = paperCount

    def print(self, pages):
        if pages <= self.paperCount:
            self.paperCount -= pages
            print(f"Printing {pages} pages.")
        else:
            print("Not enough paper in the tray.")

    def loadPaper(self, count):
        if self.paperCount + count > self.paperTrayCapacity:
            self.paperCount = self.paperTrayCapacity
            print(f"Paper tray is full. Loaded {self.paperTrayCapacity - self.paperCount} sheets of paper.")
        else:
            self.paperCount += count
            print(f"Loaded {count} sheets of paper. Total paper count: {self.paperCount}")

printer = Printer("HP LaserJet", "лазерний", False, True, 100, 50)

printer.print(10)

printer.loadPaper(50)

