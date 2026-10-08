"""
Given a string s, find the first non repeating character in it and return it's index
If it does not exiat retunr -1


Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

UNDERSTAND:
Input - a string
Output - ther index of first non repeating character
Edge Cases - empty string, case sensitive or not


PLAN:
check that string is not empty
change the string to all lowercase
make an empty dict
loop through the string
add each letter as a key with a value of 1
if the letter is already in the dict increase the value by 1

loop though dict and find all letters with value of 1 and return its index
"""

# def first_non_repeating_characters(s):
#     if not s:
#         return -1 

#     counts = {}

#     for char in s:
#         if char in counts:
#             counts[char] = counts[char] + 1
#         else:
#             counts[char] = 1

#     for index, char in enumerate(s):
#         if counts[char] == 1:
#             return index

#     return -1 

# s = "leetcode"

# s2 = "loveleetcode"

# s3 = "aabb"

# print(first_non_repeating_characters(s))
# print(first_non_repeating_characters(s2))
# print(first_non_repeating_characters(s3))


"""
You are given a 1-indexed array of intergers numbers, sorted in non-decreasing order, and an integer target
Your task is to find 2 distinct elements in the array such that they add up to the target return the 1 based indfices of the number sin the form
[index1, index2]. Where index1 < index2

Requirements:
-you may not use the same element twice
-your solution must use constant extra space


PLAN:
"""

# def two_sum(numbers, target):
#     if not numbers:
#         return []

#     left_ptr = 0
#     right_ptr = len(numbers) - 1

#     while left_ptr < right_ptr:
#         total = numbers[left_ptr] + numbers[right_ptr]

#         if total == target:
#             return [left_ptr + 1 , right_ptr + 1]
#         elif total < target:
#             left_ptr += 1
#         else:
#             right_ptr -= 1

#     return []


# def mys_funct(nums):
#     left = len(nums) - 1
#     right = len(nums) - 1

#     while right >= 0:
#         if nums[right] != 0:
#             temp = nums[right]
#             nums[right] = nums[left]
#             nums[left] = temp
#             left -= 1
#         right -= 1

#     return nums

# nums = [0,0,1,2,0,3]
# print(mys_funct(nums))


def is_palindrome(s):
    left, right = 0, len(s) 

    while left < right:
        
        left += 1
        right -= 1

        if s[left].lower() != s[right].lower(): 
            return False

    return True

# Test Cases
s1 = "amanaplanacanalPanama"
s2 = "abbd" 
print(is_palindrome(s1))
print(is_palindrome(s2)) 