from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout


class FirstDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.second_dialog = None

        layout = QVBoxLayout()

        button = QPushButton('Open Second Dialog')
        button.clicked.connect(self.open_second_dialog)
        layout.addWidget(button)

        self.setLayout(layout)

    def open_second_dialog(self):
        self.second_dialog = SecondDialog(self)
        self.second_dialog.show()
        self.reject()


class SecondDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        button = QPushButton('Close')
        button.clicked.connect(self.close)
        layout.addWidget(button)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])

    first_dialog = FirstDialog()
    first_dialog.show()

    app.exec_()
