#!/usr/bin/python
#coding=utf-8
# 模拟 NumLock 按键
import sys
from PyQt4 import QtGui,QtCore
import virtkey

class QuitButton(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Virtual NumLock')
        self.quit = QtGui.QPushButton('VirtNuLk',self)
        self.quit.setGeometry(10,10,80,55)
	self.virtk = virtkey.virtkey()

        self.connect(self.quit,QtCore.SIGNAL('clicked()'),self.virtNuLk)
	
    def virtNuLk(self):
        self.virtk.press_keysym(65407)
        self.virtk.release_keysym(65407)

app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())
