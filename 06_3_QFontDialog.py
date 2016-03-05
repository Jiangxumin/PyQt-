#!/usr/bin/python
# #coding=utf-8

#fontdialog.py

import sys
from PyQt4 import QtGui,QtCore

class FontDialog(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self)

        hbox = QtGui.QHBoxLayout()# 布局

        self.setGeometry(300,300,250,110)
        self.setWindowTitle('FontDialog')

        button = QtGui.QPushButton('Dialog',self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20,20)

        hbox.addWidget(button)# 添加到布局
        self.connect(button,QtCore.SIGNAL("clicked()"),self.showDialog)

        self.label = QtGui.QLabel('Knowledge only matters',self)
        self.label.move(130,20)

        hbox.addWidget(self.label,1)
        self.setLayout(hbox)

    def showDialog(self):
        font,ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label.setFont(font)

app = QtGui.QApplication(sys.argv)
cd = FontDialog()
cd.show()
sys.exit(app.exec_())

