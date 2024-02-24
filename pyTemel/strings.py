# -*- coding: utf-8 -*-
# substring
mesaj = "Merhaba dünya"
print(mesaj[2:13])
yeniMesaj = mesaj[12:13]
print(yeniMesaj)

#len
print(len(mesaj))
yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

#lower upper
print(mesaj.upper())
print(mesaj.lower())

#replace
#mesaj = mesaj.replace("ü", "u")
print(mesaj.replace("ü", "u"))
print(mesaj.replace("a", "e"))

#split ve strip
bilgi = "           yiğit ali 20 Uşak ".strip()
print(bilgi.split())
print("adı = " + bilgi.split()[0])
print("soyadı =" + bilgi.split()[2])


#input
#ad = input("Adınız?")
sayi1 = input("Sayı 1 =? ")
sayi2 = input("Sayı 2 =? ")
print(int(sayi1)+int(sayi2))


#TEKRAR AMAÇLI ÇALIŞMA
#%%
# substring / veriyi istedigimiz sıra aralıgında gosterir
isim = "yiğit ali "
print(isim[0:5])
yeniMesajj = isim[6:15]
print(yeniMesajj)
#%%

#len /verinini uzunlugunu soyler
print(len(isim))
yeniİsim= isim[len(isim)-1: len(isim)]
print(yeniİsim)
#%%
#lower upper / buyuk & kucuk harflerle yazar
print(isim.lower())
print(isim.upper())
#%%

#replace / eskiyi yeniyle degistirir
print(isim.replace("ali", "ALİ"))
print(isim.replace("yiğit ali ", "Ekrem Umut "))
#%%

#split ve strip /listeyi parçalar ayrı ayrı tazar
arabaParçaları = "     lastik jant direksiyon dikizAynası klima akü"
print(arabaParçaları.split()) #PARANTEZ İCİNE NE YAZARSAN ONU LİSTEDE ARAR VE ONA GORE AYİRİR !!!
print("Gerekli parça = " + arabaParçaları.split()[0])
#%%

#input /kullanıcıdan veri ister
babaAdi= input("Baba Adı ?")
anneAdi = input("Anne Adı ?")
print(babaAdi+" " +anneAdi+"'yü"+" seviyor...")

#%% 
#sort / veri içindeki kelimeleri alfabetik sıralar
cumle = "bugün hava çok güzel"

kelimeler = cumle.split()
kelimeler.sort()

# print(kelimeler)

for kelime in kelimeler:
    print(kelime)
