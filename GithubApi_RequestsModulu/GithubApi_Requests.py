import requests
 
class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"  #github api linki
        self.token = "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" #token

    #kullanıcıyı bulan metod
    def getUser(self, username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()
    
    #api ile reponun listesini çeken metod
    def getRepositories(self, username):
        yanit = requests.get(self.api_url + "/users/" + username + "/repos" )
        return yanit.json()
        
    def createRepository(self, name):
        tepki = requests.post(self.api_url + "/user/repos?access_token=" + self.token, json={
            "name" :  name,
            "description" : "this is your first repo",
            "homepage" : "https://github.com",
            "private" : False,
            "has_issues" : True,
            "has_projects" : True,
            "has_wiki" : True  
        })
        print("çalıştı")
        return tepki.json()

github = Github()

while True:
    secim = input("1-Kullanıcıyı Bul\n2-Depoları Getir\n3- Depo Oluştur\n4- Çıkış\nSeçim:  ")

    if secim == "4":
        break
    else:
        if secim == "1":
            username = input("Kullanıcı adi: ")  #bulunacak kullanıcı bilgileri alınıyor
            sonuc = github.getUser(username)    #api yle veriler çekiliyor
            print(f"name: {sonuc['name']} public depo: {sonuc['public_repos']}  takipçi: {sonuc['followers']} ")  #ekrana yazdırılıyor

        elif secim == "2":
            username = input("Kullanıcı adi: ")     #repo sabihinin kullanıcı adi giriliyor
            sonuc = github.getRepositories(username)    #repolar api ile çekiliyor.
            print("depolar: \n")
            for repo in sonuc:  #ekrana yazdırılıyor.
                print(repo["name"])

        elif secim == "3":
            name = input("Repo isim: ")
            cikti = github.createRepository(name)
            print(cikti)
        else:
            print("\n\tHatalı secim yaptınız. Geçerli deger giriniz..\n")


        

