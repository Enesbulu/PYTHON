
class Person():
    def __init__(self, ilkAd, soyad):
        self.firstName = ilkAd
        self.lastName = soyad
        print("person olusturuldu")

    def who_am_i(self):
        print("I am a person..")
    
    def eat(self):
        print("i am eating")

class Student( Person ):
    def __init__(self, ilkAd, soyad, number ):
        Person.__init__(self, ilkAd, soyad )
        self.studentNumber = number
        print("student olusturuldu")
    
    #Override-(Ezme)
    def who_am_i(self):
        print("i am a student")

    def sayHello(self):
         print(F"Merhaba Ben { s1.firstName } ")



p1 = Person( "Ahmet", "Recer" )
s1 = Student( "Gulten", "Ayaz" , 12354 )
print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " +s1.lastName + " " + str(s1.studentNumber) )
p1.who_am_i()
s1.eat()
s1.who_am_i()
s1.sayHello()