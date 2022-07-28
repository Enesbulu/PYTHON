from selenium import webdriver 
from selenium.webdriver.common.by import By #import edilmeden xpath dosyaları kullanımı yapılamıyor. Selenium 4.3.0
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = [] 
    
    def singIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(1)

        '''
        # self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        # username =self.browser.find_element(_by_xpath)("//*[@id='login_field']")
        # password= self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        # self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        '''
        #username ve password girişi için
        self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)   #Selenium 4.3.0 da kullanım şekli olarak böyle 
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)  #Selenium 4.3.0 da kullanım şekli olarak böyle 
        
        '''
        # username.send_keys(self.username) 
        # password.send_keys(self.password)
'''
        
        # time.sleep(1)
       #SingIn buton a basmak için
        self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[12]").click() #Selenium 4.3.0 da kullanım şekli olarak böyle 

    def loadFollowers(self,links):
        links[0].click()
        time.sleep(1)
        items = self.browser.find_elements(By.CSS_SELECTOR,".d-table-cell.col-9.v-align-top.pr-3")
        for itm in items:
            self.followers.append((itm.find_element(By.CSS_SELECTOR,"span.f4.Link--primary").text)+" // " + (itm.find_element(By.CSS_SELECTOR,"span.Link--secondary").text))

    def getFollowers(self):
        # self.browser.get(f"https://github.com/{self.username}?tab=followers")    #kullanıcının takipciler sayfası link
        self.browser.get("https://github.com/sadikturan?tab=followers")
        time.sleep(1)
        # item = self.browser.find_elements_by_css_selector()
        print("takipçiler:")
        items = self.browser.find_elements(By.CSS_SELECTOR,".d-table-cell.col-9.v-align-top.pr-3")
        for itm in items:
            # print(itm.find_element(By.CSS_SELECTOR,"span.f4.Link--primary").text)#isimler
            # print(itm.find_element(By.CSS_SELECTOR,"span.Link--secondary").text)    #kullanıcı adları
            # print((itm.find_element(By.CSS_SELECTOR,"span.f4.Link--primary").text)+" // " + (itm.find_element(By.CSS_SELECTOR,"span.Link--secondary").text) )
            # self.followers.append(itm.find_element(By.CSS_SELECTOR,"span.Link--secondary")).text
            # self.followers.append(itm.find_element_by_css_selector("span.Link--secondary")).text
            self.followers.append((itm.find_element(By.CSS_SELECTOR,"span.f4.Link--primary").text)+" // " + (itm.find_element(By.CSS_SELECTOR,"span.Link--secondary").text))
        
        while True :
           
            links = self.browser.find_element(By.CLASS_NAME,"pagination").find_elements(By.TAG_NAME,"a" )

            if len(links) == 1:
                if links[0].text == "Next":
                    self.loadFollowers(links)
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        items = self.browser.find_elements(By.CSS_SELECTOR,".d-table-cell.col-9.v-align-top.pr-3")
                        for itm in items:
                            self.followers.append((itm.find_element(By.CSS_SELECTOR,"span.f4.Link--primary").text)+" // " + (itm.find_element(By.CSS_SELECTOR,"span.Link--secondary").text))
                    else:
                        continue





#kullanıcıdan username ve password girişi alma
username =input("Kullanıcı adı: ")
password = input("Şifre: ")
github = Github(username, password) #github classından nesne türet ve class a username ve pasword parametrelerini gönder
github.singIn()  #github nesnesinin singIn fonksiyonunu çalıştır
github.getFollowers()  
print(len(github.followers)) #
print(github.followers)

time.sleep(4)
github.browser.close()