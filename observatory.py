from PySide2.QtWidgets import QMainWindow
import cv2 as cv
from dataclasses import dataclass
from ui.ui_MainWindow import Ui_MainWindow


@dataclass
class Observatory(QMainWindow):
    def __init__(self):
        super(Observatory, self).__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
