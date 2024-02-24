

sayi = int(input("Kaç Yıldız Olsun?"))

yildiz = ""

for x in range(1,sayi + 1):
    yildiz = yildiz + "*"
    print(yildiz)
    
    
# yıldız verisine döngü sonlanana kadar belirtilen toplama işlemini
# yaparak istenilen sayıda yıldız ekrana çıktı olarak çıkar
# verilen "i" değerinin bir öenmi yoktur istenen değer yazılabilir
#for = için demek
#range komutu parantez içiindeki sayılara göre davranır örneği ele alırsak
# "1" den başlayıp virgülden sonraki sayıya kadar altta verilen isteği yerine getirir.