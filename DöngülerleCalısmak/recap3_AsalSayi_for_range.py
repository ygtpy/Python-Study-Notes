


sayi = int(input("Sayı Giriniz "))
asalMi = "evet" #yerine True de kullanılılabilir magic string deniyor

# 2 den baslayıp girilen sayıya kdrki sayıları verilen % komut ile bölüp
# kalanı söyler ve eğer sıfıra eşit iste sayı asal değildir
for x in range(2,sayi):
    if (sayi % x ) == 0: # % bu işaret bölümden kalanı bulmamızı sağlar
        asalMi = "hayır" #yerine False de kullanılılabilir magic string deniyor
        break
    
if asalMi == "evet":
    print("ASAL")
    
else:
    print("ASAL DEĞİL")
    
    
# girilen sayıyı for in range fonksiyonu ile döndürüp
# bölümünden kalanı anlayarak asal olup olmadığını belirledik

#%%
sayi = int(input("Sayı Giriniz "))
asalMi = True


for x in range(2,sayi):
    if (sayi % x ) == 0: 
        asalMi = False
        break
    
if asalMi:
    print("ASAL")
    
else:
    print("ASAL DEĞİL")
    