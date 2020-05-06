#!/usr/bin/python3
# function that returns a tuple with the length
# of a string and its first character


def multiple_returns(sentence):
    tuple = ()
    if sentence:
        tuple = len(sentence), sentence[0],
    else:
        tuple = len(sentence), None,

    return (tuple)
