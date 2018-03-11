# Day 09
#symbolic/lesson

## Boolean functions
``` python
def is_divisible(x, y):
	'''Return True if x is divisible by y.'''
	if x % y == 0:
		return True
	else:
		return False

print(is_divisible(6, 4))
print(is_divisible(6, 3))
```

``` python
def is_divisible(x, y):
	return x % y == 0

x, y = 6, 3
if is_divisble(x, y) == True: # == True is not necessary
	print(x, "is disvisble by", y)
```

As an exercise, write a function `is_between(x, y, z)` that returns `True` if `x ≤ y ≤ z` or `False` otherwise.

``` python
def is_between(x, y, z):
	return x <= y <= z


print(is_between(3, 5, 9) # True
```

## Turing Completeness
Think Python (2e), Page 55:
> We have only covered a small subset of Python, but you might be interested to know that this subset is a complete programming language, which means that anything that can be computed can be expressed in this language. Any program ever written could be rewritten using only the language features you have learned so far (actually, you would need a few commands to control devices like the mouse, disks, etc., but that’s all).  

## More Recursion
``` python
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)


def factorial_with_loop(n):
	result = 1
	for i in range(1, n+1):
		result = result * i
	return result


def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result
	
```

> Following the ﬂow of execution is one way to read programs, but it can quickly become overwhelming. An alternative is what I call the “leap of faith”. When you come to a function call, instead of following the ﬂow of execution, you assume that the function works correctly and returns the right result.  

![](Day%2009/Screen%20Shot%202018-02-15%20at%2010.04.04%20AM.png)

## Fibonacci
``` python
def fibonacci(n):
	if n == 0:
		return 0 
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
```

## Type Checking
``` python
factorial(1.5) # n == 1 wouldn't be met for base case
factorial("bob") # factorials of strings...
factorial(-20) # factorial is not defined for negative numbers

def factorial(n):
	# guard against strings
	if not isintance(n, int):
		print("Factorial is only defined for postive integers.")
		return None
	elif n < 0:
		print("Factorial is not defined for negative integers.")
	elif n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = n * recurse
		return result
	
```
