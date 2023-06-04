class PrinterError(Exception):
    """
    Виняток, пов'язаний з помилками принтера.
    """

    def __init__(self, message):
        """
        Ініціалізує об'єкт винятку зі специфічним повідомленням помилки.

        Arguments:
        - message: повідомлення про помилку.
        """
        self.message = message
        super().__init__(self.message)
