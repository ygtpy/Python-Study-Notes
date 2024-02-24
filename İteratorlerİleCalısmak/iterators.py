
import sys
sehirler = ["Uşak","Isparta","İstanbul","Ankara"]


iteratorum = iter(sehirler)
try:
    print(next(iteratorum))
    print(next(iteratorum))
    print(next(iteratorum))
    print(next(iteratorum))
    print(next(iteratorum))
except:
    print( str(sys.exc_info()[0]))


# iterator bir liste tuple dictinoary farketmez icindeki verileri donduren komuttur
# neredeyse kullanilmaz onun yerine for dongusu daha mantiklidir


for sehir in sehirler:
    print(sehir)
    

