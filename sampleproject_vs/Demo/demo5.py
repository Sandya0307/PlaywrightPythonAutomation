# Case 4: IF super class and Sub class contains same method name with signature.
# Answer:
# If super class and sub class contains same method name with signature in this case the sub class method hides the super class method.
 
# Solution:
 
class CapitalCity:
    def show_city(self, cityname):
        print("The Capital City name is ",cityname)

 
class MetropolitanCity(CapitalCity):
    def __init__(self, cityname):
        super().show_city(cityname)
 
    def show_city(self, cityname):
        print("The Metropolitan City name is ",cityname)
 
 
obj=MetropolitanCity("Bangalore")
obj.show_city("Delhi")
 
 
# Case 5: IF super class and Sub class contains same variable name and datatype.
# Solution:
 
class Product:
    def __init__(self, pname):
        self.prodname=pname
        print("super Class Variable:",self.prodname)
 
    
class PurchaseOrder(Product):
    def __init__(self,pname1,pname2):
        super().__init__(pname1)
        self.prodname=pname2
        print("Sub Class Variable:",self.prodname)
 
 
# Execute
obj=PurchaseOrder("Lenovo Laptop","Dell Desktop")

# Polymorphism Demo in Python:

# -------------------------------------------------

# The super class reference variable can refers to each child class object, and It behaves as child class object, It represents as Dynamic Method dispatch or Poly morphism.
 
# Case 1: Polymorphism Example
 
class GeometricFigure:

    def area(self):

        print("find the Area of a Geomtric Figure")
 
 
class Sqaure(GeometricFigure):

    def area(slef):

        side=10

        result=(side * side)

        print("Area of Square :",result)
 
class Reactangle(GeometricFigure):

    def area(slef):

        length=5

        breadth=12

        result=(length * breadth)

        print("Area of Reactangle :",result)
 
class Circle(GeometricFigure):

    def area(self):

        pi=3.14

        radius=4

        result=pi * radius * radius

        print("Area of Circle :",result)
 
figure=GeometricFigure()

figure.area()
 
sqaure=Sqaure()

rect=Reactangle()

circle=Circle()
 
figure=sqaure

figure.area()
 
figure=rect

figure.area()
 
figure=circle

figure.area()
 
 
# Case 2: Polymorphism Example

class Payment:

    def pay(self):

        print("The Payment method has started")
 
class GooglePay(Payment):

    def pay(self):

        print("The Payment method has started using Google Pay")
 
class PhonePe(Payment):

    def pay(self):

        print("The Payment method has started using PhonePe")
 
class NetBanking(Payment):

    def pay(self):

        print("The Payment method has started using NetBanking")
 
payment=Payment()

payment.pay()
 
googlepay=GooglePay()

phonepe=PhonePe()

netbanking=NetBanking()
 
payment=googlepay

payment.pay()
 
payment=phonepe

payment.pay()
 
payment=netbanking

payment.pay()
 
 
 