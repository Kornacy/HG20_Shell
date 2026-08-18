from PySide6.QtWidgets import QWidget, QPushButton
from ui.ui_settings import Ui_Form


class SettingWindow(QWidget):
    saveButton: QPushButton
    acceptButton: QPushButton

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    