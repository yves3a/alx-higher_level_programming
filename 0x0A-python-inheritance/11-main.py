#!/usr/bin/python3
print("Starting import...")
Square = __import__('11-square').Square
print("Import successful")

s = Square(13)
print("Square created")

print(s)
print(s.area())