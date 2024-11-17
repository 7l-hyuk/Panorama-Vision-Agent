import sys
import winsound

import cv2
from PyQt6.QtWidgets import QFileDialog
import numpy as np
from window_ui import BaseButtons


class BasePanorama(BaseButtons):
    def __init__(self):
        super().__init__()
        self.collect_button.clicked.connect(self.collect_function)
        self.show_button.clicked.connect(self.show_function)
        self.stitch_button.clicked.connect(self.stitch_function)
        self.save_button.clicked.connect(self.save_function)
        self.quit_button.clicked.connect(self.quit_function)
        self.save2_button.clicked.connect(self.save)
        self.emboss_button.clicked.connect(self.emboss)
        self.cartoon_button.clicked.connect(self.cartoon)
        self.sketch_button.clicked.connect(self.sketch)
        self.oil_button.clicked.connect(self.oil)

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
        self.img = cv2.imread(fname[0])
        self.emboss_button.setEnabled(True)
        self.cartoon_button.setEnabled(True)
        self.sketch_button.setEnabled(True)
        self.oil_button.setEnabled(True)
        self.pick_combo.setEnabled(True)
        self.save2_button.setEnabled(True)

    def quit_function(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.close()

    def emboss(self):
        femboss = np.array([
            [-1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0]
        ])

        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        gray16 = np.int16(gray)
        self.images["embossing"] = np.uint8(
            np.clip(cv2.filter2D(gray16, -1, femboss) + 128, 0, 255)
        )
        cv2.imshow("Emboss", self.images["embossing"])

    def cartoon(self):
        self.images["cartoon"] = cv2.stylization(
            self.img,
            sigma_s=60,
            sigma_r=0.45
        )
        cv2.imshow("Cartoon", self.images["cartoon"])

    def sketch(self):
        self.images["sketch_gray"], self.images["sketch_color"] = \
            cv2.pencilSketch(
                self.img,
                sigma_s=60,
                sigma_r=0.07,
                shade_factor=0.02
            )
        cv2.imshow("Pencil Sketch(gray)", self.images["sketch_gray"])
        cv2.imshow("Pencil sketch(color)", self.images["sketch_color"])

    def oil(self):
        self.images["oil"] = cv2.xphoto.oilPainting(
            self.img, 10, 1, cv2.COLOR_BGR2Lab
        )
        cv2.imshow("Oil Painting", self.images["oil"])

    def save(self):
        fname = QFileDialog.getSaveFileName(self, "File Save", "./")
        i = self.pick_combo.currentIndex()
        OPTIONS = [
            "embossing",
            "cartoon",
            "sketch_gray",
            "sketch_color",
            "oil"
        ]
        cv2.imwrite(fname[0], self.images[OPTIONS[i]])
