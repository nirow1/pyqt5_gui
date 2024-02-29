from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal


class TextBoxesGroupbox(QGroupBox):
    TEXT_FILLED = pyqtSignal(bool)

    def __init__(self):
        self.text_boxes = []
        super(TextBoxesGroupbox, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout()

        tile_list = ["Name:", "Email address:", "Phone number:", "Race:"]
        for tile in tile_list:
            tile_textbox = QLineEdit()
            tile_textbox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.text_boxes.append(tile_textbox)

        for row, (label, textbox) in enumerate(zip(tile_list, self.text_boxes)):
            lbl = QLabel(label)
            lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
            layout.addWidget(lbl, row, 0)
            layout.addWidget(textbox, row, 1)

        for textbox in self.text_boxes:
            textbox.textChanged.connect(self.validate_text_boxes)

        self.setFixedWidth(450)
        self.setFixedHeight(500)
        self.setLayout(layout)

    def validate_text_boxes(self):
        var = all(textbox.text() for textbox in self.text_boxes)
        self.TEXT_FILLED.emit(var)
