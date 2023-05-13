import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple PyQt5 Example')

        vbox = QVBoxLayout()

        self.label = QLabel('Hello, Wrtn!')
        vbox.addWidget(self.label)

        self.edit = QLineEdit()
        vbox.addWidget(self.edit)

        self.button = QPushButton('Change Text')
        self.button.clicked.connect(self.change_label_text)
        vbox.addWidget(self.button)

        container = QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)

    def change_label_text(self):
        text = self.edit.text()
        self.label.setText(text)


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
