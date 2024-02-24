

import sqlite3

#             sqlite a baglanak icin komut
connection = sqlite3.connect("chinook.db")

#             farkli sql sorgulari
# cursor = connection.execute("select * from customers") # customer deki tum verileri ceker
# cursor = connection.execute("select FirstName,LastName from customers") # cutomer den first and last name olanlari ceker
cursor = connection.execute("""select FirstName,LastName from customers
                            where city = 'Prague' or city = 'Berlin'""") # praglilarin veya berlinilerin first and last namesini ceker / or = veya

# row = satir demek
# her 'satir icin cursor ile yazdigim sorguyu donduren fonkisyon
for row in cursor:
    print("First Name = "+ str(row [0])) # 1 . index deki (1. kolondaki) sorguyu yazar
    print("Last Name = "+ str(row [1]))
    print("                        ")
    
    
    
    
    
#         fonksiyon seklinde yazimi daha kolay
    
# import sqlite3

# def selectOperasyonlari():
#     connection = sqlite3.connect("chinook.db")
        
#     cursor = connection.execute(""" select FirstName, LastName from Customers where FirstName like '%a'  """)
        
#     for row in cursor:
#         print("First Name = "+ str(row[0]))
#         print("Last Name = "+ str(row[1]))
#         print("                       ")
        
#     connection.close()

    
    
    
connection.close()