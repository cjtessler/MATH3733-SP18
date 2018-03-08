# Day 01
January 18, 2018
#symbolic/lesson

## What is symbolic computation?
- What is a computer?
	- The machine in front of you is a *modern* computer.
	- A computer is one who computes.
	- You are a computer!
	- By today’s standards you are a slow computer with bad memory… but necessary to design and implement modern computers.
	- We need tools to aid in our computation as we move into the future
	- Watched [Early Computing: Crash Course Computer Science #1 - YouTube](https://youtu.be/O5nskjZ_GoI)
- What is *symbolic* computation?
> In computational mathematics, computer algebra, also called symbolic computation or algebraic computation, is a scientific area that refers to the study and **development of algorithms** and software for manipulating mathematical expressions and other mathematical objects.   
- Examples
  - A mathematical formula
  - A logic theorem (De Morgan’s Law)
  - A model
    - Finding an optimal route

    - Plan flights for Frontier Airlines

      ![https://f9prodcdn.azureedge.net/media/3617/route-map_2-23-18.jpg?width=448.5735735735735&height=500]()

    - Symbols ar route1, plane1, path1, city1, etc

    - Variables are time, weather, gas, personnel, etc

## Terminology
A **program** is a sequence of instructions that specify how to perform a computation.

## guess.py
```
I am thinking of a number! Try to guess the number I'm thinking of: 10
Too low! Guess again: 100
Too high! Guess again: -100
Too low! Guess again: 95
That's it! Would you like to play again? (yes/no) 
```

Main Ideas
	- Comparison (conditionals
	- input/output
	- debugging
	- repetition (looping)
	- numbers (ints, floats, etc)
	- words (strings)
	- actions (functions)
	- storing information in *variables*
	- implementing further features such as randomness

Eventually build this, take care of errors, improve gameplay

## repl.it
A **Read-Eval-Print Loop (REPL)**, also known as an interactive shell, is a simple, interactive computer programming environment that takes single user inputs (i.e. single expressions), evaluates them, and returns the result to the user; a program written in a REPL environment is executed piecewise.

## Arithmetic Operators
[Official Python Docs: 3.1. Using Python as a Calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
Arithmetic operators follow standard order of operation

- `()` : parentheses
- `**` : exponentiation
- `+` : addition
- `-` : subtraction
- `*` : multiplication
- `/` : division

## hello.py
Demonstrate `print(“hello world”)` in interactive mode.

A small program is sometimes referred to as a *script*.
``` python
print(“hello world!”)
```

- `print(arguments)`  is a function
- We *call* a function and it performs actions
- “Hello world” is a string (data type)
- Let’s break the program. Below are a few examples.
-
``` python
print("Hello World"
# SyntaxError: unexpected EOF while parsing
# EOF means "End of file"
# The Python interpreter was expecting the closing )
        
print("Hello World)
# SyntaxError: EOL while scanning string literal
# EOL mean "End of line"
# The Python interpreter was looking for the end of string, the closing "

prin("Hello world")
# NameError: name 'prin' is not defined
# "prin" is not a defined function
# We will learn how to define our own functions in the future
        
print(hello world)
# SyntaxError: invalid syntax

 print("Hello World!")
# IndentationError: unexpected indent
# Python use whitespace to determine "blocks" of code
# More on this later
```

- An error in a program is known as a “bug”
![https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2013/09/bug.jpg]()
[The First Computer Bug Ever Found! | Technology Facts - Glitch Facts - YouTube](https://www.youtube.com/watch?v=84VmwdGwYMA)

## Other Remarks
- Editor runs files through a Python Interpreter
- Notice the interpreter specifies where the error occurs

## repl.it assignments
- 000 Tutorial
- 001 More on print()
- 002 Python as a Calculator

