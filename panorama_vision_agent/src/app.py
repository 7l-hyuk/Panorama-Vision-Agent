import sys
from PyQt6.QtWidgets import QApplication
from panorama_vision_agent.src.panorama import BasePanorama


class MainPanorama(BasePanorama):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainPanorama()
    win.show()
    app.exec()
