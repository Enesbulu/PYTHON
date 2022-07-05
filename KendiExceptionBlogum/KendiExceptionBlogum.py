
""""
x = "10
if x > 5 :
    raise Exception("x 5 den buyuk olamaz.")  # kendi hata kodumuzu yazdik
"""

"""
def check_password(pws):
    import re        #re.search metodunu kullanmak icin import edildi
    if len(pws) < 8 :
        raise Exception("parola en az 8 karater olmalidir. ")
    elif not re.search("[a-z]", pws):
        raise Exception("parola kucuk harf icermelidir")
    elif not re.search("[A-Z]", pws):
        raise Exception("parola buyuk harf icermelidir")
    elif not re.search("[0-9]", pws):
        raise Exception("parola sayi icermelidir")
    elif not re.search("[_@!.]", pws):
        raise Exception("parola alpha numeric icermelidir")
    elif re.search("\s",pws):
        raise Exception("bosluk karakteri kullanamazsiniz ")

password = "1234567aA."
try:
    check_password(password) 
except Exception as exc:
    print(exc)
else:
    print("gecerli parola")
finally:
    print("validation tamamlandi")
    """



class Person:
    def __init__(self,name, year):
        if len(name)>10:
            raise Exception("name 10 karakterden buyuk olamaz")
        else:
            self.name = name


p = Person("Aliiiiiisdsdsdsffsfsf",1999)


