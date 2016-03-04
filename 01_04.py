#coding=utf-8
__author__ = 'Administrator'
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Tooltip(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(300,300,250,150)#窗口的x,y坐标，及宽和高
        self.setWindowTitle('Tooltip')
        self.setToolTip('this is a<b>QWidget</b>widget')
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglis',10))

app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())
