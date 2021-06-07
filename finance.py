# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finance.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sqlite3 import *
from PyQt5.QtCore import QDate, QTime, QDateTime
import bill
from bill import *


class Ui_FinanceWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1901, 1001))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.Overview = QtWidgets.QWidget()
        self.Overview.setObjectName("Overview")
        self.label = QtWidgets.QLabel(self.Overview)
        self.label.setGeometry(QtCore.QRect(10, 0, 811, 91))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(29)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.Overview)
        self.widget.setGeometry(QtCore.QRect(10, 80, 531, 261))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color:rgb(212, 255, 248)")
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.numService = QtWidgets.QLabel(self.widget)
        self.numService.setGeometry(QtCore.QRect(110, 80, 301, 151))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(78)
        self.numService.setFont(font)
        self.numService.setAlignment(QtCore.Qt.AlignCenter)
        self.numService.setObjectName("numService")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(410, 250, 561, 261))
        self.widget_2.setObjectName("widget_2")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(110, 80, 301, 151))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(78)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.widget_3 = QtWidgets.QWidget(self.Overview)
        self.widget_3.setGeometry(QtCore.QRect(10, 350, 531, 281))
        self.widget_3.setStyleSheet("background-color:rgb(212, 255, 248)")
        self.widget_3.setObjectName("widget_3")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.amountIncome = QtWidgets.QLabel(self.widget_3)
        self.amountIncome.setGeometry(QtCore.QRect(20, 100, 481, 151))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(78)
        self.amountIncome.setFont(font)
        self.amountIncome.setAlignment(QtCore.Qt.AlignCenter)
        self.amountIncome.setObjectName("amountIncome")
        self.widget_4 = QtWidgets.QWidget(self.Overview)
        self.widget_4.setGeometry(QtCore.QRect(20, 640, 521, 281))
        self.widget_4.setStyleSheet("background-color:rgb(212, 255, 248)")
        self.widget_4.setObjectName("widget_4")
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setGeometry(QtCore.QRect(0, 10, 521, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.numPatient = QtWidgets.QLabel(self.widget_4)
        self.numPatient.setGeometry(QtCore.QRect(110, 60, 301, 151))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(78)
        self.numPatient.setFont(font)
        self.numPatient.setAlignment(QtCore.Qt.AlignCenter)
        self.numPatient.setObjectName("numPatient")
        self.widget_5 = QtWidgets.QWidget(self.Overview)
        self.widget_5.setGeometry(QtCore.QRect(550, 640, 311, 281))
        self.widget_5.setAutoFillBackground(True)
        self.widget_5.setObjectName("widget_5")
        self.label_6 = QtWidgets.QLabel(self.widget_5)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 301, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.widget_5)
        self.dateEdit_3.setGeometry(QtCore.QRect(160, 110, 110, 22))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.dateEdit_3.setDate(QDate.currentDate())
        self.label_12 = QtWidgets.QLabel(self.widget_5)
        self.label_12.setGeometry(QtCore.QRect(190, 150, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.widget_5)
        self.dateEdit_4.setGeometry(QtCore.QRect(160, 180, 110, 22))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.dateEdit_4.setDate(QDate.addDays(QDate.currentDate(),-1))
        self.lastMonthCheck = QtWidgets.QCheckBox(self.widget_5)
        self.lastMonthCheck.setGeometry(QtCore.QRect(40, 150, 91, 17))
        self.lastMonthCheck.setObjectName("lastMonthCheck")
        self.lastMonthCheck.stateChanged.connect(self.lastMonth)
        self.lastYearCheck = QtWidgets.QCheckBox(self.widget_5)
        self.lastYearCheck.setGeometry(QtCore.QRect(40, 180, 74, 17))
        self.lastYearCheck.setObjectName("lastYearCheck")
        self.lastYearCheck.stateChanged.connect(self.lastYear)
        self.customCheck = QtWidgets.QCheckBox(self.widget_5)
        self.customCheck.setGeometry(QtCore.QRect(170, 80, 74, 17))
        self.customCheck.setObjectName("customCheck")
        self.customCheck.stateChanged.connect(self.customTime)
        self.todayCheck = QtWidgets.QCheckBox(self.widget_5)
        self.todayCheck.setGeometry(QtCore.QRect(40, 90, 74, 17))
        self.todayCheck.setObjectName("todayCheck")
        self.todayCheck.stateChanged.connect(self.today)
        self.lastWeekCheck = QtWidgets.QCheckBox(self.widget_5)
        self.lastWeekCheck.setGeometry(QtCore.QRect(40, 120, 74, 17))
        self.lastWeekCheck.setObjectName("lastWeekCheck")
        self.lastWeekCheck.setChecked(True)
        self.lastWeekCheck.stateChanged.connect(self.lastWeek)
        self.label_13 = QtWidgets.QLabel(self.Overview)
        self.label_13.setGeometry(QtCore.QRect(550, 80, 1331, 261))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:rgb(216, 255, 201)")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.widget_6 = QtWidgets.QWidget(self.Overview)
        self.widget_6.setGeometry(QtCore.QRect(550, 350, 721, 281))
        self.widget_6.setStyleSheet("background-color: rgb(212, 255, 248);")
        self.widget_6.setObjectName("widget_6")
        self.label_14 = QtWidgets.QLabel(self.widget_6)
        self.label_14.setGeometry(QtCore.QRect(90, 10, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.amountIncome_2 = QtWidgets.QLabel(self.widget_6)
        self.amountIncome_2.setGeometry(QtCore.QRect(0, 70, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(78)
        self.amountIncome_2.setFont(font)
        self.amountIncome_2.setAlignment(QtCore.Qt.AlignCenter)
        self.amountIncome_2.setObjectName("amountIncome_2")
        self.widget_7 = QtWidgets.QWidget(self.Overview)
        self.widget_7.setGeometry(QtCore.QRect(1280, 350, 601, 281))
        self.widget_7.setStyleSheet("background-color:rgb(212, 255, 248)")
        self.widget_7.setObjectName("widget_7")
        self.label_15 = QtWidgets.QLabel(self.widget_7)
        self.label_15.setGeometry(QtCore.QRect(60, 10, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.totService = QtWidgets.QLabel(self.widget_7)
        self.totService.setGeometry(QtCore.QRect(80, 90, 431, 151))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(78)
        self.totService.setFont(font)
        self.totService.setAlignment(QtCore.Qt.AlignCenter)
        self.totService.setObjectName("totService")
        self.widget_8 = QtWidgets.QWidget(self.Overview)
        self.widget_8.setGeometry(QtCore.QRect(870, 640, 581, 281))
        self.widget_8.setStyleSheet("background-color:rgb(212, 255, 248)")
        self.widget_8.setObjectName("widget_8")
        self.label_17 = QtWidgets.QLabel(self.widget_8)
        self.label_17.setGeometry(QtCore.QRect(20, 20, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.totPatient = QtWidgets.QLabel(self.widget_8)
        self.totPatient.setGeometry(QtCore.QRect(90, 80, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(78)
        self.totPatient.setFont(font)
        self.totPatient.setAlignment(QtCore.Qt.AlignCenter)
        self.totPatient.setObjectName("totPatient")
        self.logo = QtWidgets.QLabel(self.Overview)
        self.logo.setGeometry(QtCore.QRect(1490, 650, 331, 261))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.tabWidget.addTab(self.Overview, "")
        self.Transactions = QtWidgets.QWidget()
        self.Transactions.setObjectName("Transactions")
        self.tableWidget = QtWidgets.QTableWidget(self.Transactions)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 1881, 901))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.doubleClicked.connect(self.openBill)
        self.lineEdit = QtWidgets.QLineEdit(self.Transactions)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.Transactions)
        self.label_2.setGeometry(QtCore.QRect(20, 12, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Transactions)
        self.label_3.setGeometry(QtCore.QRect(530, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Transactions)
        self.label_4.setGeometry(QtCore.QRect(780, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.Transactions, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionRefresh.triggered.connect(self.search)
        self.menuFile.addAction(self.actionRefresh)
        self.menubar.addAction(self.menuFile.menuAction())
        self.commitButton = QtWidgets.QPushButton(self.widget_5)
        self.commitButton.setGeometry(QtCore.QRect(50,220,211,41))
        self.commitButton.clicked.connect(self.refreshCalled)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.lineEdit.textChanged.connect(self.search)
        self.changing=False
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select sum(amount) from billingDatabase")
        totAmount=c.fetchone()[0]
        c.execute("select count(*) from patientDatabase")
        totPatient=c.fetchone()[0]
        c.execute("select id, serviceDate, billingId from serviceDatabase")
        rows=c.fetchall()
        totService=len(rows)
        dateFormat="M d hh:mm:ss yyyy"
        targetList=[]
        for row in rows:
            dateOfService=QDateTime.fromString(row[1].split(" ",1)[1],dateFormat)
            if dateOfService.daysTo(QDateTime.currentDateTime())<=7:
                targetList.append(row[0])
        patientList=[]
        earnedSum=0
        for service in targetList:
            c.execute("select patientId from serviceDatabase where id=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                patientList.append(row[0])
            c.execute("select amount from billingDatabase where serviceId=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                earnedSum+=row[0]
        patientNum=len(set(patientList))
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Financial Overview"))
        self.label_5.setText(_translate("MainWindow", "Number of services provided last week:"))
        self.numService.setText(_translate("MainWindow", str(len(targetList))))
        self.label_8.setText(_translate("MainWindow", "50"))
        self.label_9.setText(_translate("MainWindow", "Amount of income earned last week:"))
        self.amountIncome.setText(_translate("MainWindow", "Rs. "+str(earnedSum)))
        self.label_11.setText(_translate("MainWindow", "Number of patients consulted last week:"))
        self.numPatient.setText(_translate("MainWindow", str(patientNum)))
        self.label_6.setText(_translate("MainWindow", "Set your time interval of interest"))
        self.label_12.setText(_translate("MainWindow", "To"))
        self.lastMonthCheck.setText(_translate("MainWindow", "Last Month (30 days)"))
        self.lastYearCheck.setText(_translate("MainWindow", "Last Year (365 days)"))
        self.customCheck.setText(_translate("MainWindow", "From"))
        self.todayCheck.setText(_translate("MainWindow", "Today"))
        self.lastWeekCheck.setText(_translate("MainWindow", "Last Week (7 days)"))
        self.label_13.setText(_translate("MainWindow", "  Welcome,\n"
"  Doctor."))
        self.label_14.setText(_translate("MainWindow", "Total Amount of income earned:"))
        self.amountIncome_2.setText(_translate("MainWindow", str(totAmount)))
        self.label_15.setText(_translate("MainWindow", "Total number of services provided:"))
        self.totService.setText(_translate("MainWindow", str(totService)))
        self.label_17.setText(_translate("MainWindow", "Total number of patients registered in database:"))
        self.totPatient.setText(_translate("MainWindow", str(totPatient)))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Overview), _translate("MainWindow", "Overview"))
        self.label_2.setText(_translate("MainWindow", "Search Patient:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Transactions), _translate("MainWindow", "Bill List"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.commitButton.setText(_translate("MainWindow", "Refresh"))
        c.execute("select billingDatabase.id, patientDatabase.name, billingDatabase.serviceId, serviceDatabase.serviceDate, billingDatabase.amount, billingDatabase.comment from ((billingDatabase inner join patientDatabase on patientDatabase.id=billingDatabase.patientId) inner join serviceDatabase on billingDatabase.serviceId=serviceDatabase.id)")
        rows=c.fetchall()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,400)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setColumnWidth(3,300)
        self.tableWidget.setColumnWidth(4,365)
        self.tableWidget.setColumnWidth(5,500)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Patient Name", "Service ID", "Date of Service","Amount", "Comment"])
        for i in range(len(rows)):
            id=QtWidgets.QTableWidgetItem(str(rows[i][0]))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            patientName=QtWidgets.QTableWidgetItem(str(rows[i][1]))
            patientName.setTextAlignment(QtCore.Qt.AlignCenter)
            serviceId=QtWidgets.QTableWidgetItem(str(rows[i][2]))
            serviceId.setTextAlignment(QtCore.Qt.AlignCenter)
            dos=QtWidgets.QTableWidgetItem(str(rows[i][3]))
            dos.setTextAlignment(QtCore.Qt.AlignCenter)
            amount=QtWidgets.QTableWidgetItem(str(rows[i][4]))
            amount.setTextAlignment(QtCore.Qt.AlignCenter)
            comment=QtWidgets.QTableWidgetItem(str(rows[i][5]))
            comment.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i,0,id)
            self.tableWidget.setItem(i,1,patientName)
            self.tableWidget.setItem(i,2,serviceId)
            self.tableWidget.setItem(i,3,dos)
            self.tableWidget.setItem(i,4,amount)
            self.tableWidget.setItem(i,5,comment)
        conn.close()

    def lastMonth(self):
        if not self.changing:
            self.uncheckAll()
            self.lastMonthCheck.setChecked(True)

    def lastYear(self):
        if not self.changing:
            self.uncheckAll()
            self.lastYearCheck.setChecked(True)

    def lastWeek(self):
        if not self.changing:
            self.uncheckAll()
            self.lastWeekCheck.setChecked(True)

    def today(self):
        if not self.changing:
            self.uncheckAll()
            self.todayCheck.setChecked(True)

    def customTime(self):
        if not self.changing:
            self.uncheckAll()
            self.customCheck.setChecked(True)

    def refreshCalled(self):
        if self.lastMonthCheck.isChecked():
            self.lastMonthRefresh()
        elif self.lastWeekCheck.isChecked():
            self.lastWeekRefresh()
        elif self.lastYearCheck.isChecked():
            self.lastYearRefresh()
        elif self.todayCheck.isChecked():
            self.todayRefresh()
        elif self.customCheck.isChecked():
            self.customRefresh()

    def lastMonthRefresh(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select id, serviceDate,billingId from serviceDatabase")
        rows=c.fetchall()
        dateFormat="M d hh:mm:ss yyyy"
        targetList=[]
        for row in rows:
            dateOfService=QDateTime.fromString(row[1].split(" ",1)[1],dateFormat)
            if dateOfService.daysTo(QDateTime.currentDateTime())<=30:
                targetList.append(row[0])
        patientList=[]
        earnedSum=0
        for service in targetList:
            c.execute("select patientId from serviceDatabase where id=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                patientList.append(row[0])
            c.execute("select amount from billingDatabase where serviceId=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                earnedSum+=row[0]
        patientNum=len(set(patientList))
        self.numService.setText(str(len(targetList)))
        self.numPatient.setText(str(patientNum))
        self.amountIncome.setText("Rs. "+str(earnedSum))
        self.label_5.setText("Number of services provided last month:")
        self.label_9.setText("Amount of income earned last month:")
        self.label_11.setText("Number of patients consulted last month:")
        conn.close()


    def lastYearRefresh(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select id, serviceDate,billingId from serviceDatabase")
        rows=c.fetchall()
        targetList=[]
        dateFormat="M d hh:mm:ss yyyy"
        for row in rows:
            dateOfService=QDateTime.fromString(row[1].split(" ",1)[1],dateFormat)
            if dateOfService.daysTo(QDateTime.currentDateTime())<=365:
                targetList.append(row[0])
        patientList=[]
        earnedSum=0
        for service in targetList:
            c.execute("select patientId from serviceDatabase where id=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                patientList.append(row[0])
            c.execute("select amount from billingDatabase where serviceId=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                earnedSum+=row[0]
        patientNum=len(set(patientList))
        self.numService.setText(str(len(targetList)))
        self.numPatient.setText(str(patientNum))
        self.amountIncome.setText("Rs. "+str(earnedSum))
        self.label_5.setText("Number of services provided last year:")
        self.label_9.setText("Amount of income earned last year:")
        self.label_11.setText("Number of patients consulted last year:")
        conn.close()

    def lastWeekRefresh(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select id, serviceDate,billingId from serviceDatabase")
        rows=c.fetchall()
        targetList=[]
        dateFormat="M d hh:mm:ss yyyy"
        for row in rows:
            dateOfService=QDateTime.fromString(row[1].split(" ",1)[1],dateFormat)
            if dateOfService.daysTo(QDateTime.currentDateTime())<=7:
                targetList.append(row[0])
        patientList=[]
        earnedSum=0
        for service in targetList:
            c.execute("select patientId from serviceDatabase where id=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                patientList.append(row[0])
            c.execute("select amount from billingDatabase where serviceId=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                earnedSum+=row[0]
        patientNum=len(set(patientList))
        self.numService.setText(str(len(targetList)))
        self.numPatient.setText(str(patientNum))
        self.amountIncome.setText("Rs. "+str(earnedSum))
        self.label_5.setText("Number of services provided last week:")
        self.label_9.setText("Amount of income earned last week:")
        self.label_11.setText("Number of patients consulted last week:")
        conn.close()

    def todayRefresh(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select id, serviceDate,billingId from serviceDatabase")
        rows=c.fetchall()
        targetList=[]
        dateFormat="M d hh:mm:ss yyyy"
        for row in rows:
            dateOfService=QDateTime.fromString(row[1].split(" ",1)[1],dateFormat)
            if dateOfService.secsTo(QDateTime.currentDateTime())<86400:
                targetList.append(row[0])
        patientList=[]
        earnedSum=0
        for service in targetList:
            c.execute("select patientId from serviceDatabase where id=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                patientList.append(row[0])
            c.execute("select amount from billingDatabase where serviceId=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                earnedSum+=row[0]
        patientNum=len(set(patientList))
        self.numService.setText(str(len(targetList)))
        self.numPatient.setText(str(patientNum))
        self.amountIncome.setText("Rs. "+str(earnedSum))
        self.label_5.setText("Number of services provided today:")
        self.label_9.setText("Amount of income earned today:")
        self.label_11.setText("Number of patients consulted today:")
        conn.close()

    def customRefresh(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select id, serviceDate,billingId from serviceDatabase")
        rows=c.fetchall()
        targetList=[]
        fromDate=QDateTime(self.dateEdit_3.date(),QTime(0,0,0))
        toDate=QDateTime(self.dateEdit_4.date(),QTime(0,0,0))
        dateFormat="M d hh:mm:ss yyyy"
        for row in rows:
            dateOfService=QDateTime.fromString(row[1].split(" ",1)[1],dateFormat)
            if dateOfService.daysTo(toDate)>=0 and dateOfService.daysTo(fromDate)<=0:
                targetList.append(row[0])
        patientList=[]
        earnedSum=0
        for service in targetList:
            c.execute("select patientId from serviceDatabase where id=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                patientList.append(row[0])
            c.execute("select amount from billingDatabase where serviceId=?",(str(service),))
            row=c.fetchone()
            if row!=None:
                earnedSum+=row[0]
        patientNum=len(set(patientList))
        self.numService.setText(str(len(targetList)))
        self.numPatient.setText(str(patientNum))
        self.amountIncome.setText("Rs. "+str(earnedSum))
        self.label_5.setText("Number of services provided:")
        self.label_9.setText("Amount of income earned:")
        self.label_11.setText("Number of patients consulted:")
        conn.close()

    def search(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select billingDatabase.id, patientDatabase.name, billingDatabase.serviceId, serviceDatabase.serviceDate, billingDatabase.amount, billingDatabase.comment from ((billingDatabase inner join patientDatabase on patientDatabase.id=billingDatabase.patientId) inner join serviceDatabase on billingDatabase.serviceId=serviceDatabase.id) where patientDatabase.name like ?",("%"+self.lineEdit.text()+"%",))
        rows=c.fetchall()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,400)
        self.tableWidget.setColumnWidth(2,200)
        self.tableWidget.setColumnWidth(3,300)
        self.tableWidget.setColumnWidth(4,365)
        self.tableWidget.setColumnWidth(5,500)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Patient Name", "Service ID", "Date of Service","Amount","Comment"])
        for i in range(len(rows)):
            id=QtWidgets.QTableWidgetItem(str(rows[i][0]))
            id.setTextAlignment(QtCore.Qt.AlignCenter)
            patientName=QtWidgets.QTableWidgetItem(str(rows[i][1]))
            patientName.setTextAlignment(QtCore.Qt.AlignCenter)
            serviceId=QtWidgets.QTableWidgetItem(str(rows[i][2]))
            serviceId.setTextAlignment(QtCore.Qt.AlignCenter)
            dos=QtWidgets.QTableWidgetItem(str(rows[i][3]))
            dos.setTextAlignment(QtCore.Qt.AlignCenter)
            amount=QtWidgets.QTableWidgetItem(str(rows[i][4]))
            amount.setTextAlignment(QtCore.Qt.AlignCenter)
            comment=QtWidgets.QTableWidgetItem(str(rows[i][5]))
            comment.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i,0,id)
            self.tableWidget.setItem(i,1,patientName)
            self.tableWidget.setItem(i,2,serviceId)
            self.tableWidget.setItem(i,3,dos)
            self.tableWidget.setItem(i,4,amount)
            self.tableWidget.setItem(i,5,comment)
        conn.close()

    def openBill(self):
        id=self.tableWidget.item(self.tableWidget.currentRow(),0).text()
        self.billWindow=QtWidgets.QMainWindow()
        self.billWindowUi = Ui_Bill(id)
        self.billWindowUi.setupUi(self.billWindow)
        self.billWindowUi.setMother(self,"finance")
        self.billWindow.show()

    def uncheckAll(self):
        self.changing=True
        self.todayCheck.setChecked(False)
        self.lastMonthCheck.setChecked(False)
        self.lastWeekCheck.setChecked(False)
        self.lastYearCheck.setChecked(False)
        self.customCheck.setChecked(False)
        self.changing=False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FinanceWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
