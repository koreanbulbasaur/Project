import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r'C:\Project\PYQT_study\6_close.ui')[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ui에 있는 메뉴와 활성화
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveas.triggered.connect(self.saveAsFunction)
        self.action_close.triggered.connect(self.close)

        self.opened = False
        self.opened_file_path = ''

    def CloseEvent(self, event):
        pass

    def save_file(self, fname):
        save_data = self.plainTextEdit.toPlainText()

        with open(fname, 'w', encoding='UTF8') as f:
            f.write(save_data)

        print(f'open {fname}')

    def open_file(self, fname):
        with open(fname, encoding='UTF8') as f:
            data = f.read()
        self.plainTextEdit.setPlainText(data)

        self.opened = True
        self.opened_file_path = fname

        # 파일 위치 출력
        print(f'open {fname}')

    def openFunction(self):
        # 윈도우에서 제공하는 파일열기
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            self.open_file(fname[0])


    def saveFunction(self):
        if self.opened:
            self.save_file(self.opened_file_path)
        else:
            self.saveAsFunction()

    def saveAsFunction(self):
        fname = QFileDialog.getSaveFileName(self)
        if fname[0]:
            self.save_file(fname[0])


app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()
