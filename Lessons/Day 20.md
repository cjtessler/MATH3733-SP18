# Day 20

## Dictionaries

``` python
### Dictionaries as a collection of counter
# Suppose you are given a string and want to count how many times each character appears.

def histogram(s):
    d = {}
    for l in s:
        if l not in d:  # create the key if it is not present
            d[l] = 1
        else:
            d[l] += 1   # increments the value if key is present
    return d
        
# cleaner print
def print_hist(h):
    for key in h:
        print(key, h[key])

print_hist(h)

# sort then print
def sorted_print_hist(h):
    for key in sorted(h):
        print(key, h[key])

sorted_print_hist(h)

### Nesting
## Dictionary of Lists
# Say we have a histogram, but would rather have something that maps freq -> letter
# Answers the question: What letters occur n times?
# h = {'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1}
# inverse = {1: ['p', 'a', 'o', 't'], 2: ['r']}
# Notice we are using integers for keys
# Keys must be 'hashable', which essentially means it can be mapped to an integer
# Immutable objects are hashable

def inverse_dictionary(d):
    inverse = {}
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


## List of Strings
word = 'hello'
word = list(word)
print(''.join(word))
print('-'.join(word))
        

## List of Dictionaries
# We are making Space Invaders, and need information about the aliens
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Exercise: Favorite places
# Make a dictionary called favorite_places that stores a list of 3 favorite places for 3 of your peers.
# Loop through the dictionary and print each person's name and their favorite places.
favorite_places = {
    'Cody': ['SEU', 'Home', 'Savannah'],
    'Thing1': ['Nowhere', 'Whoville', 'Over there'],
    'Thing2': ['Here', 'There', 'Somewhere']
}

for key in favorite_places:
    print(key, favorite_places[key])

## Dictionary of Dictionaries
# Puppies?
dogs = {
    'Riley': {
        'owner': 'Paul',
        'breed': 'German Shepherd',
        'gender': 'female'
        'age': 14
    },
    'Bernie': {
        'owner': 'John',
        'breed': 'Beagle',
        'gender': 'male'
        'age': 8
    }
}

for dog, _dog_info in dogs.items():
    name = dog
    owner = dog_info['owner']
    breed = dog_info['breed']
    gender = dog_info['gender']
    age = dog_info['age']
    # formated string
    print(f'{name} is a {gender} {breed} loved by {owner} for {age} years')
```

