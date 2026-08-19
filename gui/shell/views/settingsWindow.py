from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QPushButton, QSpinBox
from ui.ui_settings import Ui_Form


class SettingWindow(QWidget):
    resolutionChange = Signal(int,int)

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.saveButton.clicked.connect(self.eimtResolution)

    def setResolution(self, width: int, height: int) -> None:
        self.ui.widthSpinBox.setValue(width)
        self.ui.heightSpinBox.setValue(height)

    def eimtResolution(self) -> None:
        self.resolutionChange.emit(self.ui.widthSpinBox.value(),self.ui.heightSpinBox.value())