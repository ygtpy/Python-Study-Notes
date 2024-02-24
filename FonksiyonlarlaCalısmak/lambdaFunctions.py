
def dikAlanHesapla(a,b):
    return a*b/2

alan =dikAlanHesapla(6, 3)
print(alan)


#  yukaridaki return eden foksiyonun daha kisa yazimi "lambda" ile yapilir
# : = için demek a*b yi return et demek

dortgenAlanHesapla = lambda a,b : a*b
print(dortgenAlanHesapla(6,4))


# fonksiyonlar da bir degiskene atanabilir (orn: sehir ="Ankara" / orn: sayi= 10 gibi) 

x = dortgenAlanHesapla
print(x(6,8))
print(type(dortgenAlanHesapla))