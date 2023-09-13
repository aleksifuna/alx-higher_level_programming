#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = search
    b = replace
    new_list = (list(map((lambda x: b if x == a else x), my_list)))
    return new_list
