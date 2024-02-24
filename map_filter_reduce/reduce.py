

sayilar= [1,2,3,4,5]


from functools import reduce

sayilarFaktoriyel = reduce(lambda x,y: x*y, sayilar)
#  x sayilar kumesindeki ilk sayi y ikinci sayi ikisini carpip sonuc x oluyor
# (ornegin x=1*y=2, sonuc= 2, x= 2/ x=2*y=3, sonuc=6, x=6 / 6*4 = 24 / 24*5 = 120)

# küme islemleri yapip sonuca ulasmak 

print(sayilarFaktoriyel)

