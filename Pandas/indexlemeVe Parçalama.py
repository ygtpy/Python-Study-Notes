
import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns= ["İsim","Soyisim","Öğrenci Numarası","Test 1",
                  "Test 2","Test 3","Test 4","Final","Sonuc"]

print(notlar)

print(notlar.loc[:,"İsim"]) # tum satirlardan isimlerini ceker
print(notlar.loc[:5,"İsim"]) # tum satirlardan 5 e kdr dahil isimleri ceker
print(notlar.loc[:5,"İsim":"Test 4"]) # tum satirlardan 5 e kdr dahil isimden test 4 e kdr (her ikisi de dahil) ceker
print(notlar.loc[:5,["İsim","Soyisim","Sonuc"]]) # tum satirlardan 5 e kdr dahil isim soyisim sonuc ceker
print(notlar.loc[:5,:"Test 2"]) # tum satirlardan 5 e kdr dahil tum sutunlari test 2 dahil gosterir
print(notlar.loc[::-1,:"İsim"]) # tum satirlarin isim verisini tersten yazar
# print(notlar.loc[satir:sutun]) anlami bu




