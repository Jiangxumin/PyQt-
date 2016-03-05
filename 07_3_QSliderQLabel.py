#!/usr/bin/python
#coding=utf-8

import sys
from PyQt4 import QtGui,QtCore

class SliderLabel(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(200,200,850,550)
        self.setWindowTitle('SliderLabel')
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal,self)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setGeometry(30,40,300,30)
        self.connect(self.slider,QtCore.SIGNAL('valueChanged(int)'),self.changeValue)

        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('icons/mute.png'))
        self.label.setGeometry(160,60,600,400)
    def changeValue(self,value):
        pos = self.slider.value()
        if pos == 0:
            self.label.setPixmap(QtGui.QPixmap('icons/cloud1.png'))
        elif 0 < pos <= 30:
            self.label.setPixmap(QtGui.QPixmap('icons/cloud2.png'))
        elif 30 < pos <80:
            self.label.setPixmap(QtGui.QPixmap('icons/cloud3.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('icons/cloud4.png'))

app = QtGui.QApplication(sys.argv)
w = SliderLabel()
w.show()
sys.exit(app.exec_())

