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

    win.show()
    sys.exit(app.exec_())

window()