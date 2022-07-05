#kendine gonderilen sinirsiz sayidaki nesneyi bir listeye çeviren fonksiyon
"""def listeyeCevir(*params):
    liste=[]
    for param in params:
        liste.append(param)

    return liste
result = listeyeCevir(10,20,30,"merhaba")
print(result)"""


#gonderilen 2 sayi arasindaki asal sayilari bulma
"""def asalSayilariBul(sayi1, sayi2):
    for sayi in  range(sayi1,sayi2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if (sayi % i == 0):
                    break
            else:
                print( sayi)

sayi1 = int(input("sayi 1 giriniz: "))
sayi2 = int(input("sayi 2 giriniz: "))
asalSayilariBul(sayi1, sayi2)"""

#kendisine gonderilen bir sayinin tam bolenlerini bir liste seklinde dondurunuz.
def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if ( sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(20))