#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        comp = a_dictionary[list(a_dictionary)[0]]
        key = list(a_dictionary)[0]
        for k, v in a_dictionary.items():
            if v > comp:
                key = k
        return key
