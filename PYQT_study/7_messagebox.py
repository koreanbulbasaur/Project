import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType(r'C:\Project\PYQT_study\7_messagebox.ui')[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ui에 있는 메뉴와 활성화
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveas.triggered.connect(self.saveAsFunction)
        self.action_close.triggered.connect(self.closeEvent)

        self.opened = False
        self.opened_file_path = '제목 없음'

    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText(f'변경 내용을 {self.opened_file_path}에 저장하시겠습니까?')
        msgBox.addButton('저장', QMessageBox.YesRole)
        msgBox.addButton('저장 안 함', QMessageBox.NoRole)
        msgBox.addButton('취소', QMessageBox.RejectRole)
        ret = msgBox.exec_()
        if ret == 2:
            return ret

    def closeEvent(self, event):
        ret = self.save_changed_data()
        if ret == 2:
            event.ignore()
        print('close')

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
