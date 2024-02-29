from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


def setup_fj_logo():
    fj_logo = QtGui.QPixmap(
        'C:\\Users\\Radan Krch\\Desktop\\github_projects\\get_eep_controll\\Pictures\\4j_logo_150x50.png')
    fj_logo_label = QLabel()
    fj_logo_label.setPixmap(fj_logo)
    fj_logo_label.resize(fj_logo.width(), fj_logo.height())
    return fj_logo_label


def setup_device_picture():
    fj_logo = QtGui.QPixmap(
        'C:\\Users\\Radan Krch\\Desktop\\github_projects\\get_eep_controll\\Pictures\\device_resized.png')
    fj_logo_label = QLabel()
    fj_logo_label.setPixmap(fj_logo)
    fj_logo_label.resize(fj_logo.width(), fj_logo.height())
    return fj_logo_label
