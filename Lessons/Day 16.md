# Day 16

## Lists

``` python
c = [1, 2, 3]

# Remove a specific item
mylist = c[:] # makes a copy of c called mylist
mtlist.remove(1)
print(mylist)
print(c)

# Alias
# The association of a variable with an object is called a reference.
# In this example there are two references to the same object
aliaslist = c # make an alias for c called aliaslist
aliaslist.remove(1)
print(c)

# Trying to remove an element that is not in the list raises an error
c.remove(4) # Error
if 4 in c:
    c.remove(4)
 
# Removing an item by index
del c[0]	# del is an operator
print(c)

# Remove and store the item in a variable using the pop method
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
# Adds grocery items to a list as they are input, until the user enters "done".
# Prints the sorted list

def main():
    # initialize empty list
    grocery_list = [] 

    # adds items to list
    while item != 'done':
        item = input('Enter a grocery item or "done": ')
        grocery_list.append(item) # add to list

    # organize list alphabetically
    grocery_list.sort() 

    print()
    
    for item in grocery_list:
        print(item)

main()

### Write a function that receives a list of integers and returns their sum.
def sum_list(mylist):
    total = 0
    for i in mylist:
        total += i
    return total

print(sum_list([1, 2, 3]))	# user-defined
print(sum[1, 2, 3])			# built-in


### Nested Lists
matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(matrix[1][1])
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

