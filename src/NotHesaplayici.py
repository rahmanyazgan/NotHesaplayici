#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hazırlayan : Rahman Yazgan (rahmanyazgan@gmail.com)
# Lisans : GPL v.3
# Sürüm : 2.0
# Python version : 3.3

import platform, sys
from PyQt4 import QtGui, QtCore
from moduller.Ui_NotHesaplayici import Ui_MainWindow
from moduller.HarfNotunuHesapla import HarfNotunuHesapla
from moduller.OrtalamaHesapla import OrtalamaHesapla
from moduller.Hakkinda import Hakkinda
from moduller.Lisans import Lisans

class NotHesaplayici(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.ayarDosyasi = QtCore.QDir.homePath() + "/.NotHesaplayici-2.0/ayarlar.ini"
        self.settings = QtCore.QSettings(self.ayarDosyasi, QtCore.QSettings.IniFormat)
        
        self.ekrandaOrtala()
        self.gorunumuAyarla()
        self.sinyalleriEkle()
    
    def sinyalleriEkle(self):
        self.actionCikis.triggered.connect(self.close)
        self.actionHakkinda.triggered.connect(self.hakkindaDialog)
        self.actionLisans.triggered.connect(self.lisansGoster)
        self.actionQtHakkinda.triggered.connect(QtGui.QApplication.aboutQt)
        self.not_hesapla_toolButton.clicked.connect(self.notHesaplaDialog)
        self.ortalama_hesapla_toolButton.clicked.connect(self.ortalamaHesaplaDialog)
    
    def ekrandaOrtala(self):
        width = (QtGui.QDesktopWidget().screenGeometry().width() - self.geometry().width()) / 2
        height = (QtGui.QDesktopWidget().screenGeometry().height() - self.geometry().height()) / 2
        self.move(width, height)

    def gorunumuAyarla(self):
        windowsVersion = float(platform.version()[:3])
        if windowsVersion == 5.1:
            QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
        if windowsVersion > 5.1:
            QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("WindowsVista"))
            
    def dialogCalistir(self, hangiDialog):
        dialog = eval(hangiDialog)
        dialog.exec_()
        
    def hakkindaDialog(self):
        self.dialogCalistir("Hakkinda()")
        
    def notHesaplaDialog(self):
        self.setVisible(False)
        self.dialogCalistir("HarfNotunuHesapla()")        
        self.setVisible(True)
        
    def ortalamaHesaplaDialog(self):
        self.setVisible(False)
        self.dialogCalistir("OrtalamaHesapla(self.settings, self.ayarDosyasi)") 
        self.setVisible(True)

    def lisansGoster(self):
        self.dialogCalistir("Lisans()")
        
if __name__ == "__main__":    
    uygulama = QtGui.QApplication(sys.argv)
    program = NotHesaplayici()
    program.show()
    sys.exit(uygulama.exec_())
