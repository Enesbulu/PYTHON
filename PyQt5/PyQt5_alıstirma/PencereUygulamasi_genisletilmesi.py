from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QToolTip
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("İlk Uygulama") #uygulama penceresinin başlığına isim verme
        self.setGeometry(250,250,300,300)    #pencerenin x,y yerleşimi ve boyutlarını belirtir
        self.setWindowIcon(QIcon('icon.png'))    #title kısmına icon eklenmesi
        self.setToolTip("Toolstip örneği")
        self.initUI()

    def clicked(self) :
        print("Name: "  +  self.txt_name.text() +"  Surname: " + self.txt_surname.text() )
        self.lbl_result.setText("ad: " + self.txt_name.text() +" " + self.txt_surname.text()  )

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)    #pencere içerisine label nesnesi ekleme
        self.lbl_name.setText("Adınız: ")    #label nesnesinin text ayarlama
        self.lbl_name.move(50,30) #label ın yerleşimini yukarıdan ve soldan olarak ayarlar
    #soyadınız yazan label ekleme
        self.lbl_surname = QtWidgets.QLabel(self)    #pencere içerisine label nesnesi ekleme
        self.lbl_surname.setText("Soyadınız: ")    #label nesnesinin text ayarlama
        self.lbl_surname.move(50,70)
    #sonucu yazdırmak için label oluşturuluyor.
        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(140,160)
        self.lbl_result.resize(100,20)
        
    #textbox nesnesi ekleme
        self.txt_name = QtWidgets.QLineEdit(self)  
        self.txt_name.move(120,30)
        self.txt_name.resize(100,25)    #textbox ın boyutunu ayarlama
    #textbox nesnesi ekleme
        self.txt_surname = QtWidgets.QLineEdit(self)  
        self.txt_surname.move(120,70)
        self.txt_surname.resize(100,30) #textbox ın boyutunu ayarlama
    #buton ekleme
        self.btn_save = QtWidgets.QPushButton(self)   
        self.btn_save.setText("Kaydet")
        self.btn_save.move(120,120)
        self.btn_save.clicked.connect(self.clicked)
       



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()