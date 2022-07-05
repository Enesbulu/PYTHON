'''
##Dairenin yaricapi girilerek alanini ve cevresinin hesaplanmasi
##sabit pi ssayisi  pi :3.14
'''

kullaniciTercihi = True

while kullaniciTercihi:
    pi= 3.14    
    r = float(input("yaricap giriniz: "))
    daireninCevresi = pi * r ** 2
    daireninAlani = 2* pi * r
    print(f"Dairenin alani: {daireninAlani}")
    print(f"Dairenin cevresi: ",daireninCevresi)
    girdi = input("tekrar hesaplama yapmak ister misiniz? e/h\n")
    if "e" in girdi:
        kullaniciTercihi= True
    elif "h" in girdi:
        kullaniciTercihi= False
    else :
        print("Hatali parametre girildi..")

print("program sonu..")