# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.acceptButton = QPushButton(Form)
        self.acceptButton.setObjectName(u"acceptButton")
        self.acceptButton.setGeometry(QRect(150, 200, 75, 24))
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 90, 104, 71))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 70, 49, 16))
        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(150, 240, 75, 24))
        self.heightSpinBox = QSpinBox(Form)
        self.heightSpinBox.setObjectName(u"heightSpinBox")
        self.heightSpinBox.setGeometry(QRect(251, 70, 81, 22))
        self.heightSpinBox.setMinimum(640)
        self.heightSpinBox.setMaximum(1080)
        self.widthSpinBox = QSpinBox(Form)
        self.widthSpinBox.setObjectName(u"widthSpinBox")
        self.widthSpinBox.setGeometry(QRect(251, 130, 91, 22))
        self.widthSpinBox.setMinimum(800)
        self.widthSpinBox.setMaximum(1920)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(248, 50, 61, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(248, 110, 71, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.acceptButton.setText(QCoreApplication.translate("Form", u"Accept", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Wysokosc", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Szerokosc", None))
    # retranslateUi

