# Day 07

## Recursion

``` python
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

countdown(3)

# A function that calls itself is recursive
# we want to be sure there is a base case, else our could run forever (kind of)
# Review stack diagram

def recurse():
    recurse()
    
recurse()

# We can write a function that prints a string n times
def print_n(s, n):
    if n <= 0:		# base case
        return		# returns None, and exits the function
   	print(s)
    print_n(s, n-1)

print_n("hello", 3)
```

