from PySide6.QtWidgets import QMainWindow
from ui.ui_shell import Ui_MainWindow


class ShellWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
