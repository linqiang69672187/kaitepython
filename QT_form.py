import sys
from PyQt5 import QtCore,QtGui,uic,QtWidgets
from untitled import Ui_Dialog

form_class = uic.loadUiType("myfirstgui.ui")[0]
class MyPyQT_Form(QtWidgets.QMainWindow,form_class):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)

app = QtWidgets.QApplication(sys.argv)
myWindow = MyPyQT_Form()
myWindow.show()
app.exec_()