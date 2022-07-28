import pymongo
from bson.objectid import ObjectId

myclient= pymongo.MongoClient("mongodb+srv://root:zhi9GnHsOkojnM1W@cluster0.haujj.mongodb.net/test")  #uzak sunucu bağlantısı
mydb = myclient["node-app"] #serverda node-app database varlığını kontrol eder
mycollection= mydb["products"]

#Çok sayida kaydın filitreyle alınması
"""filter = {"name":"Samsungs11"}
sonuc = mycollection.find(filter)
for i in sonuc:
    print(i)"""

#Tek bir kaydın flitrelemesi
"""filitre = {"name":"Samsungs11"}
result = mycollection.find_one(filitre)
print(result)"""

#id ye göre sorgulama
"""sonuc1 = mycollection.find_one({"_id":ObjectId("62dbe11d6363c04d4828527a")})    #ObjectId import edilmeden dönüşüm yapılamadığı için hata verir
print(sonuc1)"""

#özel filitreleme için operatör kullanımı
"""result1 = mycollection.find({
    "name":{
        "$in" : ["Samsungs9" , "Samsungs8"] #Samsungs9 ve Samsungs8 geçen degerleri alır
    }
})

for i in result1:
    print(i)"""

result2 = mycollection.find({"Fiyatı":{ '$gt' : 10000 }})   #olması gerektiği gibi çalışmıyor. Değer döndürmüyor.
# print(result2)
for i in result2:
    print("deger")
    print(i)





