# Day 08

## Return Values

``` python
import math

e = math.exp(1.0)
print("e is", e) # math.exp(1.0) 'returns' a float, which is stored in the variable e

# area of a circle
def circle_area(radius):
    a = math.pi * radius**2
    #print(a)
    return a

circle_area(2) # does not print a, with return
print(circle_area(2))

# absolute function
def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x
  
print(absolute_value(0))
# the lines after a return do not run (dead code)

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
    
# Exercise: Write a function named compare that takes two values, x and y
# returns 1 if x > y
# returns 0 if x == y
# returns -1 if x < y
```

## Incremental Developmental

``` python
# distance.py

# Write a function distance, that determines the distance between two points
# Function is declared properly
def distance(x1, y1, x2, y2):
    return 0.0

d = distance(1, 2, 4, 6)
print(d) # should print 5.0
```

```python
# Do some intermediate computations
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print("dx is", dx)
    print("dy is", dy)
    return 0.0

d = distance(1, 2, 4, 6)
print(d) # should print 5.0
```

``` python
# square
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    # remove print statements (scaffolding)
	dsquared = dx**2 + dy**2
    print("dquared is", dsquared)
    return 0.0

d = distance(1, 2, 4, 6)
print(d) # should print 5.0
```

``` python
# square
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
	dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

d = distance(1, 2, 4, 6)
print(d) # should print 5.0

def circle_area(xc, yc, xp, yp):
    '''Determines the area of the circle given center (xc, yc) and another points (xp, yp).'''
    # distance() is a helper function
    radius = distance(xc, yc, xp, yp)
    return math.pi * radius**2
```

## Project Preview: RPSLS

https://www.youtube.com/watch?v=cSLeBKT7-sM

![Rock_Paper_Scissors_Lizard_Spock_en](G:\My Drive\_Action\Rock_Paper_Scissors_Lizard_Spock_en.svg)



0  Rock > 1 Spock > 2 paper > 3 lizard > 4 scissors > 0 Rock...

Let player 1's choice be p1 and player 2's choice be p2. 

If (p1 - p2) mod 5 is 1 or 2, then player 1 wins.

If (p1 - p2) mod 5 is 3 or 4, then player 2 wins.

If (p1 - p2) mod 5 = 0 , then tie.