from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

def show_message_box():
    msg_box = QMessageBox()
    msg_box.setText("알림")
    msg_box.setInformativeText("이것은 메시지 박스입니다.")
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)
    msg_box.exec_()

app = QApplication([])
window = QMainWindow()

button = QPushButton("메시지 박스 열기")
button.clicked.connect(show_message_box)
window.setCentralWidget(button)

window.show()
app.exec_()
