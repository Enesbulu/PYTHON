from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Edge()
        self.username = username
        self.password = password

#instagram sayfasına giriş  -Çalışıyor.
    def singIn(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        # self.browser.implicitly_wait(5) # kısa süreli kontrol ve bekleme işlemi yapar
        sleep(3)
        print("Siteye yönlendirildi.")
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        print("Giriş yapıldı.")
        sleep(5)
        print("sleep")

#takipcilerin alınması  --Metod tamamlanmadı. Kullanıcılar listeleniyor ama listesi alınamıyor!
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        self.browser.implicitly_wait(5) # kısa süreli kontrol ve bekleme işlemi yapar
        sleep(3)
        print("Kullanıcı profil sayfasına yönlendirildi.")
        followerLink = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        print( "Takipciler listeleniyor...")
        sleep(2)
        # spanlar= self.browser.find_element(By.XPATH,"//ul")
        spanlar = self.browser.find_element(By.CLASS_NAME,"_aae-")
        takipci_sayisi = len(spanlar.find_elements(By.XPATH,"//li"))    #ilk grup takipci sayisi
        sleep(0.5)
        takipci_name= spanlar.find_elements(By.CSS_SELECTOR,"#f17526545431cec > div").text() #f17526545431cec > div
        print(type(spanlar))
        print("spanlar belleğe alındı.")
        # print(f"firt count: {spanlar}")
        print(f"İLK eleman listesi: {len(spanlar)}")    #print(f"takipci sayisi: {takipci_sayisi}")   #aynı sonucu verir
        print("Takipcilerin isimleri: " + takipci_name)
        sleep(2)
        action =webdriver.ActionChains(self.browser)
        print("ilk açılan 12 takipçi listeye alındı.")
        while True: #bütün takipçilerin listelenmesi için döngü.
 ####hata var
            # spanlar.click()
            action.key_down(Keys.TAB).key_up(Keys.TAB,).perform()
            sleep(1)
            print("Tap tuşuna basıldı.")
            # self.browser.implicitly_wait(5)
            sleep(1)
            newCount = len(spanlar.find_elements(By.CSS_SELECTOR,"li"))
            if followerCount != newCount:   #bütün takipçilerin listeye alınması
                followerCount = newCount
                print(f"second count: {newCount}")
                self.browser.implicitly_wait(5)
            else:   #Takipçiler listeye eklendikten sonra döngü sonlandırılıyor.
                break
        print("Takipçiler listelendi")

        #takipçileri listeleyerek text dosyasına yazdırma
        followers = spanlar.find_element(By.CSS_SELECTOR,"li")
        self.browser.implicitly_wait(5)
        print("sleep2")
        followerList = []
        print("takipçiler diziye alınıyor...")
        for user in followers:
            link = user.find_elements(By.CSS_SELECTOR,"a").link.get_attribute("href")
            followerList.append(link)
        print("takipçiler diziye alındı.")
        print("takipçiler dosyaya yazdırılıyor...")
        with open("followers.txt", "w", encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")
        print("Takipçiler dosyaya yazdırıldı.")
        print("Takipçileri listeleme metodu tamamlandı.")


#kullanıcı takip etme metodu    #Çalışıyor
    def followUser(self,username):
        print("Kullanıcı takip fonksiyon başlıyor.")
        self.browser.get("https://www.instagram.com/" + username)
        # sleep(5)
        self.browser.implicitly_wait(5)
        print("Takip edilecek  profile gidildi.")
        followButton= self.browser.find_elements(By.TAG_NAME,"button")
        followButton=followButton[1]
        # followButton = self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_GO']/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button").text
        # followButton = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button/div").text
        # sleep(5)
        self.browser.implicitly_wait(5)
        print("Hesap takip durumu kontrol edilecek...")
        if followButton.text == "Takip Et":
            followButton.click()
            print("Hesap takip edilmeye başlandı.")
        else:
            print("Zaten takiptesin")
        # print(followButton.text)
        # print("Hesab" + username)
        print("Hesap takip metodu tamamlandı.")

#takip bırakma metodu  #Çalışıyor.
    def unFollowUser(self, username):
        print("Hesap takip bırakma fonksiyonu çalışmaya başladı.")
        self.browser.get("https://www.instagram.com/"+ username)
        # sleep(3)
        self.browser.implicitly_wait(5)
        print("Hesabın profiline yönlendirili.")
        # followButton = self.browser.find_element(By.TAG_NAME,"button")
        followButton = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/div/span/span[1]/button")
        print("Hesap takip durumu değerlendiriliyor...")
        if followButton.text != "Takiptesin":
            followButton.click()
            print("Takibi bırak butonuna basıldı.")
            sleep(3)
            onaylamaButonu = self.browser.find_element(By.XPATH,'//button[text()="Takibi Bırak"]')
            onaylamaButonu.click()
            print("Takibi bırakma onaylandı.")
            print("Takipten çıkıldı!\a")
        else:
            print("Zaten takip etmiyorsunuz!\a")



username = input("Kullanici Adı / Mail adresi: ")
password = input("Şifre: ")



inst = Instagram(username,password) #girilen kullanıcı adı ve şifre ile istenen işlemleri
inst.singIn()   #giriş yap 
inst.getFollowers()   #takipcileri listele    2+10-7 sn
sleep(4)
# inst.followUser("btkakademi") #kullanıcıyı takip et 5+5 sn
# inst.unFollowUser("btk")    #Hesabı takibi bırakma  3+3 sn
sleep(2)
print("Browser kapatılıyor...")
sleep(1)
inst.browser.close() #tarayıcıyı kapatma
print("Browser kapatıldı.")
