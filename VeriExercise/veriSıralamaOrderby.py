import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select FirstName, LastName from customers
                             where city='Prague' or city='Berlin' order by FirstName""")
# verileri 'order by FirstName' sonuna neye gore siralayacagimizi yazip siralayabiliriz

cursor = connection.execute("""select FirstName, LastName from customers
                             where city='Prague' or city='Berlin' order by FirstName desc """)
# verileri 'order by FirstName desc' sonuna 'desc' koyarak tersten siralariz

cursor = connection.execute("""select FirstName, LastName from customers
                            where city='Prague' or city='Berlin' order by FirstName, LastName """)
# burada 'order by FirstName, LastName' yaparsak FirstName'leri aynı olanları LastName'lerine gore siralar

for rowSatir in cursor:
    print("First Name = ", rowSatir[0])
    print("Last Name = ", rowSatir[1])
    print("")
    

















connection.close()