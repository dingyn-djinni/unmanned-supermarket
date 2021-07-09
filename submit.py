# -*- coding: utf-8 -*-
# author:djinni
# 一款仅实现基本的加减乘除括号功能的科学计算器，没怎么测试过，可能有bug
# development enviroment：ubuntu18.04+python3.6+pyqt5

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import sys
from calculator import Ui_calculator  # 导入生成form.py里生成的类
from PyQt5 import QtCore
from PyQt5.QtCore import *


class mywindow(QtWidgets.QWidget, Ui_calculator):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)



app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())