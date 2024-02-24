
import pandas as pd
import numpy as np

data = np.array(["Yiğit","Zeynep","Ayşe","Fatma"])
s = pd.Series(data, index=[1,2,3,4]) # index =[] yaparsak verilerin indexini secebiliriz
print(s)
print(s[1]) # 1. elemani cagirir 
# indexini degistirdigin icin kullandigin indexleri yazabilirsin 
#orn: 0. indexi vermez


data2 = {"Matematik":10, "Fizik":20, "Beden Eğitimi":100} # dictinoray = sozluk

s2 = pd.Series(data2, index = ["Beden Eğitimi","Matematik","Fizik"])
print(s2)


# print(s2[0]) # data ne olursa olsun sonradan indexi degisirse oyle kalir
# print(s2["Matematik"])



# s3 = pd.Series(5, index=[1,2,3,4,5]) 
# print(s3)
