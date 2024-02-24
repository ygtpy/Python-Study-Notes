

import sqlite3

connection = sqlite3.connect("chinook.db")



cursor = connection.execute(""" select firstName, LastName
                            from Customers where FirstName like 'alexandre'  """) # customers den firstName ve Lastname yi çek ve icinde alexandre olani goster

cursor = connection.execute(""" select FirstName, LastName
                            from Customers where FirstName like 'a%' """) # customers den firstname and lastname i cek icinde a ile baslayanlari yazdir (diger harfleri onemsiz)
                            
cursor = connection.execute(""" select FirstName, LastName from Customers Where FirstName like '%a'  """)# a ile bitenleri yazdir

cursor = connection.execute(""" select FirstName,LastName from Customers where FirstName like '%a%' """) # icinde a harfi olanlari yazdir


for row in cursor :
    print("First Name = " + str(row[0]))
    print("Last Name = " + str(row[1]))
    print("                             ")














connection.close()