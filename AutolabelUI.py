# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutolabelUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLoadModel_4K = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadModel_4K.setGeometry(QtCore.QRect(350, 70, 101, 41))
        self.btnLoadModel_4K.setObjectName("btnLoadModel_4K")
        self.btnAutoLabel = QtWidgets.QPushButton(self.centralwidget)
        self.btnAutoLabel.setGeometry(QtCore.QRect(350, 300, 101, 41))
        self.btnAutoLabel.setObjectName("btnAutoLabel")
        self.btnLoadModel_Hot = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadModel_Hot.setGeometry(QtCore.QRect(350, 120, 101, 41))
        self.btnLoadModel_Hot.setObjectName("btnLoadModel_Hot")
        self.listImg = QtWidgets.QListWidget(self.centralwidget)
        self.listImg.setGeometry(QtCore.QRect(60, 70, 231, 571))
        self.listImg.setObjectName("listImg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 61, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(350, 170, 101, 80))
        self.groupBox.setObjectName("groupBox")
        self.rdn4K = QtWidgets.QRadioButton(self.groupBox)
        self.rdn4K.setGeometry(QtCore.QRect(10, 20, 83, 16))
        self.rdn4K.setObjectName("rdn4K")
        self.rdnHot = QtWidgets.QRadioButton(self.groupBox)
        self.rdnHot.setGeometry(QtCore.QRect(10, 50, 83, 16))
        self.rdnHot.setObjectName("rdnHot")
        self.listLog = QtWidgets.QListWidget(self.centralwidget)
        self.listLog.setGeometry(QtCore.QRect(300, 370, 201, 271))
        self.listLog.setObjectName("listLog")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 340, 61, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 30, 61, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.listTxt = QtWidgets.QListWidget(self.centralwidget)
        self.listTxt.setGeometry(QtCore.QRect(510, 70, 231, 571))
        self.listTxt.setObjectName("listTxt")
        self.btnAutoLabel_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAutoLabel_2.setGeometry(QtCore.QRect(350, 250, 101, 41))
        self.btnAutoLabel_2.setObjectName("btnAutoLabel_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLoadModel_4K.setText(_translate("MainWindow", "模型1載入"))
        self.btnAutoLabel.setText(_translate("MainWindow", "開始自動標註"))
        self.btnLoadModel_Hot.setText(_translate("MainWindow", "模型2載入"))
        self.label.setText(_translate("MainWindow", "影像清單"))
        self.groupBox.setTitle(_translate("MainWindow", "標記選擇"))
        self.rdn4K.setText(_translate("MainWindow", "模型1"))
        self.rdnHot.setText(_translate("MainWindow", "模型2"))
        self.label_2.setText(_translate("MainWindow", "Log"))
        self.label_3.setText(_translate("MainWindow", "已完成清單"))
        self.btnAutoLabel_2.setText(_translate("MainWindow", "Open Imgs Folder"))

