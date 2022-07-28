from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from kullaniciBilgileri import username, password, kullaniciAdi

class Twitter:
    def __init__(self, username, password): #kurucu/temel metod oluşturma
        # self.browserProfil = webdriver.ChromeOptions()
        # self.browserProfil.add_experimental_option('prefs',{"intl.accept_languages":"en, en_US"})   #Chrome dilini ingilizce frofil oluşturuyor.
        # self.browser = webdriver.Chrome("chromedriver.exe", chrome_options= self.browserProfil )    #oluşturulan profile göre Chrome tarayıcısını açıyoruz.
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.kullaniciAdi =kullaniciAdi

    def singIn(self):
        print("--singIn Fonksiyonu Çalışmaya başladı.")
        self.browser.get("https://twitter.com/login")
        print("--Siteye gidiliyor...")
        sleep(5)
        # self.browser.get("https://twitter.com")
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        sleep(1)
        usernameInput.send_keys(self.username)
        sleep(1)
        usernameInput.send_keys(Keys.ENTER)
        # action =webdriver.ActionChains(self.browser)
        print("--Kullanıcı adı Girildi.")
        print("--Şifre sayfasına yönlendiriliyor...")
        sleep(3)
        print("--Şifre sayfasına yönlendirildi.")
        kullaniciAdiInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]")
        sleep(3)
        kullaniciAdiInput.send_keys(self.kullaniciAdi)
        kullaniciAdiInput.send_keys(Keys.ENTER)
        print("Kullanıcı adi girildi.")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        passwordInput.send_keys(self.password)
        sleep(1)
        print("--şifre girişi yapıldı.")
        passwordInput.send_keys(Keys.ENTER)
        print("--Hesaba giriş yapıldı.")
        sleep(5)
        print("--sleep bitti")










# username = input("Kullanıcı adı/e-pasta giriniz: ")
# password = input("Şifrenizi giriniz: ")
twt_bot = Twitter(username,password)
twt_bot.singIn()


twt_bot.browser.close()