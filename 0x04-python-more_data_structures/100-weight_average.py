#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight_score = 0
    weight_sum = 0
    for i in range(len(my_list)):
        weight_score += (my_list[i][0] * my_list[i][1])
        weight_sum += my_list[i][1]
    return weight_score / weight_sum
