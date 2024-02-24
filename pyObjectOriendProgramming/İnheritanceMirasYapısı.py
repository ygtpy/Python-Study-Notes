
class Person:    
    def __init__ (self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("yigit", "Zeynel", 20)
print(person1.lastName)

class Worker:
    def __init__(self,salary):
        self.salary = salary
        
class Customer:
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
 
        
sude = person1.age

    
yigit = Worker()
yigit.salary

umut = Customer()
umut.creditCardNumber    


# burada bir sistemde farkli kullanicilar icin ozellik atama uygulaması yaptık
# temel person bilgilerini ekledik ve worker and customer kullanicilari icin
# ayrı ozellikler ekledikden sonra person class indaki bilgilerle birlestirdik