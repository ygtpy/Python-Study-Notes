
import sqlite3

def insertOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    connection.execute(""" insert into customers (FirstName,LastName,Company,Address,city,state,country,PostalCode,Phone,email) values
                                ('Yiğit Ali','zeynel','babeAİ','Atapark','Uşak','TR','Türkiye','64000','+90 5034567892','yigitali@gmail.com')""")

    connection.commit() #ekleme komutu
    connection.close()
    
insertOperasyonlari()
 