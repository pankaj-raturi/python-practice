#!/usr/bin/env python3

i = 1
# fileObject = open('data1.txt', 'r')

with open('data1.txt', 'r') as fileObject:
    for line in fileObject:
        print('{}: {}'. format(i, line.strip()))
        i += 1