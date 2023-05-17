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

form_class = uic.loadUiType(r'semi_project\Design\4\3_Main.ui')[0]


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
        uic.loadUi(r'semi_project\Design\4\3_first_option.ui', self)

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
        uic.loadUi(r'semi_project\Design\4\3_second_option.ui', self)

        self.table = self.table

        self.df_option = None

        self.second_next_btn.clicked.connect(self.thirdwindow)

        self.header_Index = int(header_Index)
        self.index_Col = int(index_Col)

        self.data = data

        if data.endswith('.csv'):
            self.df = pd.read_csv(data)
        elif data.endswith('.xlsx'):
            self.df = pd.read_excel(data, index_col=self.index_Col, header=self.header_Index)

        row_count = len(self.df) + 1
        col_count = len(self.df.columns) + 1

        self.table.setRowCount(row_count)
        self.table.setColumnCount(col_count)

        for row in range(row_count):
            for col in range(col_count):
                if row == 0 and col == 0:
                    self.df.index = self.df.index.astype('object')
                    item = QTableWidgetItem(str(self.df.index.name))
                    self.table.setItem(row, col, item)
                elif row == 0:
                    item = QTableWidgetItem(str(self.df.columns[col-1]))
                    item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    item.setCheckState(Qt.CheckState.Checked)
                    self.table.setItem(row, col, item)
                elif col == 0:
                    item = QTableWidgetItem(str(self.df.index[row-1]))
                    item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    item.setCheckState(Qt.CheckState.Checked)
                    self.table.setItem(row, col, item)
                else:
                    self.df.index = self.df.index.astype('object')
                    item = QTableWidgetItem(str(self.df.iloc[row-1, col-1]))
                    self.table.setItem(row, col, item)

        self.show()

    def thirdwindow(self):
        row_list = []
        col_list = []

        row_index = 0
        col_index = 0

        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).checkState() == Qt.CheckState.Checked:
                row_index += 1

        for col in range(self.table.columnCount()):
            if self.table.item(0, col).checkState() == Qt.CheckState.Checked:
                col_index += 1

        if row_index != 0 and col_index != 0:
            for row in range(self.table.rowCount()):
                if self.table.item(row, 0).checkState() == Qt.CheckState.Checked:
                    row_list.append(row-1)

            for col in range(self.table.columnCount()):
                if self.table.item(0, col).checkState() == Qt.CheckState.Checked:
                    col_list.append(col-1)

            self.df_option = self.df.iloc[row_list, col_list]

            self.reject()
            ThirdOption(self)
        else:
            pass

class ThirdOption(QDialog):
    def __init__(self, parent):
        super(ThirdOption, self).__init__(parent)
        uic.loadUi(r'semi_project\Design\4\3_third_option.ui', self)

        self.df_option = self.parent().df_option

        self.complete_btn.clicked.connect(self.create_graph)
        self.mean_radio.toggled.connect(self.mean_radio_clicked)
        self.sum_radio.toggled.connect(self.sum_radio_clicked)
        self.another_radio.toggled.connect(self.radioButton_clicked)

        self.show()

    def create_graph(self):
        # self.plot_graph()

        if self.mean_radio.isChecked():
            pass
        elif self.sum_radio.isChecked():
            print('sum_radio_checked')
            df = self.Sum_Df()
            self.plot_graph(df)
        elif self.another_radio.isChecked():
            pass
        else:
            pass
        self.reject()


    def Sum_Df(self):
        df_sum = self.df_option.sum(axis=1)
        df_sum['합계'] = df_sum.sum()
        print(df_sum)
        return df_sum

    def mean_radio_clicked(self):
        if self.another_text.isEnabled():
            self.another_text.setDisabled(True)

    def sum_radio_clicked(self):
        if self.another_text.isEnabled():
            self.another_text.setDisabled(True)

    def radioButton_clicked(self):
        if self.another_radio.isEnabled():
            self.another_text.setEnabled(True)
        else:
            self.another_text.setDisabled(True)

    def plot_graph(self, df):
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
            plt.legend()
            plt.xticks(index, self.df_option.index)
            plt.show()

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()

app.exec_()