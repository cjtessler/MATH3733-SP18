# Day 13

## Strings

``` python
### Review

# String Addition
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)

    
# String Slices
s = 'Monty Python'
print(s[-2:0]) # prints '' because start at 'o' and cannot go back 'M'

### String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
word = 'banana'

# upper
new_word = word.upper() # we are 'invoking' upper on word
print(new_word) # prints 'BANANA'
print(word) # string methods do not change the string, they return a new string

# find
index = word.find('a')
print('a is at index', index)

# this function is more general that ours
index = word.find('na')
print('na begins at index', index)

# Exercise: Peruse the string methods in the docs. What does strip and replace do?
word = "help!!!!!!!!!!!!"
print(word.rstrip('!')) # prints 'help'
print(word.replace('!', '.'))

# isX methods return a Boolean
'1'.isalpha() # False
'1'.isdigit() # True
'a'.islower() # True
'A'.isupper() # True


### Micsellaneous
# The 'in' operator
print('a' in 'banana') # True
print('l' in 'banana') # False


# comparison
print('A' == 'a') # False
print('A' < 'a')  # True

# order
# http://www.asciichart.com/
print(ord('A'))	# 65
print(ord('a'))	# 97
print('#' < 'a') # True. why?

# chr
print(chr(65)) # A
print(chr(97)) # a
```

## Reading Word Lists

```python
# Load words.txt from http://greenteapress.com/thinkpython2/code/words.txt
fin = open('words.txt')

# Read line
print(fin.readline())
print(fin.readline())

# Remove \n
line = fin.readline()
word = line.strip()
print(word)

for line in fin:
    word = line.strip()
    print(word)
    
# Exercise: How many words contain a 'q'?
# Fact: 'q' has a relative frequency of 0.095% in the English language
def has_q(word):
    if 'q' in word:
        return True
    # returns None
    # bool(None) == False

# count the words that contain 'q'
q_counter = 0
for line in fin:
    word = line.strip()
    if has_q(word):
        q_counter += 1

print('q counter:', q_counter)

fin.close()
```

## Project Overview

#### Caesar

$c_i \equiv(p_i+k) \mod 26 \iff c_i = (p_i + k)\ \%\ 26$

Encrypt 'HELLOZ' with a key of 2

| Plaintext  | H    | E    | L    | L    | O    | Z    |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- |
| $p_i$      | 7    | 4    | 11   | 11   | 14   | 25   |
| $c_i$      | 9    | 6    | 13   | 13   | 16   | 1    |
| Ciphertext | J    | G    | N    | N    | Q    | B    |

#### Vigenère

Encrypt 'Hello World' with the key = 'ab'

| Plaintext  | H    | i    |      | W    | o    | r    | l    | d    |
| ---------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| $p_i$      | 7    | 8    |      | 22   | 14   | 17   | 11   | 3    |
| $k_j$      | 0    | 1    |      | 0    | 1    | 0    | 1    | 0    |
| $c_i$      | 7    | 9    |      | 22   | 15   | 17   | 12   | 3    |
| ciphertext | H    | j    |      | W    | p    | r    | m    | d    |

#### Pseoduocode 

Think about the algorithm before you start typing. (Pseudocode)

- Get key
- for each character in plainstring
  - if alphabetic
    - preserve case
    - shift plaintext character by key
- return ciphertext



