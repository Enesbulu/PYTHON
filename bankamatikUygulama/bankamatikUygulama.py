#Bankamatik Demo Uygulamasi
AhmetHesap = {
    'ad': 'Ahmet Cengiz',
    'hesapNo':'1234567',
    'bakiye' : 3000,
    'ekHesap':2000
    }
AliHesap = {
    "ad" : "Ali Semih",
    "hesapNo" :"9876543", 
    "bakiye": 2000,
    "ekHesap": 1000
    }

def paraCek(hesap, miktar):
    print("Merhaba ",hesap['ad'])
    if (hesap['bakiye'] >= miktar):
        hesap["bakiye"]  -= miktar
        print("paranizi cekebilirsiniz.")
    
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
       
        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanilsin mi? (e/h)")

            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKullanilacakMiktar
                print("paranizi alabilirsiniz.")
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.")
        else:
            print("uzgunuz bakiyeniz yetersiz")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} kadar paraniz vardir.")
    print(f"Ek hesap limitinizde ise {hesap['ekHesap']} TL bulunmaktadir.")

cekilecekTutar=int(input("Lutfen Cekmek istediginiz miktari giriniz: "))
paraCek(AhmetHesap, cekilecekTutar)
bakiyeSorgula(AhmetHesap)
#paraCek(AhmetHesap, cekilecekTutar )
#bakiyeSorgula(AhmetHesap)

