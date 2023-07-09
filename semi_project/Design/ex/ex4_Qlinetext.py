import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QRadioButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LineEdit 활성화/비활성화 예제")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.line_edit = QLineEdit(self)
        self.line_edit.setDisabled(True)  # 초기에 비활성화 상태로 설정
        self.layout.addWidget(self.line_edit)

        self.radio_button = QRadioButton("활성화", self)
        self.radio_button.toggled.connect(self.toggle_line_edit)
        self.layout.addWidget(self.radio_button)

    def toggle_line_edit(self):
        if self.radio_button.isChecked():
            self.line_edit.setEnabled(True)
        else:
            self.line_edit.setDisabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
