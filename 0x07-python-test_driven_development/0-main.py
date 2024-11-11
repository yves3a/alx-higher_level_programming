#!/usr/bin/python3
# Import the add_integer function from module 0-add_integer
add_integer = __import__('0-add_integer').add_integer

# Test case 1: Adding two positive integers
print(add_integer(1, 2))

# Test case 2: Adding a positive and negative integer
print(add_integer(100, -2))

# Test case 3: Using default value for b (98)
print(add_integer(2))

# Test case 4: Adding float and integer (float will be cast to int)
print(add_integer(100.3, -2))

# Test case 5: Testing type error with string input
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)

# Test case 6: Testing type error with None input
try:
    print(add_integer(None))
except Exception as e:
    print(e)
