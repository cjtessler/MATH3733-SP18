# Day 12

``` python
###### Strings ######
# A string is a sequence of characters.

### indexes
fruit = 'banana'
letter = fruit[1]
print(letter) # prints 'a'
# the expression in the bracket is the index, it begins at 0
print(fruit[0]) # prints 'b'


# len function
length = len(fruit)	# careful to not use len as variable
print(length) # prints 6
print(fruit[length]) # IndexError: string index out of range
print(fruit[length-1]) # prints 'a'


# indexing backwards
print(fruit[-1]) # prints 'a'
print(fruit[-4]) # prints 'n'


### transversal with a while loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1
    
    
### transversal with a for loop
for index in range(len(fruit)):
    print(fruit[index]
          
# If we do not need the index, we can iterate through the characters directly         
for letter in fruit:
    print(letter)
    
    
### String Slices
s = 'Monty Python'
first = s[0:5] 
print(first) # prints 'Monty'
# 0 <= i < 5

second = s[6:12]
print(second) # prints 'Python'

print(s[:3]) # prints 'Mon'
# if no starting index is given, defaults to 0
print(s[10:]) # prints 'on'

# Exercise: Print the space
print(s[5:6])


### Strings are immutable
# immutable == can't change
greeting = 'Hello, world!'

# Change the first letter to a J
greeting[0] = 'J' # TypeError: 'str' object does not support item reassignment
greeting = 'J' + greeting[1:]


### Searching
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print(find('banana', 'n')) # prints 2
print(find('banana', 'h')) # prints -1

# Exercise: Generalize the function so that it has a third parameter, the index in the word where it should start looking
def indexed_find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print(indexed_find('banana', 'n', 3)) # prints 4
print(indexed_find('banana', 'h', 3)) # prints -1


### Looping and Counting
counter = 0
for letter in 'banana':
    if letter == 'a':
        counter += 1
print(counter) # prints 2

# Exercise: Encapsulate this logic into a function called count
def count(word, l):
    counter = 0
    for letter in word:
        if letter == l:
            counter += 1
     return counter
 
print(count('banana', 'a')) # prints 2
```
