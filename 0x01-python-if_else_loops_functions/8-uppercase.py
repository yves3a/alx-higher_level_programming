#!/usr/bin/python3

def uppercase(str):
    result = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:  # Check if it's a lowercase letter
            result += chr(ord(c) - 32)  # Convert to uppercase
        else:
            result += c  # Keep the character as it is
    print("{}".format(result))
