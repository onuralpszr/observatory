from PySide2.QtWidgets import QMainWindow
import cv2 as cv
from dataclasses import dataclass
from ui.ui_MainWindow import Ui_MainWindow
from PySide2 import QtGui
import numpy as np

@dataclass
class Observatory(QMainWindow):
    def __init__(self):
        super(Observatory, self).__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)

        
        self.starry_img: str = cv.samples.findFile("starry_night.jpg")
        self.img: np.ndarray = cv.imread(self.starry_img, cv.IMREAD_UNCHANGED)


        # Open example cv image via QLabel
        self.image = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))

