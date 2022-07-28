import pymongo

myclient= pymongo.MongoClient("mongodb+srv://root:zhi9GnHsOkojnM1W@cluster0.haujj.mongodb.net/test")  #uzak sunucu bağlantısıS
mydb = myclient["node-app"] #serverda node-app database varlığını kontrol eder
mycollection= mydb["products"]

"""product = {"name":"Samsungs10", "Fiyatı":"10000"}   #eklenecek kayıt
result = mycollection.insert_one(product)    #1 adet kaydı ekleme
print(result)
print(type(result))
print(result.inserted_id)   #object id yiyazdırır
"""

#veritabanına eklenecek kayıtlar 
productList =[  
    {"name":"Samsungs11", "Fiyatı":"11000","aciklama":"almaya gerek yok"},
    {"name":"Samsungs9", "Fiyatı":"9000","kategori":["telefon","elektronik"]},
    {"name":"Samsungs8", "Fiyatı":"8000"},
    {"name":"Samsungs12", "Fiyatı":"20000"}
]
sonuc = mycollection.insert_many(productList)   #çok sayıda kayıt etmek için
print(sonuc.inserted_ids)   #Kayıtların id sini yazdırır.