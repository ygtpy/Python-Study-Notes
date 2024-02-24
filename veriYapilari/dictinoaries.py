#sözlük gibi anahtar kelimenin karşısına tanım yazabiliriz
sozluk = {
          "book": "kitap",
          "table":"masa"
          }

#bir başka yazım şekli
sozluk2 = dict(kitap = "book", masa = "table")


# Dictinoaries(Sözlük) kelime karşılığını değiştirme
sozluk["book"]= "kitap 1"

# yeni kelime ve anlamını ekleme
sozluk["pencil"] = "kalem"

#sözlükten kelime ve anlamını silme
del(sozluk["book"])

# kelime karşılığını yazdırma
print(sozluk["table"])


print(sozluk)
print(len(sozluk))