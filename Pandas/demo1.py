

import pandas as pd

notlar = pd.read_csv("grades.csv")

notlar.columns = ["İsim","Soyisim","Öğrenci Numarası","Test 1"
                  ,"Test 2","Test 3","Test 4","Final","Sonuc"]
notlar.index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]


print(notlar)


print(notlar.head())
print(notlar.tail())

print(notlar["Öğrenci Numarası"])
print("                     ")

print(notlar.iloc[3]) # indexe gore veriyi ceker
print("                     ")
print(notlar.loc[4]) # sira numarasina gore gosterir


print("                     ")
print(notlar[0:10]) # 0 inci index'ten 9 a kdr verileri yazar


#%%
isimler = (0,1,2,3,4,5,6,7,8,9)

print(isimler[0:5])












