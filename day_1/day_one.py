import numpy as np

"""
二维数组的二分查找
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


def binary_search_two_dimension(target, num_list):
    if num_list is None or len(num_list) == 0 or len(num_list[0]) == 0:
        return False
    rows, cols = 0, len(num_list[0]) - 1
    while rows < len(num_list) and cols >= 0:
        if num_list[rows][cols] == target:
            return True
        elif num_list[rows][cols] < target:
            rows += 1
        else:
            cols -= 1
    return False


def binary_search_recursion(target, num_list):
    if num_list is None or len(num_list) == 0:
        return False
    mid = len(num_list) // 2
    if num_list[mid] == target:
        return True
    elif num_list[mid] > target:
        return binary_search_recursion(target, num_list[:mid])
    else:
        return binary_search_recursion(target, num_list[mid + 1:])


def create_two_dimension():
    res, count = [], 1
    for i in range(3):
        res.append([])
        for j in range(3):
            res[i].append(count)
            count += 1
    return res


def create_two_dimension_numpy():
    return np.arange(1, 10).reshape(3, 3)


class MySolution:
    def __init__(self):
        pass


print(create_two_dimension())
print(create_two_dimension_numpy())
print(binary_search_two_dimension(9, create_two_dimension_numpy()))
