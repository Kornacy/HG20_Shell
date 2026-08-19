from PySide6.QtWidgets import QWidget
from ui.ui_startPage import Ui_Form


class StartPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)