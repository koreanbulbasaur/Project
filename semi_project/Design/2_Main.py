import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15 # 글자크기
matplotlib.rcParams['axes.unicode_minus']=False

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
        # self.print_btn.clicked.connect(self.print_data)

        self.show()

    def secondwindow(self):
        header_index = self
        self.reject()
        SecondOption(self)


class SecondOption(QDialog):
    def __init__(self, parent):
        super(SecondOption, self).__init__(parent)
        uic.loadUi(r'C:\Project\semi_project\Design\2_second_option.ui', self)

        self.second_next_btn.clicked.connect(self.thirdwindow)

        self.show()

    def thirdwindow(self):
        self.reject()
        ThirdOption(self)


class ThirdOption(QDialog):
    def __init__(self, parent):
        super(ThirdOption, self).__init__(parent)
        uic.loadUi(r'C:\Project\semi_project\Design\2_third_option.ui', self)

        self.complete_btn.clicked.connect(self.create_graph)


        self.show()

    def create_graph(self):
        self.reject()
        CreateGraph(self)

class CreateGraph():
    def __init__(self):
        pass

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()

app.exec_()
