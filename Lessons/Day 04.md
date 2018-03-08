# Day 04

**Programming Assignments due one week from class introduced. Reading Assignment 02 posted.**

## Review

### docstring

The docstring should be the first thing in the body.
https://www.python.org/dev/peps/pep-0257/

``` python
def my_func():
	'''The docstring comes first.'''
	# Now write the body.
```

### functions

Surround a function with two blank lines.

```python
def first_function():
	print("my first function")


def second_function():
	print("There were two blank lines before this function's header.")
    
# call a function
first_function()		# prints "my first function"
print(first_function())	# prints None because first_function does 'return' information
```

### long text

``` python
def america():
    print('''Oh, beautiful for spacious skies,
    For amber waves of grain,
    For purple mountain majesties
    Above the fruited plain!
    America! America!
    God shed his grace on thee,
    And crown thy good with brotherhood
    From sea to shining sea.''')
    
america()
```

### variables

Remember that names of variables can serve as a form of documentation.

```python
from math import sqrt

# This is a weird value of x...k
x = (1 + sqrt(5)) / 2

# Oh!
golden_ratio = (1 + sqrt(5)) / 2
```

### conversion

```python
print(int(10)) 
# 10 is already an int, so no need to convert it
# hurts readability

print(10 % 3)
# The modulo operator returns an in

print(str("Hello"))
# the str function isn't needed

str = "This is bad"
print(str(42))	# This should print '42', but I overwrote that function
```



##Introduction to Turtle Module

https://www.reddit.com/r/Python/comments/7mo2l8/turtle_module_drawing_a_randomised_landscape/

https://docs.python.org/3/library/turtle.html

### mypolygon.py

``` python
import turtle

# We create a Turtle object and assign it to a variable named bob
bob = turtle.Turtle()
print(bob)
turtle.mainloop()

# objects have methods, which is just a function attached to an object
bob.forward(100)
bob.left(90)
bob.forward(100)
```

Modify the program to draw a square.

``` python
import turtle

# We create a Turtle object and assign it to a variable named bob
bob = turtle.Turtle()
turtle.mainloop()

# objects have methods, which is just a function attached to an object
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
```

We can do the same thing more concisely with a `for`  loop.

```  python
for i in range(4):
    print("Hello!")

# Notice that that i increments by 1... 0, 1, 2, 3
for i in range(4):
    print(i)
```

Modify `mypolygon.py` with the `for`.

``` python
for i in range(4):
	bob.forward(100)
	bob.left(90)
```

Complete the series of exercises.

1.  Write a function called square that takes a parameter named `t`, which is a turtle. 

   It should use the turtle to draw a square.

   Write a function call that passes bob as an argument to square.

   Run the program again.

``` python
def square(t):
    '''Draws a square with sides of a given length
    
    Returns the Turtle to the starting position and location.
    '''
    for i in range(4):
        t.forward(100)
        t.left(90)

square(bob)
# Wrapping a piece of code up in afunction is called encapsulation.
# Attaches name to code, which serves as a kind of documentation.
# Allows easy code reuse
# If you ever find yourself copy and pasting, encapsulate the code
```

2. Add another parameter, named `length`, to square.

   Modify the body so length of the sides is `length`, and then modify the function call to provide a second argument. 

   Run the program again. Test your program with a range of values for length.

```python
def square(t, length):
    '''Draws a square with sides of a given length
    
    Returns the Turtle to the starting position and location.
    '''
    for i in range(4):
        t.forward(length)
        t.left(90)

square(bob, 100)
square(bob, 10)
square(bob, 1000)

# Adding a paramter to a function is called generalizaation
```

3. Make a copy of `square` and change the name to `polygon`.

   Add another parameter named `n` and modify the body so it draws an n-sided regular polygon.

   Recall the exterior angles of an n-sided polygon are 360/n degrees.

```python
def polygon(t, n, length):
    '''Draws a polygon with n sides.
    
    t: Turtle object
    n: number of line segments
    length: length (in pixels) of each side
    '''
    angle = 360.0 / n 
    for i in range(n):
        t.forward(length)
        t.left(angle)
      
polygon(bob, n=11, length=100) # n and length are 'keyword arguments'
```











