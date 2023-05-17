import sys
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import statistics
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from time import *
from ssl import Options

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
            QMessageBox.warning(self, 'file 이름 없음', 'file을 추가해주세요')
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
        else:
            QMessageBox.warning(self, '값 없음', '값을 입력해주세요')

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
            QMessageBox.warning(self, '못 넘어감', '체크 해주세요')


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
        if self.mean_radio.isChecked():
            df = self.Mean_Df()
            self.create_bar_graph(df)
            self.reject()
        elif self.sum_radio.isChecked():
            df = self.Sum_Df()
            self.create_bar_graph(df)
            self.reject()
        elif self.another_radio.isChecked():
            link = self.another_text.text()
            if link != None:
                df_denominator = self.Sum_Df(self.df_option)
                df_numerator = self.Get_Df(link)
                df = self.Div_Df(df_denominator, df_numerator)
                self.create_bar_graph(df)
                self.reject()
        else:
            QMessageBox.warning(self, 'link 없음', 'url을 넣어주세요')

    def Sum_Df(self, df):
        df_sum = df.sum(axis=1)
        df_sum = pd.DataFrame(df_sum, columns=['합계'])
        df_sum.index.name = df.index.name
        return df_sum
    
    def Mean_Df(self):
        df_mean = self.df_option.mean(axis=1)
        df_mean = pd.DataFrame(df_mean, columns=['평균'])
        df_mean.index.name = self.df_option.index.name
        return df_mean
    
    def Div_Df(self, df1, df2):
        text_col = '계산'

        df1 = df1.astype(float)
        df2 = df2.astype(float)

        df1.columns = [text_col]
        df2.columns = [text_col]

        df1 = df1.reindex(df2.index)

        df3 = df2 / df1
        return df3

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

    def create_bar_graph(self, df):
        # print(df)
        matplotlib.rcParams['font.family'] = 'Malgun Gothic'
        matplotlib.rcParams['font.size'] = 15 # 글자크기
        matplotlib.rcParams['axes.unicode_minus']=False

        N = df.shape[0]
        index = np.arange(N) * 5
        index_list = list(range(1, len(df.columns) + 1))

        w = 0.45
        rotation = 30

        if len(df.columns) % 2 == 0:
            for col, x in zip(df.columns, index_list):
                w_value = None
                if statistics.median(index_list) > x:
                    a = int(statistics.median(index_list)) - x + 1
                    w_value = -(a * w)
                    plt.bar(index + w_value, df[col], width=w)
                else:
                    b = x - int(statistics.median(index_list))
                    w_value = b * w
                    plt.bar(index + w_value, df[col], width=w)
            plt.legend()
            plt.xticks(index + w/2, df.index, rotation=rotation)
            plt.tight_layout()
            plt.show()
        else:
            for col, x in zip(df.columns, index_list):
                w_value = None
                if statistics.median(index_list) > x:
                    a = int(statistics.median(index_list)) - x
                    w_value = -(a * w)
                    plt.bar(index + w_value, df[col], width=w)
                elif x == statistics.median(index_list):
                    w_value = 0
                    plt.bar(index + w_value, df[col], width=w)
                else:
                    b = x - int(statistics.median(index_list))
                    w_value = b * w
                    plt.bar(index + w_value, df[col], width=w)
            plt.legend()
            plt.xticks(index, df.index, rotation=rotation)
            plt.tight_layout()
            plt.show()

    def Get_Df(self, link):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("window-size=1920x1080")

        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        # url = 'https://jumin.mois.go.kr/'
        url = link

        sleep(1)
        browser.get(url)

        iframe = browser.find_element(By.TAG_NAME, "iframe")
        browser.switch_to.default_content()
        browser.switch_to.frame(iframe)

        iframe_source = browser.page_source

        soup = BeautifulSoup(iframe_source, features="html.parser")


        def select_option(InputValue1, InputValue2):
            select_element = Select(browser.find_element(By.ID, InputValue1))
            options = select_element.options

            for option in options:
                if option.get_attribute("value") == InputValue2:
                    option.click()
                    break

        select_option("searchYearStart", "2022")
        select_option("searchMonthStart","12")
        select_option("searchYearEnd","2022")
        select_option("searchMonthEnd","12")

        button_element = browser.find_element(By.CLASS_NAME,'btn_search')
        button_element.click()

        series = []
        cols = []

        tmp = soup.find('div',class_='dataTables_scrollBody').find('tbody')
        for i in tmp.findAll('tr'):
            tmplist = []
            tmplist.append(i.find('td',class_='td_admin th1').get_text())
            for j in i.findAll('td',class_=''):
                readData = j.get_text().replace(" ", "")
                tmplist.append(readData.replace(",", ""))
            series.append(tmplist)

        for i in soup.findAll('div',class_='dataTables_sizing'):
            cols.append(i.get_text().replace(" ", ""))

        del cols[0]
        del cols[1]

        df_get = pd.DataFrame(series)
        df_get.columns = cols

        df_get = df_get.set_index('행정기관')
        df_Edit = df_get.loc[:,['총인구수']]

        df_Edit['총인구수'] = df_Edit['총인구수'].astype('int')
        df_delete = df_Edit.drop(df_Edit.index[0])
        print(df_delete)
        df_delete.to_excel('sample.xlsx')
        browser.quit()
        return df_delete

app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()

app.exec_()