


esyalar = ["kitap", "masa","fare","muz"]



# esyalar öğesinden indexi 0 olan ve 3 e kadar olan veriyi yazar
for esya in esyalar :
    print(esyalar[0:3])

#%%      # == (sadece girilen öğeyi yazar)
esyalar = ["kitap", "masa","fare","muz"]

for esya in esyalar:
    if esya == "masa":
        print(esya)
        
#%%       # != (girilen öğenini dışındaki öğeleri yazar)
esyalar = ["kitap", "masa","fare","muz"]

for esya in esyalar:
    if esya != "masa":
        print(esya)
        
        
        
#%%        # if'in altındaki eylemi durdurur
esyalar = ["kitap", "masa","fare","muz"]

for esya in esyalar:
    if esya == "masa":
        break
        print(esya)
    print("HAGHDSASDF")
    
    
#%%    # continue= altina girilen komut dışındaki verileri gezer    
esyalar = ["kitap", "masa","fare","muz"]

for esya in esyalar:
    if esya == "masa":
        continue
        print(esya)
    print("HAGHDSASDF")
    
#%%        # != 
esyalar = ["kitap", "masa","fare","muz"]

for esya in esyalar:
    if esya != "masa":
        continue
        print(esya)
    print("HAGHDSASDF")
    
#%%

# 0 dan baslayıp 100  kdr yazar
for x in range(100):
    print(x + 1)

#2 den basla / 20 ye kdr / 3er 3er
for x in range(2,20,3):
    print(x)










