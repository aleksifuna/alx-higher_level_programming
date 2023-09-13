#!/usr/bin/python3
def weight_average(my_list=[]):
    weight_score = 0
    weight_sum = 0
    for i in range(len(my_list)):
        weight_score += (my_list[i][0] * my_list[i][1])
        weight_sum += my_list[i][1]
    return weight_score / weight_sum
