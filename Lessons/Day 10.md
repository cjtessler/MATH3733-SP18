# Day 10

## Reassignment

``` python
>>> x = 5
>>> x
5
>>> x = 7
>>> x
7
>>> y = 8
>>> y
8
>>> y = x
>>> y
7
>>> x = 9
>>> y # changing x does not change y
7
```

## Updating Variables

``` python
>>> x = x + 1
>>> x
10
>>> z = z + 1 	# z has yet to be 'initilized'
NameError: name 'z' is not defined
>>> z = 0
>>> z = z + 1
>>> z
1
>>> z += 1		# shorthand for z = z + 1
2
>>> z *= 5
>>> z
10
```

## The `while` Statement

The `while` statement is another type of repetition/iteration. Recursion and `for` loops were other types of iteration. While we could implement all of the following ideas using `for` loops or recursion, the `while` loop provided by Python makes certain types of iteration much easier.

``` python
def countdown(n):
    while n > 0:
        print(n)
        n -= 1	# n = n - 1
        # always be sure to have some sort of increment statement with while loops. why?
    print("Blastoff") # this is not part of the while loop
```

As an exercise, rewrite the function `print_n` from Section 5.8 using iteration instead of recursion.

``` python
def print_n(s, n):
    '''Prints a string s n times.'''
	if n <= 0:
	return
print(s)
print_n(s, n-1)

def print_n(s, n):
    while n > 0:
        print(s)
        n -= 1
```

## Break

The `break` statement allows us to exit a loop early - much like `return` allows us to exit a function early.

``` python
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')
```

``` python
> not done
not done
> done
Done!
```

