import sqlite3

def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    
    cursor = connection.execute(""" select albums.Title, artists.name from artists inner join albums
                                 on artists.ArtistId = albums.ArtistId""")
                                 
                                 
    for row in cursor:
        print(" Title=  " + str(row[0])+"Name = " + str(row[1]))
        
    connection.close()
    
joinOperasyonlari()
        
