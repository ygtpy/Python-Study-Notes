

import sqlite3


connection = sqlite3.connect("chinook.db")


# cursor = connection.execute(""" select city, count(*) Customers
#                             group by city order by count(*) """) # sehirlere kac tane insan yasadigini yazar / count = saymak

cursor = connection.execute(""" select city,count(*) from Customers
                            group by city having count(*)>1 order by count(*) """) #  sehire gore gurupla ve having count(*)>1  = customer sayisi 1 den fazla olanlari ver

for row in cursor:
    print("City = " + str(row[0]))
    print("Count = " + str(row[1]))
    print("                   ")















connection.close()
