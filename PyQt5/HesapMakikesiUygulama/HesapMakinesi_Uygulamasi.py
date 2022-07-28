import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("HesapMakinesi")
        self.setGeometry(250,250,500,500)
        self.initUI()
    
    def initUI(self):
    #1. sayının labelı
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText( "Sayi1: ")
        self.lbl_sayi1.move(40,30)
    #1. sayının textboxı
        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,30)

    #1. sayının textboxı
        self.txt_sayi2 = QtWidgets.QLineEdit(self)  
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,30)

     #2. sayının labelı
        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayi2: ")
        self.lbl_sayi2.move(40,70)

    #toplama butonu oluşturma
        self.btn_topla = QtWidgets.QPushButton(self)   
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,130)
        # self.btn_topla.clicked.connect(self.toplama)
        self.btn_topla.clicked.connect(self.hesapla)

    #Çıkarma butonu
        self.btn_cikar =QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkar")
        self.btn_cikar.move(150,170)
        # self.btn_cikar.clicked.connect(self.cikarma)  
        self.btn_cikar.clicked.connect(self.hesapla)

    #Çarpma butonu
        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText("Çarp")
        self.btn_carp.move(150,210)
        # self.btn_carp.clicked.connect(self.carpma)
        self.btn_carp.clicked.connect(self.hesapla)

    #bölme butonu
        self.btn_bolme =QtWidgets.QPushButton(self)
        self.btn_bolme.setText("Bölme")
        self.btn_bolme.move(150,250)
        # self.btn_bolme.clicked.connect(self.bolme)
        self.btn_bolme.clicked.connect(self.hesapla)

    #Sonuç Labelı
        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.move(165,280)
        self.lbl_sonuc.resize(70,60)
        self.lbl_sonuc.setText("Sonuc: ")

    def toplama(self):
        sonuc = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç : " + str(sonuc)) 

    def cikarma(self):
        sonuc = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç : " + str(sonuc))

    def carpma(self):
        sonuc = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuç : " + str(sonuc))

    def bolme(self):
        sonuc = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        self.lbl_sonuc.setText("Sonuc : " + str(sonuc))

    #alternatif yöntem
    def hesapla(self):  
        islem = self.sender().text()
        sonuc=0

        if islem == "Topla":
            sonuc = int(self.txt_sayi1.text()) +int(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuc : " + str(sonuc))
        
        elif islem == "Çıkar":
            sonuc = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuc : " + str(sonuc))

        elif islem == "Bölme":
            sonuc = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuc : " + str(sonuc))

        else:
            sonuc = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
            self.lbl_sonuc.setText("Sonuc : " + str(sonuc))


def app():
    app =QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()