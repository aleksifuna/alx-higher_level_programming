#!/usr/bin/python3
def remove_char_at(str, n):
    index = 0
    str_copy = ""
    for i in str:
        if index != n:
            str_copy += i
        index += 1
    return (str_copy)
