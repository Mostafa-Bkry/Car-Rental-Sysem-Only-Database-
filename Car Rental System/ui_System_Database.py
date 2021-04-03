from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class SystemDatabase(object):
    def setup(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 586)
        MainWindow.setStyleSheet(u"")
        MainWindow.setGeometry(163,74,1000,585)
        MainWindow.setWindowIcon(QIcon('Photos\Database_icon.png'))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-image: url(photos/4.jfif);\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lable = QFrame(self.centralwidget)
        self.lable.setObjectName(u"lable")
        self.lable.setStyleSheet(u"background:none;")
        self.lable.setFrameShape(QFrame.StyledPanel)
        self.lable.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.lable)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.l1 = QLabel(self.lable)
        self.l1.setObjectName(u"l1")
        self.l1.setMinimumSize(QSize(0, 50))
        self.l1.setStyleSheet(u"background:none;\n"
"font: bold 20pt \"Papyrus\";\n"
"color: rgb(255, 255, 255);")
        self.l1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.l1)


        self.verticalLayout_2.addWidget(self.lable)

        self.Btns = QFrame(self.centralwidget)
        self.Btns.setObjectName(u"Btns")
        self.Btns.setStyleSheet(u"background:none;")
        self.Btns.setFrameShape(QFrame.StyledPanel)
        self.Btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Btns)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 14)
        self.reservationB = QPushButton(self.Btns)
        self.reservationB.setObjectName(u"reservationB")
        self.reservationB.setMinimumSize(QSize(150, 28))
        self.reservationB.setMaximumSize(QSize(150, 31))
        self.reservationB.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:10px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid red;\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.reservationB)

        self.DriversB = QPushButton(self.Btns)
        self.DriversB.setObjectName(u"DriversB")
        self.DriversB.setMinimumSize(QSize(150, 27))
        self.DriversB.setMaximumSize(QSize(150, 28))
        self.DriversB.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid red;\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.DriversB)

        self.CarB = QPushButton(self.Btns)
        self.CarB.setObjectName(u"CarB")
        self.CarB.setMinimumSize(QSize(150, 28))
        self.CarB.setMaximumSize(QSize(150, 28))
        self.CarB.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid red;\n"
"}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.CarB)

        self.CustomerB = QPushButton(self.Btns)
        self.CustomerB.setObjectName(u"CustomerB")
        self.CustomerB.setMinimumSize(QSize(150, 29))
        self.CustomerB.setMaximumSize(QSize(150, 29))
        self.CustomerB.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"selection-color: rgb(85, 255, 255);\n"
"selection-background-color: rgb(0, 255, 255);\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid red;\n"
"}\n"
"\n"
"\n"
"")
        self.CustomerB.setFlat(False)

        self.horizontalLayout.addWidget(self.CustomerB)


        self.verticalLayout_2.addWidget(self.Btns)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background: none;\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.Reservations = QWidget()
        self.Reservations.setObjectName(u"Reservations")
        self.Reservations.setStyleSheet(u"background:solid #000000;")
        self.verticalLayout_4 = QVBoxLayout(self.Reservations)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_Res_page = QFrame(self.Reservations)
        self.frame_Res_page.setObjectName(u"frame_Res_page")
        self.frame_Res_page.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-image: url(photos/3.jpg);\n"
"")
        self.frame_Res_page.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame_Res_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Refresh_FrameRes = QFrame(self.frame_Res_page)
        self.Refresh_FrameRes.setObjectName(u"Refresh_FrameRes")
        self.Refresh_FrameRes.setStyleSheet(u"background:none;")
        self.Refresh_FrameRes.setFrameShape(QFrame.StyledPanel)
        self.Refresh_FrameRes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.Refresh_FrameRes)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.RefreshBRes = QPushButton(self.Refresh_FrameRes)
        self.RefreshBRes.setObjectName(u"RefreshBRes")
        self.RefreshBRes.setMinimumSize(QSize(110, 28))
        self.RefreshBRes.setMaximumSize(QSize(110, 28))
        self.RefreshBRes.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid red;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"")

        self.verticalLayout_23.addWidget(self.RefreshBRes)


        self.verticalLayout_5.addWidget(self.Refresh_FrameRes, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.frame_Res_table = QFrame(self.frame_Res_page)
        self.frame_Res_table.setObjectName(u"frame_Res_table")
        self.frame_Res_table.setStyleSheet(u"background:none;")
        self.frame_Res_table.setFrameShape(QFrame.StyledPanel)
        self.frame_Res_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_Res_table)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Functions = QFrame(self.frame_Res_table)
        self.Functions.setObjectName(u"Functions")
        self.Functions.setStyleSheet(u"background:none;")
        self.Functions.setFrameShape(QFrame.StyledPanel)
        self.Functions.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Functions)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 12)
        self.Search = QFrame(self.Functions)
        self.Search.setObjectName(u"Search")
        self.Search.setFrameShape(QFrame.StyledPanel)
        self.Search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Search)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lesearchRes = QLineEdit(self.Search)
        self.lesearchRes.setObjectName(u"lesearchRes")
        self.lesearchRes.setMinimumSize(QSize(290, 25))
        self.lesearchRes.setMaximumSize(QSize(250, 16777215))
        self.lesearchRes.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(255, 255, 255);\n"
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
        self.lesearchRes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lesearchRes)

        self.SearchBRes = QPushButton(self.Search)
        self.SearchBRes.setObjectName(u"SearchBRes")
        self.SearchBRes.setMinimumSize(QSize(110, 28))
        self.SearchBRes.setMaximumSize(QSize(110, 28))
        self.SearchBRes.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid #000000;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.SearchBRes)


        self.verticalLayout.addWidget(self.Search, 0, Qt.AlignHCenter)

        self.Delete = QFrame(self.Functions)
        self.Delete.setObjectName(u"Delete")
        self.Delete.setFrameShape(QFrame.StyledPanel)
        self.Delete.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Delete)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ledeleteRes = QLineEdit(self.Delete)
        self.ledeleteRes.setObjectName(u"ledeleteRes")
        self.ledeleteRes.setMinimumSize(QSize(290, 25))
        self.ledeleteRes.setMaximumSize(QSize(250, 16777215))
        self.ledeleteRes.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(255, 255, 255);\n"
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
        self.ledeleteRes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.ledeleteRes)

        self.DeleteBRes = QPushButton(self.Delete)
        self.DeleteBRes.setObjectName(u"DeleteBRes")
        self.DeleteBRes.setMinimumSize(QSize(110, 28))
        self.DeleteBRes.setMaximumSize(QSize(110, 28))
        self.DeleteBRes.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid #000000;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.DeleteBRes)


        self.verticalLayout.addWidget(self.Delete, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.Functions, 0, Qt.AlignHCenter)

        self.twR = QTableWidget(self.frame_Res_table)
        if (self.twR.columnCount() < 7):
            self.twR.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.twR.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twR.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.twR.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.twR.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.twR.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.twR.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.twR.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.twR.setObjectName(u"twR")
        self.twR.setMinimumSize(QSize(735, 0))
        self.twR.setStyleSheet(u"background-color: rgb(0, 227, 227);\n"
"color:black;\n"
"border-radius:15px;")
        self.twR.setFrameShape(QFrame.NoFrame)
        self.twR.setRowCount(0)

        self.verticalLayout_7.addWidget(self.twR, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame_Res_table)

        self.frame_forigen_table = QFrame(self.frame_Res_page)
        self.frame_forigen_table.setObjectName(u"frame_forigen_table")
        self.frame_forigen_table.setStyleSheet(u"background:none;")
        self.frame_forigen_table.setFrameShape(QFrame.StyledPanel)
        self.frame_forigen_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_forigen_table)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 5, 0, 3)
        self.twFRes = QTableWidget(self.frame_forigen_table)
        if (self.twFRes.columnCount() < 2):
            self.twFRes.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.twFRes.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.twFRes.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.twFRes.setObjectName(u"twFRes")
        self.twFRes.setMaximumSize(QSize(235, 16777215))
        self.twFRes.setLayoutDirection(Qt.LeftToRight)
        self.twFRes.setStyleSheet(u"background-color: rgb(0, 227, 227);\n"
"color:black;\n"
"border-radius:15px;")
        self.twFRes.setFrameShape(QFrame.NoFrame)
        self.twFRes.horizontalHeader().setDefaultSectionSize(100)
        self.twFRes.verticalHeader().setDefaultSectionSize(34)

        self.verticalLayout_6.addWidget(self.twFRes, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame_forigen_table)


        self.verticalLayout_4.addWidget(self.frame_Res_page, 0, Qt.AlignVCenter)

        self.tabWidget.addTab(self.Reservations, "")
        self.Drivers = QWidget()
        self.Drivers.setObjectName(u"Drivers")
        self.verticalLayout_12 = QVBoxLayout(self.Drivers)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_Dri_page = QFrame(self.Drivers)
        self.frame_Dri_page.setObjectName(u"frame_Dri_page")
        self.frame_Dri_page.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-image: url(photos/3.jpg);\n"
"")
        self.frame_Dri_page.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.frame_Dri_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 30)
        self.Refresh_FrameDri = QFrame(self.frame_Dri_page)
        self.Refresh_FrameDri.setObjectName(u"Refresh_FrameDri")
        self.Refresh_FrameDri.setStyleSheet(u"background:none;")
        self.Refresh_FrameDri.setFrameShape(QFrame.StyledPanel)
        self.Refresh_FrameDri.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.Refresh_FrameDri)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.RefreshBDri = QPushButton(self.Refresh_FrameDri)
        self.RefreshBDri.setObjectName(u"RefreshBDri")
        self.RefreshBDri.setMinimumSize(QSize(110, 28))
        self.RefreshBDri.setMaximumSize(QSize(110, 28))
        self.RefreshBDri.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid red;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"")

        self.verticalLayout_24.addWidget(self.RefreshBDri)


        self.verticalLayout_8.addWidget(self.Refresh_FrameDri, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.Functions2 = QFrame(self.frame_Dri_page)
        self.Functions2.setObjectName(u"Functions2")
        self.Functions2.setStyleSheet(u"background:none;")
        self.Functions2.setFrameShape(QFrame.StyledPanel)
        self.Functions2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Functions2)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 70, 0, 70)
        self.Search2 = QFrame(self.Functions2)
        self.Search2.setObjectName(u"Search2")
        self.Search2.setFrameShape(QFrame.StyledPanel)
        self.Search2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Search2)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lesearchDri = QLineEdit(self.Search2)
        self.lesearchDri.setObjectName(u"lesearchDri")
        self.lesearchDri.setMinimumSize(QSize(290, 25))
        self.lesearchDri.setMaximumSize(QSize(250, 16777215))
        self.lesearchDri.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(255, 255, 255);\n"
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
        self.lesearchDri.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lesearchDri)

        self.SearchBDri = QPushButton(self.Search2)
        self.SearchBDri.setObjectName(u"SearchBDri")
        self.SearchBDri.setMinimumSize(QSize(110, 28))
        self.SearchBDri.setMaximumSize(QSize(110, 28))
        self.SearchBDri.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid #000000;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.SearchBDri)


        self.verticalLayout_9.addWidget(self.Search2, 0, Qt.AlignHCenter)

        self.Delete2 = QFrame(self.Functions2)
        self.Delete2.setObjectName(u"Delete2")
        self.Delete2.setFrameShape(QFrame.StyledPanel)
        self.Delete2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Delete2)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ledeleteDri = QLineEdit(self.Delete2)
        self.ledeleteDri.setObjectName(u"ledeleteDri")
        self.ledeleteDri.setMinimumSize(QSize(290, 25))
        self.ledeleteDri.setMaximumSize(QSize(250, 16777215))
        self.ledeleteDri.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(255, 255, 255);\n"
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
        self.ledeleteDri.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.ledeleteDri)

        self.DeleteBDri = QPushButton(self.Delete2)
        self.DeleteBDri.setObjectName(u"DeleteBDri")
        self.DeleteBDri.setMinimumSize(QSize(110, 28))
        self.DeleteBDri.setMaximumSize(QSize(110, 28))
        self.DeleteBDri.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid #000000;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.DeleteBDri)


        self.verticalLayout_9.addWidget(self.Delete2, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.Functions2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_Dri_table = QFrame(self.frame_Dri_page)
        self.frame_Dri_table.setObjectName(u"frame_Dri_table")
        self.frame_Dri_table.setStyleSheet(u"background:none;")
        self.frame_Dri_table.setFrameShape(QFrame.StyledPanel)
        self.frame_Dri_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_Dri_table)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.twD = QTableWidget(self.frame_Dri_table)
        if (self.twD.columnCount() < 5):
            self.twD.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.twD.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.twD.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.twD.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.twD.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.twD.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        self.twD.setObjectName(u"twD")
        self.twD.setMinimumSize(QSize(535, 0))
        self.twD.setStyleSheet(u"background-color: rgb(0, 227, 227);\n"
"color:black;\n"
"border-radius:15px;")
        self.twD.setFrameShape(QFrame.NoFrame)
        self.twD.setRowCount(0)
        self.twD.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_10.addWidget(self.twD)


        self.verticalLayout_8.addWidget(self.frame_Dri_table, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_12.addWidget(self.frame_Dri_page)

        self.tabWidget.addTab(self.Drivers, "")
        self.Cars = QWidget()
        self.Cars.setObjectName(u"Cars")
        self.verticalLayout_16 = QVBoxLayout(self.Cars)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_Car_page = QFrame(self.Cars)
        self.frame_Car_page.setObjectName(u"frame_Car_page")
        self.frame_Car_page.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-image: url(photos/3.jpg);\n"
"")
        self.frame_Car_page.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.frame_Car_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 30)
        self.Refresh_FrameCar = QFrame(self.frame_Car_page)
        self.Refresh_FrameCar.setObjectName(u"Refresh_FrameCar")
        self.Refresh_FrameCar.setStyleSheet(u"background:none;")
        self.Refresh_FrameCar.setFrameShape(QFrame.StyledPanel)
        self.Refresh_FrameCar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.Refresh_FrameCar)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.RefreshBCar = QPushButton(self.Refresh_FrameCar)
        self.RefreshBCar.setObjectName(u"RefreshBCar")
        self.RefreshBCar.setMinimumSize(QSize(110, 28))
        self.RefreshBCar.setMaximumSize(QSize(110, 28))
        self.RefreshBCar.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid red;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"")

        self.verticalLayout_46.addWidget(self.RefreshBCar)


        self.verticalLayout_11.addWidget(self.Refresh_FrameCar, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.Functions3 = QFrame(self.frame_Car_page)
        self.Functions3.setObjectName(u"Functions3")
        self.Functions3.setStyleSheet(u"background:none;")
        self.Functions3.setFrameShape(QFrame.StyledPanel)
        self.Functions3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.Functions3)
        self.verticalLayout_13.setSpacing(7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 70, 0, 70)
        self.Search3 = QFrame(self.Functions3)
        self.Search3.setObjectName(u"Search3")
        self.Search3.setFrameShape(QFrame.StyledPanel)
        self.Search3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Search3)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lesearchCar = QLineEdit(self.Search3)
        self.lesearchCar.setObjectName(u"lesearchCar")
        self.lesearchCar.setMinimumSize(QSize(290, 25))
        self.lesearchCar.setMaximumSize(QSize(250, 16777215))
        self.lesearchCar.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(255, 255, 255);\n"
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
        self.lesearchCar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lesearchCar)

        self.SearchBCar = QPushButton(self.Search3)
        self.SearchBCar.setObjectName(u"SearchBCar")
        self.SearchBCar.setMinimumSize(QSize(110, 28))
        self.SearchBCar.setMaximumSize(QSize(110, 28))
        self.SearchBCar.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid #000000;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_6.addWidget(self.SearchBCar)


        self.verticalLayout_13.addWidget(self.Search3, 0, Qt.AlignHCenter)

        self.Delete3 = QFrame(self.Functions3)
        self.Delete3.setObjectName(u"Delete3")
        self.Delete3.setFrameShape(QFrame.StyledPanel)
        self.Delete3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Delete3)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ledeleteCar = QLineEdit(self.Delete3)
        self.ledeleteCar.setObjectName(u"ledeleteCar")
        self.ledeleteCar.setMinimumSize(QSize(290, 25))
        self.ledeleteCar.setMaximumSize(QSize(250, 16777215))
        self.ledeleteCar.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(255, 255, 255);\n"
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
        self.ledeleteCar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.ledeleteCar)

        self.DeleteBCar = QPushButton(self.Delete3)
        self.DeleteBCar.setObjectName(u"DeleteBCar")
        self.DeleteBCar.setMinimumSize(QSize(110, 28))
        self.DeleteBCar.setMaximumSize(QSize(110, 28))
        self.DeleteBCar.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid #000000;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.DeleteBCar)


        self.verticalLayout_13.addWidget(self.Delete3, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.Functions3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_Car_table = QFrame(self.frame_Car_page)
        self.frame_Car_table.setObjectName(u"frame_Car_table")
        self.frame_Car_table.setStyleSheet(u"background:none;")
        self.frame_Car_table.setFrameShape(QFrame.StyledPanel)
        self.frame_Car_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_Car_table)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.twCar = QTableWidget(self.frame_Car_table)
        if (self.twCar.columnCount() < 4):
            self.twCar.setColumnCount(4)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.twCar.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.twCar.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.twCar.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.twCar.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        self.twCar.setObjectName(u"twCar")
        self.twCar.setMinimumSize(QSize(435, 0))
        self.twCar.setStyleSheet(u"background-color: rgb(0, 227, 227);\n"
"color:black;\n"
"border-radius:15px;")
        self.twCar.setSortingEnabled(False)
        self.twCar.setRowCount(0)

        self.verticalLayout_14.addWidget(self.twCar)


        self.verticalLayout_11.addWidget(self.frame_Car_table, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_16.addWidget(self.frame_Car_page)

        self.tabWidget.addTab(self.Cars, "")
        self.Customers = QWidget()
        self.Customers.setObjectName(u"Customers")
        self.verticalLayout_20 = QVBoxLayout(self.Customers)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_Cus_page = QFrame(self.Customers)
        self.frame_Cus_page.setObjectName(u"frame_Cus_page")
        self.frame_Cus_page.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-image: url(photos/3.jpg);\n"
"")
        self.frame_Cus_page.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_15 = QVBoxLayout(self.frame_Cus_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Refresh_FrameCus = QFrame(self.frame_Cus_page)
        self.Refresh_FrameCus.setObjectName(u"Refresh_FrameCus")
        self.Refresh_FrameCus.setStyleSheet(u"background:none;")
        self.Refresh_FrameCus.setFrameShape(QFrame.StyledPanel)
        self.Refresh_FrameCus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.Refresh_FrameCus)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.RefreshBCus = QPushButton(self.Refresh_FrameCus)
        self.RefreshBCus.setObjectName(u"RefreshBCus")
        self.RefreshBCus.setMinimumSize(QSize(110, 28))
        self.RefreshBCus.setMaximumSize(QSize(110, 28))
        self.RefreshBCus.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid red;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"")

        self.verticalLayout_21.addWidget(self.RefreshBCus)


        self.verticalLayout_15.addWidget(self.Refresh_FrameCus, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.Functions4 = QFrame(self.frame_Cus_page)
        self.Functions4.setObjectName(u"Functions4")
        self.Functions4.setStyleSheet(u"background:none;")
        self.Functions4.setFrameShape(QFrame.StyledPanel)
        self.Functions4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.Functions4)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 12)
        self.Search4 = QFrame(self.Functions4)
        self.Search4.setObjectName(u"Search4")
        self.Search4.setFrameShape(QFrame.StyledPanel)
        self.Search4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Search4)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lesearchCus = QLineEdit(self.Search4)
        self.lesearchCus.setObjectName(u"lesearchCus")
        self.lesearchCus.setMinimumSize(QSize(290, 25))
        self.lesearchCus.setMaximumSize(QSize(250, 16777215))
        self.lesearchCus.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(255, 255, 255);\n"
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
        self.lesearchCus.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lesearchCus)

        self.SearchBCus = QPushButton(self.Search4)
        self.SearchBCus.setObjectName(u"SearchBCus")
        self.SearchBCus.setMinimumSize(QSize(110, 28))
        self.SearchBCus.setMaximumSize(QSize(110, 28))
        self.SearchBCus.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid #000000;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_8.addWidget(self.SearchBCus)


        self.verticalLayout_17.addWidget(self.Search4, 0, Qt.AlignHCenter)

        self.Delete4 = QFrame(self.Functions4)
        self.Delete4.setObjectName(u"Delete4")
        self.Delete4.setFrameShape(QFrame.StyledPanel)
        self.Delete4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Delete4)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.ledeleteCus = QLineEdit(self.Delete4)
        self.ledeleteCus.setObjectName(u"ledeleteCus")
        self.ledeleteCus.setMinimumSize(QSize(290, 25))
        self.ledeleteCus.setMaximumSize(QSize(250, 16777215))
        self.ledeleteCus.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius:12px;\n"
"background-color: rgb(255, 255, 255);\n"
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
        self.ledeleteCus.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.ledeleteCus)

        self.DeleteBCus = QPushButton(self.Delete4)
        self.DeleteBCus.setObjectName(u"DeleteBCus")
        self.DeleteBCus.setMinimumSize(QSize(110, 28))
        self.DeleteBCus.setMaximumSize(QSize(110, 28))
        self.DeleteBCus.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color:#ffffff;\n"
"background:solid black;\n"
"border-radius:12px;\n"
"border:1px solid aqua;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color: #000000;\n"
"border-radius:12px;\n"
"border:2px #00ffff;\n"
"background:#ececec;\n"
"border:2px solid #000000;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_9.addWidget(self.DeleteBCus)


        self.verticalLayout_17.addWidget(self.Delete4, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addWidget(self.Functions4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_Cus_table = QFrame(self.frame_Cus_page)
        self.frame_Cus_table.setObjectName(u"frame_Cus_table")
        self.frame_Cus_table.setStyleSheet(u"background:none;")
        self.frame_Cus_table.setFrameShape(QFrame.StyledPanel)
        self.frame_Cus_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_Cus_table)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.twCus = QTableWidget(self.frame_Cus_table)
        if (self.twCus.columnCount() < 3):
            self.twCus.setColumnCount(3)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.twCus.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.twCus.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.twCus.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        self.twCus.setObjectName(u"twCus")
        self.twCus.setMinimumSize(QSize(335, 0))
        self.twCus.setStyleSheet(u"background-color: rgb(0, 227, 227);\n"
"color:black;\n"
"border-radius:15px;\n"
"")
        self.twCus.setFrameShape(QFrame.NoFrame)
        self.twCus.setRowCount(0)

        self.verticalLayout_18.addWidget(self.twCus)


        self.verticalLayout_15.addWidget(self.frame_Cus_table, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_forigen_table_2 = QFrame(self.frame_Cus_page)
        self.frame_forigen_table_2.setObjectName(u"frame_forigen_table_2")
        self.frame_forigen_table_2.setStyleSheet(u"background:none;")
        self.frame_forigen_table_2.setFrameShape(QFrame.StyledPanel)
        self.frame_forigen_table_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_forigen_table_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 5, 0, 3)
        self.twFCus = QTableWidget(self.frame_forigen_table_2)
        if (self.twFCus.columnCount() < 2):
            self.twFCus.setColumnCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.twFCus.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.twFCus.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        self.twFCus.setObjectName(u"twFCus")
        self.twFCus.setMaximumSize(QSize(235, 16777215))
        self.twFCus.setLayoutDirection(Qt.LeftToRight)
        self.twFCus.setStyleSheet(u"background-color: rgb(0, 227, 227);\n"
"color:black;\n"
"border-radius:15px;")
        self.twFCus.setFrameShape(QFrame.NoFrame)
        self.twFCus.setRowCount(0)

        self.verticalLayout_19.addWidget(self.twFCus)


        self.verticalLayout_15.addWidget(self.frame_forigen_table_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_20.addWidget(self.frame_Cus_page)

        self.tabWidget.addTab(self.Customers, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.CopyRight = QFrame(self.centralwidget)
        self.CopyRight.setObjectName(u"CopyRight")
        self.CopyRight.setMaximumSize(QSize(16777215, 20))
        self.CopyRight.setStyleSheet(u"background:none;")
        self.CopyRight.setFrameShape(QFrame.StyledPanel)
        self.CopyRight.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.CopyRight)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.toolB2 = QToolButton(self.CopyRight)
        self.toolB2.setObjectName(u"toolB2")
        self.toolB2.setMaximumSize(QSize(18, 18))
        self.toolB2.setStyleSheet(u"background:solid rgb(0, 85, 255);\n"
"border-radius:8px;\n"
"")
        icon = QIcon()
        icon.addFile(u"Photos/Me.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolB2.setIcon(icon)
        self.toolB2.setIconSize(QSize(30, 16))

        self.horizontalLayout_10.addWidget(self.toolB2)

        self.label_3 = QLabel(self.CopyRight)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777206, 30))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Segoe Script\";")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_3)

        self.frame_5 = QFrame(self.CopyRight)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.CopyRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.CustomerB.setDefault(False)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Database", None))
        self.l1.setText(QCoreApplication.translate("MainWindow", u"Database Tables", None))
        self.reservationB.setText(QCoreApplication.translate("MainWindow", u"Reservations", None))
        self.DriversB.setText(QCoreApplication.translate("MainWindow", u"Drivers", None))
        self.CarB.setText(QCoreApplication.translate("MainWindow", u"Cars", None))
        self.CustomerB.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.RefreshBRes.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.lesearchRes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.SearchBRes.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.ledeleteRes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.DeleteBRes.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem = self.twR.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Res_ID ", None));
        ___qtablewidgetitem1 = self.twR.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Book_Time ", None));
        ___qtablewidgetitem2 = self.twR.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem3 = self.twR.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Street", None));
        ___qtablewidgetitem4 = self.twR.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Destination ", None));
        ___qtablewidgetitem5 = self.twR.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Price ", None));
        ___qtablewidgetitem6 = self.twR.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"License_No ", None));
        ___qtablewidgetitem7 = self.twFRes.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email ", None));
        ___qtablewidgetitem8 = self.twFRes.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Res_ID ", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Reservations), QCoreApplication.translate("MainWindow", u"Reservations", None))
        self.RefreshBDri.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.lesearchDri.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Licence_No", None))
        self.SearchBDri.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.ledeleteDri.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Licence_No", None))
        self.DeleteBDri.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem9 = self.twD.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Licence_No", None));
        ___qtablewidgetitem10 = self.twD.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Driver_Name", None));
        ___qtablewidgetitem11 = self.twD.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem12 = self.twD.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem13 = self.twD.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Drivers), QCoreApplication.translate("MainWindow", u"Drivers", None))
        self.RefreshBCar.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.lesearchCar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Car_No", None))
        self.SearchBCar.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.ledeleteCar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Car_No", None))
        self.DeleteBCar.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem14 = self.twCar.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Car_No ", None));
        ___qtablewidgetitem15 = self.twCar.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Car_Type ", None));
        ___qtablewidgetitem16 = self.twCar.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Car_Color ", None));
        ___qtablewidgetitem17 = self.twCar.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"License_No ", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cars), QCoreApplication.translate("MainWindow", u"Cars", None))
        self.RefreshBCus.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.lesearchCus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.SearchBCus.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.ledeleteCus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.DeleteBCus.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem18 = self.twCus.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Email ", None));
        ___qtablewidgetitem19 = self.twCus.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Customer_Name ", None));
        ___qtablewidgetitem20 = self.twCus.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Phone ", None));
        ___qtablewidgetitem21 = self.twFCus.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Email ", None));
        ___qtablewidgetitem22 = self.twFCus.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Res_ID ", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Customers), QCoreApplication.translate("MainWindow", u"Customers", None))
        self.toolB2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"By: Mostafa Bkry", None))
    # retranslateUi