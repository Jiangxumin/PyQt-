#!/usr/bin/python
#coding=utf-8
#菜单栏
#menubar.py

import sys
from PyQt4 import QtGui,QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)

        self.resize(250,150)
        self.setWindowTitle('menubar')

        exit = QtGui.QAction(QtGui.QIcon('icons/exit.ico'),'Exit',self)
        exit.setShortcut('Ctrl+Q')#快捷键
        exit.setStatusTip('Exit application')
        exit.connect(exit,QtCore.SIGNAL('triggered()'),QtGui.qApp,QtCore.SLOT('quit()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())