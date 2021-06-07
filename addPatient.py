# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPatient.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
import patientData
from patientData import *
import addPatientEntryWarning
from addPatientEntryWarning import *
import pickle
import sqlite3
from sqlite3 import *

class Ui_AddNewPatient(object):
    def __init__(self, mother):
        self.mother=mother
    def setupUi(self, AddNewPatient):
        self.Window=AddNewPatient
        AddNewPatient.setObjectName("AddNewPatient")
        AddNewPatient.resize(584, 506)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddNewPatient)
        self.buttonBox.setGeometry(QtCore.QRect(-100, 430, 621, 41))
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
        self.label_2.setGeometry(QtCore.QRect(90, 70, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(AddNewPatient)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(AddNewPatient)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.dateEdit = QtWidgets.QDateEdit(AddNewPatient)
        self.dateEdit.dateChanged.connect(self.calculateAge)
        self.dateEdit.setGeometry(QtCore.QRect(150, 116, 101, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setMinimumDate(QDate(1800,1,1))
        self.dateEdit.setMaximumDate(QDate.currentDate()) 
        self.label_4 = QtWidgets.QLabel(AddNewPatient)
        self.label_4.setGeometry(QtCore.QRect(270, 120, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddNewPatient)
        self.label_5.setGeometry(QtCore.QRect(20, 235, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(AddNewPatient)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 230, 311, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(AddNewPatient)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(AddNewPatient)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 352, 311, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(AddNewPatient)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 295, 311, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(AddNewPatient)
        self.label_8.setGeometry(QtCore.QRect(20, 300, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(AddNewPatient)
        self.label_9.setGeometry(QtCore.QRect(10, 170, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.checkBox = QtWidgets.QCheckBox(AddNewPatient)
        self.checkBox.setGeometry(QtCore.QRect(150, 170, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.resetGenderMale)
        self.checkBox_2 = QtWidgets.QCheckBox(AddNewPatient)
        self.checkBox_2.setGeometry(QtCore.QRect(210, 170, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.resetGenderFemale)
        self.checkBox_3 = QtWidgets.QCheckBox(AddNewPatient)
        self.checkBox_3.setGeometry(QtCore.QRect(280, 170, 141, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.stateChanged.connect(self.resetGenderOther)
        self.changing=False
        self.retranslateUi(AddNewPatient)
        self.buttonBox.accepted.connect(self.add)
        self.buttonBox.rejected.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(AddNewPatient)

    def retranslateUi(self, AddNewPatient):
        _translate = QtCore.QCoreApplication.translate
        AddNewPatient.setWindowTitle(_translate("AddNewPatient", "Add New Patient"))
        self.label.setText(_translate("AddNewPatient", "Add New Patient"))
        self.label_2.setText(_translate("AddNewPatient", "Name:"))
        self.label_3.setText(_translate("AddNewPatient", "Date of Birth: "))
        self.label_4.setText(_translate("AddNewPatient", "Age: "))
        self.label_5.setText(_translate("AddNewPatient", "Phone-Number: "))
        self.label_6.setText(_translate("AddNewPatient", "Email (Optional): "))
        self.label_8.setText(_translate("AddNewPatient", "Address (Optional):"))
        self.label_9.setText(_translate("AddNewPatient", "Gender:"))
        self.checkBox.setText(_translate("AddNewPatient", "Male"))
        self.checkBox_2.setText(_translate("AddNewPatient", "Female"))
        self.checkBox_3.setText(_translate("AddNewPatient", "Other"))

    def close(self):
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

    def add(self):
        cleared=True
        pNumber=self.lineEdit_2.text()
        if pNumber=="":
            self.badEntryAlert("phone")
            cleared=False
        gender=""
        if self.checkBox.isChecked():
            gender="Male"
        elif self.checkBox_2.isChecked():
            gender="Female"
        elif self.checkBox_3.isChecked():
            gender="Other"
        else:
            self.badEntryAlert("gender")
            cleared=False
        name=self.lineEdit.text().strip()
        if name=="" or name==None:
            self.badEntryAlert("name")
            cleared=False
        dob=self.dateEdit.date()
        dob=str(dob.getDate()[0])+"-"+str(dob.getDate()[1])+"-"+str(dob.getDate()[2])
        address=self.lineEdit_4.text()
        email=self.lineEdit_3.text()
        if cleared:
            conn=sqlite3.connect("HospitalDatabase.db")
            c=conn.cursor()
            sql='''INSERT into patientDatabase(name,dateOfBirth,gender,phone,address,email) values(?,?,?,?,?,?)'''
            profile=(str(name), str(dob), str(gender) ,str(pNumber),str(address),str(email))
            c.execute(sql,profile)
            conn.commit()
            conn.close()
            self.mother.updatePatientInfo()
            self.Window.close()

    def badEntryAlert(self,criteria):
        self.Warning = QtWidgets.QDialog()
        self.WarningUi=Ui_Warning()
        self.WarningUi.setupUi(self.Warning)
        self.Warning.show()
        self.WarningUi.changeText(criteria)

    def calculateAge(self):
        dob=self.dateEdit.date().getDate()
        current=QDate.currentDate().getDate()
        age=current[0]-dob[0]
        _translate = QtCore.QCoreApplication.translate
        self.label_4.setText(_translate("AddNewPatient", "Age: "+str(age)))

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddNewPatient = QtWidgets.QDialog()
    ui = Ui_AddNewPatient()
    ui.setupUi(AddNewPatient)
    AddNewPatient.show()
    sys.exit(app.exec_())
