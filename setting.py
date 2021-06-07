# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sqlite3
from sqlite3 import *
import addPatientEntryWarning
from addPatientEntryWarning import *


class Ui_Setting(object):
    def __init__(self):
        conn=sqlite3.connect("HospitalDatabase.db")
        c=conn.cursor()
        c.execute("select * from hospitalInfoDatabase")
        data=c.fetchone()
        if data!=None:
            self.hospitalName=data[0]
            self.doctorName=data[1]
            self.logoDir=data[2]
        else:
            self.hospitalName=""
            self.doctorName=""
            self.logoDir=""
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.Window=MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 521, 951))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(300, 50, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(300, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(230, 380, 271, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.askInitialize)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 60, 781, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(550, 170, 256, 211))
        self.image_label.setObjectName("image_label")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(1240, 460, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 390, 1051, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReturn_Home = QtWidgets.QAction(MainWindow)
        self.actionReturn_Home.setObjectName("actionReturn_Home")
        self.actionReturn_Home.triggered.connect(self.close)
        self.menuHome.addAction(self.actionReturn_Home)
        self.menubar.addAction(self.menuHome.menuAction())
        self.browseButton=QtWidgets.QPushButton(MainWindow)
        self.browseButton.setObjectName("browseButton")
        self.browseButton.setGeometry(QtCore.QRect(810,347,101,31))
        self.browseButton.clicked.connect(self.browse)
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.close)
        self.lineEdit_2 = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGeometry(QtCore.QRect(540,135,781,41))
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(300,100,201,41))
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QtCore.QRect(810,185,331,41))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Setting"))
        self.label.setText(_translate("MainWindow", "Name of the hospital: "))
        self.label_2.setText(_translate("MainWindow", "Logo of the hospital: "))
        self.pushButton.setText(_translate("MainWindow", "Clear All Data - Initialization: "))
        self.label_5.setText(_translate("MainWindow", "Once you click this button, you cannot restore the hospital data, and all records of patient and services will be gone. Please be considerate pushing this button."))
        self.label_3.setText(_translate("MainWindow", "Name of Doctor"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.actionReturn_Home.setText(_translate("MainWindow", "Return Home"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindiw", "Please format your logo to 256 x 211 pixel size"))
        self.image_label.setPixmap(QPixmap(str(self.logoDir)))
        self.lineEdit.setText(str(self.hospitalName))
        self.lineEdit_2.setText(str(self.doctorName))


    def browse(self):
        import tkinter
        from tkinter import filedialog
        import os
        import shutil
        import imghdr
        root=tkinter.Tk()
        root.withdraw()
        currDir=os.getcwd()
        tempDir = filedialog.askopenfilename(parent = root, initialdir = os.getcwd(), title = "Please select a file", filetypes = (('PNG Files', '.png'), ('JPEG Files', '.jpeg'),("JPG Files",".jpg"),))
        if len(tempDir)>0:
            if tempDir==self.logoDir:
                return
            selectedType=imghdr.what(tempDir)
            target=currDir+"\sources\logo."+str(selectedType)
            shutil.copyfile(tempDir,target)
            self.logoDir=target
            self.image_label.setPixmap(QPixmap(str(self.logoDir)))

    def save(self):
        if len(self.hospitalName)>0 and len(self.doctorName)>0 and len(self.logoDir)>0:
            conn=sqlite3.connect("hospitalDatabase.db")
            c=conn.cursor()
            c.execute("update hospitalInfoDatabase set hospitalName=?,doctorName=?,logoDir=?",(self.lineEdit.text(), self.lineEdit_2.text(), self.logoDir))
            conn.commit()
            conn.close()
            self.Saved = QtWidgets.QDialog()
            self.SavedUi=Ui_Warning()
            self.SavedUi.setupUi(self.Saved)
            self.Saved.show()
            self.SavedUi.changeText("saveSuccess")
            self.Window.close()
        else:
            self.Warning = QtWidgets.QDialog()
            self.WarningUi=Ui_Warning()
            self.WarningUi.setupUi(self.Warning)
            self.Warning.show()
            self.WarningUi.changeText("noEntry")

    def askInitialize(self):
        self.Warning = QtWidgets.QDialog()
        self.WarningUi=Ui_Warning()
        self.WarningUi.setupUi(self.Warning)
        self.Warning.show()
        self.WarningUi.changeText1("initialize",self)

    def initialize(self):
        conn=sqlite3.connect("hospitalDatabase.db")
        c=conn.cursor()
        c.execute("delete from patientDatabase")
        c.execute("delete from hospitalInfoDatabase")
        c.execute("delete from serviceDatabase")
        c.execute("delete from billingDatabase")
        conn.commit()
        conn.close()

    def close(self):
        self.Window.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Setting()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
