# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午6:08
# @Author  : Lincvic
# @Email   : lincvic@yahoo.com
# @File    : mainwindow.py
# @SoftwareName: PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 486)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.num1_box = QtWidgets.QTextEdit(self.centralWidget)
        self.num1_box.setGeometry(QtCore.QRect(110, 30, 151, 31))
        self.num1_box.setObjectName("num1_box")
        self.num1_label = QtWidgets.QLabel(self.centralWidget)
        self.num1_label.setGeometry(QtCore.QRect(50, 40, 41, 21))
        self.num1_label.setObjectName("num1_label")
        self.num2_box = QtWidgets.QTextEdit(self.centralWidget)
        self.num2_box.setGeometry(QtCore.QRect(110, 90, 151, 31))
        self.num2_box.setObjectName("num2_box")
        self.num2_label = QtWidgets.QLabel(self.centralWidget)
        self.num2_label.setGeometry(QtCore.QRect(50, 100, 41, 21))
        self.num2_label.setObjectName("num2_label")
        self.TODO_label = QtWidgets.QLabel(self.centralWidget)
        self.TODO_label.setGeometry(QtCore.QRect(50, 150, 41, 21))
        self.TODO_label.setObjectName("TODO_label")
        self.plus_Button = QtWidgets.QRadioButton(self.centralWidget)
        self.plus_Button.setGeometry(QtCore.QRect(110, 150, 31, 20))
        self.plus_Button.setObjectName("plus_Button")
        self.minus_Button = QtWidgets.QRadioButton(self.centralWidget)
        self.minus_Button.setGeometry(QtCore.QRect(150, 150, 31, 20))
        self.minus_Button.setObjectName("minus_Button")
        self.multiply_Button = QtWidgets.QRadioButton(self.centralWidget)
        self.multiply_Button.setGeometry(QtCore.QRect(190, 150, 31, 20))
        self.multiply_Button.setObjectName("multiply_Button")
        self.divide_Button = QtWidgets.QRadioButton(self.centralWidget)
        self.divide_Button.setGeometry(QtCore.QRect(230, 150, 31, 20))
        self.divide_Button.setObjectName("divide_Button")
        self.result_label = QtWidgets.QLabel(self.centralWidget)
        self.result_label.setGeometry(QtCore.QRect(50, 200, 41, 21))
        self.result_label.setObjectName("result_label")
        self.cal_Button = QtWidgets.QPushButton(self.centralWidget)
        self.cal_Button.setGeometry(QtCore.QRect(270, 150, 113, 32))
        self.cal_Button.setObjectName("cal_Button")
        self.result_Window = QtWidgets.QTextEdit(self.centralWidget)
        self.result_Window.setGeometry(QtCore.QRect(110, 190, 151, 31))
        self.result_Window.setObjectName("result_Window")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 577, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        # self.cal_Button.clicked.connect(MainWindow.calResult)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.num1_label.setText(_translate("MainWindow", "数字1"))
        self.num2_label.setText(_translate("MainWindow", "数字2"))
        self.TODO_label.setText(_translate("MainWindow", "运算"))
        self.plus_Button.setText(_translate("MainWindow", "+"))
        self.minus_Button.setText(_translate("MainWindow", "-"))
        self.multiply_Button.setText(_translate("MainWindow", "*"))
        self.divide_Button.setText(_translate("MainWindow", "/"))
        self.result_label.setText(_translate("MainWindow", "结果"))
        self.cal_Button.setText(_translate("MainWindow", "计算"))

