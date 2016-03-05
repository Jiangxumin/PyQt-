#!/usr/bin/python
#coding=utf-8

import sys
from PyQt4 import QtGui,QtCore

class ToggleButton(QtGui.QWidget):
    def __init__(self,paren = None):
        QtGui.QWidget.__init__(self,paren)
        self.color = QtGui.QColor(0,0,0)
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('ToggleButon')

        self.red = QtGui.QPushButton('Red',self)
        self.red.setCheckable(True)
        self.red.move(10,10)
        self.connect(self.red,QtCore.SIGNAL('clicked()'),self.setRed)

        self.green = QtGui.QPushButton("Green",self)
        self.green.setCheckable(True)
        self.green.move(10,60)
        self.connect(self.green,QtCore.SIGNAL('clicked()'),self.setGreen)

        self.blue = QtGui.QPushButton("Blue",self)
        self.blue.setCheckable(True)
        self.blue.move(10,110)
        self.connect(self.blue,QtCore.SIGNAL('clicked()'),self.setBlue)


        self.square = QtGui.QWidget(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('Qwidget{background-color:%s}'% self.color.name())

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('cleanlooks'))

    def setRed(self):
        if self.red.isChecked():
            self.color.setRed(255)
        else:
            self.color.setRed(0)
        self.square.setStyleSheet('QWidget{background-color:%s}'%self.color.name())

    def setGreen(self):
        if self.green.isChecked():
            self.color.setGreen(255)
        else:
            self.color.setGreen(0)
        self.square.setStyleSheet('QWidget{background-color:%s}'% self.color.name())

    def setBlue(self):
        if self.blue.isChecked():
            self.color.setBlue(255)
        else:
            self.color.setBlue(0)
        self.square.setStyleSheet('QWidget{background-color:%s}'% self.color.name())

app = QtGui.QApplication(sys.argv)
w = ToggleButton()
w.show()
sys.exit(app.exec_())