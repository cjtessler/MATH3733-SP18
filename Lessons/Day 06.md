# Day 06

## Boolean Expressions

``` python
>>> 5 == 5
True
>>> 5 == 6
False
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> bool(0)
False
>>> bool(1)
True
>>> bool("hello")
True
>>> bool(None)
False
>>> bool(42)
True
```

``` python
x = 5
y = 6

# == is the comparison operator
# =  is the assignment operator
print(x == y)
print(x != y)	# not equal
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

s1 = "abb"
s2 = "abc"

print(s1 == s2)
print(s1 < s2)
print(s2 > s1)
# string comparison is done by lexographical ordering
```

## Logical Operators

``` python
# 'and' returns true if and only if both x and y are True
# 0 represents False, 1 represents True
print('x', 'y', '\t x and y')
for x in range(2):
    for y in range(2):
        print(x, y, '\t', x and y)
        
# 'or' returns False if and only if both x and y are False
print('x', 'y', '\t x or y')
for x in range(2):
    for y in range(2):
        print(x, y, '\t', x or y)
```

## Conditional Execution

``` python
x = int(input("Can I have an x please?"))
# 5, -1, 0
if x > 0:
    print('x is positive')
```

## Alternative Execution

``` python
if x % 2 == 0:
	print('x is even')
else:
    # This is a 'branh'
	print('x is odd')
```

## Chained Conditionals 

This is a very common construct. In games, may be used to do a certain action only if a certain key is pressed. Or, we can ensure that we were given the correct type of data when asking a user for input.

``` python
x = 5
y = 6

if x < y:
	print('x is less than y')
elif x > y:
	print('x is greater than y')
else:
	print('x and y are equal')
```

No limit on number of branches.

The first branch that evaluates to True runs, and the rest of the branches are ignored.

## Nested Execution

``` python
if x == y:
	print('x and y are equal')
else:
	if x < y:
		print('x is less than y')
	else:
		print('x is greater than y')
```

```python
if 0 < x:
	if x < 10:
		print('x is a positive single-digit number.')
 
if 0 < x and x < 10:
	print('x is a positive single-digit number.')
    
if 0 < x < 10: # not available in all languages
	print('x is a positive single-digit number.')
```



