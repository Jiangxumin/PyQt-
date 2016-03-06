#!/usr/bin/python
#coding=utf-8
#聚合在一起
#mainwindow.py

import  sys
from PyQt4 import QtGui,QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)

        self.resize(350,250)
        self.setWindowTitle('mainwindow')

        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        exit = QtGui.QAction(QtGui.QIcon('icons/exit.ico'),'Exit',self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip("Exit application")
        self.connect(exit,QtCore.SIGNAL('triggered()'),
                     QtGui.qApp,QtCore.SLOT('quit()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu("&File")
        file.addAction(exit)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())