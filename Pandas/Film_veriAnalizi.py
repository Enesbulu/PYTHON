import pandas as pd
df = pd.read_csv("IMDB_ErrorLogIDs1_OMDB_Detailed.csv")

##Dosya hakkında bilgilerin yazdırılması
'''result = df #dosya hakkında bilgiler verir
result = df.columns #column/sütun bilgilerini yazdırır
result = df.info    #dataframe hakkında bilgiler verir
print(result)'''

##İlk kaydı alma
"""sonuc = df.head() #ilk  5 kaydı alma
print(sonuc)

sonuc = df.head(10) #ilk 10 kaydı alma
print(sonuc)"""

##Son Kaydı gösterme
"""sonuc = df.tail()   #son 5 kayıt
print(sonuc)

sonuc = df.tail(10)
print(sonuc)"""

##Sadece Title kolonunu alma
"""sonuc = df["Title"] 
print(sonuc)

sonuc = df["Title"].head()  #title konolunun ilk 5 satırı
print(sonuc)"""

##Title ve Rated bilgilerinin yazdırılması
"""sonuc = df[["Title","Rated"]]   #Tİtle ve Rated verilerinin hepsini yazdırır.
print(sonuc)

sonuc = df[["Title","Rated"]].head ()   #Tİtle ve Rated verilerinin ilk 5 tanesini yazdırır
print(sonuc)
 
sonuc =  df[["Title","Rated"]].tail(9)  #Tİtle ve Rated verilerinin son 9 tanesini yazdırır
print(sonuc)

sonuc = df[["Title","Rated"]][5:].head()    #İkinci 5 kaydı yazdırma
print(sonuc)

sonuc = (df[ ["imdbRating"]].astype(int).head(50))>8.0  #ilk 50 filmin puanı 8 den büyük küçük olma durumu
print(sonuc)"""

# sonuc = df[df["imdbRating"] >= 2.0].head(10)

# print(sonuc)

"""
sonuc = pd.to_numeric(df["Year"].head())    #sorun var convert edilemedi
# sonc =pd.to_numeric(sonuc)
print(sonuc)"""



