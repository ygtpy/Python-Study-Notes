krediler = ["Hızlı Kredi","Maaşını Halkbanktan Alanlara Özel","Mutlu Emekli İhtiyaç Kredisi"]

#takma isim verip verilen listeleri sıralar (alias)
for kredi in krediler:
  print("güzel"+" "+kredi)
print("")
  
  # i verilen takma isim / range uzunluk'a kadar demek / len verinin uzunluğunu gösterir.
for i in range(len(krediler)):
    print(krediler[i])
print("")
    
# 3 üncü indexe kdr siralar yani 3. sıradaki veri dahil olmayacak şekilde sıralar yukarıdakiyle aynıdır /
#döngüye girer ve tüm verileri sırasıyla listeler.
for i in range (3):
  print(krediler[i])
print("")

# #10 a kdr yaz 10 dahil değil
# for i in range(10):
#   print(i)


# #1 den başla 5 dahil değil
# for i in range(1,5):
#   print(i)


# # 0 dan başla 10 a kdr ama 2 şer artarak
# for i in range (0,10,2):
#   print(i)
  
  
  
# insanlar = ["ali","veli","yigit","emir"]


# for baylar in insanlar:
#     print("knk" +" "+baylar)
    
#%% "insanlar" verisinin içindeki "bay" takma isimli verileri sırala demek   
for bay in range(len(insanlar)):
    print(insanlar[bay])
    
#%%
for bay in range(4):
    print(baylar[bay] + "m" + "i" + "r")
    
   #%% 
for i in range(5):
    print(i)
    
for i in range(1,9):
    print(i)
    
    
for i in range(1,19,3):
    print(i)