# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPatientEntryWarning.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Warning(object):
    def setupUi(self, Warning):
        Warning.setObjectName("Warning")
        Warning.resize(454, 148)
        self.Window=Warning
        self.buttonBox = QtWidgets.QDialogButtonBox(Warning)
        self.buttonBox.setGeometry(QtCore.QRect(-300, 100, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Warning)
        self.label.setGeometry(QtCore.QRect(20, 40, 421, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.criteria=None
        self.retranslateUi(Warning)
        self.buttonBox.accepted.connect(self.accepted)
        self.buttonBox.rejected.connect(self.canceled)
        QtCore.QMetaObject.connectSlotsByName(Warning)

    def retranslateUi(self, Warning):
        _translate = QtCore.QCoreApplication.translate
        Warning.setWindowTitle(_translate("Alert", "Dialog"))
        self.label.setText(_translate("Warning", "TextLabel"))

    def changeText(self,criteria):
        self.criteria=criteria
        if criteria=="name":
            self.label.setText("Please enter a valid name of the patient.")
        elif criteria=="gender":
            self.label.setText("Please indicate gender identity of the patient.")
        elif criteria=="phone":
            self.label.setText("Please enter a valid phone number.")
        elif criteria=="saveSuccess":
            self.label.setText("Save Success!")
        elif criteria=="noPatientSelected":
            self.label.setText("There is no patient selected. \nPlease retry after selecting a patient.")
        elif criteria=="noRecord":
            self.label.setText("There is no record loaded. \nThere is no record to delete.")
        elif criteria=="deleted":
            self.label.setText("Successfully Deleted")
        elif criteria=="noEntry":
            self.label.setText("There is no entry given. Please enter all fields.")
        elif criteria=="noRecordAddBill":
            self.label.setText("Please save before you add the bill")

    def changeText1(self,criteria,mother):
        if criteria=="delete":
            self.criteria=criteria
            self.label.setText("Once you delete, the profile cannot be restored. \nContinue?")
        elif criteria=="askWhetherToSave1" or criteria=="askWhetherToSave2":
            self.label.setText("Would you like to save current service record?")
            self.criteria=criteria
        elif criteria=="askDelete":
            self.label.setText("Once you delete, the record cannot be restored. \nContinue?")
            self.criteria=criteria
        elif criteria=="initialize":
            self.label.setText("Once you initialize, the entire database, including patient, record, \nand finance data will be deleted. Continue?")
            self.criteria=criteria
        self.mother=mother

    def canceled(self):
        self.Window.close()

    def accepted(self):
        if self.criteria=="delete":
            self.mother.delete()
        elif self.criteria=="askWhetherToSave1":
            self.mother.saveRecordNoAlert()
            self.mother.openServiceRecord()
        elif self.criteria=="askWhetherToSave2":
            self.mother.returnHome()
        elif self.criteria=="askDelete":
            self.mother.deleteRecord()
        elif self.criteria=="initialize":
            self.mother.initialize()
        self.Window.close()
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Warning = QtWidgets.QDialog()
    ui = Ui_Warning()
    ui.setupUi(Warning)
    Warning.show()
    sys.exit(app.exec_())
