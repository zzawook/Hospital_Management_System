# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serviceRecord.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sqlite3 import *
import diagnosis
from diagnosis import *
import html2text
from PyQt5.QtCore import QDate, QTime, QDateTime

class Ui_ServiceRecord(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1015)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 1901, 881))
        self.listWidget.setObjectName("tableWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1420, 10, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1600, 3, 301, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.search)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1490, 40, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1600, 43, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1760, 40, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuRefresh = QtWidgets.QAction(MainWindow)
        self.menuRefresh.setObjectName("actionRefresh")
        self.menuRefresh.triggered.connect(self.search)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuFile.addAction(self.menuRefresh)
        self.menubar.addAction(self.menuFile.menuAction())
        self.buttonList=[]
        self.updateRecord(True,"")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Service Records"))
        self.label.setText(_translate("MainWindow", "Filter by Patient Name: "))
        self.label_5.setText(_translate("MainWindow", "Service Records"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuRefresh.setText(_translate("MainWindow","Refresh"))

    def updateRecord(self,initialize,name):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select * from serviceDatabase")
        rows=c.fetchall()
        self.buttonList=[]
        self.listWidget.setColumnCount(7)
        self.listWidget.setRowCount(len(rows))
        self.listWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.listWidget.setColumnWidth(0,30)
        self.listWidget.setColumnWidth(1,250)
        self.listWidget.setColumnWidth(2,120)
        self.listWidget.setColumnWidth(3,390)
        self.listWidget.setColumnWidth(4,490)
        self.listWidget.setColumnWidth(5,490)
        self.listWidget.setColumnWidth(6,105)
        self.listWidget.setHorizontalHeaderLabels(["ID","Patient Name","Date/Time","Symtom","Diagnosis","Prescription","Detail"])
        for i in range(len(rows)):
            self.listWidget.setRowHeight(i,50)
            recordId=QtWidgets.QTableWidgetItem(str(rows[i][0]))
            font=QtGui.QFont()
            font.setPointSize(9)
            recordId.setFont(font)
            recordId.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,0,recordId)
            sql='''select name from patientDatabase where id=?'''
            c.execute(sql,(rows[i][1],))
            patientName=QtWidgets.QTableWidgetItem(c.fetchone()[0])
            patientName.setFont(font)
            patientName.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,1,patientName)
            dateObject=rows[i][2].split(" ")
            (dayName,month,numDay,time,year)=(str(dateObject[0]),int(dateObject[1]),int(dateObject[2]),str(dateObject[3]),int(dateObject[4]))
            date=QtWidgets.QTableWidgetItem(getMonthName(month)+" "+str(numDay)+", "+str(year)+"("+dayName+")"+"\n"+str(time))
            date.setFont(font)
            date.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,2,date)
            symptomText=html2text.html2text(str(rows[i][3])).replace("*","-")
            symptom=QtWidgets.QTableWidgetItem(symptomText)
            symptom.setFont(font)
            symptom.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,3,symptom)
            diagnoseText=html2text.html2text(str(rows[i][4])).replace("*","-")
            diagnose=QtWidgets.QTableWidgetItem(diagnoseText)
            diagnose.setFont(font)
            diagnose.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,4,diagnose)
            prescriptionText=html2text.html2text(str(rows[i][5])).replace("*","-")
            prescription=QtWidgets.QTableWidgetItem(prescriptionText)
            prescription.setFont(font)
            prescription.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,5,prescription)
            self.button=QtWidgets.QPushButton("View Details")
            self.button.setObjectName("button"+str(i))
            index = QtCore.QPersistentModelIndex(self.listWidget.model().index(i, 6))
            self.button.clicked.connect(lambda *args, index=index: self.openServiceRecord(index.row()))
            self.buttonList.append(self.button)
            self.listWidget.setCellWidget(i,6,(self.buttonList[-1]))
        conn.close()

    def search(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select * from serviceDatabase where patientId in (select id from patientDatabase where name like ?)",("%"+self.lineEdit.text()+"%",))
        records=c.fetchall()
        targetList=[]
        self.buttonList=[]
        self.listWidget.setColumnCount(7)
        self.listWidget.setRowCount(len(records))
        self.listWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.listWidget.setColumnWidth(0,30)
        self.listWidget.setColumnWidth(1,250)
        self.listWidget.setColumnWidth(2,120)
        self.listWidget.setColumnWidth(3,390)
        self.listWidget.setColumnWidth(4,490)
        self.listWidget.setColumnWidth(5,480)
        self.listWidget.setColumnWidth(6,105)
        self.listWidget.setHorizontalHeaderLabels(["ID","Patient Name","Date/Time","Symtom","Diagnosis","Prescription","Detail"])
        for i in range(len(records)):
            self.listWidget.setRowHeight(i,50)
            recordId=QtWidgets.QTableWidgetItem(str(records[i][0]))
            font=QtGui.QFont()
            font.setPointSize(9)
            recordId.setFont(font)
            recordId.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,0,recordId)
            sql='''select name from patientDatabase where id=?'''
            c.execute(sql,(records[i][1],))
            patientName=QtWidgets.QTableWidgetItem(c.fetchone()[0])
            patientName.setFont(font)
            patientName.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,1,patientName)
            dateObject=records[i][2].split(" ")
            (dayName,month,numDay,time,year)=(str(dateObject[0]),int(dateObject[1]),int(dateObject[2]),str(dateObject[3]),int(dateObject[4]))
            date=QtWidgets.QTableWidgetItem(getMonthName(month)+" "+str(numDay)+", "+str(year)+"("+dayName+")"+"\n"+str(time))
            date.setFont(font)
            date.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,2,date)
            symptomText=html2text.html2text(str(records[i][3])).replace("*","-")
            symptom=QtWidgets.QTableWidgetItem(symptomText)
            symptom.setFont(font)
            symptom.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,3,symptom)
            diagnoseText=html2text.html2text(str(records[i][4])).replace("*","-")
            diagnose=QtWidgets.QTableWidgetItem(diagnoseText)
            diagnose.setFont(font)
            diagnose.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,4,diagnose)
            prescriptionText=html2text.html2text(str(records[i][5])).replace("*","-")
            prescription=QtWidgets.QTableWidgetItem(prescriptionText)
            prescription.setFont(font)
            prescription.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,5,prescription)
            self.button=QtWidgets.QPushButton("View Details")
            self.button.setObjectName("button"+str(i))
            index = QtCore.QPersistentModelIndex(self.listWidget.model().index(i, 6))
            self.button.clicked.connect(lambda *args, index=index: self.openServiceRecord(index.row()))
            self.buttonList.append(self.button)
            self.listWidget.setCellWidget(i,6,(self.buttonList[-1]))
        conn.close()

    def openServiceRecord(self,row):
        self.thisServiceRecord=QtWidgets.QMainWindow()
        id=self.listWidget.item(row,0).text()
        self.SRUi=diagnosis.Ui_diagnosisWindow()
        self.SRUi.setupUi(self.thisServiceRecord)
        self.SRUi.setNotNew()
        self.SRUi.loadRecord(id)
        self.SRUi.getBills()
        self.thisServiceRecord.show()
        
def getMonthName(givenMonth):
    month=int(givenMonth)
    if month==1:
        return "Jan"
    elif month==2:
        return "Feb"
    elif month==3:
        return "Mar"
    elif month==4:
        return "Apr"
    elif month==5:
        return "May"
    elif month==6:
        return "Jun"
    elif month==7:
        return "Jul"
    elif month==8:
        return "Aug"
    elif month==9:
        return "Sep"
    elif month==10:
        return "Oct"
    elif month==11:
        return "Nov"
    else: return "Dec"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ServiceRecord()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
