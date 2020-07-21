#!/usr/bin/env python3

#####################
#   Speaking Cat
# Taking input from user and showing it back in cat speakig bubble.
# Dynamic lengt of the Speacking bubble
#####################

def cat_say ( catMessage ) :

    inputLength = len(catMessage)
    catlength = 13

    print()
    print( '{}{}'. format(' ' * catlength, '_' * inputLength))
    print( '{}< {} >'. format(' ' * (catlength - 2), catMessage))
    print( '{}{}'. format(' ' * catlength, '-' * inputLength))

    # print( ' ' * (catlength-2) + '/' )
    print( '{}/'. format(' ' * (catlength-2)) )

    # Cat
    print(' /\_/\ ', ' ', '/ ')
    print('( o.o )')
    print(' > ^ <')



# Handle direct call through shell

if __name__ == '__main__':
    userInput = input('Hi! Please enter something: ')
    cat_say(userInput)