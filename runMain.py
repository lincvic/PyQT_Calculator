# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 下午6:08
# @Author  : Lincvic
# @Email   : lincvic@yahoo.com
# @File    : runMain.py
# @SoftwareName: PyCharm
from PyQt5 import QtWidgets
import mainwindow
import sys

class CalApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        mainwindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.cal_Button.clicked.connect(self.calResult)

    def calResult(self):
        num1 = int(self.num1_box.toPlainText())
        num2 = int(self.num2_box.toPlainText())

        if (self.plus_Button.isChecked()):
            result = num1 + num2
        elif (self.minus_Button.isChecked()):
            result = num1 - num2
        elif (self.multiply_Button.isChecked()):
            result = num1 * num2
        elif (self.divide_Button.isChecked()):
            result = num1 / num2

        self.result_Window.setText(str(result))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CalApp()
    window.show()
    sys.exit(app.exec_())