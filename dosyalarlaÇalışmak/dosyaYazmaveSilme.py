#                ekleme

# .write fonksiyonu dosyanin içine veri eklemenizi saglar

fileToAppend = open("ogrenciler.txt","a")
fileToAppend.write("yigit")
fileToAppend.write("\n") # altindaki isimi altina yazdirir "ceyda
fileToAppend.write("ceyda")



fileToAppend = open("ogrenciler.txt","w")
# tüm verileri siler ve üstüne yazar
fileToAppend.write("mehmet")


# .close fonksiyonu dosyayi kapatir

fileToAppend.close()


#%%

#                silme

import os

if os.path.exists("ogrenciler.txt"): # dosya varmi yokmu onu kontrol eder
    os.remove("ogrenciler.txt") # dosyayi siler
    
else:
    print("dosya yok")


os.rmdir("empty") # direkt klasoru siler


