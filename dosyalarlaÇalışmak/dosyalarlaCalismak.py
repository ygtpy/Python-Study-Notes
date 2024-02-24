# r  Read, a append ( yeni datalar ekliyebilme),
# w write(yoksa dosya yenisini oluştur ve dosyanın üzerine yazar), 
# x creat,
 
#f =  'f'ile / bir dosyadaki verileri cekmemizi sağlar
f =open("musteriler.txt")


#            ic ice kullanilmaz 

# butun dosyayi gezer
print(f.read())

#dosyadaki tek bir satiri gezer
print(f.readline())

#f= file /dosyadaki butun satirlari gezer
for l in f : 
    print(l)
    
f.close()

