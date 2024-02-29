from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class DeviceControl(QGroupBox):
    def __init__(self):
        self.read_button = QPushButton('Vyčti EEPROM')
        self.write_button = QPushButton('Zapiš EEPROM')
        self.export_button = QPushButton('Exportovat EEPROM')
        self.save_location = QLineEdit('Cíl ukládání zajete sem(absolutní cesta)')
        super(DeviceControl, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget(self)
        layout = QGridLayout(central_widget)

        self.save_location.setFixedWidth(450)
        self.write_button.setDisabled(True)
        self.read_button.setDisabled(True)
        self.export_button.setDisabled(True)

        layout.addWidget(self.read_button, 0, 0)
        layout.addWidget(self.write_button, 0, 1)
        layout.addWidget(self.export_button, 0, 2)
        layout.addWidget(self.save_location, 0, 3)

        self.setFixedSize(960, 80)
        self.setLayout(layout)
