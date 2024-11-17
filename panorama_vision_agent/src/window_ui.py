from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QLabel,
    QComboBox
)


class BaseButtons(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Panorama Video")
        self.setGeometry(200, 200, 1000, 1000)

        self.collect_button = QPushButton("collect", self)
        self.collect_button.setGeometry(10, 25, 100, 30)

        self.show_button = QPushButton("show", self)
        self.show_button.setGeometry(110, 25, 100, 30)
        self.show_button.setEnabled(False)

        self.stitch_button = QPushButton("stitch", self)
        self.stitch_button.setGeometry(210, 25, 100, 30)
        self.stitch_button.setEnabled(False)

        self.save_button = QPushButton("save", self)
        self.save_button.setGeometry(310, 25, 100, 30)
        self.save_button.setEnabled(False)

        self.quit_button = QPushButton("quit", self)
        self.quit_button.setGeometry(450, 25, 100, 30)

        self.emboss_button = QPushButton("embossing", self)
        self.emboss_button.setGeometry(10, 70, 100, 30)
        self.emboss_button.setEnabled(False)

        self.cartoon_button = QPushButton("cartoon", self)
        self.cartoon_button.setGeometry(110, 70, 100, 30)
        self.cartoon_button.setEnabled(False)

        self.sketch_button = QPushButton("pencil sketch", self)
        self.sketch_button.setGeometry(210, 70, 100, 30)
        self.sketch_button.setEnabled(False)

        self.oil_button = QPushButton("oil", self)
        self.oil_button.setGeometry(310, 70, 100, 30)
        self.oil_button.setEnabled(False)

        self.pick_combo = QComboBox(self)
        self.pick_combo.addItems(
            ["embossing", "cartoon", "sketch(gray)", "sketch(coloer)", "oil"]
        )
        self.pick_combo.setGeometry(410, 70, 110, 30)
        self.pick_combo.setEnabled(False)

        self.save2_button = QPushButton("save", self)
        self.save2_button.setGeometry(520, 70, 100, 30)
        self.save2_button.setEnabled(False)

        self.images = dict()

        self.label = QLabel("Welcome!", self)
        self.label.setGeometry(10, 100, 600, 170)
