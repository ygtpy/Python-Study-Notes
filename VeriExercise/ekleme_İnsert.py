import sqlite3

def insertCostumer():
    
    connection = sqlite3.connect("chinook.db")
    
    connection.execute("""insert into customers (firstName,lastName,city,email) values("Hakan","Hocamız","Isparta","nabe@gmail.com") """)
    # insert into customers (firstName,lastN...) values(Hakan,Hoc...) yazarak ekleme yaptim

        
    connection.commit()   
    connection.close()


insertCostumer()


#%%

connection = sqlite3.connect("chinook.db")
cursor = connection.execute("""select FirstName from customers where city='Isparta' """)


for row in cursor:
    print(row[0])
    
    
connection.close()