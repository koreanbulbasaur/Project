import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt
import statistics

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

        if index_Col != '' and header_Index != '':
            self.reject()
            SecondOption(self.parent(), data, header_Index, index_Col)

class SecondOption(QDialog):
    def __init__(self, parent, data, header_Index, index_Col):
        super(SecondOption, self).__init__(parent)
        uic.loadUi(r'C:\Project\semi_project\Design\2_second_option.ui', self)

        self.firsttable = self.first_table
        self.secondtable = self.second_table

        self.df_option = None

        self.second_next_btn.clicked.connect(self.thirdwindow)
        self.T_btn.clicked.connect(self.t_btn_test)

        self.header_Index = int(header_Index)
        self.index_Col = int(index_Col)

        self.data = data

        if data.endswith('.csv'):
            self.df = pd.read_csv(data)
        elif data.endswith('.xlsx'):
            # print(self.header_Index)
            self.df = pd.read_excel(data, index_col=self.index_Col, header=self.header_Index)

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
        row_list = []
        col_list = []

        row_index = 0
        col_index = 0

        for row in range(self.firsttable.rowCount()):
            if self.firsttable.item(row, 0).checkState() == Qt.CheckState.Checked:
                row_index += 1
        
        for col in range(self.secondtable.rowCount()):
            if self.secondtable.item(col, 0).checkState() == Qt.CheckState.Checked:
                col_index += 1


        if row_index != 0 and col_index != 0:
            for row in range(self.firsttable.rowCount()):
                if self.firsttable.item(row, 0).checkState() == Qt.CheckState.Checked:
                    print(self.firsttable.item(row, 0).text())
                    row_list.append(row)
            
            for col in range(self.secondtable.rowCount()):
                if self.secondtable.item(col, 0).checkState() == Qt.CheckState.Checked:
                    print(self.secondtable.item(col, 0).text())
                    col_list.append(col)

            print('-'*100)
            print(row_list)
            print(col_list)

            self.df_option = self.df.iloc[row_list, col_list]
            # print(self.df_option)

            self.reject()
            ThirdOption(self)
        else:
            pass

    def t_btn_test(self):
        pass

class ThirdOption(QDialog):
    def __init__(self, parent):
        super(ThirdOption, self).__init__(parent)
        uic.loadUi(r'C:\Project\semi_project\Design\2_third_option.ui', self)

        self.complete_btn.clicked.connect(self.create_graph)

        self.df_option = self.parent().df_option

        self.show()

    def create_graph(self):

        self.reject()
        self.plot_graph()

    def plot_graph(self):
        print(self.df_option)
        matplotlib.rcParams['font.family'] = 'Malgun Gothic'
        matplotlib.rcParams['font.size'] = 15 # 글자크기
        matplotlib.rcParams['axes.unicode_minus']=False

        N = self.df_option.shape[0]
        index = np.arange(N) * 5
        index_list = list(range(1, len(self.df_option.columns) + 1))

        w = 0.45

        if len(self.df_option.columns) % 2 == 0:
            for col, x in zip(self.df_option.columns, index_list):
                w_value = None
                if statistics.median(index_list) > x:
                    a = int(statistics.median(index_list)) - x + 1
                    w_value = -(a * w)
                    plt.bar(index + w_value, self.df_option[col], width=w)
                else:
                    b = x - int(statistics.median(index_list))
                    w_value = b * w
                    plt.bar(index + w_value, self.df_option[col], width=w)
                print(w_value)
            plt.legend()
            plt.xticks(index + w/2, self.df_option.index)
            plt.show()
        else:
            for col, x in zip(self.df_option.columns, index_list):
                w_value = None
                if statistics.median(index_list) > x:
                    a = int(statistics.median(index_list)) - x
                    w_value = -(a * w)
                    plt.bar(index + w_value, self.df_option[col], width=w)
                elif x == statistics.median(index_list):
                    w_value = 0
                    plt.bar(index + w_value, self.df_option[col], width=w)
                else:
                    b = x - int(statistics.median(index_list))
                    w_value = b * w
                    plt.bar(index + w_value, self.df_option[col], width=w)
                print(w_value)
            plt.legend()
            plt.xticks(index, self.df_option.index)
            plt.show()

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()

app.exec_()