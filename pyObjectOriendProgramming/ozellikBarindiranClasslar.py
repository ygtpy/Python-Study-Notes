
# Property

class Person:    
    def __init__ (self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("yigit", "zeynel", 20)
print(person1.lastName)

# bir kisiye ait ozellikleri sisteme yuklemek ıstersek boyle bir sistem kullanmıs oluruz


class Worker:
    def __init__(self,salary):
        self.salary = salary
        
class Customer:
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
yigit = Worker()
yigit.salary

umut = Customer()
umut.creditCardNumber    