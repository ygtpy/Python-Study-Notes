
import sqlite3


def updateCustomer():
    connection = sqlite3.connect("chinook.db")
    
    connection.execute(""" update customers set city ='Uşak' where city = 'Isparta' """)# guncelle customers deki city si usak olanlari isparta yap
    
    
    connection.commit()
    connection.close()
    
updateCustomer()
