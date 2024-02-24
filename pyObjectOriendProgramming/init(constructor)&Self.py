class Matematik:
#contructer = yapıcı blok
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("bitti")
        
    def topla (self):
        return self.sayi1 + self.sayi2
    
    def cikar (self):
        return self.sayi1 - self.sayi2
    
    def carp (self):
        return self.sayi1 * self.sayi2
    
    def bol (self):
        return self.sayi1 / self.sayi2
    
    #  fonksiyonu boyle bir veri ismine aktarirsak  bellekte ayri oluşur
matematik = Matematik(6,5)
matematik2 = Matematik(5,6)
print("Çarpım = " +str(matematik2.carp()))



    # def __init__(self,sayi1,sayi2):
    #     self.sayi1 = sayi1
    #     self.sayi2 = sayi2
    #     print("bitti")
    
    
# burada self.sayi1 = diye verdigimiz tanim sayi1 in icindeki degerleri
# girilen parametrelerle degistirir(def __init__(self,sayi1,sayi2): parametreler")