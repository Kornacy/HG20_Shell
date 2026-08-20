from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QStackedWidget, QWidget
from ui.ui_shell import Ui_MainWindow
from shell.views.settingsWindow import SettingWindow
from shell.views.startPage import StartPage
from shell.views.resultsPage import ResultPage
class ShellWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._pages: dict[str, tuple[QWidget, str]] = {}
        self.settingPage = SettingWindow()
        self.startPage = StartPage()   
        self._history: list[str] = []
        self._currentPage: str | None = None

        #Dodawanie ekranów na shell
        self.addPage("settings",self.settingPage,"Ustawienia")
        self.addPage("main",self.startPage,"HandGame 2.0")
        self.addPage("results",ResultPage(),"Wyniki")

        #Ekran startowy
        self.openPage("main")

        self.settingPage.resolutionChange.connect(self.applyResolution)
        self.settingPage.setResolution(self.width(), self.height())

        self.startPage.requestPage.connect(self.openPage)
        #Przyciski
        self.ui.backButton.clicked.connect(lambda: self.goBack())
        self.ui.settingsButton.clicked.connect(lambda: self.openPage("settings"))

    def addPage(self, id: str, page: QWidget, title: str) -> None:
        self._pages[id] = (page, title)
        self.ui.stackedWidget.addWidget(page)

    def openPage(self, id: str) -> None:
        if id not in self._pages:
            return
        if id == self._currentPage:
            return
        if self._currentPage is not None:
            self._history.append(self._currentPage)
        self._currentPage = id
        page, title = self._pages[id]
        self.ui.screenTitle.setText(title)
        self.ui.stackedWidget.setCurrentWidget(page)

    def applyResolution(self, width: int, height: int) -> None:
        self.resize(width, height)

    def goBack(self) -> None:
        if not self._history:
            return
        prevId = self._history.pop()
        self._currentPage = prevId
        page, title = self._pages[prevId]
        self.ui.screenTitle.setText(title)
        self.ui.stackedWidget.setCurrentWidget(page)