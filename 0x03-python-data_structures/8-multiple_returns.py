#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        first_char = "None"
    else:
        first_char = sentence[0]

    length = len(sentence)
    new_tuple = (length, first_char)
    return new_tuple
