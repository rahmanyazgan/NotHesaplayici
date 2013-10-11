# -*- coding: utf-8 -*-

# Hazırlayan : Rahman Yazgan (rahmanyazgan@gmail.com)
# Lisans : GPL v.3

from PyQt4 import QtGui
from moduller.Ui_HarfNotunuHesapla import Ui_Dialog
 
class HarfNotunuHesapla(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        
        self.sinyalleriEkle()
        self.validatorleriEkle()
        
    def sinyalleriEkle(self):
        self.hesapla_pushButton.clicked.connect(self.hesapla)
        self.temizle_pushButton.clicked.connect(self.temizle)
        self.quiz_yuzde_lineEdit.textChanged.connect(self.quizYuzdeKontrol)
        self.odev_yuzde_lineEdit.textChanged.connect(self.odevYuzdeKontrol)
        self.vize_yuzde_lineEdit.textChanged.connect(self.vizeYuzdeKontrol)
        self.final_yuzde_lineEdit.textChanged.connect(self.finalYuzdeKontrol)
        self.quiz_lineEdit.textChanged.connect(self.quizKontrol)
        self.odev_lineEdit.textChanged.connect(self.odevKontrol)
        self.vize_lineEdit.textChanged.connect(self.vizeKontrol)
        self.final_lineEdit.textChanged.connect(self.finalKontrol)
        self.ortalama_lineEdit.textChanged.connect(self.ortalamaKontrol)
        
    # İlgili lineEdit bileşenlerine sadece sayı girilebilecek.
    def validatorleriEkle(self):
        self.validatorQuizYuzde = QtGui.QDoubleValidator(0, 100.0, 2, self.quiz_yuzde_lineEdit)
        self.validatorOdevYuzde = QtGui.QDoubleValidator(0, 100.0, 2, self.odev_yuzde_lineEdit)
        self.validatorVizeYuzde = QtGui.QDoubleValidator(0, 100.0, 2, self.vize_yuzde_lineEdit)
        self.validatorFinalYuzde = QtGui.QDoubleValidator(0, 100.0, 2, self.final_yuzde_lineEdit)
        
        self.validatorQuiz = QtGui.QDoubleValidator(0, 100.0, 2, self.quiz_lineEdit)
        self.validatorOdev = QtGui.QDoubleValidator(0, 100.0, 2, self.odev_lineEdit)
        self.validatorVize = QtGui.QDoubleValidator(0, 100.0, 2, self.vize_lineEdit)
        self.validatorFinal = QtGui.QDoubleValidator(0, 100.0, 2, self.final_lineEdit)
        self.validatorOrtalama = QtGui.QDoubleValidator(0, 100.0, 2, self.ortalama_lineEdit)
        
        self.quiz_yuzde_lineEdit.setValidator(self.validatorQuizYuzde)
        self.odev_yuzde_lineEdit.setValidator(self.validatorOdevYuzde)
        self.vize_yuzde_lineEdit.setValidator(self.validatorVizeYuzde)
        self.final_yuzde_lineEdit.setValidator(self.validatorFinalYuzde)
        
        self.quiz_lineEdit.setValidator(self.validatorQuiz)
        self.odev_lineEdit.setValidator(self.validatorOdev)
        self.vize_lineEdit.setValidator(self.validatorVize)
        self.final_lineEdit.setValidator(self.validatorFinal)
        self.ortalama_lineEdit.setValidator(self.validatorOrtalama)
        
    def degiskenleriTanimla(self):
        self.notTurleri = ["quiz", "odev", "vize", "final"]
        
        for veri in self.notTurleri:
            self.dersNotlariKontrol(veri)
            self.notYuzdesiKontrol(veri)
        
        self.dersNotlariKontrol("ortalama")
        
        self.notlariTanimla()
        self.yuzdeleriTanimla()
    
    def notlariTanimla(self):
        self.quiz = float(self.quiz_lineEdit.text())
        self.odev = float(self.odev_lineEdit.text())
        self.vize = float(self.vize_lineEdit.text())
        self.final = float(self.final_lineEdit.text())
        self.ortalama = float(self.ortalama_lineEdit.text())
    
    def yuzdeleriTanimla(self):
        self.quizYuzde = float(self.quiz_yuzde_lineEdit.text())
        self.odevYuzde = float(self.odev_yuzde_lineEdit.text())
        self.vizeYuzde = float(self.vize_yuzde_lineEdit.text())
        self.finalYuzde = float(self.final_yuzde_lineEdit.text())
        
    def temizle(self):
        self.quiz_lineEdit.clear()
        self.odev_lineEdit.clear()
        self.vize_lineEdit.clear()
        self.final_lineEdit.clear()
        self.quiz_yuzde_lineEdit.clear()
        self.odev_yuzde_lineEdit.clear()
        self.vize_yuzde_lineEdit.setText("40")
        self.final_yuzde_lineEdit.setText("60")
        self.ortalama_lineEdit.clear()
        self.hamnot_label.clear()
        self.sonuc_label.clear()
        self.ybn_label.clear()
        
    def quizYuzdeKontrol(self):
        self.lineEditKontrol("Quiz yüzdesi", self.quiz_yuzde_lineEdit)
        
    def odevYuzdeKontrol(self):
        self.lineEditKontrol("Ödev yüzdesi", self.odev_yuzde_lineEdit)
        
    def vizeYuzdeKontrol(self):
        self.lineEditKontrol("Vize yüzdesi", self.vize_yuzde_lineEdit)
        
    def finalYuzdeKontrol(self):
        self.lineEditKontrol("Final yüzdesi", self.final_yuzde_lineEdit)
        
    def quizKontrol(self):
        self.lineEditKontrol("Quiz notu", self.quiz_lineEdit)
        
    def odevKontrol(self):
        self.lineEditKontrol("Ödev notu", self.odev_lineEdit)
        
    def vizeKontrol(self):
        self.lineEditKontrol("Vize notu", self.vize_lineEdit)
        
    def finalKontrol(self):
        self.lineEditKontrol("Final notu", self.final_lineEdit)
        
    def ortalamaKontrol(self):
        self.lineEditKontrol("Sınıf ortalaması", self.ortalama_lineEdit)     
                
    def lineEditKontrol(self, hangiNot, lineEdit):
        dersNotu = str(lineEdit.text())
        dersNotu = dersNotu.replace(",", ".").replace("..", ".").replace("e", "").replace("E", "")
        
        lineEdit.setText(dersNotu)
                
        self.mesajGosterKontrol(hangiNot, dersNotu, lineEdit)
                
    def mesajGosterKontrol(self, hangiNot, dersNotu, lineEdit):
        if len(dersNotu) != 0:
            if 100.0 < float(dersNotu):
                QtGui.QMessageBox.information(self, "Hata", hangiNot + " 100 den büyük olamaz.", "Kapat")
                lineEdit.clear()
                
    def dersNotlariKontrol(self, hangiNot):
        if eval("self." + hangiNot + "_lineEdit.text()") != "":
            pass
        else:
            eval("self." + hangiNot + "_lineEdit.setText('0')")
            
    def notYuzdesiKontrol(self, hangiNot):        
        if eval("self." + hangiNot + "_yuzde_lineEdit.text()") != "":
            pass
        else:
            eval("self." + hangiNot + "_yuzde_lineEdit.setText('0')")
            
    def yuzdeToplamiKontrol(self):
        toplam = self.quizYuzde + self.odevYuzde + self.vizeYuzde + self.finalYuzde
        
        if 100.0 < toplam:
            QtGui.QMessageBox.information(self, "Hata", "Notların yüzdeleri toplamı 100 den büyük olamaz.", "Kapat")
            return False
        else:
            return True   
        
    def hesapla(self):
        self.degiskenleriTanimla()
        
        if self.yuzdeToplamiKontrol():
            self.hamnot_hesapla(self.quiz, self.odev, self.vize, self.final)
            
            if 30 <= self.final:
                self.harf_tablosu(self.hamnot)
            else:
                self.sonuc_label.setText("FF")
        
    def hamnot_hesapla(self, quiz, odev, vize, final):
        quiz = quiz * self.quizYuzde
        odev = odev * self.odevYuzde
        vize = vize * self.vizeYuzde
        final = final * self.finalYuzde
        
        self.hamnot = (quiz + odev + vize + final) / 100.0
        sonuc = str(self.hamnot)[:5]
        
        self.hamnot_label.setText(sonuc)
        
    def harf_tablosu(self, hamnot):
        if 30 <= hamnot:
            try:
                if self.ortalama <= 70:
                    YBN = 0.5 * (1.0 + 70.0/self.ortalama) * float(hamnot)
                    
                    if YBN >= 100:
                        YBN = 100
                        
                    hamnot = YBN
                    
                hamnotDuzenli = str(hamnot)[:5]
                self.ybn_label.setText(hamnotDuzenli)
            
                if 90 <= hamnot <= 100:
                    self.sonuc_label.setText("AA")
                if 85 <= hamnot < 90:
                    self.sonuc_label.setText("BA")
                if 80 <= hamnot < 85:
                    self.sonuc_label.setText("BB")
                if 75 <= hamnot < 80:
                    self.sonuc_label.setText("CB")
                if 70 <= hamnot < 75:
                    self.sonuc_label.setText("CC")
                if 60 <= hamnot < 70:
                    self.sonuc_label.setText("DC")
                if 50 <= hamnot < 60:
                    self.sonuc_label.setText("DD")
                if 40 <= hamnot < 50:
                    self.sonuc_label.setText("FD")
                if 0 <= hamnot < 40:
                    self.sonuc_label.setText("FF")
            except ZeroDivisionError:
                QtGui.QMessageBox.information(self, "Uyarı", 
                                              "Sıfıra bölme tanımsızdır.\nSınıf ortalamasının sayısal değerini arttırın.",
                                              "Kapat")
        else:
            self.sonuc_label.setText("FF")