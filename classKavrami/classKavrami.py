#class kullanarak dairenin cevresini ve alanini bulma

class Circle:
    #Class object attributer /Class seviyesinde tanimlama
    pi =  3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

     #Methods 
    def cevre_hesapla(self):
         return  2 * self.pi * self.yaricap
     
    def alanHesapla(self):
         return self.pi * (self.yaricap ** 2)

daire1 = Circle()   #yaricap degeri girilmediginde default 1 degerini alacak
daire2 = Circle(5)  #yaricap deerinin kendi isteginize gore gonderiyoruz bu sefer
print(f"c1 Alan: { daire1.alanHesapla() } Cevre: { daire1.cevre_hesapla() } ")
print(f"c2 Alan: { daire2.alanHesapla() } Cevre: { daire2.cevre_hesapla() } ")
