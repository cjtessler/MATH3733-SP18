# Day 05

## Last Time

```python
import turtle

# We create a Turtle object and assign it to a variable named bob
bob = turtle.Turtle()
print(bob)
turtle.mainloop()

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

Continue the exercises:

4. Write a function called `circle` that takes a turtle `t`, and radius `r` , as parameters and draws an approximate circle by calling `polygon` with an appropriate length and number of sides.

   Test your function with a range of values for `r` .

``` python
import turtle
from math import pi

bob = turtle.Turtle()
turtle.mainloop()

# --snip--
    
def circle(t, r):
        ''' Draws an approximated circle.'''
    circumference = 2 * pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)
    
  
circle(bob, 10)
circle(bob, 100)
circle(bob, 1000)
```

One limitation of this solution is that `n` is constant. Large n, yield poor approximations. We do not want to complicate the *interface* by adding more parameters.

Choose an appropriate value of `n` depending on the circumference.

``` python
def circle(t, r):
        ''' Draws an approximated circle.'''
    circumference = 2 * pi * r
    # n = (circumference / 3) + 3 to illustrate preconditions
    n = int(circumference / 3) + 3	# adding three guarentees the polygon has at least 3 sides
    length = circumference / n
    polygon(t, length, n)
```

5. Make a more general version of `circle` called `arc` that takes an additional parameter, angle, which determine what fraction of the circle to draw.

   `angle` is in units of degrees, so when `angle=360`, `arc` should draw a complete circle.

```python
def arc(t, r, angle):
    arc_length = 2 * pi * r * (angle / 360)
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    
    for i in range(n):
        t.forward(step_length)
        t.left(step_angle)
```

We have used the same code in multiple places.

```python
# Refactoring
def polyline(t, n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

    
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
    
    
def arc(t, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = float(angle) / n
        polyline(t, n, step_length, step_angle)
 

def circle(t, r):
    arc(t, r, 360)
```



## Closing Comments

Where are docstrings used

Optimal solution for triangle problem

