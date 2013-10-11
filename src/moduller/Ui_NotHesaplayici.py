# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python33\ui\NotHesaplayici.ui'
#
# Created: Thu Mar  7 21:08:34 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from moduller import NotHesaplayici_rc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(352, 195)
        MainWindow.setMinimumSize(QtCore.QSize(352, 195))
        MainWindow.setMaximumSize(QtCore.QSize(352, 195))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 331, 151))
        self.groupBox.setMinimumSize(QtCore.QSize(331, 151))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 308, 131))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.not_hesapla_toolButton = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.not_hesapla_toolButton.setMinimumSize(QtCore.QSize(140, 100))
        self.not_hesapla_toolButton.setMaximumSize(QtCore.QSize(140, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resimler/not.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.not_hesapla_toolButton.setIcon(icon)
        self.not_hesapla_toolButton.setIconSize(QtCore.QSize(64, 64))
        self.not_hesapla_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.not_hesapla_toolButton.setObjectName(_fromUtf8("not_hesapla_toolButton"))
        self.horizontalLayout.addWidget(self.not_hesapla_toolButton)
        self.ortalama_hesapla_toolButton = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.ortalama_hesapla_toolButton.setMinimumSize(QtCore.QSize(140, 100))
        self.ortalama_hesapla_toolButton.setMaximumSize(QtCore.QSize(140, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resimler/ortalama.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ortalama_hesapla_toolButton.setIcon(icon1)
        self.ortalama_hesapla_toolButton.setIconSize(QtCore.QSize(64, 64))
        self.ortalama_hesapla_toolButton.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.ortalama_hesapla_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.ortalama_hesapla_toolButton.setObjectName(_fromUtf8("ortalama_hesapla_toolButton"))
        self.horizontalLayout.addWidget(self.ortalama_hesapla_toolButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 352, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuDosya = QtGui.QMenu(self.menuBar)
        self.menuDosya.setObjectName(_fromUtf8("menuDosya"))
        self.menuYardim = QtGui.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menuYardim.setFont(font)
        self.menuYardim.setObjectName(_fromUtf8("menuYardim"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionCikis = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/resimler/cikis.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCikis.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.actionCikis.setFont(font)
        self.actionCikis.setObjectName(_fromUtf8("actionCikis"))
        self.actionHakkinda = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.actionHakkinda.setFont(font)
        self.actionHakkinda.setObjectName(_fromUtf8("actionHakkinda"))
        self.actionQtHakkinda = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.actionQtHakkinda.setFont(font)
        self.actionQtHakkinda.setObjectName(_fromUtf8("actionQtHakkinda"))
        self.actionLisans = QtGui.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.actionLisans.setFont(font)
        self.actionLisans.setObjectName(_fromUtf8("actionLisans"))
        self.menuDosya.addAction(self.actionCikis)
        self.menuYardim.addAction(self.actionLisans)
        self.menuYardim.addSeparator()
        self.menuYardim.addAction(self.actionHakkinda)
        self.menuYardim.addAction(self.actionQtHakkinda)
        self.menuBar.addAction(self.menuDosya.menuAction())
        self.menuBar.addAction(self.menuYardim.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Not Hesaplayıcı", None))
        self.not_hesapla_toolButton.setText(_translate("MainWindow", "Harf Notunu\n"
"Hesapla", None))
        self.not_hesapla_toolButton.setShortcut(_translate("MainWindow", "1", None))
        self.ortalama_hesapla_toolButton.setText(_translate("MainWindow", "Ortalama\n"
"Hesapla", None))
        self.ortalama_hesapla_toolButton.setShortcut(_translate("MainWindow", "2", None))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya", None))
        self.menuYardim.setTitle(_translate("MainWindow", "Yardım", None))
        self.actionCikis.setText(_translate("MainWindow", "Çıkış", None))
        self.actionCikis.setShortcut(_translate("MainWindow", "Esc", None))
        self.actionHakkinda.setText(_translate("MainWindow", "Hakkında", None))
        self.actionHakkinda.setShortcut(_translate("MainWindow", "F1", None))
        self.actionQtHakkinda.setText(_translate("MainWindow", "Qt Hakkında", None))
        self.actionLisans.setText(_translate("MainWindow", "Lisans", None))
