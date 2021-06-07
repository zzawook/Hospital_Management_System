# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bill.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sqlite3 import *
import addPatientEntryWarning
from addPatientEntryWarning import *


class Ui_Bill(object):
    def __init__(self, id):
        conn=sqlite3.connect("hospitalDatabase.db")
        c=conn.cursor()
        c.execute("select patientDatabase.name, serviceDatabase.serviceDate, billingDatabase.amount, billingDatabase.comment from ((billingDatabase inner join patientDatabase on patientDatabase.id=billingDatabase.patientId) inner join serviceDatabase on serviceDatabase.id=billingDatabase.serviceId) where billingDatabase.id=?",(id,))
        data=c.fetchone()
        self.id=id
        self.patientName=data[0]
        self.dos=data[1]
        self.amount=data[2]
        self.comment=data[3]
        conn.close()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(471, 395)
        self.Window=Dialog
        self.mother=None
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(270, 320, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(15, 190, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(130, 70, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 130, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 185, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(str(self.amount))
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 240, 311, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(self.comment)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(344, 10, 101, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.deleteBill)
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Patient Name:"))
        self.label_2.setText(_translate("Dialog", "Date of Service: "))
        self.label_3.setText(_translate("Dialog", "Amount Paid:  Rs."))
        self.label_4.setText(_translate("Dialog", self.patientName))
        self.label_5.setText(_translate("Dialog", self.dos))
        self.label_6.setText(_translate("Dialog", "Comment:"))
        self.pushButton.setText(_translate("Dialog", "Delete This Bill"))

    def setMother(self, mother, prevScreen):
        self.mother=mother
        self.prevScreen=prevScreen

    def deleteBill(self):
        conn=sqlite3.connect("hospitalDatabase.db")
        c=conn.cursor()
        c.execute("delete from billingDatabase where id=?",(str(self.id)))
        conn.commit()
        conn.close()
        self.warningWindow = QtWidgets.QMainWindow()
        self.warningUi = Ui_Warning()
        self.warningUi.setupUi(self.warningWindow)
        self.warningUi.changeText("deleted")
        self.warningWindow.show()
        if self.prevScreen=="diagnosis":
            self.mother.getBills()
        elif self.prevScreen=="finance":
            self.mother.search()
        self.Window.close()
        
    def accept(self):
        conn=sqlite3.connect("hospitalDatabase.db")
        c=conn.cursor()
        c.execute("update billingDatabase set amount=?, comment=? where id=?", (self.lineEdit.text(), self.lineEdit_2.text(), self.id))
        conn.commit()
        conn.close()
        if self.prevScreen=="diagnosis":
            self.mother.getBills()
        elif self.prevScreen=="finance":
            self.mother.search()
        self.Window.close()

    def reject(self):
        self.Window.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Bill(1)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
