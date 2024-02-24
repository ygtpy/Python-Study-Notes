

import sqlite3


def deleteCustomer():
    
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" Delete from customers where customerid=61 """)
                    # (""" Delete from customers where city = 'Uşak' """)
                    # (""" Delete from customers where city = 'Uşak' or country='Germany' """)
                    
 # farkli sorgu sekilleri                   
                    
                    
                    
    connection.commit()
    connection.close()

deleteCustomer()