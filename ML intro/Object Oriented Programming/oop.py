"""Classes and Objects:
A class is a blueprint for creating objects, while an object is an instance of a class. Classes define the attributes (data) and methods (functions) 
that objects of that class will have. Here's an example:"""
class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The {self.color} {self.brand} car's engine is starting")
"""Creating Objects:
To create an object from a class, you need to instantiate it using the class name followed by parentheses. Here's an example:"""
my_car = Car("Tesla", "red")

"""Accessing Attributes and Methods:
You can access an object's attributes and methods using the dot notation (.). Here's an example:"""
print(my_car.brand)
print(my_car.color)
my_car.start_engine()

#Example 2 --F1
class formula1:
    def __init__(self,driver,racing_team,power_trains,points):
        self.driver = driver
        self.racing_team = racing_team
        self.power_trains = power_trains
        self.points = points
    
    def race_results(self):
        print(f"The monaco winner is {self.driver} of {self.racing_team},powered by {self.power_trains} with {self.points} points")

f1_results = formula1("Max verstappen", "Redbull racing","Rebdull power Trains","25")
print(f1_results.driver)
print(f1_results.racing_team)
print(f1_results.power_trains)
print(f1_results.points)

f1_results.race_results()


"""Inheritance
Inheritance is a mechanism where one class (child/subclass) derives properties from another class (parent/superclass). 
It allows you to create a hierarchy of classes with shared attributes and methods. Here's an example:"""
class ElectricCar(Car):
    def charge_battery(self):
        print(f"The {self.color} {self.brand} electric car is charging its battery")

my_electric_car =ElectricCar("Kia", "blue")
my_electric_car.start_engine()
my_electric_car.charge_battery()



#Example 2 --f1 
class formulaE(formula1):
        def fE_results(self):
            print(f"The winning formualaE driver is {self.driver} for the {self.racing_team} with {self.points} points")

fomulaelectric = formulaE("Lawson Davis","Mercedes","HPPT", "45")
fomulaelectric.fE_results()           



"""Polymorphism:
Polymorphism allows objects of different classes to be treated as objects of a 
common superclass. It enables different objects to respond to the same method in different ways. 
Here's an example:"""
def describe_vehicles(vehicle):
    print(f"The {vehicle.color} {vehicle.brand} is a vehicle")

my_vehicle = Car("BMW","Black")
my_electric_vehicle =ElectricCar("nISSAN", "Green")









"""Encapsulation:
Encapsulation refers to the bundling of data (attributes) and methods (functions) within a class, and 
controlling access to them. It helps in hiding the internal details of an object and provides a way to interact with the object through well-defined interfaces.
 In Python, encapsulation can be achieved by using access modifiers."""

class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number #protected attribute
        self.__balance = balance #Hidden attribute

    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,amount):
        if amount <=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

"""In this example, the _account_number attribute is protected (conventionally denoted by a single leading underscore), 
which indicates that it should not be accessed directly from outside the class. 
The __balance attribute is private (denoted by double leading underscores), making it even more restricted."""



"""Abstraction:
Abstraction focuses on providing essential information to the outside world while hiding the internal implementation details. 
It allows you to define interfaces and abstract classes that can be inherited and implemented by other classes.
python
"""
from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.142*self.radius**2

"""In this example, the Shape class is an abstract class with an abstract method area(). 
It cannot be instantiated directly but serves as a blueprint for other classes like Rectangle and Circle. 
These subclasses inherit from Shape and provide their own implementation of the area() method."""



"""Method Overriding:
Method overriding occurs when a subclass provides its own implementation of a method that is already defined in its superclass. 
It allows you to customize the behavior of inherited methods."""
class Animal:
    def make_sound(self):
        print("The animal makes a sound")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")

my_animal = Animal()
my_cat = Cat()
my_dog = Dog()

my_animal.make_sound()  # Output: The animal makes a sound.
my_cat.make_sound()  # Output: The cat meows.
my_dog.make_sound()  # Output: The dog barks.
