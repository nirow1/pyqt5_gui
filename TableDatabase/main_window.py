from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from GuiClasses.textbox_widget import TextBoxesGroupbox
from GuiClasses.table_view import PeopleView
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        self.save_button = QPushButton("Save")
        self.update_button = QPushButton("Update")
        self.table = PeopleView()
        self.text_boxes = TextBoxesGroupbox()
        self.text_boxes.TEXT_FILLED.connect(self.all_textboxes_filled)
        super(MainWindow, self).__init__()
        self.setGeometry(450, 200, 1100, 700)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        self.save_button.setDisabled(True)
        self.save_button.setFixedSize(150, 50)
        self.update_button.setFixedSize(150, 50)

        layout.addWidget(self.text_boxes, 0, 0)
        layout.addWidget(self.save_button, 1, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.update_button, 2, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.table, 0, 1, 3, 1)

    def all_textboxes_filled(self, is_filled):
        self.save_button.setDisabled(not is_filled)

    def on_add_person(self, person):
        self.table.append_person(person)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
