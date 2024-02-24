
 
import numpy as np

a = np.floor(10*np.random.random((3,4))) # floor = kusuratli sayilari en bastaki sayiya indirger
# 0 dan 10 a kdr random sayilarla 3 satir 4 sutunluk erey olustur

print(a)
print(a.shape) # dizi yapisini gosteriri ( 3,4)

print(a.ravel()) #duz bir liste gibi veriyi yazar

a = a.ravel() # esitlersek veri tamamiyle degisir
print(a)
print(a.shape)


# print(a.reshape(2,6)) # duz veriyi tablo halinde yazar
# a = a.reshape(2,6)
print(a.T)

print(a.reshape(2,-1)) # 2 satir yap kafana gore sutun ayarla demek

## ÖNEMLİ = elimizdeki bir veriyi degistirirken yeniden tablo haline duzenlerken ELEMAN SAYISINI KORU
#               örnek
#   a = np.floor(10*np.random.random((3,4)))   \              12 eleman
#    a = a.reshape(2,6)                        / ikisinde de               var

