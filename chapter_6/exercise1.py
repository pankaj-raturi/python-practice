#!/usr/bin/env python3


def noun():
    noun = input('Please enter the noun: ')
    return noun

def verb():
    verb = input('Please enter the verb: ')
    return verb

def adjective():
    return input('Pleaes enter the adjective: ')

def story(noun, verb, adjective):
    story = "In this course you will learn how to {1}.  " \
        "It's so easy even a {0} can do it.  " \
        "Trust me, it will be very {2}.".format(noun, verb, adjective)
    print(story)


story(noun(), verb(), adjective())