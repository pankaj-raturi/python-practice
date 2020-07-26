#!/usr/bin/env python3

separatorLength = 40

lname = 'Raturi'
name = 'Pankaj ' + lname

# Get length of the string
length = len(name)

# String Function
lower = name.lower()

print (lower)

# * is repetation operator for string
print ( '-' * separatorLength)

# Integer Object
age = 30

# Convert Integers to string objects
# Required to be concatenated with String Objects
print(name + ' Age: ' + str(age))
print ( '-' * separatorLength)

# ---------------------------------------------------------
# Formating String

formatted = 'I am {1}\nMy Age is {0} years'. format(age,name)

print (formatted)

print ( '-' * separatorLength)

# -----------------------------------------------------------
# Format Specification (specifying the width of the objects for printing)

print('{0:10} | {1:>10}'. format('Fruits', 'Quantity'))
print('{0:10} | {1:>10.2f}'. format('Orange', 10))
print ( '-' * separatorLength)

# -----------------------------------------------------------
# Accept standard input

person = input('Please identify yourself: ')
print('Hi {}. How are you?'.format(person))