
import numpy as np


b = np.array([[1.9,2,3],[4,5,6],[7,8,9]])

print(b.dtype) # veri tipini soyler
# listedeki tek bir veri genel turden farkli olursa
# ornegin yukaridaki listede cogunluk integer ve bir tane float var
# butun veri float olarak gorlulur. 
# float integeri kapsar

print(b.ndim) # kac boyutlu
print(b.shape) # kaca kaclık veri ( 3 satir / 3 sutun) 

print("                               ")

a = np.array([1,2,3,4,5,6])
a = a.reshape(3,2) # bu sekilde yapilandirirsak direkt a verisine islemis oluruz

# print(a.reshape(2, 3)) # bu sekilde yapilandirmak kalici olmaz

