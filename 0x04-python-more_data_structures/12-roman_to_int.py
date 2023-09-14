#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    my_int = 0
    a = roman_string
    if len(a) > 1:
        for i in range(len(a)):
            if i < (len(a) - 1) and rom[a[i]] < rom[a[i + 1]]:
                my_int -= rom[a[i]]
            else:
                my_int += rom[a[i]]
    else:
        my_int += rom[a]
    return my_int
