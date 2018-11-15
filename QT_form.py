import sys
from PyQt5 import QtWidgets
from untitled import Ui_Dialog

class MyPyQT_Form(Ui_Dialog):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)



    def initUI(self):
        self.setWindowTitle("QFileDialog")
        self.setGeometry(400,400,300,260)


        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())