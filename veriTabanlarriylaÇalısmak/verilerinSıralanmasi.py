


import sqlite3


connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select FirstName, LastName from customers
                            where city='London' or city = 'Paris'  order by FirstName""") # order by FirstName yazarsak/ firstname e gore siralar

cursor = connection.execute(""" select Address, FirstName from customers
                            order by Address asc """) # asc default yazmasak da olur ve yukselen demek kucukten buyuge

cursor = connection.execute(""" select FirstName, LastName from customers
                            where city = 'London' or city = 'Paris' order by FirstName desc """) # order by "kategori" desc yazarsak alfabenin  tersi seklinde siralar
                            
cursor = connection.execute(""" select * from customers
                            order by FirstName, LastName desc """) # order by FirstName, LastName /isime gore sirala isimleri ayni olanlari soyadina gore sirala demek

for row in cursor:
    print("first name = "+ str(row[1]))
    print("last name = "+ str( row[2]))
    print("                           ")
    
          
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
connection.close()
