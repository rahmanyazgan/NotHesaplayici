# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from moduller.Ui_Lisans import Ui_Dialog

class Lisans(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
