
import json
import os

#User Class
class User:
    def __init__(self,username,password, email):
        self.username = username
        self.password = password
        self.email = email

#class USerRepository: kullanici bilgileri tutuluyor, isleniyor, gosteriliyor.
class UserRepository:
    def __init__(self):
        self.users = [] #kullanicinin bilgileri dizi olarak tutulur.
        self.isLoggedIn = False #kullanici login oldu mu?
        self. currentUser = {} #giris yapan kulanici bilgileri tutulacak
        self.loadUsers()

#loadUsers 
    def loadUsers(self):
        if os.path.exists(" users.json"):
            with open(" users.json","r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:   
                    user = json.loads(user)
                    newUser = User(username = user["username"], password = user["password"], email = user["email"] )
                    self.users.append(newUser)
            

#register : kayit ol
    def register(self, user : User ):
        self.users.append(user)
        self.saveToFile()
        print("Kullanici olusturuldu.")
        

#login
    def login(self,username,password):
        
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print("login yapildi.")
                break

#logout
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Cikis Yapildi.")

#Identity   giris yapan kisinin bilgierini isler
    def identity(self):
        if self.isLoggedIn:
            print(f"USERNAME: { self.currentUser.username }")
        else:
            print("Giris Yapilmadi.")


 #saveToFile    : dosyaya (veri tabani/ .json dosyasina) kaydetme
    def saveToFile(self):
        list = []
        list.append( json.dumps(user.__dict__) +"\n")    #user class indaki bilgileri listeye atarak .json dosyasina kaydediyoruz.
        with open( " users.json","w") as file:
            json.dump(list, file)



repository = UserRepository()   #kullanici deposu olusturma, kullanici bilgilelri saklamak icin

#Secim Menusu
while True:
    print("Menu".center(50,"*"))
    secim= input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\n Seciminiz: ")
   
    if secim == "5" :   #uygulamadan cikma
        break

    else:
        if secim == "1" :   #register  : #kullanici bilgileri aliniyor
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            user = User(  username = username, password = password,email = email  ) #bilgiler user class icine parametre olarak gonderiliyor 
            repository.register(user)
            print(username)
            

        elif secim == "2" : #login : giris yapma
            if repository.isLoggedIn:
                print("Zaten login oldunuz.")

            else:
                username = input("username : ")
                password = input("password : ")
                repository.login(username, password)


        elif secim == "3" : #logout : cikis yapma
            repository.logout()
            

        elif  secim == "4"  :   #display username  : kullanici adini gosterme
            repository.identity()   #kimlik deposu
           
            
        else:
            print("!!Yanlis secim. Lutfen tekrar deneyiniz.")

