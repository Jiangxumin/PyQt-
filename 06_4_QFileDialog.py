#!/usr/bin/python
#coding=utf-8

import sys
from PyQt4 import QtGui, QtCore

class OpenFile(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('OpenFile')
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)# 设置中心部件
        self.statusBar()#状态栏
        self.setFocus()

        exit = QtGui.QAction(QtGui.QIcon('icons/cloud.png'),'open',self)
        exit.setShortcut("Ctrl+O")
        exit.setStatusTip('Open new file')
        self.connect(exit,QtCore.SIGNAL('triggered()'),self.showDialog)

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)

    def showDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self,'Open file','./')
        file = open(filename)
        data = file.read()
        self.textEdit.setText(data)
app = QtGui.QApplication(sys.argv)
cd = OpenFile()
cd.show()
sys.exit(app.exec_())
