import sys
from Gui_Classes.connection_bar import ConnectionBar
from Gui_Classes.table_view import TableView
from Gui_Classes.device_controll import DeviceControl
from PyQt5.QtWidgets import *


class SJMainWindow(QMainWindow):
    def __init__(self):
        self.connection_bar = ConnectionBar()
        self.table_view = TableView()
        self.device_control = DeviceControl()
        super(SJMainWindow, self).__init__()
        self.setMinimumSize(1100, 730)
        self.setWindowTitle('Nastavení servisní jednotky')
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        layout = QGridLayout(central_widget)

        layout.addWidget(self.connection_bar, 0, 0)
        layout.addWidget(self.table_view, 1, 0)
        layout.addWidget(self.device_control, 2, 0)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SJMainWindow()
    win.show()
    sys.exit(app.exec_())
