
studentsSet = {"Engin", "Derin", "Salih", "Ahmet", "Yigit"}
# studentsSet2 = set("Umut","Emir","Sunal")
print(studentsSet)

print (type(studentsSet))

#ogrencileri listeler
for student in studentsSet:
    print(student)
    
 #True False cikar   
print("Derin" in studentsSet)    

#(eger)listede varsa (mesaj yazar)
if "Derin" in studentsSet:
    print("listede var")
    
# else "derin" in studentsSet:
#     print("yok")

#Eleman ekler
studentsSet.add("Ali")
print(studentsSet)

#set listesine coklu elemanlar ekler
studentsSet.update(["Merve","Mert","Sude"])
print(studentsSet)

#siler
studentsSet.remove("Sude")
print(len(studentsSet))

#hata vermeden siler
studentsSet.discard("Sude")
print(len(studentsSet))

# random eleman siler (cok kullanilmaz)
# x = studentsSet.pop()
# print(len(studentsSet))
# print(studentsSet)

#siler ama set() kalir
x = studentsSet.clear()
print(len(studentsSet))

#komple siler
del studentsSet



