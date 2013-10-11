# -*- coding: utf-8 -*-

# Hazırlayan : Rahman Yazgan (rahmanyazgan@gmail.com)
# Lisans : GPL v.3

from PyQt4 import QtCore, QtGui
from moduller.Ui_OrtalamaHesapla import Ui_Dialog

class OrtalamaHesapla(QtGui.QDialog, Ui_Dialog):
    def __init__(self, settings, ayarDosyasi):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        self.degiskenleriTanimla(settings, ayarDosyasi)
        self.sinyalleriEkle()
        
        self.dosya = QtCore.QFile(self.ayarDosyasi)
        if self.dosya.exists(self.ayarDosyasi):
            if self.dosya.size() != 0:
                try:
                    self.ayarlariUygula()
                except:
                    pass
        
        self.varsayilanPencereBoyutu()

    def sinyalleriEkle(self):
        self.temizle_pushButton.clicked.connect(self.temizle)
        self.hesapla_pushButton.clicked.connect(self.ortalamayiHesapla)
        self.ders_ekle_pushButton.clicked.connect(self.dersEkle)
        self.ders_sil_pushButton.clicked.connect(self.dersSil)
        self.gno_durumu_checkBox.clicked.connect(self.bilesenleriEtkinlestir)
        self.ogrenim_durumu_comboBox.currentIndexChanged.connect(self.ogrenimDurumuDegisti)
    
    def degiskenleriTanimla(self, settings, ayarDosyasi):
        self.settings = settings
        self.ayarDosyasi = ayarDosyasi

        self.dersSayisi = 9
        self.dersSayisiVarsayilan = 9
        self.eklenenDersSayisi = 0
        
        # Sonradan eklenen comboBoxları sırayla gezebilmek için kullanıldı.
        self.sayi = 0

        self.veriler = ["ders_adi", "kredi", "harf_notu"]
        
        self.harfNotuTablosu = {"AA" : 4.0, "BA" : 3.5,
                                "BB" : 3.0, "CB" : 2.5,
                                "CC" : 2.0, "DC" : 1.5,
                                "DD" : 1.0, "FD" : 0.5,
                                "FF" : 0}
        
        # İlgili dönem sonunda sahip olunması gereken genel not ortalamalarıdır.
        # İAU yönetmeliğine göre 1. dönem için ortalama şartı yoktur,
        # 1. dönemdeki notlar kodlama kısmında gözardı edilecektir.
        self.onLisansSartliGecisOrtalamalari = {"1" : 1.80, "2" : 1.80,
                                                "3" : 1.90, "4" : 2.00}
        
        self.lisansSartliGecisOrtalamalari = {"1" : 1.80, "2" : 1.80,
                                              "3" : 1.80, "4" : 1.85,
                                              "5" : 1.85, "6" : 1.90,
                                              "7" : 1.90, "8" : 2.00}
        
        self.eklenenKrediComboBoxlar = []
        self.eklenenHarfNotuComboBoxlar = []
        self.eklenenSonucLabeller = []
        self.eklenenLineEditler = []
        self.eklenenHorizontalLayoutlar = []
    
    def bilesenleriEtkinlestir(self):
        if self.gno_durumu_checkBox.isChecked():
            self.ogrenim_durumu_comboBox.setEnabled(True)
            self.sinif_comboBox.setEnabled(True)
            self.donem_comboBox.setEnabled(True)
        else:
            self.ogrenim_durumu_comboBox.setEnabled(False)
            self.sinif_comboBox.setEnabled(False)
            self.donem_comboBox.setEnabled(False)
            
    def varsayilanPencereBoyutu(self):
        if self.dersSayisi < 15:
            x = self.geometry().x()
            y = self.geometry().y()
            width = 636
            height = 498
            
            self.setGeometry(x, y, width, height)
            
            self.ekrandaOrtala()
            
    def ekrandaOrtala(self):
        self.move((QtGui.QDesktopWidget().screenGeometry().width() - self.geometry().width()) / 2,
                  (QtGui.QDesktopWidget().screenGeometry().height() - self.geometry().height()) / 2)
            
    def ogrenimDurumuDegisti(self, indis):
        durum = self.ogrenim_durumu_comboBox.currentText()
        
        self.sinif_comboBox.clear()
        
        if durum == "Lisans":
            sinifSayisi = 4
        else:
            sinifSayisi = 2
            
        for i in range(1, sinifSayisi + 1, 1):
            kod = 'self.sinif_comboBox.addItem("' + str(i) + '")'
            eval(kod)
            
        self.sinif_comboBox.setCurrentIndex(0)
        
        self.ayarlariUygula()
    
    def ayarlariKaydet(self):
        self.settings.setValue("NotHesaplayici/surum", "2.0")
        
        self.settings.setValue("OrtalamaHesapla/geometry", self.geometry())
        self.settings.setValue("OrtalamaHesapla/eklenen_ders_sayisi", self.eklenenDersSayisi)
        self.settings.setValue("OrtalamaHesapla/gno_durumu", self.gno_durumu_checkBox.checkState())
        self.settings.setValue("OrtalamaHesapla/ogrenim_durumu", self.ogrenim_durumu_comboBox.currentIndex())
        self.settings.setValue("OrtalamaHesapla/sinif", self.sinif_comboBox.currentIndex())
        self.settings.setValue("OrtalamaHesapla/donem", self.donem_comboBox.currentIndex())

        self.varsayilanAyarlariKullan("Ayarları Kaydet")
        
        for veri in self.veriler:
            for i in range(self.dersSayisiVarsayilan + 1, self.dersSayisi + 1, 1):
                self.ayarlar("Ayarları Kaydet", veri, i)
            
            self.sayi = 0

    def ayarlariUygula(self):
        surum = self.settings.value("NotHesaplayici/surum")
        
        if surum == "2.0":
            rect = self.settings.value("OrtalamaHesapla/geometry")
            self.setGeometry(QtCore.QRect(rect))
    
            eklenenDersSayisi = int(self.settings.value("OrtalamaHesapla/eklenen_ders_sayisi"))

            if eklenenDersSayisi > 0:
                for i in range(eklenenDersSayisi, 0, -1):
                    self.dersEkle()
            
            gnoDurumu = int(self.settings.value("OrtalamaHesapla/gno_durumu"))
            
            if gnoDurumu == 2:
                self.gno_durumu_checkBox.setChecked(True)
            else:
                self.gno_durumu_checkBox.setChecked(False)
                    
            self.bilesenleriEtkinlestir()
            
            indis = int(self.settings.value("OrtalamaHesapla/ogrenim_durumu"))
            self.ogrenim_durumu_comboBox.setCurrentIndex(indis)
            
            indis = int(self.settings.value("OrtalamaHesapla/sinif"))
            self.sinif_comboBox.setCurrentIndex(indis)
            
            indis = int(self.settings.value("OrtalamaHesapla/donem"))
            self.donem_comboBox.setCurrentIndex(indis)
    
            self.varsayilanAyarlariKullan("Ayarları Uygula")
            
            for veri in self.veriler:
                for i in range(self.dersSayisiVarsayilan + 1, self.dersSayisi + 1, 1):            
                    self.ayarlar("Ayarları Uygula", veri, i)
                
                self.sayi = 0
            
        # Silinen comboBoxların ve lineEditlerin ayarı vs. ayar dosyasında kalmasın diye tüm ayarlar 
        # kullanıldıktan sonra siliniyor. Program kapanırken ayarlar temiz bir şekilde kaydedilmiş olacak.
        self.settings.clear()
        
    def varsayilanAyarlariKullan(self, durum):
        for veri in self.veriler:            
            for i in range(1, self.dersSayisiVarsayilan + 1, 1):
                self.ayarlar(durum, veri, i)
            
            self.sayi = 0

    def ayarlar(self, durum, bilesen, sayi):
        if durum == "Ayarları Kaydet":
            
            if bilesen == "ders_adi":
                if sayi < 10:
                    kod = "self.ders_adi_lineEdit_" + str(sayi) + ".text()"
                    dersAdi = eval(kod)
                    
                    self.settings.setValue("OrtalamaHesapla/ders_adi_" + str(sayi), dersAdi)
                
                if sayi >= 10:
                    
                    
                    if self.sayi < self.eklenenDersSayisi:
                        dersAdi = self.eklenenLineEditler[self.sayi].text()
                        self.settings.setValue("OrtalamaHesapla/ders_adi_" + str(sayi), dersAdi)
                        
                        self.sayi += 1
            else:
                if sayi < 10:
                    kod = 'self.' + bilesen + "_comboBox_" + str(sayi) + ".currentIndex()"
                    indis = eval(kod)
    
                    self.settings.setValue("OrtalamaHesapla/" + bilesen + "_" + str(sayi), indis)
                    
                # Sonradan eklenen derslerin verilerini kaydeden kısım.
                if sayi >= 10:
                    comboBox = self.hangiComboBox(bilesen)
    
                    if self.sayi < self.eklenenDersSayisi:
                        indis = comboBox[self.sayi].currentIndex()
                        self.sayi += 1
    
                        self.settings.setValue("OrtalamaHesapla/" + bilesen + "_" + str(sayi), indis)

        if durum == "Ayarları Uygula":
            try:
                if bilesen == "ders_adi":
                    
                    if sayi < 10:
                        dersAdi = self.settings.value("OrtalamaHesapla/ders_adi_" + str(sayi))
                        kod = 'self.ders_adi_lineEdit_' + str(sayi) + '.setText("' + dersAdi + '")'
                        eval(kod)
                    
                    if sayi >= 10:
                        dersAdi = self.settings.value("OrtalamaHesapla/ders_adi_" + str(sayi))
                        
                        if self.sayi < self.eklenenDersSayisi:
                            self.eklenenLineEditler[self.sayi].setText(dersAdi)
                            self.sayi += 1
                    
                else:
                    comboBox = self.hangiComboBox(bilesen)
                    
                    indis = int(self.settings.value("OrtalamaHesapla/" + bilesen + "_"  + str(sayi)))
                    
                    if sayi < 10:
                        kod = 'self.' + bilesen + '_comboBox' + "_" + str(sayi) + \
                              '.setCurrentIndex(' + str(indis) + ')'
                        eval(kod)
                        
                    # Sonradan eklenen comboBoxlara veriler ekleniyr.
                    if sayi >= 10:                    
                        if self.sayi < self.eklenenDersSayisi:
                            comboBox[self.sayi].setCurrentIndex(indis)
                            self.sayi += 1
            except TypeError:
                pass                    

    def hangiComboBox(self, krediHarfNotu):
        if krediHarfNotu == "kredi":
            comboBox = self.eklenenKrediComboBoxlar
        else:
            comboBox = self.eklenenHarfNotuComboBoxlar

        return comboBox

    def dersEkle(self):
        # Yeni ders eklemek için gerekli bileşenler oluşturuluyor.
        self.ders_horizontalLayout = QtGui.QHBoxLayout()
        self.ders_horizontalLayout.setObjectName("ders_horizontalLayout")

        self.ders_no_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.sizePolicyEkle("label", "self.ders_no_label")
        self.ders_no_label.setSizePolicy(self.sizePolicyWidget)
        self.ders_no_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ders_no_label.setObjectName("ders_no_label")

        self.ders_adi_lineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sizePolicyEkle("lineEdit", "self.ders_adi_lineEdit")
        self.ders_adi_lineEdit.setSizePolicy(self.sizePolicyWidget)
        self.ders_adi_lineEdit.setText("")
        self.ders_adi_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ders_adi_lineEdit.setObjectName("ders_adi_lineEdit")

        self.kredi_comboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.kredi_comboBox.setObjectName("kredi_comboBox")

        self.harf_notu_comboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.harf_notu_comboBox.setObjectName("harf_notu_comboBox_22")

        # ComboBoxlara gerekli veriler ekleniyor.
        self.comboBoxAddItem("kredi", "self.kredi_comboBox")
        self.comboBoxAddItem("harf_notu", "self.harf_notu_comboBox")

        self.sonuc_label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.sonuc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sonuc_label.setObjectName("sonuc_label")

        # Yeni eklenen widgetler horizontalLayout'a ekleniyor.
        self.ders_horizontalLayout.addWidget(self.ders_no_label)
        self.ders_horizontalLayout.addWidget(self.ders_adi_lineEdit)
        self.ders_horizontalLayout.addWidget(self.kredi_comboBox)
        self.ders_horizontalLayout.addWidget(self.harf_notu_comboBox)
        self.ders_horizontalLayout.addWidget(self.sonuc_label)

        # Yeni eklenen horizontalLayout verticalLayout'a ekleniyor.
        self.verticalLayout.addLayout(self.ders_horizontalLayout)

        # Yeni eklenen labellara görünmesi istenen yazı ekleniyor.
        kod = 'self.sonuc_label.setText("...")'
        eval(kod)

        kod = 'self.ders_no_label.setText("' + str(self.dersSayisi + 1) + '")'
        eval(kod)


        harfNotlari = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FD", "FF"]

        # Yeni eklenen comboBoxlara harf notları ve kredi sayıları ekleniyor.
        for j in range(0, 11, 1):
            kod = 'self.kredi_comboBox.setItemText(' + str(j) + ', "' + str(j) + '")'
            eval(kod)

        for k in range(0, 9, 1):
            kod = 'self.harf_notu_comboBox.setItemText(' + str(k) + ', "' + harfNotlari[k] + '")'
            eval(kod)

        # Yeni eklenen dersleri silerken, widgetların içeriğini temizlerken ve
        # saklayacağımız ayarlarda kullanacağımız widgetlar listelelere ekleniyor.
        self.eklenenHorizontalLayoutlar.append(self.ders_horizontalLayout)
        self.eklenenLineEditler.append(self.ders_adi_lineEdit)
        self.eklenenKrediComboBoxlar.append(self.kredi_comboBox)
        self.eklenenHarfNotuComboBoxlar.append(self.harf_notu_comboBox)
        self.eklenenSonucLabeller.append(self.sonuc_label)

        # Eklenen ders sayisi ve toplam ders saysı bilgileri
        self.dersSayisi += 1
        self.eklenenDersSayisi += 1

        self.geometryAyarla()
    
    # Yeni eklenen label ve lineEditların düzgün görünmesini sağlar.
    def sizePolicyEkle(self, widgetTuru, hangiWidget):
        if widgetTuru == "label":
            self.sizePolicyWidget = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)

        if widgetTuru == "lineEdit":
            self.sizePolicyWidget = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)

        self.sizePolicyWidget.setHorizontalStretch(0)
        self.sizePolicyWidget.setVerticalStretch(0)

        kod = "self.sizePolicyWidget.setHeightForWidth(" + hangiWidget + ".sizePolicy().hasHeightForWidth())"
        eval(kod)

    def comboBoxAddItem(self, krediHarfNotu, comboBox):
        if krediHarfNotu == "harf_notu":
            for i in range(1, 10, 1):
                kod = str(comboBox) + '.addItem("")'
                eval(kod)
        else:
            for i in range(1, 12, 1):
                kod = str(comboBox) + '.addItem("")'
                eval(kod)

    def geometryAyarla(self):
        yukseklik = self.geometry().height()

        x = self.geometry().x()
        width = self.geometry().width()
        height = yukseklik + 20

        if self.geometry().y() > 30:
            y = self.geometry().y() - 10

            rect = QtCore.QRect(x, y, width, height)

            if yukseklik <= 600:
                self.setGeometry(rect)

    def dersSil(self):
        if self.eklenenDersSayisi > 0:
            silinecekLayout = self.eklenenHorizontalLayoutlar[self.eklenenDersSayisi -1]

            self.layoutSil(silinecekLayout)

            self.eklenenHorizontalLayoutlar.pop()
            self.eklenenHarfNotuComboBoxlar.pop()
            self.eklenenKrediComboBoxlar.pop()
            self.eklenenSonucLabeller.pop()
            self.eklenenLineEditler.pop()

            self.eklenenDersSayisi -= 1
            self.dersSayisi -= 1

        self.ortalamayiHesapla()

    def layoutSil(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()

                if widget is not None:
                    widget.deleteLater()
                else:
                    self.layoutSil(item.layout())

    def temizle(self):
        soru = QtGui.QMessageBox.question(self, "Uyarı",
                                          "Ders adları, kredi bilgileri, harf notları gibi bilgiler " +
                                          "ve sonradan eklenen derslerin hepsini silmek istiyor musunuz?\n\n",
            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if soru == QtGui.QMessageBox.Yes:
            
            self.settings.clear()
            
            for i in range(1, self.eklenenDersSayisi + 1, 1):
                self.dersSil()
            
            self.eklenenDersSayisi = 0

            for i in range(1, self.dersSayisiVarsayilan + 1, 1):
                kodlar = ["self.kredi_comboBox_" + str(i) + ".setCurrentIndex(0)",
                          "self.harf_notu_comboBox_" + str(i) + ".setCurrentIndex(0)",
                          "self.sonuc_label_" + str(i) + '.setText("...")',
                          "self.ders_adi_lineEdit_" + str(i) + ".clear()"]
                
                for kod in kodlar:
                    eval(kod)

            for i in range(0, self.eklenenDersSayisi, 1):
                self.eklenenKrediComboBoxlar[i].setCurrentIndex(0)
                self.eklenenHarfNotuComboBoxlar[i].setCurrentIndex(0)
                self.eklenenSonucLabeller[i].setText("...")
                self.eklenenLineEditler[i].clear()
                
            self.gno_durumu_checkBox.setChecked(False)
            self.bilesenleriEtkinlestir()
            
            self.ogrenim_durumu_comboBox.setCurrentIndex(0)
            self.sinif_comboBox.setCurrentIndex(0)
            self.donem_comboBox.setCurrentIndex(0)

            self.ortalama_sonuc_label.setText("...")
            
            self.ayarlariUygula()

    def ortalamayiHesapla(self):
        sonuclar = self.krediHarfNotuCarpimSonuclariniBul()

        alinanKrediToplami = self.krediHarfNotuCarpimiToplami(sonuclar)
        derslerinKrediToplami = self.alinanKrediToplami()

        try:
            sonuc = str(alinanKrediToplami / derslerinKrediToplami)
            sonucDuzenli = "<font color='#FF0000'>" + sonuc[:4] + "</font>"
        except ZeroDivisionError:
            sonucDuzenli = "<font color='#FF0000'>0</font>"

        self.ortalama_sonuc_label.setText(sonucDuzenli)
        
        self.gnoDurumunuOgren()
        
    def gnoDurumunuOgren(self):
        if self.gno_durumu_checkBox.isChecked():
            veri = self.ortalama_sonuc_label.text()
            veri = veri.replace("<font color='#FF0000'>", "").replace("</font>", "")
            ortalama = float(veri)
            
            ogrenimDurumu = self.ogrenim_durumu_comboBox.currentText()
            sinif = int(self.sinif_comboBox.currentText())
            donem = int(self.donem_comboBox.currentText())
            yariyil = self.yariyilBul(sinif, donem)
            
            if yariyil > 1:                
                gecmeNotu = self.gecmeNotunuBul(ogrenimDurumu, yariyil)                
                
                if ortalama >= gecmeNotu:
                    self.mesajGoster("DD/DC harf notuna sahip derslerden geçtiniz.")
                else:
                    if (yariyil == 1) or (yariyil == 3) or (yariyil == 5) or (yariyil == 7):
                        eklenecekMetin = "\nFakat yıl sonuna kadar " + \
                                          str(self.gecmeNotunuBul(ogrenimDurumu, yariyil + 1)) + \
                                          " genel not ortalamasına ulaşırsanız \ntüm DD/DC notlu derslerden geçmiş olacaksınız."
                    
                    else:
                        eklenecekMetin = ""
                        
                    self.mesajGoster("DD/DC harf notuna sahip derslerden kaldınız." + eklenecekMetin)
            else:
                self.mesajGoster("1. dönem için genel not ortalaması şartı aranmaz.")
                
    def yariyilBul(self, sinif, donem):
        yariyillar = {"1-1" : 1, "1-2" : 2,
                      "2-1" : 3, "2-2" : 4,
                      "3-1" : 5, "3-2" : 6,
                      "4-1" : 7, "4-2" : 8}
        
        veri = str(sinif) + '-' + str(donem)
        yariyil = yariyillar.get(veri)
        
        return yariyil
                
    def gecmeNotunuBul(self, ogrenimDurumu, kacinciYariyil):
        yariyil = str(kacinciYariyil)
        if ogrenimDurumu == "Lisans":
            gecmeNotu = self.lisansSartliGecisOrtalamalari.get(yariyil)
        else:
            gecmeNotu = self.onLisansSartliGecisOrtalamalari.get(yariyil)
            
        return gecmeNotu

    def mesajGoster(self, metin):
        QtGui.QMessageBox.information(self, "Bilgilendirme", metin, "Tamam")
            
    def harfNotuDegeriniBul(self, harfNotu):
        harfNotununKarsiligi = self.harfNotuTablosu.get(harfNotu)

        return harfNotununKarsiligi

    def krediHarfNotuCarpimSonuclariniBul(self):
        sonuclar = []

        for i in range(1, self.dersSayisiVarsayilan + 1, 1):
            kod = "self.kredi_comboBox_" + str(i) + ".currentText()"
            kredi = float(eval(kod))

            kod = "self.harf_notu_comboBox_" + str(i) + ".currentText()"
            harfNotu = str(eval(kod))

            harfNotuDegeri = self.harfNotuDegeriniBul(harfNotu)

            sonuc = kredi * harfNotuDegeri
            sonuclar.append(sonuc)

            kod = "self.sonuc_label_" + str(i) + '.setText("' + str(sonuc) + '")'
            eval(kod)

        for i in range(0, self.eklenenDersSayisi, 1):
            kredi = float(self.eklenenKrediComboBoxlar[i].currentText())
            harfNotu = self.eklenenHarfNotuComboBoxlar[i].currentText()

            harfNotuDegeri = self.harfNotuDegeriniBul(harfNotu)

            sonuc = kredi * harfNotuDegeri
            sonuclar.append(sonuc)

            self.eklenenSonucLabeller[i].setText(str(sonuc))

        return sonuclar

    def krediHarfNotuCarpimiToplami(self, liste):
        toplam = 0

        for i in liste:
            toplam = toplam + i

        return toplam

    def alinanKrediToplami(self):
        toplamKredi = 0

        for i in range(1, self.dersSayisiVarsayilan + 1, 1):
            kod = "self.kredi_comboBox_" + str(i) + ".currentText()"
            kredi = eval(kod)

            toplamKredi = toplamKredi + float(kredi)

        for i in range(0, self.eklenenDersSayisi, 1):
            kredi = self.eklenenKrediComboBoxlar[i].currentText()

            toplamKredi = toplamKredi + float(kredi)

        return toplamKredi

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.ayarlariKaydet()
            self.close()

    def closeEvent(self, event):
        self.ayarlariKaydet()
        event.accept()
