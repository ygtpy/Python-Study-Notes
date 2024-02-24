

import numpy as np


a = np.arange(10)

#        dizi, class vb. icin kopyalama
c = a.copy()

c[0]=99
print(c)
print(a)



# sayisal verilerde boyle kopya alinabilir
ab = 100
ba = 50

ba = ab
ab = ba

print(ab)
print("                  ")



#        view islemi

d = a.view()
print(a)
print(d)
print("            ")

d[0]= 250
print(a)
print(d)
print("           ")

d.shape = 2,5
print(a)
print(d)
print("       ")

a[0] = 123
print(a)
print(d)
   # burada a daki verileri d ile esitledik
   # yani a da ne degisirse d de de degisiyor 
   # d de ne degisirse a da da degisiyor
   # ama ornegin d nin tablo yapisi degisince a etkilenmiyor
   









