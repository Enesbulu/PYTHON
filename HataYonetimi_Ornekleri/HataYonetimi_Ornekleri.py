
#liste elemanairi icindeki sayisal degerleri bulma
"""
liste = ["1","2","3","4","5a","asd","50 ","08c"]    

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
"""


#kullanici q ya basmadikca her inputun sayi olmasini kontrol eden fonksiyon
"""
while True:
    sayi = input("sayi: ")
    if sayi == "q":
        break   #donguden cikmak icin 
    try:    #hatanin alinabilecegi kod blogu
        result = float(sayi)
        print("girdiginiz sayi: ", result )
        break   #donguden cikmak icin 
        
    except:
        print("gecersiz sayi")  #hata mesaji
        continue    #donguyu hata alsa da devam ettirir
"""


#girilen parolda icinde turkce karakterde hata firlatma
"""
turkce_karakterler = ' ' #turkce karakterler ide sebebiyle syntaxError utf-8 hatasina dusuyor
parola = input("parola: ")
for i in parola:
    if i in turkce_karakterler:
        raise TypeError("Parola turkce karakterler iceremez")
    else:
        pass
print("gecerli parola.. ")
"""


#faktoriyel fonksiyonu oluþturup gelen degere hata mesaji üretme
"""def faktoriyel(x):
    x = int(x)
    if x< 0:
        raise ValueError("Negatif deger")

    result = 1
    for i in range(1, x+1):
        result *= i
    return result

for x in [5,10,20,30,45,"80a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err :
        print( err )
        continue
    print(y)
 """