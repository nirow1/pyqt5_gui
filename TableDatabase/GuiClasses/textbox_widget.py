from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *


class TextBoxesGroupbox(QtWidgets.QGroupBox):
    ALL_TXT_FILLED = QtCore.pyqtSignal(bool)

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

        #for textbox in self.text_boxes:
            #textbox.editingFinished.connect(self.validate_text_boxes)
        self.setFixedWidth(450)
        self.setLayout(layout)

    def validate_text_boxes(self):
        if all(textbox.text() for textbox in self.textboxes):
            print('working')
            self.emit_all_textboxes_filled()

    def emit_all_text_boxes_filled(self):
        self.ALL_TXT_FILLED.emit(True)
