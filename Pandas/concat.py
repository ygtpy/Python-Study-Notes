import pandas as pd


data1 = {
            'id':[1,2,3,4],
            'ad':["Ayşe","Hatice","Fatma","Mehmet"],
            'soyad':["x","x","x","x"]
        }

data2 = {
            "id":[1,3,4,7],
            "ad":["Yiğit","Zeynep","Döndü","Mustafa"],
            "soyad":["x","x","x","x"]
        }

data1df = pd.DataFrame(data1)
data2df = pd.DataFrame(data2)



print(pd.concat([data1df,data2df])) # iki veya daha fazla tabloyu alt alta birlesirir

print(pd.concat([data1df,data2df]),axis=1) # iki veya daha fazla tabloyu yan yana birlestirir 

# örn : 1'inci tablo kişilerin ad soyad olsun 2'inci tablo ise ayni kisilerin ikameti vs olsun,
# bu tur parcali tablolari birlestirmek icin kullanilir




