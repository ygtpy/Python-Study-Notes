

import sys

liste = [7,"yiğit",0,2,"9"]

for x in liste:
    try:
        print("Sayı = " + str(x))
        sonuc = 70/ int(x)
        print("Sonuç = " + str(sonuc))

        
    except ValueError:
        print("Hata = Bir sayı giriniz! " + str (sys.exc_info()[0]))

        
    except ZeroDivisionError:
        print("Hata = Payda sıfır olamaz " + str(sys.exc_info()[0]))
        
    finally:
        print("işlemler bitti") 
        print("")
        
        # ister try calısın yada except calıssın her turlu çalısan, yazilimi patlatmadan devam etmesini saglayan kod blogu