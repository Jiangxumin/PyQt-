#coding=utf-8
__author__ = 'Administrator'

import sys
from PyQt4 import QtGui

class MessageBox(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('message box')

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?",
                                           QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            print "yes"
            event.accept()
            pass
        else:
            print "no"
            event.ignore()
            pass
app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())
