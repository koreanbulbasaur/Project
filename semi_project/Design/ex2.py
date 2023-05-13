import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.windonw_width, self.window_height = 700, 500
        self.resize(self.windonw_width, self.window_height)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.btn = QPushButton(
            '&Retrieve Values', clicked=self.retrieveCheckboxValues)
        self.layout.addWidget(self.btn)

        self.table = QTableWidget(3, 3)
        self.table.setStyleSheet(
            'QAbstractItemVies::indicator {width: 25px; height: 25px;} QTableWidget::item {width: 500px; height:40px;}')
        self.layout.addWidget(self.table)

        for row in range(3):
            for col in range(3):
                if col % 3 == 0:
                    item = QTableWidgetItem('Item {0}-{1}'.format(row, col))
                    item.setFlags(Qt.ItemFlag.ItemIsUserCheckable |
                                  Qt.ItemFlag.ItemIsEnabled)
                    item.setCheckState(Qt.CheckState.Unchecked)
                    self.table.setItem(row, col, item)
                else:
                    self.table.setItem(row, col, QTableWidgetItem(
                        'Item {0}-{1}'.format(row, col)))

    def retrieveCheckboxValues(self):
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).checkState() == Qt.CheckState.Checked:
                print([self.table.item(row, col).text()
                      for col in range(self.table.columnCount())])
        print('-'*100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        Qwidget {
            font-size : 17px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')
