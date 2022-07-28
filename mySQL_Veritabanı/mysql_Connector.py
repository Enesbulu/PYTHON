#MySql e bağlanma, giriş yapma ve bit tablo oluşturma işlemleri
import mysql.connector

#veritabanına bağlantı ve giriş yapıldı.
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root123",
    database = "mydatabase" #kullanılacak database belirtilmesi
)


print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase") #CREATE DATABASE sql komutuyla mydatabase varitabanı oluşturuldu.

"""#Oluşturulmuş database lerin hepsini gösterir
mycursor.execute("SHOW DATABASES")  
for x in mycursor:
    print(x)"""

# mycursor.execute("CREATE TABLE customers ( name VARCHAR(255), address VARCHAR(255))") #tablo oluşturuldu


mycursor.execute("SHOW DATABASES")  
for x in mycursor:
    print(x)
