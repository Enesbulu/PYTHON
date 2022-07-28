import pymongo

myclient= pymongo.MongoClient("mongodb+srv://root:zhi9GnHsOkojnM1W@cluster0.haujj.mongodb.net/test")  #uzak sunucu bağlantısı
mydb = myclient["node-app"] #serverda node-app database varlığını kontrol eder
mycollection= mydb["products"]

"""deger = mycollection.find_one() #bulduğu ilk kaydı görüntüler
print(deger)"""

#Bütün degerlerin kolon bilgileriyle getirir
"""for i in mycollection.find():
    print(i)"""

for i in mycollection.find({},{"_id":0,"name":1,"Fiyatı":1}):   #Bütün verileri filitreleyerek getirir.0 ları almaz, 1leri alır
    print(i)




