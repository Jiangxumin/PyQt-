#!/usr/bin/python
#coding=utf-8

import sys
from PyQt4 import QtGui, QtCore

class ProgreessBar(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('ProgressBar')

        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.button = QtGui.QPushButton('Start',self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40,80)

        self.button_clean = QtGui.QPushButton('Clean',self)
        self.button_clean.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_clean.move(130,80)

        self.connect(self.button,QtCore.SIGNAL("clicked()"),self.onStart)
        self.connect(self.button_clean,QtCore.SIGNAL("clicked()"),self.setClean)

        self.timer = QtCore.QBasicTimer()
        self.step = 0
    def timerEvent(self, event):
        if self.step > 100:
            self.timer.stop()
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def onStart(self):
        if self.timer.isActive():
            self.timer.stop()
            self.button.setText("start")
        else:
            self.timer.start(100,self)
            self.button.setText('stop')

    def setClean(self):
        self.step = 0
        self.pbar.setValue(self.step)

app = QtGui.QApplication(sys.argv)
icon = ProgreessBar()
icon.show()
sys.exit(app.exec_())