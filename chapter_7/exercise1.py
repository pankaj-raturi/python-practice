#!/usr/bin/env python3

# To do list Holder
to_do_list = []

# Input Holder
# Temp. Value to begin with the loop
data = 'test'

# Loop through user inputs
while len(data) > 0 :
    """ data variable holds the user input. Keep on asking untill blank value in the input data """

    data = input('Enter a task for your to­do list.  Press <enter> when done: ')

    if data :
        # Pusth to the user list
        to_do_list.append(data)
        print('Task Added')


# Dispalay findal output
print()
print('Your to do List:')
print('-' * 18)

for task in to_do_list :
    print(task)
