
class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla ( self) :
        return self.sayi1 + self.sayi2
    
    def cikar (self):
        return self.sayi1 - self.sayi2
    
    def carp (self):
        return self.sayi1 * self.sayi2
    
    def bol (self):
        return self.sayi1 / self.sayi2
    
matematik = Matematik(5, 5)
# matematik2 = Matematik(6, 6)
print("Toplam = " + str(matematik.topla()))