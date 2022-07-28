# python -m PyQt5.uic.pyuic tasarim.ui -o tasarin.py -x komutuyla convert ediliyor.
from PyQt5 import QtWidgets
import sys
from tasarim import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui  = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_bolme.clicked.connect(self.hesapla)
        self.ui.btn_carp.clicked.connect(self.hesapla)
        self.ui.btn_topla.clicked.connect(self.hesapla)
        self.ui.btn_cikar.clicked.connect(self.hesapla)

    def hesapla(self):  
        islem = self.sender().objectName()  #tıklanan buton un adının alınması
        sonuc=0

        if islem == self.ui.btn_topla.objectName(): #tıklanan butonun hangisi olduğunu buton isimlerinden karşılaştırılması
            sonuc = int(self.ui.txt_sayi1.toPlainText()) +int(self.ui.txt_sayi2.toPlainText())
            # self.ui.lbl_sonuc.setText("Sonuc : " + str(sonuc))
        
        elif islem ==self.ui.btn_cikar.objectName():
            sonuc = int(self.ui.txt_sayi1.toPlainText()) - int(self.ui.txt_sayi2.toPlainText())
            # self.ui.lbl_sonuc.setText("Sonuc : " + str(sonuc))

        elif islem == self.ui.btn_bolme.objectName():
            sonuc = int(self.ui.txt_sayi1.toPlainText()) / int(self.ui.txt_sayi2.toPlainText())
            # self.ui.lbl_sonuc.setText("Sonuc : " + str(sonuc))

        elif islem == self.ui.btn_carp.objectName():
            sonuc = int(self.ui.txt_sayi1.toPlainText()) * int(self.ui.txt_sayi2.toPlainText())
            # self.ui.lbl_sonuc.setText("Sonuc : " + str(sonuc))

        self.ui.lbl_sonuc.setText("Sonuc : " + str(sonuc))

    

def app():
    app =QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()