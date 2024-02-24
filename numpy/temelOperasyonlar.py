
import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)


c = a-b

d = b**3

e = 10* np.sin(a)
print(e>7) # e deki veriler 7 den buyuk ise true ciktisi verir

print(a*b)

print(a@b) # @ = operator ve matris carpimini verir
print(a.dot(b)) # matris carpimini verir

f = np.ones((2,4))
g = np.zeros((2,4))

h = np.random.random((2,4)) # random sayilar olusturur

i = np.sum(b) # verinin icindeki tum sayilari toplar
print(b.sum())

j = np.min(b) # veri icindeki en kucuk veriyi yazar
k = np.max(h) # veri icindeki en buyuk veriyi yazar

l = np.sqrt(b) # sayilarin karekokunu alir













