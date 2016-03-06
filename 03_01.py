#!/usr/bin/python
#coding=utf-8
#PyQt4中的菜单和工具栏

#statusbar.py

import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)

        self.resize(250,150)
        self.setWindowTitle('status')
        self.statusBar().showMessage('Ready')# self.stbar = self.statusBar()
                                             # self.stbar.showMessage("Ready")

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
