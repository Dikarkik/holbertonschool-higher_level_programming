#!/usr/bin/python3
# function that converts a Roman numeral to an integer


def roman_to_int(roman_string):
    if isinstance(roman_string, str) == 0:
        return 0
    romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    i = len(roman_string) - 1
    while i >= 0:
        if i == 0:
            total += romans.get(roman_string[i])
        else:
            if romans.get(roman_string[i - 1]) >= romans.get(roman_string[i]):
                total += romans.get(roman_string[i])
            else:
                total += romans.get(roman_string[i]) - romans.get(
                    roman_string[i - 1])
                i -= 1
        i -= 1
    return total
