#coding=utf-8
#将窗口放在屏幕中间

__author__ = 'Administrator'

import sys
from PyQt4 import QtGui

class Center(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)

        self.setWindowTitle('client')
        self.resize(250,150)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()#获取显示器分辨率
        size = self.geometry()#获取QWidget窗口大小
        self.move((screen.width() - size.width())/2,
            (screen.height() - size.height())/2)

app = QtGui.QApplication(sys.argv)
qb = Center()
qb.show()
sys.exit(app.exec_())

