#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if type(my_list) is list:
        if idx < 0 and idx >= len(my_list):
            return my_list
        del my_list[idx]
        return my_list
