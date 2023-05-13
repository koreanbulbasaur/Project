import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r'C:\Project\semi_project\Design\2_Main.ui')[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.open_btn.clicked.connect(self.openFunction)
        self.graph_btn.clicked.connect(self.createGraph)

    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            self.plainTextEdit.setPlainText(fname[0])

    def createGraph(self):
        FirstOption(self)


class FirstOption(QDialog):
    def __init__(self, parent):
        super(FirstOption, self).__init__(parent)
        uic.loadUi(r'C:\Project\semi_project\Design\2_first_option.ui', self)

        self.first_next_btn.clicked.connect(self.secondwindow)

        self.show()

    def secondwindow(self):
        SecondOption(self)


class SecondOption(QDialog):
    def __init__(self, parent):
        super(SecondOption, self).__init__(parent)
        uic.loadUi(r'C:\Project\semi_project\Design\2_second_option.ui', self)
        self.show()


app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()
