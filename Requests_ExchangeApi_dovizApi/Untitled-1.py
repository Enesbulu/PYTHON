import requests
import json

api_url ="https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz"

result = requests.get(api_url ) #url den çekilen degerler json olarak result a atılıyor.
result = json.loads(result.text)    # json türünden resulta dictionary/sözlük olarak result a aktarılıyor.

print("USD/TR   Alış: " + result["USD"]["BanknoteSelling"] + " -- " + "Satış: " + result["USD"]["BanknoteBuying"])  #kur değerler yazdırılıyor.
print("EUR/TR   Alış: " + result["EUR"]["BanknoteSelling"] + " -- " + "Satış: " + result["EUR"]["BanknoteBuying"])

# usd_satis = result["USD"]["BanknoteBuying"]
# usd_alis= result["USD"]["BanknoteSelling"]
# euro_alis= result["EUR"]["BanknoteSelling"]
# euro_satis = result["EUR"]["BanknoteBuying"]

bozulan_doviz = input("bozulan döviz türü:(USD,EUR,...)  ")
alinan_doviz= input("alınan döviz türü:(USD,EUR,...)  ")

miktar = float(input(" Bozdurmak istediğiniz miktar: "))

bozulan_doviz = float(result[bozulan_doviz]["BanknoteBuying"])
alinan_doviz = float(result[alinan_doviz]["BanknoteSelling"])


hesapla = (bozulan_doviz/alinan_doviz) * miktar

print(hesapla)



