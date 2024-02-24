
import numpy as np

a = np.floor(10*np.random.random((2,3)))
b = np.floor(10*np.random.random((2,3)))

print(a)
print(b)
print("                  ")

c = np.vstack((a,b)) # dikey birlestirir
print(c)
print("                    ")
d = np.hstack((a,b)) # yatay birlestirir
print(d)











