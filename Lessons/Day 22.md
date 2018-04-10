# Day 22

## Inheritance

### The `__init__()` Method for a Child Class

Superclass and subclass

```python
class Car():
    """"A simple attempt to represent a car."""
    # --snip-- #

# A child class inherits all of attributes of its parent class.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attibutes of the parent class."""
        super().__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

### Defining Attributes and Methods for the Child Class

A child class can have its own attributes.

``` python
class Car():
    """"A simple attempt to represent a car."""
    # --snip-- #

# A child class inherits all of attributes of its parent class.
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attibute sof the parent class.
        Then initialize the attributes specific to an eletric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {str(self.battery_size)}-kHw battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

my_old_car = Car('chevy', 'lumina', 1994)
my_old_car.describe_battery() #'Car' object has no attribute 'describe_battery'
```

### Overriding Methods from the Parent Class

Suppose we have varying functionality between the parent and child class.

``` python
class Car():
    """"A simple attempt to represent a car."""
    # --snip-- #
    
    def fill_gas_tank(self):
        print("You've got a full tank!")

# A child class inherits all of attributes of its parent class.
class ElectricCar(Car):
    # --snip-- #
    
    def fill_gas_tank(self):
        print("This car does not need a gas tank!")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.fill_gas_tank()

my_old_car = Car('chevy', 'lumina', 1994)
my_old_car.fill_gas_tank()
```

### Exercise

``` python
# Exercise
'''
An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the  Restaurant class you wrote earlier. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
'''

class Restaurant():
	"""A simple attempt to model a restaurant."""
	
	def __init__(self, restaurant_name, restaurant_type):
		"""Initalize attributes."""
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type
		self.number_served = 0
		
	def describe_restaurant(self):
		"""Prints a description of the restaurant."""
		print(f"{self.restaurant_name.title()} serves {self.restaurant_type}.")
		
	def set_number_served(self, num):
		self.number_served = num
		
	def increment_number_served(self, num):
		self.number_served += num

class IceCreamStand(Restaurant):
	"""Represents aspects of a restaurant, specific to an ice cream stand."""

	# Provide a default value for restaurant_type
	def __init__(self, restaurant_name, restaurant_type='ice cream'):
		"""
		Initialize attrbiutes of the parent class.
		Then initalize attrivutes specific to an ice cream stand.
		"""
		super().__init__(restaurant_name, restaurant_type)
		self.flavors = ["vanilla", "chocolate", "strawberry"]
		
	def display_flavors(self):
		"""Displays the available ice cream flavors."""
		print("The available flavors are:")
		for flavor in self.flavors:
			print("\t", flavor)
			
my_ice_cream_place = IceCreamStand("handles")
my_ice_cream_place.describe_restaurant()
my_ice_cream_place.display_flavors()      
```

### Instances as Attributes

Our `ElectricCar` class could have a lot of battery methods. Let's separate those.

``` python
class Car():
	# --snip-- #

        
class Battery():
    """A simple attempt to model a battery for a car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {str(self.battery_size)}-kHw battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            distance = 240
        elif self.battery_size == 85:
            distance = 270

        message = f"This car can go approximately {str(distance)} miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attibute sof the parent class.
        Then initialize the attributes specific to an eletric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

### Importing an Entire Module

``` python
# car.py
"""A set of classes used to represent gas and electric cars."""
class Car():
	# --snip-- #

        
class Battery():
	# --snip-- #


class ElectricCar(Car):
	# --snip-- #
```

``` python
# main.py
import car

my_tesla = car.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

### Exercises

1. Using your latest  Restaurant class, store it in a module . Make a separate file that imports  Restaurant. Make a  Restaurant instance, and call one of  Restaurant ’s methods to show that the  import statement is working properly .
2. Write a method that adds an ice cream flavors to the flavors attribute in `IceCreamStand`.