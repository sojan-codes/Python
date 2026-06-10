class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def Details(self):
        print("Brand :", self.brand)
        print("Color :", self.color)

car1 = Car('BMW', 'Red')
car2 = Car('Toyota', 'Green')

car1.Details()
car2.Details()

# To print name 

class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def FullName(self):
        print('Full Name :', self.fname, self.lname)

fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")

Name1 = Name(fname, lname)
Name1.FullName()
        
# Calculator
class Calculator: 
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def addition(self):
        print(self.n1 + self.n2)

    def substraction(self):
        print(self.n1 - self.n2)

    def multiplication(self):
        print(self.n1 * self.n2)

    def division(self):
        print(self.n1 / self.n2)

value1 = Calculator(5, 6)
value1.addition()
value1.substraction()
value1.multiplication()
value1.division()

    
        