import diagnosis
from diagnosis import *
import home
from home import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app=QtWidgets.QApplication(sys.argv)
home.start()
sys.exit(app.exec_())
