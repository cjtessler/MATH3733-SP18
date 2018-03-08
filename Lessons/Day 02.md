# Day 02
#symbolic/lesson

## Why Python
- It’s easy to understand
- It’s popular in today’s market
- The skills are transferable to any language
- It’s open source (developed by the community)
- There are currently 126,788 packages to extend its functionality
- We will talk more about it’s history and future in time
- https://stackoverflow.blog/2017/09/06/incredible-growth-python/

## hello_with_variables.py
A *variable* is a name that refers to a value.
```python
m = "Hello variables"
print(m)

# variables should be descriptive
message = "My message"
print(message)
```

The `=` is the assignment operator. Notice that variable names can be more than single letters.

``` python
print(7)
my_number = 1
print(my_number)

your_number = 14
our_number = my_number + your_number
print(our_number

# print function with multiple arguments
first_name = "Cody"
last_name = "Tessler”
print(first_name, last_name)

# print function with sep argument
print("Today's date is")
print(1, 22, 2018, sep='/')
```

The `print()` function can take more than one argument.  It concatenates the strings. [2. Built-in Functions — Python 3.6.4 documentation](https://docs.python.org/3/library/functions.html#print)

### Rules for variables
- No spaces. Use underscore in place of a space
- The first character of a variable name must be a letter or the underscore character.
- No characters are allowed in a variable name besides alphanumeric (alphabet or numeric) characters and the underscore ("_") character (no special characters like &, !, +, $, etc.)
- Python is case sensitive, so two variables with the same name but different case (i.e. Craig vs craig) are two different variables
- You can't use any of Python's built in "reserved words” or *keywords* (i.e. you can't create a variable called "print" because that would conflict with the print function) 
	- Typing the following commands into the interactive shell will print the a list of keywords.
``` python
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## string_operations.py
``` python
first = "dragon"
second = "fly"
third = first + second
print(third) # prints 'dragonfly'

l1 = "na"
l2 = "hey"
l3 = "goodbye"

print(l1 * 4 * 2, l2 * 3, l3, sep=" ") # print "nananananananana heyheyhey goodbye"
```

[Documentation for Input Function](https://docs.python.org/3/library/functions.html#input)

## Data Types
A *value* is a basic object that that program works with. We can use the type() function to determine the type of a value.
``` python
>>> type(2) 
<class 'int'>

>>> type(42.0) 
<class 'float'>

>>> type('Hello, World!') 
<class 'str'>

>>> # Data Type Converstion
>>> price = "1.99"
>>> type(price)
<class 'str'>

>>> real_price = float(price)
>>> type(real_price)
<class 'float'>

>>> float_to_int = int(real_price)
>>> float_to_int
1
```
More on classes later

## input.py
``` python
your_name = input("what is your name?")
print("Hello", your_name)

your_age = input("How old are you?")
print("You are ", your_age, "years old.")

older_age = your_age + 1
# the input() function returns a string
type(your_age)
# convert a string to an int using the int() function
older_age = int(your_age) + 1
print("Next year you will be ", older_age)
```

## more_math.py
- // : integer division (applies floor function after division)
- % : modulo

``` python
# division returns a float
print(4 / 2)		# 2.0, float
print(3 / 2) 		# 1.5, float

# integer division returns an int by droppng the frational part
print(4 // 2)		# 1, int
print(3 // 2) 	# 1, int

# examples of modulo operator %
# a % b -> remainder when a is divided by b
print(3 % 2) 		# 1
print(11 % 3)		# 2
```


