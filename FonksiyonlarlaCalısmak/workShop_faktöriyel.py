
# sayı girilecek o sayıya kdr bütün rakamlar çarpılacak
sayi = int(input("Sayı Gir "))
faktoriyel =1

if sayi <0:
    print("Negaitif Sayilarin Faktöriyeli Hesaplanamaz")
    
elif sayi == 0:
    print("Sıfırın Faktöriyeli = 1")
    
else:
    for x  in range(1,sayi+1):
        faktoriyel = faktoriyel * x
    print(faktoriyel)

#%%
sayi1 = int(input("Sayi "))

for x  in range(1,sayi1 + 1):
    print(x)
# fonksiyonda  x tanimi 1 den baslayip kullanicinin girdigi sayiya kadar 1' er 1'er artarak ekrana yazilir

#%%
sayi2 = int(input("sayı gir "))
faktor = 1

if sayi2 <0:
    print("Hesaplanamaz")
    
elif sayi2 == 0 :
    print("Sıfırın fk = 1 ")
    
else:
    for i in range (1,sayi2):
        faktor = faktor * i
    print(faktor)