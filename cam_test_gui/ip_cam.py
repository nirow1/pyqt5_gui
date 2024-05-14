from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import sys
import cv2
import queue
import threading
import time


class CameraViewer(QMainWindow):
    def __init__(self, camera_ip, username, password):
        super().__init__()
        self.camera_ip = camera_ip
        self.username = username
        self.password = password

        self.setWindowTitle("IP Camera Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.video_label = QLabel(self)
        self.layout.addWidget(self.video_label)
        self.central_widget.setLayout(self.layout)

        # Create a QTimer to capture screenshots every 3 seconds
        self.screenshot_timer = QTimer(self)
        self.screenshot_timer.timeout.connect(self.capture_cam)
        self.screenshot_timer.start(200)  # 3 seconds interval

        self.cam = cv2.VideoCapture(f"rtsp://{self.username}:{self.password}@{self.camera_ip}/1")
        self.cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    def capture_cam(self):
        ret, frame = self.cam.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape

            window_width = self.video_label.width()
            window_height = self.video_label.height()

            aspect_ratio = w / h

            new_w = int(window_width * 0.8)
            new_h = int((new_w / aspect_ratio))

            if new_h > window_height:
                new_h = window_height
                new_w = int(new_h * aspect_ratio)

            resized_frame = cv2.resize(frame, (new_w, new_h))

            bytes_per_line = ch * new_w
            q_image = QImage(resized_frame.data, new_w, new_h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.video_label.setPixmap(pixmap)


if __name__ == "__main__":
    camera_ip = "192.168.1.50"
    username = "admin"
    password = "4Jtech.pristup"

    app = QApplication(sys.argv)
    viewer = CameraViewer(camera_ip, username, password)
    viewer.show()
    sys.exit(app.exec_())
