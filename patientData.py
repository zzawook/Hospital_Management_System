# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patientData.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
import addPatient
from addPatient import *
import pickle
import changePatient
from changePatient import *
import sqlite3

class Ui_PatientWindow(object):
    def setupUi(self, MainWindow):
        self.Window=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 1901, 931))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1680, 10, 221, 51))
        self.pushButton_2.clicked.connect(self.returnHome)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        self.menuReturnHome = QtWidgets.QAction(MainWindow)
        self.menuReturnHome.setObjectName("menuReturnHome")
        self.menuReturnHome.triggered.connect(self.returnHome)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuHome.addAction(self.menuReturnHome)
        self.menubar.addAction(self.menuHome.menuAction())
        self.updatePatientInfo()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add New Patient"))
        self.pushButton.clicked.connect(self.openAddPatient)
        self.pushButton_2.setText(_translate("MainWindow", "Return to Home"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.menuReturnHome.setText(_translate("MainWindow", "Return to Home"))

    def openChangePatient(self,row):
        self.changeWindow=QtWidgets.QDialog()
        id=self.tableWidget.item(row,0).text()
        self.changeUi=Ui_ChangePatient(id,self)
        self.changeUi.setupUi(self.changeWindow)
        self.changeWindow.show()

    def returnHome(self):
        self.Window.close()

    def openAddPatient(self, row):
        self.AddWindow=QtWidgets.QMainWindow()
        self.AddUi=Ui_AddNewPatient(self)
        self.AddUi.setupUi(self.AddWindow)
        self.AddWindow.show()

    def updatePatientInfo(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select * from patientDatabase")
        rows=c.fetchall()
        conn.close()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.buttonList=[]
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,327)
        self.tableWidget.setColumnWidth(2,128)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,200)
        self.tableWidget.setColumnWidth(5,600)
        self.tableWidget.setColumnWidth(6,250)
        self.tableWidget.setColumnWidth(7,180)
        self.tableWidget.setHorizontalHeaderLabels(["ID","Name","Date of Birth","Gender","Phone Number","Address","Email Address", "Change Profile"])
        for i in range(len(rows)):
            id=QtWidgets.QTableWidgetItem(str(rows[i][0]))
            id.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(i,0,id)
            name=QtWidgets.QTableWidgetItem(rows[i][1])
            name.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(i,1,name)
            age=str(QDate.currentDate().getDate()[0]-int(rows[i][2].split("-")[0]))
            dobString=(rows[i][2].split("-")[0],rows[i][2].split("-")[1],rows[i][2].split("-")[2])
            dob=QtWidgets.QTableWidgetItem(str(dobString[0])+" / "+str(dobString[1])+" / "+str(dobString[2])+"  ("+age+")")
            dob.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(i,2,dob)
            gender=rows[i][3]
            genderItem=QtWidgets.QTableWidgetItem(gender)
            genderItem.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(i,3,genderItem)
            pNumber=QtWidgets.QTableWidgetItem(str(rows[i][4]))
            pNumber.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(i,4,pNumber)
            addressItem=QtWidgets.QTableWidgetItem(rows[i][5])
            addressItem.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(i,5,addressItem)
            email=QtWidgets.QTableWidgetItem(str(rows[i][6]))
            email.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget.setItem(i,6,email)
            self.button=QtWidgets.QPushButton("View/Change Profile")
            self.button.setObjectName("button"+str(i))
            index = QtCore.QPersistentModelIndex(self.tableWidget.model().index(i, 7))
            self.button.clicked.connect(lambda *args, index=index: self.openChangePatient(index.row()))
            self.buttonList.append(self.button)
            self.tableWidget.setCellWidget(i,7,(self.buttonList[-1]))

                    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PatientWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
