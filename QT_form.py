import sys
from PyQt5 import QtCore,QtGui,uic,QtWidgets
from untitled import Ui_Dialog

form_class = uic.loadUiType("myfirstgui.ui")[0]
class MyPyQT_Form(QtWidgets.QMainWindow,form_class):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        x = self.pushButton.x();
        y = self.pushButton.y();
        x+=5
        y+=5
        self.pushButton.move(x,y)
        self.textEdit.append(str(x)+str(y))

app = QtWidgets.QApplication(sys.argv)
myWindow = MyPyQT_Form()
myWindow.show()
app.exec_()