

sayi1 = int(input("Sayı 1 = "))
sayi2 = int(input("Sayı 2 = "))
sayi3 = int(input("Sayı 3 = "))

# if (sayi1 >= sayi2) & (sayi1 >= sayi3):
#     print(sayi1)
    
# elif (sayi2 >= sayi1 & sayi2 >=  sayi3):
#     print(sayi2)

# else:
#     print(sayi3)
    

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
    enBuyuk = (sayi1)
    
elif (sayi2 >= sayi1 and sayi2 >=  sayi3):
    enBuyuk = (sayi2)

else:
    enBuyuk = (sayi3)
    
print("En Büyük = ", enBuyuk)