# Day 03
#symbolic/lesson

A *function* is a named sequence of statements that perform computation. When you define a function, you specify the name and sequence of statements. Later, you can “call” the function by name.
``` python
>>> type(42)
<class ‘int’>
```
Name: type
Argument: 42
Return value: <class ‘int’>

## Math Functions
A *module* is a file that contains a collection of related functions.
``` python
>>> import math
>>> math
<module 'math' (built-in>

>>> help(math)

>>> math.log10(100)
2.0
```

Find the cosine function in the documentation and then compute  ![](Day%2003/BC46C644-D375-4826-A3DC-15F09F3608A0.png) and verify the result is the same as computing ![](Day%2003/8F33E8F0-B475-4E04-A944-F910A34CC682.png).

``` python
>>> # We can use composition f o g
>>> # Let's compute cos(45 degrees)

>>> degrees = 45
>>> # Need to convert this to radians
>>> radians = degrees / 180.0 * math.pi
>>> math.cos(degrees)
0.707...
>>> math.cos( 45 / 180.0 * math.pi )
0.707...
```

## Adding New Functions
A *function definition specifies the name of a new function and the sequence of statements that run with the function is called.

``` python
# lyrics.py

def print_lyrics(): # def is a keyword in the function's "header"
	# notice the "body" is indented 1 tab = 4 spaces
	print("Na na na na")
	print("Na na na na")
	print("Hey Hey Hey")
	print("Goodbye")

print_lyrics() # calls the function we just wrote

# a function can call another function
def chorus():
	print_lyrics()
	print() # prints extra line
	print_lyrics()

chorus()

# We did not tell these functions to 'return' anything inparticular
# A function will return None by default
# Think Python refers to these as void functions
```

Write a function that prints outs the lyrics to your favorite song. Each verse, chorus, bridge, etc should be written in the body of its own function. One function call will print the lyrics to the entire song.

## Flow of Execution
Run debug and discuss what is happening: stack, scope, local variables and flow.

![](Day%2003/29B76261-4D21-41FE-9839-7F2DF55856A9.png)

[Visualize Python, Java, JavaScript, TypeScript, and Ruby code execution](http://www.pythontutor.com/visualize.html#code=%23%20lyrics.py%0A%0Adef%20print_lyrics%28%29%3A%20%23%20def%20is%20a%20keyword%20in%20the%20function's%20%22header%22%0A%20%20%20%20%23%20notice%20the%20%22body%22%20is%20indented%201%20tab%20%3D%204%20spaces%0A%20%20%20%20print%28%22Na%20na%20na%20na%22%29%0A%20%20%20%20print%28%22Na%20na%20na%20na%22%29%0A%20%20%20%20print%28%22Hey%20Hey%20Hey%22%29%0A%20%20%20%20print%28%22Goodbye%22%29%0A%0Aprint_lyrics%28%29%20%23%20calls%20the%20function%20we%20just%20wrote%0A%0A%23%20a%20function%20can%20call%20another%20function%0Adef%20chorus%28%29%3A%0A%20%20%20%20print_lyrics%28%29%0A%20%20%20%20print%28%29%20%23%20prints%20extra%20line%0A%20%20%20%20print_lyrics%28%29%0A%0Achorus%28%29&cumulative=false&curInstr=16&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Parameters and arguments
A function can take a parameter called an *argument*.

``` python
# happy_birthday.py

def happy_birthday():
	print("Happy birthday to you")
	print("Happy birthday to you")
	print("Happy birthday dear... person")
	print("Happy birthday to you")

happy_birthday()

def special_happy_birthday(person):
# the input is stored in the variable person
# person = "Cody"
	print("Happy birthday to you")
	print("Happy birthday to you")
	print("Happy birthday dear", person)
	print("Happy birthday to you")

special_happy_birthday("Cody")

# variables used inside a function are 'local'
# They can't be used outside the functions
# They are essentially destroyed after the function is done
# print(person)

```

## Floating Point Error
``` python
>>> 0.1 + 0.2
0.30000000000000004
```

## cos_in_degrees.py
Read the following code and complete the TODOs.
``` python
from math import cos, pi 
# only imports specific functions and removes the need for dot notataion
# i.e., write 'cos(pi)' instead of 'math.cos(math.pi)'

def cos_in_degrees(degrees):
	''' Prints the cosine value of the given degrees. 
		This is called a docstring. It gives information about what a does and returns.
	'''
	# TODO: complete the function
	radians = (degrees / 180.0) * pi
	print(cos(radians))
	
cos_in_degrees(0)	# should print 1
cos_in_degrees(45) 	# should print 0.707...
cos_in_degrees(90)	# should print 6.123233995736766e-17, which is approximately 0
cos_in_degrees(-135)	# should print -0.7071067811865475
# be aware of corner cases, 

# radians is local to the cos_in_degrees function
# print(radians)
```












