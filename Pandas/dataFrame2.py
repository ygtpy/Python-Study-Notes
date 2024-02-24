

import pandas as pd

data = [["Engin",33,"Ankara"],["Derin",4,"İstanbul"],["Salih",32,"Mardin"]]
df = pd.DataFrame(data,columns=["İsim","Yaş","İkamet"],index=[1,2,3])
print(df)



data2 = {"İsim": ["Yiğit ali","Döndü","Mustafa"],
        "Yaş": [20,42,44],
        "İkamet": ["Isparta","Uşak","Ankara"]}
df2 = pd.DataFrame(data2,columns=["İsim","Yaş","İkamet"],index=[1,2,3])

print(df2)
print("             ")

# print(df2.loc[1]) # sira numarasina gore gosterir
# print(df2.iloc[0]) # indexe gore veri gosterir

# df3 = df2.append(df) # 2 farkli datlari formatlari ayni ise birlestirir
# print(df3)

print(df2.head()) # en bastan 5 veriyi gosterir
print(df2.tail()) # sondaki 5 datayi gosterir