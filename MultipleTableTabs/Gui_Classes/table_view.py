from PyQt5 import QtCore
from Gui.Gui_Utils.create_elements import setup_device_picture
from PyQt5.QtWidgets import *


class TableView(QGroupBox):
    def __init__(self):
        self.central_unit_tab = QTableWidget()
        self.trigger_tab = QTableWidget()
        self.generator_tab = QTableWidget()
        self.device_picture = setup_device_picture()
        super(TableView, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout()

        central_tab = QTabWidget()
        central_tab.addTab(self.central_unit_tab, 'Central unit')
        central_tab.addTab(self.trigger_tab, 'Trigger')
        central_tab.addTab(self.generator_tab, 'Generátor')

        self.set_central_unit_tab()

        layout.addWidget(central_tab, 0, 0)
        layout.addWidget(self.device_picture, 0, 1, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.setFixedSize(960, 540)
        self.setLayout(layout)

    def set_central_unit_tab(self):
        self.central_unit_tab.setColumnCount(3)
        self.central_unit_tab.setHorizontalHeaderLabels(['Název', 'Hodnota', 'Délka(byte)'])
        self.central_unit_tab.setColumnWidth(0, 20 * 8)
        self.central_unit_tab.setColumnWidth(1, 25 * 8)
        self.central_unit_tab.setColumnWidth(2, 11 * 8)
