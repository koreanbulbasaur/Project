from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QCheckBox, QWidget, QHBoxLayout
import sys
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.table_widget = QTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.table_widget.setRowCount(4)
        self.table_widget.setHorizontalHeaderLabels(['index', 'a', 'c'])
        self.table_widget.setColumnCount(3)

        for row in range(4):
            for column in range(3):
                # 첫 번째 열에만 체크박스를 추가합니다.
                if column == 0:
                    checkbox_widget = QWidget()
                    checkbox = QCheckBox()
                    layout = QHBoxLayout(checkbox_widget)
                    layout.addWidget(checkbox)
                    layout.setAlignment(Qt.AlignCenter)
                    layout.setContentsMargins(0, 0, 0, 0)

                    self.table_widget.setCellWidget(row, column, checkbox_widget)
                else:
                    item = QTableWidgetItem(f"Item {row}, {column}")
                    self.table_widget.setCellWidget(row, column, checkbox_widget)
                    self.table_widget.setItem(row, column, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())