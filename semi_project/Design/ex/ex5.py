import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.radioButton1 = QRadioButton("Option 1")
        self.radioButton2 = QRadioButton("Option 2")
        self.radioButton3 = QRadioButton("Option 3")

        self.radioButton1.setChecked(True)  # 초기 선택 설정

        layout = QVBoxLayout()
        layout.addWidget(self.radioButton1)
        layout.addWidget(self.radioButton2)
        layout.addWidget(self.radioButton3)

        self.setLayout(layout)

        self.radioButton1.clicked.connect(self.radioButtonClicked)
        self.radioButton2.clicked.connect(self.radioButtonClicked)
        self.radioButton3.clicked.connect(self.radioButtonClicked)

    def radioButtonClicked(self):
        if self.radioButton1.isChecked():
            print("Option 1 선택")
        elif self.radioButton2.isChecked():
            print("Option 2 선택")
        elif self.radioButton3.isChecked():
            print("Option 3 선택")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
