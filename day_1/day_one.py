from typing import List, Optional

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


"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy，则经过替换之后的字符串为We%20Are%20Happy。
"""


def get_str_no_space_stack(str_params):
    stack = []
    for i in str_params:
        if i == ' ':
            stack.append('%20')
            continue
        stack.append(i)
    return ''.join(stack)


def get_str_replace_space(str_params):
    str_list, original_len = list(str_params), len(str_params) - 1
    for i in range(original_len + 1):
        if str_list[i] == ' ':
            str_list.append('1')
            str_list.append('2')
    new_len = len(str_list) - 1
    while 0 <= original_len < new_len:
        c = str_list[original_len]
        original_len -= 1
        if c != ' ':
            str_list[new_len] = c
            new_len -= 1
        else:
            str_list[new_len] = '0'
            new_len -= 1
            str_list[new_len] = '2'
            new_len -= 1
            str_list[new_len] = '%'
            new_len -= 1
    return "".join(str_list)


"""
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.res = []

    def get_reverse_list_recurse(self, node_list):
        if node_list:
            if node_list.next:
                self.get_reverse_list_recurse(node_list.next)
            self.res.append(node_list.val)
        return self.res


def get_reverse_list(node_list):
    stack = []
    while node_list:
        stack.append(node_list.val)
        node_list = node_list.next
    return stack[::-1]


"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def generate_tree(self, pre_order: List[int], in_order: List[int]) -> Optional[TreeNode]:
    if not pre_order or not in_order:
        return None
    root = TreeNode(pre_order[0])
    index = in_order.index(pre_order[0])
    root.left = self.generate_tree(pre_order[1:index + 1], in_order[:index])
    root.right = self.generate_tree(pre_order[index + 1:], in_order[index + 1:])
    return root


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

def remove_duplicates(nums: List[int]) -> int:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i + 1])
        else:
            i += 1
    return len(nums)


a = [0, 0, 1, 1, 2, 3, 4]
print(remove_duplicates(a))
