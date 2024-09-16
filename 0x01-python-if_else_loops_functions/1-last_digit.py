#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNumber = abs(number) % 10

if number < 0:
    lastNumber = -1 * lastNumber

if lastNumber > 5:
    print(f"Last digit of {number} is {lastNumber} and is greater than 5")

elif lastNumber == 0:
    print(f"Last digit of {number} is {lastNumber} and is 0")

elif lastNumber > 5:
    print(f"Last digit of {number} is {lastNumber} and is greater than 5")
else:
    print(f"Last digit of {number} is", end=" ")
    print(f"{lastNumber} and is less than 6 and not 0")
