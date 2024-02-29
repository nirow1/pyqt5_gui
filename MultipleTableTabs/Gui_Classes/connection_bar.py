from Gui.Gui_Utils.create_elements import setup_fj_logo
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import re


class ConnectionBar(QGroupBox):
    def __init__(self):
        self.fj_logo = setup_fj_logo()
        self.con_button = QPushButton('Připojit')
        self.ip_range = QLineEdit('formát: 1-255, 255 ')
        super(ConnectionBar, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout()

        finding_ip = QLabel('IP: 192.168.1.')

        self.con_button.setDisabled(True)

        self.ip_range.textChanged.connect(self.validate_text)
        self.ip_range.setFixedWidth(13*8)

        found_ip = QLabel('Nalezená IP: 192.168.1.'+'31')
        found_ip.setFixedWidth(150)

        layout.addWidget(self.con_button, 0, 0)
        layout.addWidget(finding_ip, 0, 1, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.ip_range, 0, 2, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(found_ip, 0, 3, 0, 3, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.fj_logo, 0, 6, 0, 4, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        self.setFixedSize(960, 80)
        self.setLayout(layout)

    def validate_text(self):
        pattern = r"^[1-9]\d{0,2}-[1-9]\d{0,2}$"
        ip_range = self.ip_range.text()

        try:
            if re.match(pattern, ip_range):
                self.con_button.setDisabled(False)
            elif re.match(r"^\d+$", ip_range) is not None and int(ip_range) <= 255:
                self.con_button.setDisabled(False)
            else:
                self.con_button.setDisabled(True)
        except Exception as e:
            print(e)
