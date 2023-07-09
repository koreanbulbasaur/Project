import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r'C:\Project\PYQT_study\1_hello.ui')[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()
