# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowOWisXG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1164, 650)
        MainWindow.setMinimumSize(QSize(1000, 650))
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setEnabled(False)
        self.actionSaveAs = QAction(MainWindow)
        self.actionSaveAs.setObjectName(u"actionSaveAs")
        self.actionSaveAs.setEnabled(False)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_frame = QLabel(self.centralwidget)
        self.image_frame.setObjectName(u"image_frame")

        self.horizontalLayout.addWidget(self.image_frame)

        self.image_frame_after = QLabel(self.centralwidget)
        self.image_frame_after.setObjectName(u"image_frame_after")

        self.horizontalLayout.addWidget(self.image_frame_after)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1164, 30))
        self.menuOpen_File = QMenu(self.menuBar)
        self.menuOpen_File.setObjectName(u"menuOpen_File")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuOpen_File.menuAction())
        self.menuOpen_File.addAction(self.actionOpen_File)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"Dosya A\u00e7", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Kaydet", None))
        self.actionSaveAs.setText(QCoreApplication.translate("MainWindow", u"Farkl\u0131 Kaydet", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Dosya Kapat", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"Yeni Dosya", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.image_frame.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.image_frame_after.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuOpen_File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

