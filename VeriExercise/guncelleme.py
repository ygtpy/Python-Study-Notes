
import sqlite3

def updateCostumer():
    
    connection = sqlite3.connect("chinook.db")
    connection.execute("""update customers set city='İstanbul' where city='Isparta' """)
    # update customers set city='İstanbul' where city='Isparta'
    # yazarak sehri Isparta olanlarınkini istanbul ile degistirdim
    
    
    
    
    
    
    connection.commit()
    connection.close()
updateCostumer()