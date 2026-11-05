"""
Given two ints 'x' and 'n', where n is non-neg, write a function power()
that recusrsively computes and returns x^n

Understand: 
Input: 1 integers x and n
Output: the result of x^n
Edge Cases: x or n is 0,  x is a neg

Plan:
Check is n = 0 b/c that means that x^0 = 1
x^n = x * x^(n-1)

"""


import math
import os
import random
import re
import sys
import ast



#
# Complete the 'power' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER n
#

# def power(x, n):
#     # Write your code here
#     if n == 0:
#         return 1

#     return x * power(x , n - 1)


"""
You are given a list of char 'letters' that is sorted in non-decreasing order, and a character 'target'.
There are at least 2 diff chars in letters

Return the smallest char in letters that is lexicographically greater (occurs later in alphabet) than target. 
If such a char does not exist, return the first char in letters

Your solution must have O(log n) time complexity

Understand: 
Input: list of chars(increasing order) and a char
Output: a char of the alphabetically next closest char after target
Edge Cases: empty list, target is not a char


"""

# def next_greatest_letter(letters, target):
#     # Write your code here
#     left = 0
#     right = len(letters)

#     while left < right:
#         mid = (left + right) // 2

#         if letters[mid] <= target:
#             left = mid + 1
#         else:
#             right = mid

#     if left == len(letters):
#         return letters[0]
    
    
#     return letters[left]


# letters = ["c","f","j"]

# target = "a"

# print(next_greatest_letter(letters, target))

# Example Input: letters = ["c","f","j"], target = "a"
# Expected Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in
# letters is 'c'.

# Example Input: letters = ["x","x","y","y"], target = "z"
# Expected Output: "x"
# Explanation: There are no characters in letters that is lexicographically 
# greater than 'z' so we return letters[0].


"""
Given an arr of ints 'nums' sorted in ascending order, find the starting and ending pos of a given target value

If the target is not found in the array, return [-1, -1]

Must run the algorithm with O(log n) runtime complexity
"""

def search_range(nums, target):
    def find_first():

        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    def find_last():
        
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    first = find_first()

    if first == -1:
        return [-1,-1]

    last = find_last()

    return [first, last]


        

nums = [5,7,7,8,8,10]
target = 8


print(search_range(nums, target))


"""
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
"""