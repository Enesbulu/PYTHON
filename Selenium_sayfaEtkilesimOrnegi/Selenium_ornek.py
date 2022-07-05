from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# url = "http://github.com" #github sürümü farklı olduğu için çalışmıyor
url ="https://www.google.com.tr/" #google da çalışıyor.
driver.get(url)

aramaGirdi = driver.find_element("name","q")    #gönderilen parametreler
time.sleep(1)   #programı uyutuyor.
aramaGirdi.send_keys("Python")  #arama yapılacak kelime
# aramaGirdi.submit() #search işlemini yapmak için
aramaGirdi.send_keys(Keys.ENTER)
time.sleep(3)
sonuc = driver.find_elements_by_css_selector(".repo-list-item h3 a")

for element in sonuc:
    print(element.text)
driver.close()  #sayfayı kapatır.