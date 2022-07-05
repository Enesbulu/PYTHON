import random

print("0-100 arasi rastgele sayi yi bilmeniz istenmektedir.\n__IYI EGLENCELER__\n")
sayi = random.randint(0,10)
hak = caniniz = int(input("Kac defada bilebilirsiniz?  "))
sayac = 0

while hak > 0 :
    hak -= 1
    tahmin = int(input("Tahmininiz: "))
    sayac += 1
    if sayi == tahmin:
        print(f"Dogru tahmin. {sayac} defada bildiniz. Puaniniz: {100 - (100/caniniz) * (sayac -1)}")
        break
    elif sayi > tahmin :
        print("yukari")
    else:
        print("asagi")

    if hak == 0 :
        print(f"Hakkiniz kalmadi. Dogru sayi : {sayi}")