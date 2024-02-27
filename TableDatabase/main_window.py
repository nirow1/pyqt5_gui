from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *
from GuiClasses.textbox_widget import TextBoxesGroupbox
from GuiClasses.table_view import PeopleView
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        self.table = PeopleView()
        super(MainWindow, self).__init__()
        self.setGeometry(450, 200, 1100, 700)
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        save_button = QPushButton("Save")
        save_button.setFixedSize(150, 50)
        update_button = QPushButton("Update")
        update_button.setFixedSize(150, 50)



        text_boxes = TextBoxesGroupbox()
        text_boxes.setFixedHeight(500)

        # Place buttons in specific grid cells
        layout.addWidget(text_boxes, 0, 0)
        layout.addWidget(save_button, 1, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(update_button, 2, 0, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.table, 0, 1, 3, 1)

    def on_add_person(self, person):
        self.table.append_person(person)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
