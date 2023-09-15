#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary) != 0:
        comp = a_dictionary[list(a_dictionary)[0]]
        key = list(a_dictionary)[0]
        for k in list(a_dictionary):
            v = a_dictionary[k]
            if v > comp:
                key = k
        return key
    else:
        return None
