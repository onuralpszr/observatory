from dataclasses import dataclass

import cv2 as cv
import numpy as np
from PySide2 import QtGui
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QMainWindow

from ui.ui_MainWindow import Ui_MainWindow


@dataclass
class Observatory(QMainWindow):
    def __init__(self):
        super(Observatory, self).__init__()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menuOpen_File.triggered.connect(self.image_select)
        self.ui.menuBar.setNativeMenuBar(False)

    def image_select(self) -> None:
        image_filename, _ = QFileDialog.getOpenFileName(self, self.tr("Load Image"), self.tr("~/"),
                                                        self.tr("Images (*.jpg)"))
        self.cv_reader(image_filename)

    def cv_reader(self, image_filename) -> None:
        """ Opening Image file and read with opencv """

        self.img = cv.imread(image_filename, cv.IMREAD_UNCHANGED)
        self.image = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0],
                                  QtGui.QImage.Format_RGB888).rgbSwapped()
        self.ui.image_frame.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.cv_gray_scale(image_filename=image_filename)

    def cv_gray_scale(self,image_filename):
        self.img = cv.imread(image_filename, cv.IMREAD_GRAYSCALE)
        self.image = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0],
                                  QtGui.QImage.Format_Grayscale8).rgbSwapped()
        self.ui.image_frame_after.setPixmap(QtGui.QPixmap.fromImage(self.image))

