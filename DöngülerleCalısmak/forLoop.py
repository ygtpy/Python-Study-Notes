

sehirler = ["Uşak","İstanbul","Isparta",]

# print(sehirler[0])
# print(sehirler[1])
# print(sehirler[2])

# for dan sonraki "sehir" takma ad olarak kullanılır.
 # girilen verideki her elemanı sırasıyla gezer, sırasıyla listeler.
 
# for sehir in sehirler:
#      print(sehir[0:3])


# eğer(if) sehir "Uşak" a eşit ise...komut

# for sehir in sehirler:
#     if sehir == "Uşak":
#         print(sehir,"için kod = ", sehir[0:3])


# eğer(if) "uşak" dışında diğer tüm elemanlar yazılır 

for sehir in sehirler:
    if sehir != "Uşak":
        print(sehir,"için kod = ", sehir[0:3]) # if için
 # indenteysın yani komut hizasına dikkat et            
    print("*******") # for için
 # ",' artı demek
    
#%%
##///////////////////break/////////////////////// 

for sehir in sehirler:
# break #komut sağladığı durumda komutu durdurur
    if sehir == "Uşak":
        # break
        print(sehir,"için kod = ", sehir[0:3])
        
        
        
#%%        
#///////////////////continue/////////////////////// 
sehirler = ["Isparta","İstanbul","Uşak",]
for sehir in sehirler:
    if sehir == "Uşak":
        continue # geçerli olan komutu yazmaz
        
        print(sehir,"için kod = ", sehir[0:3])
        
 

#%%
#///////////////////range/////////////////////// 

for x in range(5):
    print(x+1)
    
for x in range(1,5):
    print(x)
    
for x in range(1,10,2):
    print(x)
    
    








