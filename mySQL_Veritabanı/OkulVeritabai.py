from datetime import datetime
from connections import connection
import mysql.connector

class Student:

    connection =connection
    mycursor = connection.cursor()
    def __init__(self,studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student( StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)
        try:
            Student.connection.commit()
            print( f"{Student.mycursor.rowcount} tane kayıt eklendi.")

        except mysql.connector.Error as err:
            print("Hata: ",err)
        finally:
            print("Veritabanı bağlantısı kesildi.")
            Student.connection.close()
        
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student( StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print( f"{Student.mycursor.rowcount} tane kayıt eklendi.")

        except mysql.connector.Error as err:
            print("Hata: ",err)
        finally:
            print("Veritabanı bağlantısı kesildi.")
            Student.connection.close()



# ahmet = Student("108","ahmet","yılmaz",datetime(2005,5,17),"E")
# ahmet.saveStudent()
# print("işlem tamamlandı")

"""mycursor.execute("SHOW DATABASES")  
for x in mycursor:
    print(x)"""

ogrenciler = [
    ("201","Ahmet","Yılmaz",datetime(2005,5,17),"E"),
    ("202","Hasan","Ozgür",datetime(2007,6,17),"E"),
    ("203","Nur","Kurt",datetime(2002,5,18),"K"),
    ("204","Aysel","Yaka",datetime(2003,7,17),"K")
]

Student.saveStudents(ogrenciler)


"""mycursor.executemany(sql,ogrenciler )
try:
    connection.commit()
    print( f"{mycursor.rowcount} tane kayıt eklendi.")

except mysql.connector.Error as err:
    print("Hata: ",err)
finally:
    print("Veritabanı bağlantısı kesildi.")
    connection.close()"""

