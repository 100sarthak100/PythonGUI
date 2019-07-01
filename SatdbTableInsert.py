# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\MAHE\Desktop\MPTgui 3.0\SatdbTableInsert1.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_DialogIns(object):
    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setWindowIcon(QtGui.QIcon('C:\\Users\\MAHE\\Desktop\\MPTgui\\Icon\\icon1.jpg'))
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def InsertData(self):
        sat = (self.tableWidget.item(row, 0).text() for row in range(self.tableWidget.rowCount()))
        targetazimuth = (self.tableWidget.item(row, 1).text() for row in range(self.tableWidget.rowCount()))
        targetelevation = (self.tableWidget.item(row, 2).text() for row in range(self.tableWidget.rowCount()))

        conn = sqlite3.connect("login.db")
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO SAT(Sattelite,TargetAzimuth,TargetElevation)"
                        "VALUES ('%s' , '%s' , '%s' )" % (''.join(sat),
                                                          ''.join(targetazimuth),
                                                          ''.join(targetelevation)))
            print("data inserted successfully")
        self.showMessageBox('Database', 'Data Inserted Successfully')
        conn.close()


    def setupUi(self, DialogIns):
        DialogIns.setObjectName("DialogIns")
        DialogIns.resize(452, 338)
        self.widget = QtWidgets.QWidget(DialogIns)
        self.widget.setGeometry(QtCore.QRect(10, 10, 431, 321))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(430, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.btn_insert = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_insert.setFont(font)
        self.btn_insert.setObjectName("btn_insert")
        self.verticalLayout.addWidget(self.btn_insert)

        self.retranslateUi(DialogIns)
        QtCore.QMetaObject.connectSlotsByName(DialogIns)

        self.btn_insert.clicked.connect(self.InsertData)

    def retranslateUi(self, DialogIns):
        _translate = QtCore.QCoreApplication.translate
        DialogIns.setWindowTitle(_translate("DialogIns", "Database"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("DialogIns", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DialogIns", "SATELLITE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DialogIns", "TARGET AZIMUTH"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DialogIns", "TARGET ELEVATION"))
        self.btn_insert.setText(_translate("DialogIns", "INSERT DATA"))

        DialogIns.setWindowFlags(DialogIns.windowFlags() |
                                  QtCore.Qt.WindowSystemMenuHint |
                                  QtCore.Qt.WindowMinMaxButtonsHint)
        DialogIns.setWindowIcon(QtGui.QIcon('C:\\Users\\MAHE\\Desktop\\MPTgui\\Icon\\icon1.jpg'))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogIns = QtWidgets.QDialog()
    ui = Ui_DialogIns()
    ui.setupUi(DialogIns)
    DialogIns.show()
    sys.exit(app.exec_())
