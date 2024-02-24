
# class belirlerken büyük harfle basla
class Matematik :
    def topla (self,sayi1,sayi2):
        return sayi1 + sayi2
    
    def cikar (self,sayi1,sayi2):
        return sayi1 - sayi2
    
    def carp (self,sayi1,sayi2):
        return sayi1 * sayi2
    
    def bol (self,sayi1,sayi2):
        return sayi1 / sayi2
    
    #  fonksiyonu boyle bir veri ismine aktarirsak  bellekte ayri oluşur
matematik1 = Matematik()
print("Çarpım = " +str(matematik1.carp(6,7)))
    
# evet class, bir veri tanimlarken yukarideki ornek gibi matematik1 verisini Matematik class ına esitlersek
# Matematik class ının icindeki tum fonksiyonlari uzunca kodlar yazmadan istedigimiz zaman cagirabiliriz
# class bu ise yarar



