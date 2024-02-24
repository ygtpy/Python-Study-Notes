

import numpy as np

sayilar = np.array([0,5,10,15,20,25,30])

print(sayilar[::-1]) # tersten butun verileri siralar
print(sayilar[::1])
# print(sayilar[2])
# print(sayilar[2:6])
print(sayilar[0:1])


sayilar2 = np.array([[0,5,10],[15,20,25]])
print(sayilar2[0,2]) #	 0 inci gruptan indexi 2 olan sayiyi gosterir
print(sayilar2[:,2]) # tum gruplardaki indexi 2 olan sayiyi gosterir / : = tum satirlar icin demek
# print(sayilar2[0,2]) = print(sayilar2[satir,sutun]) demek

print(sayilar2[:,0:2]) # tum  satir, gruplarda 0 inci indexten 2 dahil degil e kadar gosterir

print(sayilar2[-1,:]) # son satirdaki gruptaki veriyi gosterir
print(sayilar2[:,-1]) # tum satirlardan grubun sonundaki veriyi yazar