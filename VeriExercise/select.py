import sqlite3 as sq3

connection = sq3.connect("chinook.db")

# cursor = connection.execute(" select * from customers ")
# burada select * yildiz ile yazarsak hepsini cek demek oluyor

# cursor = connection.execute("select FirstName, LastName from customers")
# sadece FirstName ve LastName kolonlarindaki verileri cekiyoruz yazdirmak istersek indexlerine gore yani FirstName[0] LastName[1] siralariz

# cursor = connection.execute("select FirstName, LastName from customers where city='Prague'")
# Burada bir sart kostuk yani Prague'li olanların Firt&LastName'lerini getir dedik

cursor = connection.execute("select FirstName, LastName from customers where city='Prague' or city='Berlin' ")
# burada sehiri(city) Prague veya Berlin olanlarin FirtName, LastNamele'lerini cektik

for row in cursor:
    print("First Name =", row[0])
    print("Last Name =", row[1])
    print("")












connection.close()


