#!/usr/bin/env python3

persons = {
    'Pankaj': 'Is a programmer',
    'Jetinder': 'Is an engineer',
}

def display(persons):
    for person, fact in persons.items():
        print('{}: {}'. format(person, fact))


display(persons)

print()

persons['Jetinder'] = 'Is a mechanical engineer'
persons['Harinder'] = 'I a Pharamacist'

display(persons)