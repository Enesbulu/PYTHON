import mysql.connector

#Tek giriş yapmak için oluşturulan metod
def insertProduct(name,price,imageURL,description):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root123",
        database = "node_app"
    )
    cursor = connection.cursor()
    sql = "INSERT INTO Products(name,price,imageURL,description) VALUES(%s,%s,%s,%s) "
    values = (name,price,imageURL,description)
    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata : ", err)
    finally:
        connection.close()
        print("database bağlantısı kesildi")

#Birden çok kayıt girmek için oluşturulan metod
def insertProducts(list):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root123",
        database = "node_app"
    )
    cursor = connection.cursor()
    sql = "INSERT INTO Products(name,price,imageURL,description) VALUES(%s,%s,%s,%s) "
    values = list
    cursor.executemany(sql,values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata : ", err)
    finally:
        connection.close()
        print("database bağlantısı kesildi")


list = []
while True:
    name = input("ürün adi: ")
    price = float(input("fiyatı: "))
    imageURL = input("ürün resim adi: ")
    description = input("ürün açıklamasi: ")
    list.append((name,price,imageURL,description))
    durum = input("KAyıt yapmaya devam etmek istiyor musunuz?(e/h)")
    if durum == "h":
        print("Bilgiler vvaritabanına aktarılıyor..")
        print(list)
        insertProducts(list)
        break



# insertProduct(name,price,imageURL,description)

