from TableDatabase.Utils.csv_data_editor import get_people_list
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *


class PeopleView(QtWidgets.QGroupBox):
    def __init__(self):
        self.table_view = QTableWidget()
        super(PeopleView, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.table_view.setColumnCount(5)

        self.table_view.setHorizontalHeaderLabels(['Name', 'Email address', 'Phone Number', 'race', 'X'])
        self.table_view.setColumnWidth(0, 20 * 8)
        self.table_view.setColumnWidth(1, 24 * 8)
        self.table_view.setColumnWidth(2, 13 * 8)
        self.table_view.setColumnWidth(3, 10 * 8)
        self.table_view.setColumnWidth(4, 2 * 8)

        layout = QGridLayout()
        layout.addWidget(self.table_view)
        self.fill_table_view()

        self.setLayout(layout)

    def fill_table_view(self):

        for person in get_people_list():
            row_pos = self.table_view.rowCount()
            self.table_view.insertRow(row_pos)
            for col, data in enumerate(person):
                self.table_view.setItem(row_pos, col, QTableWidgetItem(data))

            x_button = QPushButton("X")
            self.table_view.setCellWidget(row_pos, 4, x_button)

