#!/usr/bin/python
#coding=utf-8

import sys
from PyQt4 import  QtGui,QtCore

class Calendar(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self)
        self.setGeometry(300,300,350,300)
        self.setWindowTitle("Calendar")
        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.connect(self.cal,QtCore.SIGNAL('selectionChanged()'),self.showDate)

        self.label = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.cal)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def showDate(self):
        date = self.cal.selectedDate()
        self.label.setText(str(date.toPyDate()))

app = QtGui.QApplication(sys.argv)
w = Calendar()
w.show()
sys.exit(app.exec_())
