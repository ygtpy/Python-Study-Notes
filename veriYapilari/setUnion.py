

setA ={1,2,3,4,5}
setB ={1,3,4,6,7,8}


#iki listeyi aynı veriler içermesine rağmen tekrarlamadan gösterir
print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))


#iki listede aynı olan elemanları gösterir
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))


#iki listede farklı olan elemanları gösterir 
#A'nın B'den farkı
print(setA - setB)
print(setA.difference(setB))
#B'nin A'dan farkı
print(setB.difference(setA))


#iki listedeki aynı elemanların DIŞIndaki verileri bir arada gösterir
print(setA ^ setB )
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))

print(setA.difference(setB))
print(setB.difference(setA))

