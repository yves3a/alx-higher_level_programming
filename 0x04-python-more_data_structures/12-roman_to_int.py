#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    values = [roman_values[char] for char in roman_string]
    total = sum(value if value >= next_value else -value
                for value, next_value in zip(values, values[1:] + [0]))

    return total
