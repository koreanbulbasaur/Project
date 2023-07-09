import os
import sys
from time import sleep

from PyQt5.QtWidgets import *
from PyQt5 import uic

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('211012.ui')
form_class = uic.loadUiType(form)[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_test.clicked.connect(self.progress_loading)

    def progress_loading(self):
        for i in range(101):                        # 1~100 까지
            self.progress.setValue(i)               # i 증가
            sleep(0.1)                              # 0.1초마다 수행
        self.msg_box()

    def msg_box(self):
        msg = QMessageBox()                         # msg 변수에 msgbox 할당
        msg.setWindowTitle("테스트용")               # 제목설정
        msg.setText('완료')                          # 내용설정
        msg.exec_()                                 # 메세지박스 실행

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()