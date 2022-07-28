from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    


    win.setWindowTitle("İlk Uygulama") #uygulama penceresinin başlığına isim verme
    win.setGeometry(250,250,300,300)    #pencerenin x,y yerleşimi ve boyutlarını belirtir
    win.setWindowIcon(QIcon('icon.png'))    #title kısmına icon eklenmesi
    win.setToolTip("Toolstip örneği")   # açıklama baloncuğu çıkarma

    lbl_name = QtWidgets.QLabel(win)    #pencere içerisine label nesnesi ekleme
    lbl_name.setText("Adınız: ")    #label nesnesinin text ayarlama
    lbl_name.move(50,30) #label ın yerleşimini yukarıdan ve soldan olarak ayarlar

    lbl_surname = QtWidgets.QLabel(win) #soyadınız yazan label ekleme
    lbl_surname.setText("soyadınız")
    lbl_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)  #textbox nesnesi ekleme
    txt_name.move(120,30)

    txt_surname = QtWidgets.QLineEdit(win)  #textbox nesnesi ekleme
    txt_surname.move(120,70)

    def cliced(self) :
        print("butona tıklandı, Name: " + txt_name.text() + "  Surname: " + lbl_surname.text())

    btn_save = QtWidgets.QPushButton(win)   #buton ekleme
    btn_save.setText("Kaydet")
    btn_save.move(120,120)
    btn_save.clicked.connect(cliced)





    win.show()
    sys.exit(app.exec_())

window()


##Widgests neneleri
#QLabel
# QComboBox
# QCheckBox
# QPushButton
# QRadioButton
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar
