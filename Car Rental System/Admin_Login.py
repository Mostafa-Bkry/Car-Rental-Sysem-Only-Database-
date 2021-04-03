import sys
import mysql.connector
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from ui_MainWindow_car import Ui_MainWindow
from ui_System_Database import SystemDatabase

#--------------------------------------------------------------------------------------
#Database connection
try:
    con = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = '12345',
                database = 'database_mysql')
    #QMessageBox.about(self, 'Connection', 'Connection Succeded')
except mysql.connector.Error as e:
    print(e)
    print('Error: Check your database connection')
    #QMessageBox.about(self, 'Connection', 'Connection Faild')
    sys.exit(1)
cur = con.cursor(buffered=True)
#-------------------------------------------------------------------------------

class Ui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setGeometry(230,150,757,504)
        self.setWindowTitle('Admin')
        self.setWindowIcon(QIcon('photos\icon.jfif'))
        self.ui.B1.clicked.connect(self.login)

    def login(self):
        if self.ui.ale1.text() != 'Mostafa Ala' or self.ui.ale2.text() != '123':
            QMessageBox.about(self, 'Login Error', 'Please, check your user name or password')
        else:
            self.ui.B1.setText(('System Database'))
            self.ui.label.setText(self.ui.ale1.text())
            self.ui.label.setStyleSheet('font:19pt family;color: white')
            self.ui.B1.setMinimumSize(QSize(150, 29))
            self.ui.B1.clicked.connect(self.database)

    def database(self):
        QMessageBox.about(self, 'Login', 'Welcome, ' + self.ui.ale1.text() + ' to system database')
        self.window = QMainWindow()
        self.ui = SystemDatabase()
        self.ui.setup(self.window)
        self.window.show()
        window.hide()
        #-------------------------------------------------------------------------------
        #Moving between pages of QTapWidget
        self.ui.reservationB.clicked.connect(lambda: self.ui.tabWidget.setCurrentWidget(self.ui.Reservations))
        self.ui.DriversB.clicked.connect(lambda: self.ui.tabWidget.setCurrentWidget(self.ui.Drivers))
        self.ui.CarB.clicked.connect(lambda: self.ui.tabWidget.setCurrentWidget(self.ui.Cars))
        self.ui.CustomerB.clicked.connect(lambda: self.ui.tabWidget.setCurrentWidget(self.ui.Customers))
        #-------------------------------------------------------------------------------
        self.ui.SearchBRes.clicked.connect(self.SearchBRes)
        self.ui.DeleteBRes.clicked.connect(self.DeleteBRes)
        self.ui.SearchBDri.clicked.connect(self.SearchBDri)
        self.ui.DeleteBDri.clicked.connect(self.DeleteBDri)
        self.ui.SearchBCar.clicked.connect(self.SearchBCar)
        self.ui.DeleteBCar.clicked.connect(self.DeleteBCar)
        self.ui.SearchBCus.clicked.connect(self.SearchBCus)
        self.ui.DeleteBCus.clicked.connect(self.DeleteBCus)
        self.ui.RefreshBRes.clicked.connect(self.RefreshBRes)
        self.ui.RefreshBDri.clicked.connect(self.RefreshBDri)
        self.ui.RefreshBCar.clicked.connect(self.RefreshBCar)
        self.ui.RefreshBCus.clicked.connect(self.RefreshBCus)

    def RefreshBRes(self):
        cur = con.cursor(buffered=True)
        Res_table = "select * from reservation"
        cur.execute(Res_table)
        fetch = cur.fetchall()
        self.ui.twR.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twR.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twR.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        Foreign_table = "select * from customer_reservations"
        cur.execute(Foreign_table)
        fetch = cur.fetchall()
        self.ui.twFRes.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twFRes.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twFRes.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
    def RefreshBDri(self):
        cur = con.cursor(buffered=True)
        Dri_table = "select * from driver"
        cur.execute(Dri_table)
        fetch = cur.fetchall()
        self.ui.twD.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twD.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twD.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def RefreshBCar(self):
        cur = con.cursor(buffered=True)
        car_table = "select * from car"
        cur.execute(car_table)
        fetch = cur.fetchall()
        self.ui.twCar.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twCar.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twCar.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def RefreshBCus(self):
        cur = con.cursor(buffered=True)
        Cus_table = "select * from customer"
        cur.execute(Cus_table)
        fetch = cur.fetchall()
        self.ui.twCus.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twCus.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twCus.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        Foreign_table = "select * from customer_reservations"
        cur.execute(Foreign_table)
        fetch = cur.fetchall()
        self.ui.twFCus.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twFCus.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twFCus.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    def SearchBRes(self):
        cur = con.cursor(buffered=True)
        #check---------------------------------------------------------------------
        if self.ui.lesearchRes.text() == '':
            QMessageBox.about(self, 'Search Error', 'Please, add ID')
            return 1
        try:
            Res_search = int(self.ui.lesearchRes.text())
        except:
            QMessageBox.about(self, 'Search Error', 'Please, only search by ID')
            return 1
        #--------------------------------------------------------------------------
        query = 'select * from reservation where Res_ID  = %s'
        cur.execute(query, (Res_search,))
        fetch = cur.fetchall()
        self.ui.twR.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twR.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twR.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
        Foreign_search = int(self.ui.lesearchRes.text())
        query = 'select * from customer_reservations where Res_ID  = %s'
        cur.execute(query, (Foreign_search,))
        fetch = cur.fetchall()
        self.ui.twFRes.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twFRes.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twFRes.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
    def SearchBDri(self):
        cur = con.cursor(buffered=True)
        #check---------------------------------------------------------------------
        if self.ui.lesearchDri.text() == '':
            QMessageBox.about(self, 'Search Error', 'Please, add License_No')
            return 1
        try:
            Dri_search = int(self.ui.lesearchDri.text())
        except:
            QMessageBox.about(self, 'Search Error', 'Please, only search by License_No')
            return 1
        #--------------------------------------------------------------------------
        query = 'select * from driver where License_No = %s'
        cur.execute(query, (Dri_search,))
        fetch = cur.fetchall()
        self.ui.twD.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twD.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twD.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
    def SearchBCar(self):
        cur = con.cursor(buffered=True)
        #check---------------------------------------------------------------------
        if self.ui.lesearchCar.text() == '':
            QMessageBox.about(self, 'Search Error', 'Please, add Car_No')
            return 1
        try:
            Car_search = int(self.ui.lesearchCar.text())
        except:
            QMessageBox.about(self, 'Search Error', 'Please, only search by Car_No')
            return 1
        #--------------------------------------------------------------------------
        query = 'select * from car where Car_No = %s'
        cur.execute(query, (Car_search,))
        fetch = cur.fetchall()
        self.ui.twCar.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twCar.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twCar.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                
    def SearchBCus(self):
        cur = con.cursor(buffered=True)
        Cus_search = self.ui.lesearchCus.text()
        #check---------------------------------------------------------------------
        if Cus_search == '':
            QMessageBox.about(self, 'Search Error', 'Please, add Email')
            return 1
        elif len(Cus_search.split('@')) != 2:
            QMessageBox.about(self, 'Search Error', 'Invalid Email')
            return 1
        elif Cus_search.split('@')[1].split('.')[0] != 'gmail':
            QMessageBox.about(self, 'Search Error', 'Invalid Email (' +
                              Cus_search.split('@')[1].split('.')[0] + ')')
            return 1
        elif Cus_search.split('@')[1].split('.')[1] != 'com':
            QMessageBox.about(self, 'Search Error', 'Invalid Email (' +
                              Cus_search.split('@')[1].split('.')[1] + ')')
            return 1
        #---------------------------------------------------------------------------
        query = 'select * from customer where Email = %s'
        cur.execute(query, (Cus_search,))
        fetch = cur.fetchall()
        self.ui.twCus.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twCus.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twCus.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        Foreign_search = self.ui.lesearchCus.text()
        query = 'select * from customer_reservations where Email  = %s'
        cur.execute(query, (Foreign_search,))
        fetch = cur.fetchall()
        self.ui.twFCus.setRowCount(0)
        for row_number, row_data in enumerate(fetch):
            self.ui.twFCus.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.twFCus.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def DeleteBRes(self):
        cur = con.cursor(buffered=True)
        #check---------------------------------------------------------------------
        if self.ui.ledeleteRes.text() == '':
            QMessageBox.about(self, 'Delete Error', 'Please, add ID')
            return 1
        try:
            Res_Delete = int(self.ui.ledeleteRes.text())
        except:
            QMessageBox.about(self, 'Delete Error', 'Please, only delete by ID')
            return 1
        #--------------------------------------------------------------------------
        query = 'delete from reservation where Res_ID = %s'
        try:
            cur.execute(query, (Res_Delete,))
            QMessageBox.about(self, 'Checkup', 'ID: ' + str(Res_Delete) + ' was deleted successfully')
        except:
            QMessageBox.about(self, 'Checkup', 'ID: ' + str(Res_Delete) + ' can not be deleted')
            return 1
        
    def DeleteBDri(self):
        cur = con.cursor(buffered=True)
        #check---------------------------------------------------------------------
        if self.ui.ledeleteDri.text() == '':
            QMessageBox.about(self, 'Delete Error', 'Please, add License_No')
            return 1
        try:
            Dri_Delete = int(self.ui.ledeleteDri.text())
        except:
            QMessageBox.about(self, 'Delete Error', 'Please, only delete by License_No')
            return 1
        #--------------------------------------------------------------------------
        query = 'delete from driver where License_No = %s'
        try:
            cur.execute(query, (Dri_Delete,))
            QMessageBox.about(self, 'Checkup', 'License_No: ' + str(Dri_Delete) + ' was deleted successfully')
        except:
            QMessageBox.about(self, 'Checkup', 'License_No: ' + str(Dri_Delete) + ' can not be deleted')
            return 1
        
    def DeleteBCar(self):
        cur = con.cursor(buffered=True)
        #check---------------------------------------------------------------------
        if self.ui.ledeleteCar.text() == '':
            QMessageBox.about(self, 'Delete Error', 'Please, add Car_No')
            return 1
        try:
            Car_Delete = int(self.ui.ledeleteCar.text())
        except:
            QMessageBox.about(self, 'Delete Error', 'Please, only delete by Car_No')
            return 1
        #--------------------------------------------------------------------------
        query = 'delete from car where Car_No = %s'
        try:
            cur.execute(query, (Car_Delete,))
            QMessageBox.about(self, 'Checkup', 'Car_No: ' + str(Car_Delete) + ' was deleted successfully')
        except:
            QMessageBox.about(self, 'Checkup', 'Car_No: ' + str(Car_Delete) + ' can not be deleted')
            return 1
                            
    def DeleteBCus(self):
        cur = con.cursor(buffered=True)
        Cus_Delete = self.ui.ledeleteCus.text()
        #check---------------------------------------------------------------------
        if Cus_Delete == '':
            QMessageBox.about(self, 'Delete Error', 'Please, add Email')
            return 1
        elif len(Cus_Delete.split('@')) != 2:
            QMessageBox.about(self, 'Delete Error', 'Invalid Email')
            return 1
        elif Cus_Delete.split('@')[1].split('.')[0] != 'gmail':
            QMessageBox.about(self, 'Delete Error', 'Invalid Email (' +
                              Cus_Delete.split('@')[1].split('.')[0] + ')')
            return 1
        elif Cus_Delete.split('@')[1].split('.')[1] != 'com':
            QMessageBox.about(self, 'Delete Error', 'Invalid Email (' +
                              Cus_Delete.split('@')[1].split('.')[1] + ')')
            return 1
        #---------------------------------------------------------------------------
        query = 'delete from customer where Email  = %s'
        try:
            cur.execute(query, (Cus_Delete,))
            QMessageBox.about(self, 'Checkup', 'Email: ' + str(Cus_Delete) + ' was deleted successfully')
        except:
            QMessageBox.about(self, 'Checkup', 'Email: ' + str(Cus_Delete) + ' can not be deleted')
            return 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())

