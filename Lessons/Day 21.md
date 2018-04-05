# Day 21

Object-Oriented Programming 
Crash Course Python (Chapter 9)
We write classes to represent read-world things and situations, and we create objects based on these classes When we write a class, we define the general behavior that a whole category of objects can have.

## Classes

```python
### Example: Turtle ###
# import the Turtle class from the turtle module
from turtle import Turtle

# instantiate a turtle object from the class
Bob = Turtle()
Bob.color('blue')
Bob.shape("turtle")
Bob.forward(100)

# instantiate a second turtle object from the class
Katie = Turtle()
Katie.color('red')
Katie.left(180)
```

## dog.py

```python
### Creating and Using a Class
# dog.py
class Dog():	# convention: names of classes are capitalized
   	"""A simple attempt to model a dog."""
    
    def __init__(self, name, age):	# runs whenever an object is instantiated
        """Initialize name and age attributes."""
        # Any variable prefixed with self is available to every method in the class
        self.name = name
        self.age = age		
        
    def sit(self):	# a method is a function that is a part of a class
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over.")
        
 ### Making an instance from a class
my_dog = Dog('willie', 6)

# we use dot notation to access class attributes and methods
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
```

## restaurant.py v1

```python
# Exercise: restaraunt.py
'''Make a class called  Restaurant . The  __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called  open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called  restaurant from your class . Print the two attributes individually, and then call both methods .'''

class Restaurant():
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, restaurant_type):
        """Initalize attributes."""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        
        
    def describe_restaurant(self):
        """Prints a description of the restaurant."""
        print(f"{self.restaurant_name.title()} serves {self.restaurant_type}.")
        
        
    def open_restaurant(self):
        """Opens the restaurant."""
        print(f"{self.restaurant_name.title()} is open!")
        

pizza_place = Restaurant("Place Pizza", "pizza")

print(pizza_place.restaurant_name)
print(pizza_place.restaurant_type)
pizza_place.describe_restaurant()
pizza_place.open_restaurant()
```

## car.py

``` python
### Working with Classes and Instances

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_old_car = Car('chevy', 'lumina', 1994)	# Create instance of the car
print(my_old_car.get_descriptive_name())	# Calls method
```

## car.py v2

Added lines 11, 20, 27

``` python
### Setting a Default Value for an Attribute

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    
    def read_odometer(self): # added
        """Print a statement showing the car mileage."""
        print(f"This car has {self.odometer_reading} miles on it")

my_old_car = Car('chevy', 'lumina', 1994)
print(my_old_car.get_descriptive_name())

# odometer
my_old_car.read_odometer()
my_old_car.odometer_reading = 100000
my_old_car.read_odometer()
```

``` python
### Setting a Default Value for an Attribute

class Car():
    """A simple attempt to represent a car."""
    # -- snip-- #
    
    def update_odometer(self, mileage):
        """Set the odometer reading to a given value."""
        self.odometer = mileage

my_old_car = Car('chevy', 'lumina', 1994)

my_old_car.update_odometer(42000)
my_old_bar.read_odometer()
my_old_car.update_odometer(0)
```

``` python
class Car():
    """A simple attempt to represent a car."""
    # -- snip-- #
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
        	self.odometer = mileage
        else:
            print("You can't roll back an odometer!")
            
	def increment_odometer(self, miles):
        self.odometer_reading += miles)
        
my_old_car = Car('chevy', 'lumina', 1994)

my_old_car.update_odometer(10000)
my_old_car.read_odometer()

my_old_car.increment_odometer(10)
my_old_car.read_odometer()

my_old_car.update_odometer(0)
```

## restaurant.py v2

``` python
# Exercise
'''Start with your program from earlier.
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.

Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business'''

class Restaurant():
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, restaurant_type):
        """Initalize attributes."""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type\
       	self.number_served = 0

    # --snip-- #
        
    def set_number_served(self, num):
        self.number_served = num
        
    def increment_number_served(self, num):
        self.number_served += num

pizza_place = Restaurant("Place Pizza", "pizza")

print(pizza_place.restaurant_name)
print(pizza_place.restaurant_type)
pizza_place.describe_restaurant()
pizza_place.open_restaurant()

print()
print(pizza_place.number_served)
pizza_place.set_number_served(10)
print(pizza_place.number_served)

print()
pizza_place.increment_number_served(10)
print(pizza_place.number_served)
```









