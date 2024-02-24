
import json # cekmek

with open("users.json") as users:  # dosya okuma islemi 7 dosyayi oku ve ' users e adı altinda olustur
    data = json.load(users) # json formatina donusturme
    print(data[0]["name"])  # elimizdeki verinin "0 inci indexinin "name ini getir 
    print(data[0]["email"])
    print(data[2]["address"]["street"])
    print(data[2]["address"]["geo"]["lat"])
    print("                        ")  
    for x in range(5):
        print(data[x]["name"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print("                        ")    
        # ilk bes degere ulasma