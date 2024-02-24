import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select city,count(*) from customers group by city order by count(*) """)
# customer'lari city'e gore grupladik ve hangi sehirde kac customer oldugunu yazdirdik 

cursor = connection.execute("""select city,count(*) from customers group by city having count(*)>1 order by count(*)""")
#  burada 'group by city having count(*)>1' sehirdeki musteri sayisinin 1 den buyuk olanlari yazdirdik


for row in cursor:
    print("City = ", row[0])
    print("Count = ", str(row[1]))
    print("")












connection.close()







