import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute(""" select FirstName, LastName from customers where FirstName like '%a%' """)
# FirstName'inde a olan customer'lari ceker

cursor = connection.execute(""" select FirstName, LastName from customers where FirstName like 'a%' """)
# FirstName'inin basi 'a' ile baslayanlar

cursor = connection.execute("""select FirstName, LastName from customers where city like '%a'  """)
# FirstName'inin sonu 'a' ile bitenler


for row in cursor:
    print("First Name = ", row[0])
    print("Last Name = ", row[1])
    print("")

connection.close()




