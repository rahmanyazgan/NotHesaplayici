# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python33\ui\Hakkinda.ui'
#
# Created: Thu Mar  7 21:08:34 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(461, 290)
        Dialog.setMinimumSize(QtCore.QSize(461, 290))
        Dialog.setMaximumSize(QtCore.QSize(461, 290))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        Dialog.setFont(font)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 441, 271))
        self.tabWidget.setMinimumSize(QtCore.QSize(441, 271))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.hakkinda_tab = QtGui.QWidget()
        self.hakkinda_tab.setObjectName(_fromUtf8("hakkinda_tab"))
        self.hakkinda_label = QtGui.QLabel(self.hakkinda_tab)
        self.hakkinda_label.setGeometry(QtCore.QRect(10, 10, 421, 231))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.hakkinda_label.setFont(font)
        self.hakkinda_label.setObjectName(_fromUtf8("hakkinda_label"))
        self.tabWidget.addTab(self.hakkinda_tab, _fromUtf8(""))
        self.yazar_tab = QtGui.QWidget()
        self.yazar_tab.setObjectName(_fromUtf8("yazar_tab"))
        self.yazar_label = QtGui.QLabel(self.yazar_tab)
        self.yazar_label.setGeometry(QtCore.QRect(10, 10, 391, 171))
        self.yazar_label.setObjectName(_fromUtf8("yazar_label"))
        self.tabWidget.addTab(self.yazar_tab, _fromUtf8(""))
        self.hata_bildirimi_tab = QtGui.QWidget()
        self.hata_bildirimi_tab.setObjectName(_fromUtf8("hata_bildirimi_tab"))
        self.hata_bildirimi_label = QtGui.QLabel(self.hata_bildirimi_tab)
        self.hata_bildirimi_label.setGeometry(QtCore.QRect(10, 10, 391, 171))
        self.hata_bildirimi_label.setObjectName(_fromUtf8("hata_bildirimi_label"))
        self.tabWidget.addTab(self.hata_bildirimi_tab, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Hakkında", None))
        self.hakkinda_label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Not Hesaplayıcı 2.0</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Harf Notunu Hesapla kısmı Bağıl Değerlendirme Sistemine </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">göre harf notunu hesaplamaktadır.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Ortalama Hesapla kısmı ise</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">dönem sonu ortalamanızı bulmanıza yardımcı olur.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Aldığınız tüm derslerin notlarını girerek</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">hesaplarsanız genel not ortalamınızı bulur.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Proje Sayfası: </span><a href=\"http://code.google.com/p/nothesaplayici\"><span style=\" font-family:\'Sans\'; font-size:11pt; text-decoration: underline; color:#0000ff;\">http://code.google.com/p/nothesaplayici</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hakkinda_tab), _translate("Dialog", "Hakkında", None))
        self.yazar_label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Rahman YAZGAN</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:rahmanyazgan@gmail.com\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; text-decoration: underline; color:#0000ff;\">rahmanyazgan@gmail.com</span></a></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.yazar_tab), _translate("Dialog", "Yazar", None))
        self.hata_bildirimi_label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Hataları bildirmek veya</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">programa katkıda bulunmak için</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"mailto:rahmanyazgan@gmail.com\"><span style=\" font-family:\'MS Shell Dlg 2\'; text-decoration: underline; color:#0000ff;\">rahmanyazgan@gmail.com</span></a><span style=\" font-family:\'Sans\';\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">adresini kullanabilirsiniz.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hata_bildirimi_tab), _translate("Dialog", "Hata Bildirimi ve Destek", None))

