# Class & Object
# In Python, a class is a blueprint for creating objects. An object is an instance of a class.
# Classes encapsulate data for the object and methods to manipulate that data.
class Car:
    def __init__(self, brand, model):  # constructor
        self.brand = brand
        self.model = model
    
    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

# Create object
my_car = Car("Toyota", "Corolla")
my_car.drive()  # Toyota Corolla is driving.


# encapsulation

class BankAccount :
    def __init__(self, balance=0):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance
    
acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())

# Inheritance
class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # call the constructor of the parent class
        self.battery_size = battery_size
    
    def charge(self):
        print(f"{self.brand} {self.model} is charging with a {self.battery_size} kWh battery.")

electric_car = ElectricCar("Tesla", "Model S", 75)
electric_car.drive()  # Tesla Model S is driving.
electric_car.charge()  # Tesla Model S is charging with a 75 kWh battery

# Polymorphism
class Animal:
    def make_sound(self):
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
for animal in (Dog(), Cat()):
    print(animal.make_sound())  # Woof! Meow!

# Abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass # abstract method that must be implemented by subclasses


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(f"Area: {shape.area()}")  # Area: 78.5, Area: 16