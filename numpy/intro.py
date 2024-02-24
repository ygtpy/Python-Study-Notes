
import numpy as np

# arange = 15 e kdr yaz demek
# reshape = 3 satira ve 5 sutuna bol demek
a = np.arange(15).reshape(3, 5)           # reshape = yeniden yapilandir demek

print(a)
print(type(a))
print(" Dimension Count = " +str(a.ndim))
print("                            ")


b = np.arange(10)

print(b)
print(b.shape) # 10 a birlik yani 1 SATİR 10 TANE DEGER İCERİR oldugunu soyler
print(" Dimension Count = " +str(b.ndim))  # kac boyutlu oldugunu soyler