#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    for score, weight in my_list:
        total += score * weight
    result = total / sum(weight for score, weight in my_list)
    return result
