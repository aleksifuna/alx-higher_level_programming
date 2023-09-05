#!/usr/bin/python3
def uppercase(str):
    upper_case = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            upper_case += "{:c}".format(ord(i) - 32)
        else:
            upper_case += i
    print(upper_case)
