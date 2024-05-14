import time
import cv2
import queue
from threading import Thread


class VideoScreenshot(object):
    def __init__(self, src: str):
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)

        # Take screenshot every x seconds
        self.screenshot_interval = 5

        # Default resolutions of the frame are obtained (system dependent)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def show_frame(self):
        # Display frames in main program
        if self.status:
            cv2.imshow('frame', self.frame)

        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        # Save obtained frame periodically
        self.frame_count = 0
        def save_frame_thread():
            while True:
                try:
                    cv2.imwrite('./frame.png', self.frame)
                    self.frame_count += 1
                    time.sleep(self.screenshot_interval)
                except AttributeError:
                    pass
        Thread(target=save_frame_thread, args=()).start()


if __name__ == '__main__':
    rtsp_stream_link = f"rtsp://admin:4Jtech.pristup@192.168.1.50/1"
    video_stream_widget = VideoScreenshot(rtsp_stream_link)
    video_stream_widget.save_frame()

