#!/usr/bin/env python3

travel_distance = input('Hi! How many miles you want to travel: ')
travel_distance = float(travel_distance)

if( travel_distance < 3 ):
    print ('I sugges to walk to your destination')
elif( travel_distance < 300 ):
    print('I suggest to drive towards your destination')
else:
    print('I suggest flying to your destination')
