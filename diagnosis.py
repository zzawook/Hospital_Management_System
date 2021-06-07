# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnosis.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import patientSearch
from patientSearch import *
import sqlite3
from sqlite3 import *   
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QDateTime
from addPatientEntryWarning import *
import addPatientEntryWarning
import html2text
import serviceRecord
from serviceRecord import *
import bill
from bill import *

class Patient(object):
    def __init__(self,id):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select * from patientDatabase where id=? limit 1",(id,))
        patientData=c.fetchall()
        if len(patientData)>1:
            self.openWarning()
        else:
            self.id=id
            self.name=patientData[0][1]
            self.dob=patientData[0][2]
            self.gender=patientData[0][3]
            self.phone=patientData[0][4]
            self.address=patientData[0][5]
            self.email=patientData[0][6]
        conn.close()

class Record(object):
    def __init__(self,id):
        self.recordId=id
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select * from serviceDatabase where id=? limit 1",(id,))
        recordData=c.fetchall()
        if len(recordData)>1:
            self.openWarning()
        else:
            self.patientId=recordData[0][1]
            self.serviceDate=recordData[0][2]
            self.symptom=recordData[0][3]
            self.diagnosis=recordData[0][4]
            self.prescription=recordData[0][5]
            self.comment=recordData[0][6]
            self.billingId=recordData[0][7]
        conn.close()

class Ui_diagnosisWindow(object):
    def setupUi(self, diagnosisWindow):
        self.Window=diagnosisWindow
        diagnosisWindow.setObjectName("diagnosisWindow")
        diagnosisWindow.resize(1920, 1015)
        self.newRecord=True
        self.patient=None
        self.prevRecord=None
        self.centralwidget = QtWidgets.QWidget(diagnosisWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 421, 881))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 391, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 391, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 391, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 401, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 391, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10,100,381,81))
        self.label_6.setObjectName("label_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 350, 401, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 530, 401, 281))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 820, 201, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.searchPatient)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(430, 80, 20, 881))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(450, 70, 1451, 881))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 40, 1421, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 1401, 101))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.selectionChanged.connect(self.clearInit1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox.activated[str].connect(self.convertHTML1)
        self.comboBox.setGeometry(QtCore.QRect(250, 3, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 190, 1421, 211))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 30, 1401, 171))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.selectionChanged.connect(self.clearInit2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 3, 191, 22))
        self.comboBox_2.activated[str].connect(self.convertHTML2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 410, 1421, 301))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 30, 1401, 261))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.selectionChanged.connect(self.clearInit3)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_3.setGeometry(QtCore.QRect(250, 3, 191, 22))
        self.comboBox_3.activated[str].connect(self.convertHTML3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 720, 1421, 151))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 30, 1401, 111))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.selectionChanged.connect(self.clearInit4)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_4.setGeometry(QtCore.QRect(250, 3, 191, 22))
        self.comboBox_4.activated[str].connect(self.convertHTML4)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        map(lambda box: box.setEditable(False),[self.comboBox, self.comboBox_2, self.comboBox_3, self.comboBox_4])
        map(lambda box: textEdit.textChanged.connect(self.detectActivate), [self.textEdit, self.textEdit_2, self.textEdit_3, self.textEdit_4])
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1672, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        diagnosisWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(diagnosisWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuBill = QtWidgets.QMenu(self.menubar)
        self.menuBill.setObjectName("menuBill")
        diagnosisWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(diagnosisWindow)
        self.statusbar.setObjectName("statusbar")
        diagnosisWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(diagnosisWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.saveRecord)
        self.actionPrint = QtWidgets.QAction(diagnosisWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint.triggered.connect(self.printRecord)
        self.actionLoad = QtWidgets.QAction(diagnosisWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.triggered.connect(self.askToSaveThenOpen)
        self.actionDelete = QtWidgets.QAction(diagnosisWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionDelete.triggered.connect(self.askDelete)
        self.actionAddBill = QtWidgets.QAction(diagnosisWindow)
        self.actionAddBill.setObjectName("actionAddBill")
        self.actionAddBill.triggered.connect(self.addBill)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionDelete)
        self.menuBill.addAction(self.actionAddBill)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuBill.menuAction())
        self.pastRecordTable = QtWidgets.QTableWidget(self.groupBox_3)
        self.pastRecordTable.setGeometry(QtCore.QRect(10, 20, 381, 150))
        self.pastRecordTable.setRowCount(3)
        self.pastRecordTable.setRowHeight(0,39)
        self.pastRecordTable.setRowHeight(1,39)
        self.pastRecordTable.setRowHeight(2,39)
        self.pastRecordTable.setColumnCount(3)
        self.pastRecordTable.setColumnWidth(0,121)
        self.pastRecordTable.setColumnWidth(1,121)
        self.pastRecordTable.setColumnWidth(2,121)
        self.pastRecordTable.setHorizontalHeaderLabels(["Date","Diagnosis","Prescription"])
        self.pastRecordTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.billTable = QtWidgets.QTableWidget(self.groupBox_4)
        self.billTable.setGeometry(QtCore.QRect(5,30,390,241))
        self.billTable.setColumnCount(2)
        self.billTable.setColumnWidth(0,230)
        self.billTable.setColumnWidth(1,150)
        self.billTable.setHorizontalHeaderLabels(["Comment", "Amount"])
        self.billTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.billTable.doubleClicked.connect(self.chooseBill)
        self.retranslateUi(diagnosisWindow)
        QtCore.QMetaObject.connectSlotsByName(diagnosisWindow)

    def retranslateUi(self, diagnosisWindow):
        _translate = QtCore.QCoreApplication.translate
        diagnosisWindow.setWindowTitle(_translate("diagnosisWindow", "Hospital Management System"))
        self.label.setText(_translate("diagnosisWindow", "Examination / Diagnosis"))
        self.groupBox.setTitle(_translate("diagnosisWindow", "Patient Information"))
        self.label_2.setText(_translate("diagnosisWindow", "Name: "))
        self.label_3.setText(_translate("diagnosisWindow", "Age:"))
        self.label_4.setText(_translate("diagnosisWindow", "Phone Number:"))
        self.groupBox_2.setTitle(_translate("diagnosisWindow", "Last 3 Visits"))
        self.label_5.setText(_translate("diagnosisWindow", "Last Visits"))
        self.label_6.setText(_translate("diagnosisWindow", "Gender: "))
        self.groupBox_3.setTitle(_translate("diagnosisWindow", "Past Consultation Records"))
        self.groupBox_4.setTitle(_translate("diagnosisWindow", "Bills (Double-Click to open)"))
        self.pushButton.setText(_translate("diagnosisWindow", "Choose Patient"))
        self.groupBox_5.setTitle(_translate("diagnosisWindow", "Consultation"))
        self.groupBox_6.setTitle(_translate("diagnosisWindow", "Symptoms / Physical Examination"))
        self.comboBox.setItemText(0, _translate("diagnosisWindow", "Free Writing"))
        self.comboBox.setItemText(1, _translate("diagnosisWindow", "Unordered List"))
        self.comboBox.setItemText(2, _translate("diagnosisWindow", "Ordered List"))
        self.groupBox_7.setTitle(_translate("diagnosisWindow", "Diagnosis"))
        self.comboBox_2.setItemText(0, _translate("diagnosisWindow", "Free Writing"))
        self.comboBox_2.setItemText(1, _translate("diagnosisWindow", "Unordered List"))
        self.comboBox_2.setItemText(2, _translate("diagnosisWindow", "Ordered List"))
        self.groupBox_8.setTitle(_translate("diagnosisWindow", "Prescription"))
        self.comboBox_3.setItemText(0, _translate("diagnosisWindow", "Free Writing"))
        self.comboBox_3.setItemText(1, _translate("diagnosisWindow", "Unordered List"))
        self.comboBox_3.setItemText(2, _translate("diagnosisWindow", "Ordered List"))
        self.groupBox_9.setTitle(_translate("diagnosisWindow", "Comments"))
        self.comboBox_4.setItemText(0, _translate("diagnosisWindow", "Free Writing"))
        self.comboBox_4.setItemText(1, _translate("diagnosisWindow", "Unordered List"))
        self.comboBox_4.setItemText(2, _translate("diagnosisWindow", "Ordered List"))
        self.pushButton_2.setText(_translate("diagnosisWindow", "Return to Home"))
        self.pushButton_2.clicked.connect(self.returnHome)
        self.menuFile.setTitle(_translate("diagnosisWindow", "File"))
        self.menuBill.setTitle(_translate("diagnosisWindow", "Bills"))
        self.actionSave.setText(_translate("diagnosisWindow", "Save"))
        self.actionPrint.setText(_translate("diagnosisWindow", "Print"))
        self.actionLoad.setText(_translate("diagnosisWindow", "Open other record"))
        self.actionDelete.setText(_translate("diagnosisWindow", "Delete"))
        self.actionAddBill.setText(_translate("diagnosisWindow", "Add Bill"))

    def clearInit1(self):
        if self.textEdit.toPlainText()=="Start typing here":
            content=self.textEdit.toHtml()
            self.textEdit.setHtml(content.replace("Start typing here"," "))

    def clearInit2(self):
        if self.textEdit_2.toPlainText()=="Start typing here":
            content=self.textEdit_2.toHtml()
            self.textEdit_2.setHtml(content.replace("Start typing here"," "))

    def clearInit3(self):
        if self.textEdit_3.toPlainText()=="Start typing here":
            content=self.textEdit_3.toHtml()
            self.textEdit_3.setHtml(content.replace("Start typing here"," "))

    def clearInit4(self):
        if self.textEdit_4.toPlainText()=="Start typing here":
            content=self.textEdit_4.toHtml()
            self.textEdit_4.setHtml(content.replace("Start typing here"," "))

    def convertHTML1(self):
        content=self.textEdit.toPlainText()
        if self.comboBox.currentText()=="Unordered List":
            newContent="<ul><li>"
            if len(content)==0:
                newContent+="Start typing here</li></ul>"
            else:
                for i in range(len(content)-1):
                    if content[i+1]=="\n":
                        newContent+=content[i]+"</li>"
                    elif content[i-1]=="\n":    
                        newContent+="<li>"+content[i]
                    else:
                        newContent+=content[i]
                newContent+=content[-1]+"</li></ul>"
            self.textEdit.setHtml(newContent)
        elif self.comboBox.currentText()=="Ordered List":
            newContent="<ol><li>"
            if len(content)==0:
                newContent+="Start typing here</li></ol>"
            else:
                for i in range(len(content)-1):
                    if content[i+1]=="\n":
                        newContent+=content[i]+"</li>"
                    elif content[i-1]=="\n":
                        newContent+="<li>"+content[i]
                    else:
                        newContent+=content[i]
                newContent+=content[-1]+"</li></ol>"
            self.textEdit.setHtml(newContent)
        else:
            self.textEdit.clear()
            self.textEdit.insertPlainText(content)

    def convertHTML2(self):
        content=self.textEdit_2.toPlainText()
        if self.comboBox_2.currentText()=="Unordered List":
            newContent="<ul><li>"
            if len(content)==0:
                newContent+="Start typing here</li></ul>"
            else:
                for i in range(len(content)-1):
                    if content[i+1]=="\n":
                        newContent+=content[i]+"</li>"
                    elif content[i-1]=="\n":
                        newContent+="<li>"+content[i]
                    else:
                        newContent+=content[i]
                newContent+=content[-1]+"</li></ul>"
            self.textEdit_2.setHtml(newContent)
        elif self.comboBox_2.currentText()=="Ordered List":
            newContent="<ol><li>"
            if len(content)==0:
                newContent+="Start typing here</li></ol>"
            else:
                for i in range(len(content)-1):
                    if content[i+1]=="\n":
                        newContent+=content[i]+"</li>"
                    elif content[i-1]=="\n":
                        newContent+="<li>"+content[i]
                    else:
                        newContent+=content[i]
                newContent+=content[-1]+"</li></ol>"
            self.textEdit_2.setHtml(newContent)
        else:
            self.textEdit_2.clear()
            self.textEdit_2.insertPlainText(content)

    def convertHTML3(self):
        content=self.textEdit_3.toPlainText()
        if self.comboBox_3.currentText()=="Unordered List":
            newContent="<ul><li>"
            if len(content)==0:
                newContent+="Start typing here</li></ul>"
            else:
                for i in range(len(content)-1):
                    if content[i+1]=="\n":
                        newContent+=content[i]+"</li>"
                    elif content[i-1]=="\n":
                        newContent+="<li>"+content[i]
                    else:
                        newContent+=content[i]
                newContent+=content[-1]+"</li></ul>"
            self.textEdit_3.setHtml(newContent)
        elif self.comboBox_3.currentText()=="Ordered List":
            newContent="<ol><li>"
            if len(content)==0:
                newContent+="Start typing here</li></ol>"
            else:
                for i in range(len(content)-1):
                    if content[i+1]=="\n":
                        newContent+=content[i]+"</li>"
                    elif content[i-1]=="\n":
                        newContent+="<li>"+content[i]
                    else:
                        newContent+=content[i]
                newContent+=content[-1]+"</li></ol>"
            self.textEdit_3.setHtml(newContent)
        else:
            self.textEdit_3.clear()
            self.textEdit_3.insertPlainText(content)

    def convertHTML4(self):
        content=self.textEdit_4.toPlainText()
        if self.comboBox_4.currentText()=="Unordered List":
            newContent="<ul><li>"
            if len(content)==0:
                newContent+="Start typing here</li></ul>"
            else:
                for i in range(len(content)-1):
                    if content[i+1]=="\n":
                        newContent+=content[i]+"</li>"
                    elif content[i-1]=="\n":
                        newContent+="<li>"+content[i]
                    else:
                        newContent+=content[i]
                newContent+=content[-1]+"</li></ul>"
            self.textEdit_4.setHtml(newContent)
        elif self.comboBox_4.currentText()=="Ordered List":
            newContent="<ol><li>"
            if len(content)==0:
                newContent+="Start typing here</li></ol>"
            else:
                for i in range(len(content)-1):
                    if content[i+1]=="\n":
                        newContent+=content[i]+"</li>"
                    elif content[i-1]=="\n":
                        newContent+="<li>"+content[i]
                    else:
                        newContent+=content[i]
                newContent+=content[-1]+"</li></ol>"
            self.textEdit_4.setHtml(newContent)
        else:
            self.textEdit_4.clear()
            self.textEdit_4.insertPlainText(content)

    def askDelete(self):
        if self.prevRecord==None:
            self.warningWindow = QtWidgets.QMainWindow()
            self.warningUi = Ui_Warning()
            self.warningUi.setupUi(self.warningWindow)
            self.warningUi.changeText("noRecord")
            self.warningWindow.show()
        else:
            self.warningWindow = QtWidgets.QMainWindow()
            self.warningUi = Ui_Warning()
            self.warningUi.setupUi(self.warningWindow)
            self.warningUi.changeText1("askDelete",self)
            self.warningWindow.show()

    def deleteRecord(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("delete from serviceDatabase where id=?",(self.prevRecord.recordId))
        c.execute("delete from billingDatabase where serviceId=?",(self.prevRecord.recordId))
        conn.commit()
        conn.close()
        self.warningWindow = QtWidgets.QMainWindow()
        self.warningUi = Ui_Warning()
        self.warningUi.setupUi(self.warningWindow)
        self.warningUi.changeText("deleted")
        self.warningWindow.show()
        self.Window.close()

    def searchPatient(self):
        self.newWindow=QtWidgets.QMainWindow()
        self.ui=Ui_patientSearch(self)
        self.ui.setupUi(self.newWindow)
        self.newWindow.show()

    def saveRecord(self):
        if self.patient==None:
            self.warningWindow = QtWidgets.QMainWindow()
            self.warningUi = Ui_Warning()
            self.warningUi.setupUi(self.warningWindow)
            self.warningUi.changeText("noPatientSelected")
            self.warningWindow.show()
            return
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        if self.prevRecord==None:
            c.execute("insert into serviceDatabase(patientId, serviceDate, symptom, diagnosis, prescription, comment) values(?,?,?,?,?,?)",(self.patient.id, QDateTime.toString(QDateTime.currentDateTime()),self.textEdit.toHtml(),self.textEdit_2.toHtml(),self.textEdit_3.toHtml(),self.textEdit_4.toHtml()))
            self.lastRowId=c.lastrowid
            conn.commit()
            self.prevRecord=Record(self.lastRowId)
        else:
            c.execute("update serviceDatabase set symptom=?, diagnosis=?, prescription=?, comment=? where id=?",(self.textEdit.toHtml(),self.textEdit_2.toHtml(),self.textEdit_3.toHtml(),self.textEdit_4.toHtml(),self.prevRecord.recordId))
            conn.commit()
        self.saveConfirm=QtWidgets.QMainWindow()
        self.saveConfirmUi=Ui_Warning()
        self.saveConfirmUi.setupUi(self.saveConfirm)
        self.saveConfirmUi.changeText("saveSuccess")
        self.saveConfirm.show()
        conn.close()

    def saveRecordNoAlert(self):
        if self.patient==None:
            self.warningWindow = QtWidgets.QMainWindow()
            self.warningUi = Ui_Warning()
            self.warningUi.setupUi(self.warningWindow)
            self.warningUi.changeText("noPatientSelected")
            self.warningWindow.show()
            return
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        if self.prevRecord==None:
            c.execute("insert into serviceDatabase(patientId, serviceDate, symptom, diagnosis, prescription, comment) values(?,?,?,?,?,?)",(self.patient.id, QDateTime.toString(QDateTime.currentDateTime()),self.textEdit.toHtml(),self.textEdit_2.toHtml(),self.textEdit_3.toHtml(),self.textEdit_4.toHtml()))
            self.lastRowId=c.lastrowid
            conn.commit()
            self.prevRecord=Record(self.lastRowId)
        else:
            c.execute("update serviceDatabase set symptom=?, diagnosis=?, prescription=?, comment=? where id=?",(self.textEdit.toHtml(),self.textEdit_2.toHtml(),self.textEdit_3.toHtml(),self.textEdit_4.toHtml(),self.prevRecord.recordId))
            conn.commit()
        conn.close()

    def ifNotEmpty(self):
        if len(self.textEdit.toPlainText())!=0 and self.textEdit.toPlainText()!="Start typing here":
            return True
        elif len(self.textEdit_2.toPlainText())!=0 and self.textEdit_2.toPlainText()!="Start typing here":
            return True
        elif len(self.textEdit_3.toPlainText())!=0 and self.textEdit_3.toPlainText()!="Start typing here":
            return True
        elif len(self.textEdit_4.toPlainText())!=0 and self.textEdit_4.toPlainText()!="Start typing here":
            return True
        return False

    def askToSaveThenOpen(self):
        if self.patient!=None and self.ifNotEmpty():
            self.warningWindow = QtWidgets.QMainWindow()
            self.warningUi = Ui_Warning()
            self.warningUi.setupUi(self.warningWindow)
            self.warningUi.changeText1("askWhetherToSave1",self)
            self.warningWindow.show()
        else:
            self.openServiceRecord()

    def askToSaveThenClose(self):
        if self.patient!=None and self.ifNotEmpty() and next=="openServiceRecord":
            self.warningWindow = QtWidgets.QMainWindow()
            self.warningUi = Ui_Warning()
            self.warningUi.setupUi(self.warningWindow)
            self.warningUi.changeText1("askWhetherToSave2",self)
            self.warningWindow.show()
        else:
            self.Window.close()

    def openServiceRecord(self):
        self.serviceRecord = QtWidgets.QMainWindow()
        self.serviceRecordUi = Ui_ServiceRecord()
        self.serviceRecordUi.setupUi(self.serviceRecord)
        self.serviceRecord.show()
        self.Window.close()

    def printRecord(self):
        import webbrowser
        import shutil
        import os
        from bs4 import BeautifulSoup
        import time
        original=r"C:\Users\zzawo\Desktop\My Developing, Programming\HMS\record.html"
        target=r"C:\Users\zzawo\Desktop\My Developing, Programming\HMS\recordTemp.html"
        shutil.copyfile(original,target)
        self.saveRecordNoAlert()
        if self.patient==None:
            return
        with open("recordTemp.html","r",encoding="utf-8") as record:
            soup=BeautifulSoup(record,"html.parser")
        idTag=soup.find("div",{"id":"patientId"})
        idTag.extend([str(self.patient.id)])
        patientNameTag=soup.find("div",{"id":"patientName"})
        patientNameTag.extend([self.patient.name])
        patientDobTag=soup.find("div",{"id":"patientDOB"})
        patientDobTag.extend([self.patient.dob])
        patientGenderTag=soup.find("div",{"id":"patientGender"})
        patientGenderTag.extend([self.patient.gender])
        dateTag=soup.find("div",{"id":"date"})
        dateTag.extend([self.prevRecord.serviceDate])
        recordIdTag=soup.find("div",{"id":"recordId"})
        recordIdTag.extend([str(self.prevRecord.recordId)])
        billingIdTag=soup.find("div",{"id":"billingId"})
        billingIdTag.extend([str(self.prevRecord.billingId)])
        
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select amount from billingDatabase where serviceId=?",(self.prevRecord.recordId,))
        if c.fetchone()==None or len(c.fetchall())<1:
            amount="No payment"
        else:
            amount=str(c.fetchone()[0])
        c.execute("select * from hospitalInfoDatabase limit 1")
        hospitalInfo=c.fetchone()
        hospitalName=hospitalInfo[0]
        doctorName=hospitalInfo[1]
        logoDir=hospitalInfo[2]
        conn.close()
        amountTag=soup.find("div",{"id":"amountPaid"})
        amountTag.extend([amount])
        symptomTag=soup.find("div",{"id":"symptomText"})
        symptomTag.extend([html2text.html2text(self.prevRecord.symptom).replace("*","-")])
        diagnosisTag=soup.find("div",{"id":"diagnosisText"})
        diagnosisTag.extend([html2text.html2text(self.prevRecord.diagnosis).replace("*","-")])
        prescriptionTag=soup.find("div",{"id":"prescriptionText"})
        prescriptionTag.extend([html2text.html2text(self.prevRecord.prescription).replace("*","-")])
        commentTag=soup.find("div",{"id":"commentText"})
        commentTag.extend([html2text.html2text(self.prevRecord.comment).replace("*","-")])
        doctorNameTag=soup.find("h2",{"id":"doctorName"})
        doctorNameTag.extend([str(doctorName)])
        hospitalNameTag=soup.find("h2",{"id":"hospitalName"})
        hospitalNameTag.extend([str(hospitalName)])
        logoTag=soup.find("img",{"id":"logo"})
        logoTag['src']=logoDir
        g=open("recordTemp.html","w",encoding="UTF-8")
        g.write(str(soup))
        g.close()
        webbrowser.open_new_tab("C:/Users/zzawo/Desktop/My Developing, Programming/HMS/recordTemp.html")
        time.sleep(3)
        if os.path.exists("recordTemp.html"):
            os.remove("recordTemp.html")

    def loadRecord(self, recordId):
        self.prevRecord=Record(recordId)
        self.loadPatient(self.prevRecord.patientId)
        self.textEdit.setHtml(self.prevRecord.symptom)
        self.textEdit_2.setHtml(self.prevRecord.diagnosis)
        self.textEdit_3.setHtml(self.prevRecord.prescription)
        self.textEdit_4.setHtml(self.prevRecord.comment)

    def loadPatient(self,id):
        self.patient=Patient(id)
        self.label_2.setText("Name: "+self.patient.name)
        age=str(QDate.currentDate().getDate()[0]-int(self.patient.dob.split("-")[0]))
        self.label_3.setText("Age: "+age+" ("+self.patient.dob+")")
        self.label_4.setText("Gender: "+self.patient.gender)
        self.label_6.setText("Phone Number: "+self.patient.phone)
        temp=self.loadPatientPastVisits(id)
        if len(temp)>0:
            pastVisits=temp[0]
            pastVisitString=""
            for pastVisit in pastVisits:
                pastVisitString+=pastVisit+"\n"
            self.label_5.setText(pastVisitString)
        else:
            self.label_5.setText("No Past Visit")
        pastRecords=self.loadPatientPastRecords(id)
        for i in range(len(pastRecords)):
            self.pastRecordTable.setItem(i,0,QtWidgets.QTableWidgetItem(pastRecords[i][0]))
            diagnosisText=html2text.html2text(pastRecords[i][1]).replace("*","-")
            self.pastRecordTable.setItem(i,1,QtWidgets.QTableWidgetItem(diagnosisText))
            prescriptionText=html2text.html2text(pastRecords[i][2]).replace("*","-")
            self.pastRecordTable.setItem(i,2,QtWidgets.QTableWidgetItem(prescriptionText))

    def loadPatientPastVisits(self, patientId):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select serviceDate from serviceDatabase where patientId=? limit 3",(patientId,))
        pastDates=c.fetchall()
        conn.close()
        return pastDates
        
    def loadPatientPastRecords(self, patientId):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select serviceDate, diagnosis, prescription from serviceDatabase where patientId=? limit 3",(patientId,))
        pastRecords=c.fetchall()
        conn.close()
        return pastRecords

    def addBill(self):
        if self.prevRecord!=None and self.patient!=None:
            conn=sqlite3.connect("hospitalDatabase.db")
            c=conn.cursor()
            c.execute("insert into billingDatabase(patientId, serviceId, amount, comment) values(?,?,?,?)",(self.patient.id, self.prevRecord.recordId, 0, ""))
            conn.commit()
            conn.close()
            self.getBills()
        else:
            self.warningWindow = QtWidgets.QMainWindow()
            self.warningUi = Ui_Warning()
            self.warningUi.setupUi(self.warningWindow)
            self.warningUi.changeText("noRecordAddBill")
            self.warningWindow.show()

    def getBills(self):
        if self.prevRecord!=None and self.patient!=None:
            conn=sqlite3.connect("hospitalDatabase.db")
            c=conn.cursor()
            c.execute("select * from billingDatabase where serviceId=?",(str(self.prevRecord.recordId)))
            self.rows=c.fetchall()
            self.billTable.setRowCount(len(self.rows))
            for i in range(len(self.rows)):
                amountItem=QtWidgets.QTableWidgetItem(str(self.rows[i][3]))
                amountItem.setTextAlignment(QtCore.Qt.AlignCenter)
                commentItem=QtWidgets.QTableWidgetItem(self.rows[i][4])
                commentItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.billTable.setItem(i,0,commentItem)
                self.billTable.setItem(i,1,amountItem)
            conn.close()

    def chooseBill(self):
        id=self.rows[self.billTable.currentRow()][0]
        self.billWindow=QtWidgets.QMainWindow()
        self.billWindowUi = Ui_Bill(id)
        self.billWindowUi.setupUi(self.billWindow)
        self.billWindowUi.setMother(self,"diagnosis")
        self.billWindow.show()
        
    def setNotNew(self):
        self.newRecord=False
        self.pushButton.setEnabled(False)

    def returnHome(self):
        self.Window.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diagnosisWindow = QtWidgets.QMainWindow()
    ui = Ui_diagnosisWindow()
    ui.setupUi(diagnosisWindow)
    diagnosisWindow.show()
    sys.exit(app.exec_())

def openDiagnosis():
    diagnosisWindow = QtWidgets.QMainWindow()
    ui = Ui_diagnosisWindow()
    ui.setupUi(diagnosisWindow)
    diagnosisWindow.show()
    return diagnosisWindow
