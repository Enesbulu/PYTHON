#error handling => Hata Yonetimi

"""
try:
    x =  int( input( " x:  " ) )   
    y =  int( input( " y:  " ) )   
    print( x/y )

except (ZeroDivisionError, ValueError) as exc:
    print(" hatali deger girdiniz. ")
    print(exc)
    """

while True:
    try:        #hatanin alinacagi yer
        x =  int( input( " x:  " ) )   
        y =  int( input( " y:  " ) )   
        print( x/y )

    except Exception as ex :    #hatanin yakalanip gosterildigi yer
        print(" hatali deger girdiniz. ", ex)
    
    else:   #hata yakalanmazsa calisan yer
        break
    finally:    #her iki durumda da calisan yer
        print(" try except sonlandi. ")
