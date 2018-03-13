# Day 16

## Lists

``` python
### Removing items from a list
c = [1, 2, 3]

# remove a specific item
mylist = c[:] # makes a copy of c called mylist
mtlist.remove(1)
print(mylist)
print(c)

# Alias
aliaslist = c # make an alias for c called aliaslist
aliaslist.remove(1)
print(c)
# The association of a variable with an object is called a reference.
# In this example there are two references to the same object

c.remove(4) # Error
if 4 in c:
    c.remove(4)
 
# remove at an index
del c[0]	# del is an operator
print(c)

# remove and store
value_at_zero = c.pop(0)
print(c)
print(value_at_zero)

### Ordering a list
mylist = [9, 3, 11]
mylist.sort() # modifies original list

mylist = [9, 3, 11]
print(sorted(mylist)) 	# returns a copy that is sorted
print(mylist)			# sorted() does not modify original list

mylist.reverse()		# modifies original list
print(mylist)

### Other methods
mylist = [9, 3, 11]

# index
print(mylist.index(3)) 	# 1
print(mylist.index(5))	# ValueError
x = 3
if x in mylist:
    print(x, "is at index", mylist.index(x))
    
# extrema
print(min(mylist))
print(max(mylist))

# split
text = input('Enter some text: ')
text.split()
print(text)
print('You entered', len(text), 'words.')

scores = '90,67,87,102,77,80'
scores = scores.split(',')
print(scores)

# list()
# Requires an object you can iterate over (iterable).
print(list(range(100)))
print(list('hello'))
print(list(42)) # TypeError: 'int' object is not iterable


### Exercise: Grocery List Input
# Adds grocery items to a list as they are input, until the user enters "done."

def main():
    grocery_list = [] # initialize empty list

    item = input('Enter a grocery item or "done": ')

    while item != 'done':
        grocery_list.append(item) # add to list
        item = input('Enter a grocery item or "done": ')

    grocery_list.sort() # organize list alphabetically

    print()
    
    for item in grocery_list:
        print(item)

main()

### rite a function that receives a list of integers and returns their sum.
def sum_list(mylist):
    total = 0
    for i in mylist:
        total += i
    return total

print(sum_list([1, 2, 3]))	# user-defined
print(sum[1, 2, 3])			# built-in

### Tuples
# Tuples are essentially immutable lists.
dimensions = (1920, 1080)
print(dimensions[0])
print(dimensions[1])
dimensions[0] = 1080 # TypeError

# reassign a tupe
dimensions = (1280, 720)

### Other List Topics
# nested arrays
matix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(matrix[1][1])

# list comprehensions
mysquares = []
for x in range(10):
    mysquares.append(x**2)
    
print(mysquares)

mysquares = [x**2 for x in range(10)]
print(mysquares)
```

Posted exercises 35 and 36.

## Cryptography Help

``` python
def rotate_letter(l, k):
    '''Helper function that rotates a character by k letters.'''
    # set start at ord('A') == 65 or ord('a') == 97
    
    # obtain character order between 0 and 25
    c = ord(l) - start
    # rotate c with k modulo 26
    
    # add back starting
    
    # convert back to chr and return

def caesar(message, k):
    # guard aginst improper input
    
    # empty string for ciphertext
    ciphertext = ''
    
    # iterate through each letter in message
    for l in message:
        # rotate alpha chararacters with helper function rotate_letter
        
        # else add l to ciphertext
        
    return ciphertext
        

def vigerence(message, k):
    # guard aginst improper input
    
    # empty string for ciphertext
    ciphertext = ''
    
    # hold current position index
    current_key_index = 0
    
    # iterate through each letter in message
    for l in message:
        # obtain current rotation
        current_k = ord(k[current_key_index]) - ord('a')	# this assumes lower case key
        
        # rotate alpha chararacters with helper function rotate_letter
        
        	# increment current_key_index modulo length of key
            
        # else add l to ciphertext
        
    return ciphertext
```

