import sys
import winsound

import cv2
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QLabel,
    QFileDialog
)
import numpy as np


class Panorama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panorama Video")
        self.setGeometry(200, 200, 700, 200)

        collect_button = QPushButton("collect", self)
        collect_button.setGeometry(10, 25, 100, 30)
        collect_button.clicked.connect(self.collect_function)

        self.show_button = QPushButton("show", self)
        self.show_button.setGeometry(110, 25, 100, 30)
        self.show_button.setEnabled(False)
        self.show_button.clicked.connect(self.show_function)

        self.stitch_button = QPushButton("stitch", self)
        self.stitch_button.setGeometry(210, 25, 100, 30)
        self.stitch_button.setEnabled(False)
        self.stitch_button.clicked.connect(self.stitch_function)

        self.save_button = QPushButton("save", self)
        self.save_button.setGeometry(310, 25, 100, 30)
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_function)

        quit_button = QPushButton("quit", self)
        quit_button.setGeometry(450, 25, 100, 30)
        quit_button.clicked.connect(self.quit_function)

        self.label = QLabel("Welcome!", self)
        self.label.setGeometry(10, 70, 600, 170)

    def collect_function(self):
        self.show_button.setEnabled(False)
        self.stitch_button.setEnabled(False)
        self.save_button.setEnabled(False)
        self.label.setText("C: collect, Q: quit video")

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            sys.exit("Camera Connection Failed!")

        self.imgs = []
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            cv2.imshow("Video Display", frame)

            key = cv2.waitKey(1)
            if key == ord("c"):
                self.imgs.append(frame)
            elif key == ord("q"):
                self.cap.release()
                cv2.destroyWindow("Video Display")
                break

        if len(self.imgs) >= 2:
            self.show_button.setEnabled(True)
            self.stitch_button.setEnabled(True)
            self.save_button.setEnabled(True)

    def show_function(self):
        self.label.setText(f"Collected Video: {len(self.imgs)} photos")
        stack = cv2.resize(self.imgs[0], dsize=(0, 0), fx=0.25, fy=0.25)
        for i in range(1, len(self.imgs)):
            stack = np.hstack((
                stack,
                cv2.resize(self.imgs[i], dsize=(0, 0), fx=0.25, fy=0.25)
            ))
        cv2.imshow("Image Collection", stack)

    def stitch_function(self):
        stitcher = cv2.Stitcher.create()
        status, self.img_stitched = stitcher.stitch(self.imgs)
        if status == cv2.STITCHER_OK:
            cv2.imshow("Image Stitched Panorama", self.img_stitched)
        else:
            winsound.Beep(3000, 500)
            self.label.setText("Panorama Creation Failed! (Please Retry...)")

    def save_function(self):
        fname = QFileDialog.getSaveFileName(self, "Save File", "./")
        cv2.imwrite(fname[0], self.img_stitched)

    def quit_function(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Panorama()
    win.show()
    app.exec()
