from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(751, 490)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-image: url(photos/1.jpg);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background:none;\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.H_Layout = QHBoxLayout(self.frame)
        self.H_Layout.setObjectName(u"H_Layout")
        self.frame_lable = QFrame(self.frame)
        self.frame_lable.setObjectName(u"frame_lable")
        self.frame_lable.setFrameShape(QFrame.NoFrame)
        self.frame_lable.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lable)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.label_2 = QLabel(self.frame_lable)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 16777215))
        self.label_2.setStyleSheet(u"font: 26pt \"Papyrus\";\n"
"color: rgb(255, 253, 180);\n"
"color: rgb(0, 255, 127);\n"
"")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.frame_lable)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.H_Layout.addWidget(self.frame_lable, 0, Qt.AlignTop)

        self.frame_info = QFrame(self.frame)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setMaximumSize(QSize(250, 400))
        self.frame_info.setFrameShape(QFrame.NoFrame)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_info)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 65, -1, 120)
        self.frame_icon = QFrame(self.frame_info)
        self.frame_icon.setObjectName(u"frame_icon")
        self.frame_icon.setMaximumSize(QSize(16777215, 65))
        self.frame_icon.setFrameShape(QFrame.NoFrame)
        self.frame_icon.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_icon)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.frame_icon)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.toolB1 = QToolButton(self.frame_icon)
        self.toolB1.setObjectName(u"toolB1")
        self.toolB1.setMinimumSize(QSize(0, 51))
        self.toolB1.setMaximumSize(QSize(51, 51))
        self.toolB1.setStyleSheet(u"border-radius:25px;\n"
"background-color: rgb(0, 0, 0);")
        icon = QIcon()
        icon.addFile(u"Photos/Person.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.toolB1.setIcon(icon)
        self.toolB1.setIconSize(QSize(150, 176))

        self.horizontalLayout_2.addWidget(self.toolB1)

        self.frame_6 = QFrame(self.frame_icon)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_icon)

        self.ale1 = QLineEdit(self.frame_info)
        self.ale1.setObjectName(u"ale1")
        self.ale1.setMaximumSize(QSize(16777215, 30))
        self.ale1.setLayoutDirection(Qt.LeftToRight)
        self.ale1.setAutoFillBackground(False)
        self.ale1.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(179, 255, 108);\n"
"border:1px solid black;\n"
"}\n"
"\n"
"QLineEdit:hover \n"
"{\n"
"background:solid #e3e3e3;\n"
"border:1px solid blue;\n"
"}\n"
"\n"
"\n"
"")
        self.ale1.setInputMethodHints(Qt.ImhNone)
        self.ale1.setFrame(True)
        self.ale1.setAlignment(Qt.AlignCenter)
        self.ale1.setClearButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.ale1)

        self.ale2 = QLineEdit(self.frame_info)
        self.ale2.setObjectName(u"ale2")
        self.ale2.setMaximumSize(QSize(16777215, 30))
        self.ale2.setAutoFillBackground(False)
        self.ale2.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(179, 255, 108);\n"
"border:1px solid black;\n"
"}\n"
"\n"
"QLineEdit:hover \n"
"{\n"
"background:solid #e3e3e3;\n"
"border:1px solid blue;\n"
"}\n"
"\n"
"\n"
"")
        self.ale2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.ale2.setFrame(True)
        self.ale2.setEchoMode(QLineEdit.Password)
        self.ale2.setAlignment(Qt.AlignCenter)
        self.ale2.setClearButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.ale2)

        self.frame_B1 = QFrame(self.frame_info)
        self.frame_B1.setObjectName(u"frame_B1")
        self.frame_B1.setFrameShape(QFrame.NoFrame)
        self.frame_B1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_B1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_B1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_7)

        self.B1 = QPushButton(self.frame_B1)
        self.B1.setObjectName(u"B1")
        self.B1.setMinimumSize(QSize(75, 26))
        self.B1.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.B1.setAutoFillBackground(False)
        self.B1.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid #a2f077;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid #000000;\n"
"}\n"
"\n"
"")
        self.B1.setFlat(False)

        self.horizontalLayout_3.addWidget(self.B1)

        self.frame_8 = QFrame(self.frame_B1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_B1, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.H_Layout.addWidget(self.frame_info)

        self.frame_empty = QFrame(self.frame)
        self.frame_empty.setObjectName(u"frame_empty")
        self.frame_empty.setFrameShape(QFrame.NoFrame)
        self.frame_empty.setFrameShadow(QFrame.Raised)

        self.H_Layout.addWidget(self.frame_empty)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 20))
        self.frame_2.setStyleSheet(u"background:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolB2 = QToolButton(self.frame_2)
        self.toolB2.setObjectName(u"toolB2")
        self.toolB2.setMaximumSize(QSize(18, 18))
        self.toolB2.setStyleSheet(u"background:solid rgb(0, 85, 255);\n"
"border-radius:8px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"Photos/Me.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolB2.setIcon(icon1)
        self.toolB2.setIconSize(QSize(30, 16))

        self.horizontalLayout_4.addWidget(self.toolB2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777206, 30))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Segoe Script\";")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">AdMin Login</span></p></body></html>", None))
        self.label.setText("")
        self.toolB1.setText("")
        self.ale1.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Your Name", None))
        self.ale2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Password", None))
        self.B1.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.toolB2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"By: Mostafa Bkry", None))
    # retranslateUi