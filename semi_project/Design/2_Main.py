import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt

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

        self.file_name = None


    def openFunction(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            self.text_file.setPlainText(fname[0])
            self.file_name = fname[0]

    def createGraph(self):
        if self.file_name == None:
            return
        else:
            FirstOption(self)


class FirstOption(QDialog):
    def __init__(self, parent):
        super(FirstOption, self).__init__(parent)
        uic.loadUi(r'C:\Project\semi_project\Design\2_first_option.ui', self)

        self.header_Index = None
        self.index_Col = None

        self.first_next_btn.clicked.connect(self.secondwindow)

        self.show()

    def secondwindow(self):
        header_Index = self.Index_Row.text()
        index_Col = self.Index_Column.text()

        data = self.parent().file_name

        self.reject()
        SecondOption(self.parent(), data, header_Index, index_Col)

class SecondOption(QDialog):
    def __init__(self, parent, data, header_Index, index_Col):
        super(SecondOption, self).__init__(parent)
        uic.loadUi(r'C:\Project\semi_project\Design\2_second_option.ui', self)

        self.firsttable = self.first_table
        self.secondtable = self.second_table

        self.second_next_btn.clicked.connect(self.thirdwindow)
        self.T_btn.clicked.connect(self.retrieveCheckboxValues)

        self.header_Index = int(header_Index)
        self.index_Col = index_Col

        self.data = data

        if data.endswith('.csv'):
            self.df = pd.read_csv(data)
        elif data.endswith('.xlsx'):
            # print(self.header_Index)
            self.df = pd.read_excel(data, index_col=self.header_Index)

        self.firsttable.setRowCount(len(self.df))
        self.firsttable.setColumnCount(1)
        self.firsttable.setHorizontalHeaderLabels([self.df.index.name])

        for row in range(len(self.df)):
            self.df.index = self.df.index.astype('object')
            item = QTableWidgetItem(str(self.df.index[row]))
            item.setFlags(Qt.ItemFlag.ItemIsUserCheckable |Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.firsttable.setItem(row, 0, item)

        self.secondtable.setRowCount(len(self.df.columns))
        self.secondtable.setColumnCount(1)
        self.secondtable.setHorizontalHeaderLabels(['열'])

        for col in range(len(self.df.columns)):
            item = QTableWidgetItem(str(self.df.columns[col]))
            item.setFlags(Qt.ItemFlag.ItemIsUserCheckable |Qt.ItemFlag.ItemIsEnabled)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.secondtable.setItem(col, 0, item)

        self.show()

    def thirdwindow(self):
        self.reject()
        ThirdOption(self, self.df)

    def retrieveCheckboxValues(self):
        for row in range(self.firsttable.rowCount()):
            if self.firsttable.item(row, 0).checkState() == Qt.CheckState.Checked:
                print([self.firsttable.item(row, col).text()
                      for col in range(self.firsttable.columnCount())])
        print('-'*100)

class ThirdOption(QDialog):
    def __init__(self, parent, df):
        super(ThirdOption, self).__init__(parent)
        uic.loadUi(r'C:\Project\semi_project\Design\2_third_option.ui', self)

        self.df = df

        self.complete_btn.clicked.connect(self.create_graph)

        self.show()

    def create_graph(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        value = self.df.iloc[row, col]
        # value 값을 이용하여 차트 그리기
        self.reject()


app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()

app.exec_()