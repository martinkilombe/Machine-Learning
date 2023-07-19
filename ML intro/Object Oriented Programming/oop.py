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




#Comments
#Single line comment

"""THIS IS A MULTI LINE COMMENT
COMMENT 1
COMMENT 2
COMMENT 3"""

var = input("enter your name")
print(var)

#Conditions
var = 45
if var ==45:
    print("Var matches")
else:
    print("Var does not match")


if 5 < 10:
    print("Five is less than 10")
else:
    print("Number is not less than 10")
#multiple conditions
var = 47
if var ==45:
    print("Var matched")
elif var==46:
    print("var matched 1st elif")
elif var==47:
    print("var matched 2nd elif")
else:
    print("no VAR matches")


#number2
x =50
if x<0:
    print("X is a negative number")
elif x<=25:
    print("X is in the 25th percentile")
elif x==75:
    print("X is in the 75th percentile")
elif x>=90:
    print("X is in the 90th percentile")
else:
    print("match is not found")
#Loops
"""While Loop:
The while loop repeats a block of code as long as a certain condition is true.
 Here's the general syntax of a while loop:
 while condition:
    # Code to be executed as long as the condition is true
"""
i = 1
while i <=5:
    print(i)
    i+=1
"""Summing Numbers:
Let's say you want to calculate the sum of numbers from 1 to a given integer n. You can use a while loop to achieve this:"""
n = 5
sum = 0
i =1

while i<=n:
    sum+=i
    i+=1
print("sum",sum)

"""User Input Validation:
You can use a while loop to repeatedly ask the user for input until a valid input is provided. 
For instance, let's ask the user to enter a positive integer:"""
num = -1
while num <=0:
    num = int(input("Enter a positive integer: "))
print("You entered:", num)

"""Password Validation:
In this example, we'll ask the user to enter a password and continue prompting until the correct password is entered:"""
password = "secret"

while True:
    user_password = input("enter password: ")

    if user_password ==password:
        print("Access granted")
        break
    else:
        print("incorrect password. Try again")
"""For Loop:
The for loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any other iterable object. Here's the general syntax of a for loop:
for variable in iterable:
    # Code to be executed for each item in the iterable
"""
#list
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)

#multiple list
names = ["Alice","Bob","charlie"]
ages = [25,42,45]

for name,age in zip(names,ages):
    print(name,age)

#range
for r in range(1,6):
    print(r)

#string
message = "Hello, world!"
for m in message:
    print(m)

#dictionaries
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

for student in student_scores:
    print(student, student_scores[student])

#Using Enumerate
fruits= ["apple","banana","Cherry"]

for index,fruit in enumerate(fruits):
    print(index,fruit)

#example 2
formula = ["Redbull","Aston Martin","Ferrari"]

for index, f in enumerate(formula):
    print(f"Index :{index} Fruit:{f}")

#control flow statements : break , continue , pass
for r in range(1,6):
    if r ==3:
        continue  # Skip the iteration when i is 3
    if r ==5:
        break   # Terminate the loop when i is 5
    print(r)
else:
    pass

for r in range(1,6):
    print(r)
else:
    print("loop complete")

#nested loops
for i in range(1,4):
    for j in range(1,3):
        print(f"({i},{j})")




#Input and output operations
print("Python coding")
print("python \tcoding")

age = 67
age2022 = 66
print("My name is {0}".format(age))
print(f"My age is {age} and my age in 2022 is {age2022}")

#inputs
name= int(input("Enter your name"))
print(name)

name= input("Enter your name")
age = int(input("Enter your age"))
print(name,age)





#Data structures in python -- List, tuple, dictionaries, sets
#list
#sorting
list = [1,2,4,5,6]
list.sort(reverse=True) #sorts in reverse
list

#appending
list.append(24)
list

#remove
list.pop() #removes the last item
list
#Extent
ext = [7,8,9,10,11] 
list.extend(ext) #extends the list above
list

#count
c =list.count(2) #counts how many times 2 appears
print(c)

#Acessing elements
numbers = [10, 20, 30, 40, 50]

print(numbers[0]) #first number :10
print(numbers[2]) #Third number 30
print(numbers[-1]) #last element 50
print(numbers[-3])  #Third item from the end

"""Slicing Lists
You can extract a portion of a list using slicing. The syntax for slicing is list[start:stop:step]. 
Remember that the stop index is exclusive."""
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[1:4])    # Output: [20, 30, 40]
print(numbers[:3])     # Output: [10, 20, 30] (from start to index 2)
print(numbers[3:])     # Output: [40, 50, 60, 70, 80] (from index 3 to end)
print(numbers[::2])    # Output: [10, 30, 50, 70] (every second element)
print(numbers[::-1])   # Output: [80, 70, 60, 50, 40, 30, 20, 10] (reversed list)

"""Modifying Lists
Lists are mutable, so you can change their elements, add new elements, or remove existing ones."""
f1_teams = ["Redbull","Mercedes","Ferrari"]
print(f1_teams)

#Change elements
f1_teams[1]= "Williams" #changes Mercedes with Williams
f1_teams

#Adding elements -- append(), -- extend()
f1_teams.append("Alpha Romeo")
f1_teams

#inserting
f1_teams.insert(2,"Mercedes")
f1_teams

#removing elements
f1_teams.remove("Mercedes")
f1_teams

#2 Tuples -- immutable , indexed, duplication
# Creating tuples
empty_tuple = ()
single_element_tuple = (42,)
fruits = ("apple", "banana", "orange")
coordinates = 10, 20  # Parentheses are optional

print(fruits)      # Output: ('apple', 'banana', 'orange')
print(coordinates) # Output: (10, 20)
 
#Accessing elements
coordinates = (10, 20, 30)
print(coordinates[0])   # Output: 10
print(coordinates[2])   # Output: 30
print(coordinates[-1])  # Output: 30 (last element)
print(coordinates[-2])  # Output: 20 (second element from the end)

#Tuple Unpacking ---Tuple unpacking is a convenient feature in Python that allows you to assign the elements of a tuple to individual variables in a single line of code.
Austria_results = (1,2,3,4,5)
Max, Charles, Perez, Russell,Hamilton = Austria_results

#Immutability--As mentioned earlier, tuples are immutable. Once created, you cannot modify their elements or their size.
coordinates = (10, 20)

# Attempt to modify an element (will raise an error)
coordinates[0] = 5  # TypeError: 'tuple' object does not support item assignment

# Attempt to add an element (will raise an error)
coordinates.append(30)  # AttributeError: 'tuple' object has no attribute 'append'

#Common Operations with Tuples---Though tuples are immutable, you can still perform various operations on them, like slicing, concatenation, and repetition.
numbers = (1,2,3,4,5)
print(numbers[1:4])     # Output: (2, 3, 4)
print(numbers + (6, 7)) # Output: (1, 2, 3, 4, 5, 6, 7)
print(numbers * 2)      # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

#Tuple Packing and Unpacking
point = 10,20
print(point) #packing

x,y = 5,10
print(x)
print(y)

#Dictionaries
"""Dictionary Methods
Python provides various built-in methods for working with dictionaries. Some commonly used methods include:

len(dictionary): Returns the number of key-value pairs in the dictionary.
dictionary.keys(): Returns a list of all keys in the dictionary.
dictionary.values(): Returns a list of all values in the dictionary.
dictionary.items(): Returns a list of tuples containing key-value pairs.
dictionary.get(key): Returns the value associated with the given key.
key in dictionary: Returns True if the key exists in the dictionary, otherwise False.
dictionary.pop(key): Removes the key-value pair for the given key and returns the value.
dictionary.clear(): Removes all key-value pairs from the dictionary.
"""
Spa_Gp = {
    1: "Max verstappen",
    2: "Sergio Perez",
    3: "Lewis Hamilton",
    4: "George Russell"
}
print(Spa_Gp)


# Using the dict() constructor
animals = dict(cat="meow", dog="bark", bird="tweet")

#updating 
Spa_Gp[1]= "Fernando Alonso"
print(Spa_Gp)

#Acessing values --[]. .get()
WDC ={
    "Max Verstappen":1,
    "Fernando Alonso":2,
    "Sergio Perez":3
}
print(WDC["Max Verstappen"])
print(WDC["Fernando Alonso"])
print(WDC["Sergio Perez"])

for w in WDC:
    print(w,WDC[w])

#modyfying dictionaries
#Adding new value
WDC["George Russell"] = 4
WDC

#change value
WDC["George Russell"] =6
WDC

print(len(WDC))
print(WDC.keys())
print(WDC.values())
print(WDC.items)
print(WDC.get("Max Verstappen"))


#nested Dictionaries
person= {
    "F.name":"Martin",
    "L.name":"muti",
    "Address":{
        "city":"Nairobi",
        "zipCode":"1002"
    }
}

print(person["Address"]["city"])