

sayi1 = int(input("Sayı 1 Giriniz = "))
sayi2 = int(input("Sayı 2 Giriniz = "))
sayi3 = int(input("Sayı 3 Giriniz = "))

if (sayi1 >= sayi2) & (sayi1 >= sayi3):
    print("En Büyük "+ str(sayi1))
    
elif (sayi2 >= sayi1) & (sayi2 >= sayi3):
    print("En Büyük "+ str(sayi2))
    
else:
    print( str(sayi3) + " En Büyük ")
    enBuyuk = sayi3
    

