import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LineEdit 활성화/비활성화 예제")
        self.setGeometry(100, 100, 300, 200)

        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(50, 50, 200, 30)
        self.line_edit.setDisabled(True)  # 초기에 비활성화 상태로 설정

        self.button = QPushButton("활성화", self)
        self.button.setGeometry(50, 100, 200, 30)
        self.button.clicked.connect(self.toggle_line_edit)

    def toggle_line_edit(self):
        if self.line_edit.isEnabled():
            self.line_edit.setDisabled(True)
            self.button.setText("활성화")
        else:
            self.line_edit.setEnabled(True)
            self.button.setText("비활성화")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
