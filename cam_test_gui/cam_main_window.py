from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PySide2.QtGui import QImage,QPixmap
import cv2
import sys
import time



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 1200)
        self.setStyleSheet("background: lightgrey;")
        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            sys.exit()

        self.status = QStatusBar()
        self.status.setStyleSheet("background: white;")
        self.setStatusBar(self.status)

        self.save_path = ""
        self.viewfinder = QCameraViewfinder()
        self.viewfinder.show()
        self.setCentralWidget(self.viewfinder)

        self.select_camera(0)

        toolbar = QToolBar("Camera Tool Bar")
        self.addToolBar(toolbar)

        click_action = QAction("Click photo", self)
        click_action.setStatusTip("Capture a picture")
        click_action.setToolTip("Capture picture")
        toolbar.addAction(click_action)

        change_folder_action = QAction("Change save location", self)
        change_folder_action.setStatusTip("Change the folder where pictures will be saved.")
        change_folder_action.setToolTip("Change save location")
        toolbar.addAction(change_folder_action)

        camera_selector = QComboBox()
        camera_selector.setStatusTip("Choose a camera to take pictures")
        camera_selector.setToolTip("Select Camera")
        camera_selector.setToolTipDuration(2500)

    def select_camera(self, index):
        self.camera = QCamera(self.available_cameras[index])

        # setting view finder to the camera
        self.camera.setViewfinder(self.viewfinder)

        # setting capture mode to the camera
        self.camera.setCaptureMode(QCamera.CaptureStillImage)

        # if any error occur show the alert
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))

        # start the camera
        self.camera.start()

        # creating a QCameraImageCapture object
        self.capture = QCameraImageCapture(self.camera)

        # showing alert if error occur
        self.capture.error.connect(lambda error_msg, error,
                                          msg: self.alert(msg))

        # when image captured showing message
        self.capture.imageCaptured.connect(lambda d,
                                                  i: self.status.showMessage("Image captured : "
                                                                             + str(self.save_seq)))

        # getting current camera name
        self.current_camera_name = self.available_cameras[index].description()

        # initial save sequence
        self.save_seq = 0

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.video_label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
