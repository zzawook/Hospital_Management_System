# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePatient.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
import pickle
import addPatientEntryWarning
from addPatientEntryWarning import *
import sqlite3
from sqlite3 import *
import html2text
import diagnosis
from diagnosis import *

class Ui_ChangePatient(object):
    def __init__(self,id,prevWindow):
        self.id=id
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select name from patientDatabase where id=?",self.id)
        self.name=c.fetchone()
        c.execute("select dateOfBirth from patientDatabase where id=?",self.id)
        self.dateOfBirth=c.fetchone()
        c.execute("select phone from patientDatabase where id=?",self.id)
        self.phone=c.fetchone()
        c.execute("select gender from patientDatabase where id=?",self.id)
        self.gender=c.fetchone()
        c.execute("select address from patientDatabase where id=?",self.id)
        self.address=c.fetchone()
        c.execute("select email from patientDatabase where id=?",self.id)
        self.email=c.fetchone()
        c.execute("select * from serviceDatabase where patientId=?",self.id)
        self.record=c.fetchall()
        self.mother=prevWindow
        conn.close()


    def setupUi(self, AddNewPatient):
        self.Window=AddNewPatient
        AddNewPatient.setObjectName("AddNewPatient")
        AddNewPatient.resize(1920, 1015)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddNewPatient)
        self.buttonBox.setGeometry(QtCore.QRect(1270, 940, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(AddNewPatient)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLineWidth(7)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddNewPatient)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(AddNewPatient)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(AddNewPatient)
        self.label_3.setGeometry(QtCore.QRect(450, 65, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(AddNewPatient)
        self.dateEdit.setGeometry(QtCore.QRect(570, 56, 101, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(AddNewPatient)
        self.label_4.setGeometry(QtCore.QRect(690, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddNewPatient)
        self.label_5.setGeometry(QtCore.QRect(810, 65, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(AddNewPatient)
        self.lineEdit_2.setGeometry(QtCore.QRect(940, 60, 311, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(AddNewPatient)
        self.label_6.setGeometry(QtCore.QRect(1340, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(AddNewPatient)
        self.lineEdit_3.setGeometry(QtCore.QRect(1470, 62, 311, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(AddNewPatient)
        self.label_8.setGeometry(QtCore.QRect(20, 170, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.listWidget = QtWidgets.QTableWidget(AddNewPatient)
        self.listWidget.setGeometry(QtCore.QRect(10, 210, 1901, 721))
        self.listWidget.setObjectName("listWidget")
        self.checkBox = QtWidgets.QCheckBox(AddNewPatient)
        self.checkBox.setGeometry(QtCore.QRect(100, 135, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(AddNewPatient)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 135, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(AddNewPatient)
        self.checkBox_3.setGeometry(QtCore.QRect(240, 135, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox.stateChanged.connect(self.resetGenderMale)
        self.checkBox_2.stateChanged.connect(self.resetGenderFemale)
        self.checkBox_3.stateChanged.connect(self.resetGenderOther)
        self.label_9 = QtWidgets.QLabel(AddNewPatient)
        self.label_9.setGeometry(QtCore.QRect(30, 130, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(AddNewPatient)
        self.lineEdit_4.setGeometry(QtCore.QRect(560, 130, 1221, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(AddNewPatient)
        self.label_10.setGeometry(QtCore.QRect(420, 140, 131, 16))
        self.button1 = QtWidgets.QPushButton(AddNewPatient)
        self.button1.setGeometry(QtCore.QRect(1542,10,241,41))
        self.button1.clicked.connect(self.deleteSelected)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.changing=False
        self.buttonList=[]
        self.retranslateUi(AddNewPatient)
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.returnBack)
        QtCore.QMetaObject.connectSlotsByName(AddNewPatient)

    def retranslateUi(self, AddNewPatient):
        _translate = QtCore.QCoreApplication.translate
        AddNewPatient.setWindowTitle(_translate("AddNewPatient", "Change Patient Data"))
        self.label.setText(_translate("AddNewPatient", "Change Patient Data"))
        self.label_2.setText(_translate("AddNewPatient", "Name:"))
        self.label_3.setText(_translate("AddNewPatient", "Date of Birth: "))
        self.label_4.setText(_translate("AddNewPatient", "Age: "))
        self.label_5.setText(_translate("AddNewPatient", "Phone-Number: "))
        self.label_6.setText(_translate("AddNewPatient", "Email Address: "))
        self.label_8.setText(_translate("AddNewPatient", "Consultancy Record:"))
        self.checkBox.setText(_translate("AddNewPatient", "Male"))
        self.checkBox_2.setText(_translate("AddNewPatient", "Female"))
        self.checkBox_3.setText(_translate("AddNewPatient", "Other"))
        self.label_9.setText(_translate("AddNewPatient", "Gender:"))
        self.label_10.setText(_translate("AddNewPatient", "Address:"))
        self.lineEdit.setText(_translate("AddNewPatient", self.name[0]))
        self.lineEdit_2.setText(_translate("AddNewPatient", self.phone[0]))
        self.lineEdit_3.setText(_translate("AddNewPatient", self.email[0]))
        self.lineEdit_4.setText(_translate("AddNewPatient", self.address[0]))
        self.button1.setText(_translate("AddNewPatient", "Delete Patient Profile"))
        self.dateEdit.setDate(QDate(int(self.dateOfBirth[0].split("-")[0]),int(self.dateOfBirth[0].split("-")[1]),int(self.dateOfBirth[0].split("-")[2])))
        self.changing=True
        if self.gender[0]=="Male":
            self.checkBox.setChecked(True)
        elif self.gender[0]=="Female":
            self.checkBox_2.setChecked(True)
        else:
            self.checkBox_3.setChecked(True)
        self.changing=False
        self.listWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.listWidget.setRowCount(len(self.record))
        self.listWidget.setColumnCount(6)
        self.listWidget.setHorizontalHeaderLabels(["ID","Date / Time","Symptom","Diagnosis","Prescription","Detail"])
        self.listWidget.setColumnWidth(0,80)
        self.listWidget.setColumnWidth(1,250)
        self.listWidget.setColumnWidth(2,418)
        self.listWidget.setColumnWidth(3,500)
        self.listWidget.setColumnWidth(4,500)
        self.listWidget.setColumnWidth(5,150)
        for i in range(len(self.record)):
            self.listWidget.setRowHeight(i,50)
            recordId=QtWidgets.QTableWidgetItem(str(self.record[i][0]))
            font=QtGui.QFont()
            font.setPointSize(9)
            recordId.setFont(font)
            recordId.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,0,recordId)
            dateObject=self.record[i][2].split(" ")
            (dayName,month,numDay,time,year)=(str(dateObject[0]),int(dateObject[1]),int(dateObject[2]),str(dateObject[3]),int(dateObject[4]))
            date=QtWidgets.QTableWidgetItem(getMonthName(month)+" "+str(numDay)+", "+str(year)+"("+dayName+")"+"\n"+str(time))
            date.setFont(font)
            date.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,1,date)
            symptomText=html2text.html2text(str(self.record[i][3])).replace("*","-")
            symptom=QtWidgets.QTableWidgetItem(symptomText)
            symptom.setFont(font)
            symptom.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,2,symptom)
            diagnoseText=html2text.html2text(str(self.record[i][4])).replace("*","-")
            diagnose=QtWidgets.QTableWidgetItem(diagnoseText)
            diagnose.setFont(font)
            diagnose.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,3,diagnose)
            prescriptionText=html2text.html2text(str(self.record[i][5])).replace("*","-")
            prescription=QtWidgets.QTableWidgetItem(prescriptionText)
            prescription.setFont(font)
            prescription.setTextAlignment(QtCore.Qt.AlignCenter)
            self.listWidget.setItem(i,4,prescription)
            self.button=QtWidgets.QPushButton("View Details")
            self.button.setObjectName("button"+str(i))
            index = QtCore.QPersistentModelIndex(self.listWidget.model().index(i, 5))
            self.button.clicked.connect(lambda *args, index=index: self.openServiceRecord(index.row()))
            self.buttonList.append(self.button)
            self.listWidget.setCellWidget(i,5,(self.buttonList[-1]))

    def openServiceRecord(self,row):
        self.thisServiceRecord=QtWidgets.QMainWindow()
        id=self.listWidget.item(row,0).text()
        self.SRUi=diagnosis.Ui_diagnosisWindow()
        self.SRUi.setupUi(self.thisServiceRecord)
        self.SRUi.setNotNew()
        self.SRUi.loadRecord(id)
        self.thisServiceRecord.show()
          
    def save(self):
        cleared=True
        if not self.lineEdit_2.text()=="":
            self.phone=self.lineEdit_2.text()
        else:
            self.badEntryAlert("phone")
            cleared=False
        if self.checkBox.isChecked():
            gender="Male"
        elif self.checkBox_2.isChecked():
            gender="Female"
        elif self.checkBox_3.isChecked():
            gender="Other"
        else:
            self.badEntryAlert("gender")
            cleared=False
        if not self.lineEdit.text()=="":
            self.name=self.lineEdit.text()
        else:
            self.badEntryAlert("name")
            cleared=False
        self.address=self.lineEdit_4.text()
        self.email=self.lineEdit_3.text()
        self.dateOfBirth=str(self.dateEdit.date().getDate()[0])+"-"+str(self.dateEdit.date().getDate()[1])+"-"+str(self.dateEdit.date().getDate()[2])
        if cleared:
            profile=(self.name,self.dateOfBirth,gender,self.phone,self.address,self.email,int(self.id))
            self.updatePatientData(profile)
            self.mother.updatePatientInfo()
            self.Window.close()

    def badEntryAlert(self,criteria):
        self.Warning = QtWidgets.QDialog()
        self.WarningUi=Ui_Warning()
        self.WarningUi.setupUi(self.Warning)
        self.Warning.show()
        self.WarningUi.changeText1(criteria,self)

    def updatePatientData(self, profile):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        sql='''UPDATE patientDatabase set name=?,dateOfBirth=?,gender=?,phone=?,address=?,email=? where id=?'''
        c.execute(sql, profile)
        conn.commit()
        conn.close()

    def returnBack(self):
        self.Window.close()

    def deleteSelected(self):
        self.badEntryAlert("delete")

    def delete(self):
         conn=sqlite3.connect("HospitalDatabase.db")
         c=conn.cursor()
         sql='DELETE from patientDatabase where id=?'
         c.execute(sql,(self.id,))
         c.execute("delete from serviceDatabase where patientId=?",(self.id))
         c.execute("delete from billingDatabase where patientid=?",(self.id))
         conn.commit()
         conn.close()
         self.mother.updatePatientInfo()
         self.Window.close()


    def resetGenderMale(self):
        if not self.changing:
            self.uncheckAll()
            self.checkBox.setChecked(True)

    def resetGenderFemale(self):
        if not self.changing:
            self.uncheckAll()
            self.checkBox_2.setChecked(True)

    def resetGenderOther(self):
        if not self.changing:
            self.uncheckAll()
            self.checkBox_3.setChecked(True)

    def uncheckAll(self):
        self.changing=True
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        self.checkBox_3.setChecked(False)
        self.changing=False

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

#if __name__ == "__main__"::

#    import sys
 #   app = QtWidgets.QApplication(sys.argv)
#    AddNewPatient = QtWidgets.QDialog()
 #   ui = Ui_ChangePatient()
  #  ui.setupUi(AddNewPatient)
   # AddNewPatient.show()
    #sys.exit(app.exec_())
