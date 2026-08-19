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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 394)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.heightSpinBox = QSpinBox(Form)
        self.heightSpinBox.setObjectName(u"heightSpinBox")
        sizePolicy.setHeightForWidth(self.heightSpinBox.sizePolicy().hasHeightForWidth())
        self.heightSpinBox.setSizePolicy(sizePolicy)
        self.heightSpinBox.setMinimumSize(QSize(0, 25))
        self.heightSpinBox.setMinimum(640)
        self.heightSpinBox.setMaximum(1080)

        self.gridLayout.addWidget(self.heightSpinBox, 1, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.widthSpinBox = QSpinBox(Form)
        self.widthSpinBox.setObjectName(u"widthSpinBox")
        sizePolicy.setHeightForWidth(self.widthSpinBox.sizePolicy().hasHeightForWidth())
        self.widthSpinBox.setSizePolicy(sizePolicy)
        self.widthSpinBox.setMinimumSize(QSize(0, 25))
        self.widthSpinBox.setMinimum(800)
        self.widthSpinBox.setMaximum(1920)

        self.gridLayout.addWidget(self.widthSpinBox, 3, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.textEdit, 5, 0, 1, 1)

        self.acceptButton = QPushButton(Form)
        self.acceptButton.setObjectName(u"acceptButton")
        sizePolicy.setHeightForWidth(self.acceptButton.sizePolicy().hasHeightForWidth())
        self.acceptButton.setSizePolicy(sizePolicy)
        self.acceptButton.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.acceptButton, 6, 0, 1, 1)

        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.saveButton, 7, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Wysokosc", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Szerokosc", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.acceptButton.setText(QCoreApplication.translate("Form", u"Accept", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

