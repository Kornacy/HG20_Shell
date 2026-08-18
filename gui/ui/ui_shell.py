# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shell.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, 49, 801, 551))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 10, 75, 24))
        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(710, 10, 75, 24))
        self.screenTitle = QLabel(self.centralwidget)
        self.screenTitle.setObjectName(u"screenTitle")
        self.screenTitle.setGeometry(QRect(360, 10, 91, 21))
        self.screenTitle.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        self.screenTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.screenTitle.setText(QCoreApplication.translate("MainWindow", u"HandGame 2.0", None))
    # retranslateUi

