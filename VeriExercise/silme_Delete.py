import sqlite3 

def deleteCustomer():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" Delete from customers where FirstName='Hakan' """)
    # Delete from customers yazarak ismi hakan olanlari sildim
    
    connection.commit()
    connection.close()


deleteCustomer()