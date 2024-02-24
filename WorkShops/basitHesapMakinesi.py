islemler = ("1 = Toplama","2 = Çıkarma","3 = Çarpma","4 = Bölme")

for i in islemler:
    print(str(i))


islem = int(input("İşlem Seçiniz..."))
if islem > 4 :
    print("Yanlış İşlem")
else:
    sayi1 = int(input("Sayı 1 = "))
    sayi2 = int(input("Sayı 2 = "))
    
        
if islem == 1:
    print(sayi1 + sayi2)
            
if islem == 2:
    print(sayi1 - sayi2)
            
if islem == 3:
    print(sayi1 * sayi2)
            
if islem == 4:
    print(sayi1 / sayi2)
 
    
    
   

#%%
# farkli yapilisi

islemler = ("1 = Toplama","2 = Çıkarma","3 = Çarpma","4 = Bölme")

for i in islemler:
    print(str(i))

def topla (sayi3,sayi4):
    return sayi3 + sayi4

def cikar (sayi3,sayi4):
    return sayi3 - sayi4

def carp (sayi3,sayi4):
    return sayi3 *sayi4

def bol (sayi3,sayi4):
    return sayi3 / sayi4

islemz = int(input("İşlem Seçiniz..."))

if islemz > 4:
    print("Geçersiz İşlem !!")

else:
    sayi3 = int(input("Sayı 1 = "))
    sayi4 = int(input("Sayı 2 = "))

if islemz == 1:
    print(topla(sayi3, sayi4))
    
elif islemz == 2:
    print(cikar(sayi3, sayi4))
    
elif islemz == 3:
    print(carp(sayi3, sayi4))

elif islemz == 4:
    print(bol(sayi3, sayi4))








