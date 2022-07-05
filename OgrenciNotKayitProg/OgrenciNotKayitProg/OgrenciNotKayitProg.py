durum="0"   #deger girisini kontrol etmek icin olusturulmus degisken
#giris kontorlu
def girilen_not_kontrolu(girilenNot): #girilen notun 100 den buyuk yda 0 dan kucuk olma durumlarini kotrol eder
    girNot=int(girilenNot)
    if girNot>100 or girNot <0 : 
        #raise Exception("Aralik disi not giri. Lutfen notu kontrol ediniz!! ")
        print("Hatali Not Girisi!")
    else:   #dogru aralikda girilince durum degerini degistirir
        durum ="1"
        return durum 

#ortalamalari oku
def ortalamalari_oku():
    with open("sinav_notlari.txt","r", encoding= "utf-8" ) as file:
        for satir in file:
            #print(not_hesapla(satir))  #dizi elemani olarak yazdiriyor.
            print( not_hesapla(satir))
            ##ortalamalari, harf karsiliklarini ayri bir dosyaya kaydediliyor.
            #with open("not_ortalamalari.txt","a",encoding = "utf-8" ) as file:
            #   file.write(not_hesapla(satir) + "\n")   
       
#Not gir
def not_gir():
    
    ad = input("Ogrenci Adi: ")
    soyad = input ("Ogrenci Soyadi: ") 
    #her girilen deger icin aralik kontrolu yapýlýyor
    while True:     
        not1 = input("Not 1: ") #vize#
        olasilik= girilen_not_kontrolu(not1)
        if olasilik =="1":
            break   
    while True:
        not2 = input("Not 2: ") #final
        olasilik = girilen_not_kontrolu(not2)
        if olasilik == "1":
            break
    #not3 = input("Not 3: ")
    with open("sinav_notlari.txt","a",encoding = "utf-8" ) as file:
        #file.write(ad + " " + soyad + " " + ": " + not1 + "," + not2 + "," + not3 + "\n" )   
        file.write(ad + " " + soyad + " " + ": " + not1 + "," + not2 + "\n" )   

#notlari kaydet       
def notlari_kayit_et():
    with open("sinav_notlari.txt","r", encoding = "utf-8") as file1:
        liste =[]
        for i in file1:
            liste.append(not_hesapla(i))
        with open("not_ortalamalari.txt", "w", encoding= "utf-8") as file2:
            for i in liste:
                file2.write(i + "\n")
        print("Notlar kaydedildi.")

#not  hesaplama
def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = float(notlar[0])
    not2 = float(notlar[1])
    #not3 = int(notlar[2])
    #ortalama = ( not1 + not2 + not3 ) / 3 
    ortalama = float(not1 * (0.4)  + not2 * (0.6) )
   
    if not2<35:
        harf = "FF" + " Final notunuz yetesizdir. "
       
    elif  ortalama <= 100 and ortalama >= 90:
        harf = "AA"
    elif ortalama >=85 and ortalama <= 89:
        harf ="BA"
    elif ortalama >= 80 and ortalama <= 84:
        harf = "BB"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "CB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CC"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "DC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DD"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "FD"
    elif ortalama >= 0 and ortalama <= 49:
        harf = "FF"
    else:
        raise Exception("Ortalama Hesaplama Hatasi! Aralik disi [0-100] ortalama hesaplandi.")
    return ogrenciAdi + " : " + str( int (not1)) +"--" + str( int (not2)) + "   " + str(ortalama) + " - " + harf

def dosyalari_temizle():
   dosya1 = open("sinav_notlari.txt","w",encoding = "utf-8" )
   dosya2 =  open("not_ortalamalari.txt", "w", encoding= "utf-8")


#giris tercih menusu
while True:
    islem= input(" 1- Notlari Oku\n 2- Not Gir\n 3- Notlari Kaydet\n 4- Cikis\n 5- Dosyalari Temizle\n ")
    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayit_et()
    elif islem ==  "4":
        break
    elif islem == "5":
        onay= input("Dikkat!! Dosyalarin icindeki bilgiler silinecektir. Onayliyor musunuz? e/h \n")
        if onay == "e":
            dosyalari_temizle()
            print("Dosyalarin icerigi temizlendi!!")
        else:
            print("Dosya icerikleri silinmedi.")
    else:
        print("Hatali Secim yaptiniz Lutfen Tekrar Deneyiniz")
        
