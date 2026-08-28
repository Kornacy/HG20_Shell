from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QStackedWidget, QWidget
from PySide6.QtCore import Qt
from ui.ui_shell import Ui_MainWindow
from shell.views.settingsWindow import SettingWindow
from shell.views.startPage import StartPage
from shell.views.resultsPage import ResultPage
class ShellWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.windowGeometry = None

        screen = self.screen()
        available = screen.availableGeometry()


        startWidth = min(1280, available.width())
        startHeight = min(720, available.height())

        self.resize(startWidth, startHeight)
        self.move(available.center()-self.frameGeometry().center())
        

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
        self.settingPage.setResolution(startWidth, startHeight)
        self.settingPage.fullScreenRequest.connect(self.showFullScreen)

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
        if self.isFullScreen():
            self.showNormal()
        screen = self.screen()
        available = screen.availableGeometry()
        frame = self.frameGeometry()
        heightDiff = frame.height() - self.height()
        widthDiff = frame.width() - self.width()
        width = min(width, available.width()-widthDiff)
        height = min(height, available.height()-heightDiff)
        
        self.resize(width, height)
        self.windowGeometry = self.geometry()
        self._keepOnScreen()

    def _keepOnScreen(self) -> None:
        screen = self.screen()
        available = screen.availableGeometry()
        frame = self.frameGeometry()

        x=frame.x()
        y=frame.y()

        if frame.right()>available.right():
            x=available.right() - frame.width() + 1
        if frame.bottom() > available.bottom():
            y = available.bottom() - frame.height() + 1
        if x < available.left():
            x = available.left()
        if y < available.top():
            y = available.top()
        self.move(x,y)


    def goBack(self) -> None:
        if not self._history:
            return
        prevId = self._history.pop()
        self._currentPage = prevId
        page, title = self._pages[prevId]
        self.ui.screenTitle.setText(title)
        self.ui.stackedWidget.setCurrentWidget(page)


    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key.Key_F11 and self.isFullScreen():
            self.showNormal()
            self.setGeometry(self.windowGeometry)
            self.settingPage.ui.fullScreenCheckBox.setChecked(False) 
        elif event.key() == Qt.Key.Key_F11 and not self.isFullScreen():
            self.windowGeometry = self.geometry()
            self.showFullScreen()
            self.settingPage.ui.fullScreenCheckBox.setChecked(True) 
        else:
            super().keyPressEvent(event)