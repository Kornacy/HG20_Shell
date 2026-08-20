from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QStackedWidget, QWidget
from ui.ui_shell import Ui_MainWindow
from shell.views.settingsWindow import SettingWindow
from shell.views.startPage import StartPage
class ShellWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._pages: dict[str, tuple[QWidget, str]] = {}
        self.settingPage = SettingWindow()   
        self.addPage("settings",self.settingPage,"Ustawienia")
        self.addPage("main",StartPage(),"HandGame 2.0")
        self.openPage("main")
        self.settingPage.resolutionChange.connect(self.applyResolution)
        self.settingPage.setResolution(self.width(), self.height())
        self.ui.backButton.clicked.connect(lambda: self.openPage("main"))
        self.ui.settingsButton.clicked.connect(lambda: self.openPage("settings"))

    def addPage(self, id: str, page: QWidget, title: str) -> None:
        self._pages[id] = (page, title)
        self.ui.stackedWidget.addWidget(page)

    def openPage(self, id: str) -> None:
        page, title = self._pages[id]
        self.ui.screenTitle.setText(title)
        self.ui.stackedWidget.setCurrentWidget(page)

    def applyResolution(self, width: int, height: int) -> None:
        self.resize(width, height)
