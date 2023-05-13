import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r'C:\Project\PYQT_study\4_get_file.ui')[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ui에 있는 메뉴와 활성화
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)

    def openFunction(self):
        # 윈도우에서 제공하는 파일열기
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]:
            # 파일을 가져와서 notepad에 출력
            with open(fname[0], encoding='UTF8') as f:
                data = f.read()
            self.plainTextEdit.setPlainText(data)

            # 파일 위치 출력
            print(f'open {fname[0]}')


    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self)
        if fname[0]:
            save_data = self.plainTextEdit.toPlainText()
            with open(fname[0], 'w', encoding='UTF8') as f:
                f.write(save_data)

            print(f'open {fname[0]}')


app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()
