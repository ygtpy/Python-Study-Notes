 

tupleListe = (2,4,6,"Ankara",(2,3,4),[])
liste = [2,4,6,"Ankara",(2,3,4),()]

#tuple içindeki veri değiştirilemez
liste[0] = 6
# tupleListe[0] = 6

# 1 den 2 dahil değil kadar veri gösterir(vs normal liste)
print(tupleListe[1:2])
print(liste[1:2])

#Sondan ikinci index
print(tupleListe[-2])
print(liste[-2])

#Sonuna virgül koymazsak tuple listesi anlaşılmaz 
tupleDeger = ("yiğit",)
print(tupleDeger)

print(type(tupleDeger))
print(type(liste))
print(tupleListe)
print(liste)
print(len(tupleListe))
print(len(liste))

      