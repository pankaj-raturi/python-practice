#!/usr/bin/env python3

#####################
#   Speaking Cat
#####################

userInput = input('Hi! Please enter something: ')
inputLength = len(userInput)
catlength = 13

print()
print( '{}{}'. format(' ' * catlength, '_' * inputLength))
print( '{}< {} >'. format(' ' * (catlength - 2), userInput))
print( '{}{}'. format(' ' * catlength, '-' * inputLength))


# print( ' ' * (catlength-2) + '/' )
print( '{}/'. format(' ' * (catlength-2)) )

# Cat
print(' /\_/\ ', ' ', '/ ')
print('( o.o )')
print(' > ^ <')

