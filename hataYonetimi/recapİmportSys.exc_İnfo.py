

import sys

liste = [9,"yiğit",6,4,"2",0]


for x in liste:
    try:
        print("SAYI = " + str(x))
        sonuc =90/ int(x)
        print("SONUÇ = "+ str(sonuc))

    except:
        print(str(x) + " Hesaplanamadı :( " + str(sys.exc_info()[0]))
        
        
        
     #farklı yazımı   
        
import sys

lists =[9,"yiğit",6,4,"2",0]

for i in lists:
    try:
        print("Sayı= " + str(i))
        sonucc = 90/int(i) 
        print("Sonuc= "+ str(sonucc))
        
    except ValueError:
        print(str(i) + " bir sayı değil " + str(sys.exc_info()[0]))
        
    except ZeroDivisionError:
        print(str(i) + " sıfıra bölüm olamaz " + str(sys.exc_info()[0]))
    except :
        print("Bir hata oluştu")
        

#%%

import sys

for x in liste:
    try:
        print("sayı= ", str(x))
        sonuclar = 2* int(x)
        print("sonuç= ",str(sonuclar))
    except:
        print(str(x),"hesaplayamadık abii ",str(sys.exc_info()[0]) )
    finally:
        print("İŞLEMLER BİTTİ ÇOK ŞÜKÜR")