# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\MAHE\Desktop\MPTgui 3.0\SatdbTable2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from SatdbTableInsert import Ui_DialogIns


class Ui_DialogSat(object):
    def insertOpen(self):
        self.insertwindow = QtWidgets.QDialog()
        self.ui =Ui_DialogIns()
        self.ui.setupUi(self.insertwindow)
        self.insertwindow.show()
        #DialogSat.close()

    def loadData(self):
        conn = sqlite3.connect("login.db")
        query = "SELECT * FROM SAT"
        result = conn.execute(query)
        self.tableWidget.setRowCount(0)

        for  row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for col_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,col_number,QtWidgets.QTableWidgetItem(str(data)))

        conn.close()

    def setupUi(self, DialogSat):
        DialogSat.setObjectName("DialogSat")
        DialogSat.resize(444, 326)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        DialogSat.setFont(font)
        self.widget = QtWidgets.QWidget(DialogSat)
        self.widget.setGeometry(QtCore.QRect(0, 0, 441, 321))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_load = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_load.setFont(font)
        self.btn_load.setObjectName("btn_load")
        self.horizontalLayout.addWidget(self.btn_load)
        self.btn_insert = QtWidgets.QPushButton(self.widget)
        self.btn_insert.setObjectName("btn_insert")
        self.horizontalLayout.addWidget(self.btn_insert)
        self.btn_quit = QtWidgets.QPushButton(self.widget)
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout.addWidget(self.btn_quit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogSat)
        QtCore.QMetaObject.connectSlotsByName(DialogSat)

        self.btn_load.clicked.connect(self.loadData)
        self.btn_insert.clicked.connect(self.insertOpen)

    def retranslateUi(self, DialogSat):
        _translate = QtCore.QCoreApplication.translate
        DialogSat.setWindowTitle(_translate("DialogSat", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DialogSat", "SATELLITE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DialogSat", "AZIMUTH"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DialogSat", "ELEVATION"))
        self.btn_load.setText(_translate("DialogSat", "LOAD"))
        self.btn_insert.setText(_translate("DialogSat", "INSERT"))
        self.btn_quit.setText(_translate("DialogSat", "DELETE"))

        DialogSat.setWindowFlags(DialogSat.windowFlags() |
                                 QtCore.Qt.WindowSystemMenuHint |
                                 QtCore.Qt.WindowMinMaxButtonsHint)
        DialogSat.setWindowIcon(QtGui.QIcon('C:\\Users\\MAHE\\Desktop\\MPTgui\\Icon\\icon1.jpg'))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogSat = QtWidgets.QDialog()
    ui = Ui_DialogSat()
    ui.setupUi(DialogSat)
    DialogSat.show()
    sys.exit(app.exec_())
