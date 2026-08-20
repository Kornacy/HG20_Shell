from PySide6.QtWidgets import QWidget
from ui.ui_startPage import Ui_Form
from PySide6.QtCore import Signal

class StartPage(QWidget):

    requestPage = Signal(str)
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.resultsButton.clicked.connect(lambda: self.requestPage.emit("results"))