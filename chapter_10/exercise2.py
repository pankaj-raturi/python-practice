#!/usr/bin/env python3

animalsList = []

with open('animals.txt', 'r') as animalsFile:
    for animal in animalsFile:
        animalsList.append(animal.strip())

#Sort the animalsList
animalsList.sort()


#Create animals-sorted fiel and iterate through the list again to pu the data in
with open('animals-sorted.txt', 'w') as animalsFile:
    for animal in animalsList:
        animalsFile.write('{}\n'. format(animal))
