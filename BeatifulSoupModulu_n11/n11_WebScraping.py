from hashlib import new
from unicodedata import name
import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class":"column"}, limit=2)

for li in list:
    name = li.div.a.h3.text #ürün adını çeker
    link = li.div.a.get("href") #ürünün linkini çeker
    # oldPrice = li.find("div",{"class":"pro"},{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    newPrice = li.find("div",{"class":"priceContainer"}).text.strip().strip("TL")
    # print(oldPrice)
    print(newPrice)

