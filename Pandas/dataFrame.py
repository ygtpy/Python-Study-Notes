
import pandas as pd


data = [10,20,30,40,50]
df = pd.DataFrame(data)
# print(df)


data2 = ["Yiğit ",20,"Uşak"], ["Zeynep ",15,"İstanbul"], ["ilayda",42,"Ankara"], ["Mustafa",44,"Uşak"]

df2 = pd.DataFrame(data2,columns=["İsim","Yaş","İkamet"],index=[1,2,"Canım Annem","Babam"])
# columns=[] ile colon isimlerini belirleriz
# index = [] le index lerini degistirip atayabiliriz
print(df2)
print("          ")

data3 = {"İsim": ["Yiğit","Döndü","Mustafa"],
         "Yaş": [20,42,44],
         "İkamet": ["Isparta","Uşak","Uşak"]} # dictinoary(sozluk) verilerini de bu sekilde donutururuz

df3 = pd.DataFrame(data3,columns=["İsim","Yaş","İkamet"],index=[1,2,3])
print(df3)
print("     ")
# print(df3["İsim"])
# print("    ")
# print(df3["Yaş"])
# print("     ")
# print(df3["İkamet"])

# df3.pop("İkamet")
# del df3["İkamet"]
# print(df3)
# ikiside sutun siler

