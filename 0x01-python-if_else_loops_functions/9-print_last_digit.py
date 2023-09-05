#!/usr/bin/python3
def print_last_digit(number):
    last_digit = "{}".format(str(number)[-1])
    if ord(last_digit) > 47 and ord(last_digit) < 58:
        print(last_digit)
        return (int(last_digit))
    else:
        return (None)
