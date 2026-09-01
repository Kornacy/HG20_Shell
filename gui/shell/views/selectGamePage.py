from PySide6.QtWidgets import QWidget, QPushButton, QSpinBox
from ui.ui_gameSelect import Ui_Form

class SelectGamePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

