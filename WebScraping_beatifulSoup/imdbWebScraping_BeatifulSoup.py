import requests
from bs4 import BeautifulSoup


url ="https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=470df400-70d9-4f35-bb05-8646a1195842&pf_rd_r=VX3MD8YSQDDZCSBGZ5ZV&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=topenglish&ref_=chttentp_ql_3"
html = requests.get(url).content    #sayfa html kodları çwkiliyor
soup =BeautifulSoup(html,"html.parser") #çekilen kodlar htmlden işlenebilir hale çevriliyor.

list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=10) #cekilecek bilgilerin filitrelendiği yer
for tr in list:
    title = tr.find("td",{"class": "titleColumn"}). find("a").text  #film adi
    year =tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")   #film yapım yılı
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text  # imdb puanı
    print(title +" - "+ year + " -- " + rating)

