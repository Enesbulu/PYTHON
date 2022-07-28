import pymongo

# myclient= pymongo.MongoClient("mongodb://localhost:27017")    #localhost/local bağlantısı
myclient= pymongo.MongoClient("mongodb+srv://root:zhi9GnHsOkojnM1W@cluster0.haujj.mongodb.net/test")  #uzak sunucu bağlantısı

mydb = myclient["node-app"] #serverda node-app database varlığını kontrol eder
print(mydb.list_collection_names()) #database de olan collection ları listeler
print(myclient.list_database_names())   #serverda bulunan database leri listeler

