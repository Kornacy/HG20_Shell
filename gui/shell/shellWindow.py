from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QStackedWidget, QWidget
from ui.ui_shell import Ui_MainWindow
from shell.views.settingsWindow import SettingWindow
class ShellWindow(QMainWindow):
    backButtton: QPushButton
    screenTitle: QLabel
    settingsButton: QPushButton
    stackedWidget: QStackedWidget

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._pages: dict[str, QWidget] = {}
        self.settingPage = SettingWindow()   
        self.addPage("settings",self.settingPage)

        self.settingPage.resolutionChange.connect(self.applyResolution)
        self.settingPage.setResolution(self.width(), self.height())

        self.ui.settingsButton.clicked.connect(lambda: self.openPage("settings"))
    def addPage(self, name: str, page: QWidget) -> None:
        self._pages[name] = page
        self.ui.stackedWidget.addWidget(page)
    def openPage(self, name: str) -> None:
        page = self._pages[name]
        self.ui.stackedWidget.setCurrentWidget(page)

    def applyResolution(self, width: int, height: int) -> None:
        self.resize(width, height)
