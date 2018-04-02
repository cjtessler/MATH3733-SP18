# Day 17

``` python
##### List Comprehensions #####
mysquares = []
for x in range(10):
    mysquares.append(x**2)
    
print(mysquares)

# {x^2 : x in [0, 9)}
mysquares = [x**2 for x in range(10)]
print(mysquares)

# Exercise:  Generate a list of the first 4 powers of 2.
mypowers = [2^i for i in range(4)]
print(mypowers)

# Find all of the number from 1-1000 that are divisible by 7
div_by_7 = [x for x in range(1001) if x % 7 == 0]
print(div_by_7)

# Syntax: [var_expression for var in iterable if condition]

# Exercise: Find all of the words in a string that are less than 4 letters.
s = 'the quick brown fox jumped over the lazy dog'
small_words = [word for word in s.split() if len(word) < 4]
print(small_words)

## Exercises:
# Find all of the numbers from 1-1000 that have a 3 in them
# Count the number of spaces in a string
# Remove all of the vowels in a string

## Challenges:
# Use a dictionary comprehension to count the length of each word in a sentence.
# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
# For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by

##### Tuples #####

# Tuples are essentially immutable lists.
dimensions = (1920, 1080)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 1080 # TypeError

# reassign a tuple
dimensions = (1280, 720)

##### Dictionaries #####
# A dictionary is more general than a list.
# A list's elements were accessed using integer indices.
# A dictionary's elements are accessed by using key

# Initialize an empty dictionary
eng2sp = dict() 
eng2sp = {}
print(eng2sp)

# Add elements to a dictionary
# New in Python 3.6 Dictionaries are ordered in the way you add items.
# Think Python uses Python 3.5
eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp['two'] = 'dos'
print(eng2sp)

# Create/Update a dictionary
# Syntax: {key: value, ...}
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

# Access elements in a dictionary
print(eng2sp['two'])
#print(eng2sp['four']) # KeyError


### Iterate through a dictionary
# Looks at keys by default
for entry in eng2sp:
    print(entry) 

for key in eng2sp.keys():
    print(key)

print('one' in eng2sp)
print('uno' in eng2sp)

# Iterate through values
for value in eng2sp.values():
    print(value)

### Exercise: Make a dictionary containing everyone's favorite number.
our_numbers = {
    'student1': 5,
    'student2': 10,
}

### Exercise: Write a function that finds the average our_numbers
### The parameter should be a dictionary d, with the numbers stored as the values.
def averaage_values(d):
    total = 0
    for num in d.values():
        total += num
    return total / len(d) 
    # return sum(d.values()) / len(d)

print(averaage_values(our_numbers))

### Dictionaries as a collection of counters
# Suppose you are given a string and want to count how many times each letter appears.
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            # create the key is not present
            d[c] = 1
        else:
            # increment the value if k is present
            d[c] += 1
    return d

h = histogram('parrot')
print(h)
```