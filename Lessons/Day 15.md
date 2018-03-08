# Day 15

https://slides.com/codytessler/lists/

## Lists

``` python
##### Lists #####
# with variables
t1 = 100
t2 = 90
t3 = 70.5

# with lists
grades = [100, 90, 70.5]
print(grades)
print(grades[0])
print(grades[1:2])

### Add grades to the list
# Operations
grades = grades + [100, 50, 85] # concatenates list
print(grades)
grades *= 2 # concatenates a copy of the current list to the end
print(grades)

grade[1] = 100 # changes the value stored at index 1 to 100 (lists are mutable)


# Append Method
grades.append(42)
print(grades)

# Wrong ways...
grades = grades.append(42) 	# deletes current grade list
grades + [42]				# does not save new item
grades = grades + 42		# list concatenation requires two lists

### Iterating over a list
for grade in grades:
    print(grades)

### Exercise: Write a program that counts of the of A's, B's, C's, and failures in a list of grades. Use a 10-point scale.
# create counter variables
a = 0
b = 0
c = 0
fail = 0

# start iterating through list
# check in which range each grade lies
# and add to appropriate counter
for grade in grades:
    if grade > 90:
        a += 1
    elif 80 < grade <= 90:
        b += 1
    elif 70 < grade <= 80:
        c += 1
    else:
        fail += 1

# output
print ("A's: ", a)
print ("B's: ", b)
print ("C's: ", c)
print ("Fails: ", fail)

### Use indexing when modifying elements
# taxes
prices = [0.99, 14.95, 7.00]

for p in prices: # makes a copy of p
    p *= 1.07
   
print(prices) # notice prices haven't changed

for index in range(len(prices)):
    p[index] *= 1.07

print(prices)

### Searching
my_grocery_list = ['milk', 'cake', 'pizza']
if 'cake' in my_grocery:
    print('yum!')
else:
    print('nope')

    
### Exercise: Given these two lists, write a program that finds all elements that exist in both lists (i.e. the integer 2 exists in both lists). Store your results in a new list and print it out to the user. The expected answer is: [1, 2, 3]

a = [1,2,3,4,5]
b = [2,3,10,11,12,1]

c = []
for element in a:
    if element in b:
        c.append(element)
        # c += [element]
    
print(c)

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
del c[0]
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

# text emthods
text = input('Enter some text: ')
text.split()
print(text)
print('You entered', len(text), 'words.')

scores = '90,67,87,102,77,80'
scores = scores.split(',')
print(scores)

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

### Other List Topics
# nested arrays
matix = [[1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]]

print(matrix[1][1])

# list comprehensions
mysquares = [x**2 for x in range(10)]
print(mysquares)

mysquares = []
for x in range(10):
    mysquares.append(x**2)
    
print(mysquares)

# list()
print(list(range(100)))

# map

# filter

# reduce
```

