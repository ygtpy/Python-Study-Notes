import sqlite3

def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute(""" select * from artists inner join albums on artists.ArtistId = albums.ArtistId""")
    # artis ile albumleri (artist'deki artisId ye) ve (album'deki artistId ye) gore birlestir demek

    for row in cursor:
        print("Title ",row[0], " Name ", row[1])

        
        
    connection.close()
    
joinOperasyonlari()