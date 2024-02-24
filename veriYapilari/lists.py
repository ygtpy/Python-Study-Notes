
#ekleme /çıkarma
ogrenciler = ["yiğit","sude","emir"]
ogrenciler.append("emine")
ogrenciler.remove("sude")
print(ogrenciler)
print(ogrenciler[2])


#list constructor
sehirler= list(("uşak","antalya"))
print(sehirler)
print(len(sehirler))
    
#list constructor
sehirlerr = list(("uşak","antalya","izmir","antalya","antalya","antalya"))
print(sehirlerr)
print(len(sehirlerr))

#count fonksiyonu = kaç tane olduğunu söyler
print("antalya Sayısı =" + str(sehirlerr.count("antalya")))

#index = kaçıncı sırada olduğu
print("antalya indexi =" + str(sehirlerr.index("antalya"))) 

#indexine(sırasına) göre veriyi silme
sehirlerr.pop(2)
sehirlerr.pop(0)

#ekleme / liste içindeki verileri tamamen silme / ters çevirme
sehirlerr.insert(0, "Denizli")
#print(sehirlerr.clear())#
sehirlerr.reverse()
print(sehirlerr)

#                          kopyasını alma
sehirlerr3 = sehirlerr.copy()

#yeni veriyi eşitleme ( kopya oluşmaz aynı yerde olur) ve içinden veri değiştirme
sehirlerr2 = sehirlerr
sehirlerr2[0] ="kastamonu"


print(sehirlerr)
print(sehirlerr2)
print(sehirlerr3)

# listeleri birleştirme
sehirlerr.extend(sehirlerr2)

# alfabatik veya sayısal olarak listeleme
sehirlerr.sort()

sehirlerr.reverse()
print(sehirlerr)












