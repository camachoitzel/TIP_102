"""
Given a string s return True if every character in the string is unique. Return false if any characters in s are repeated

Understand:
    -input: string s
    -output: boolean stating if there is a repeated char in s 
    -edge cases: empty string

Plan:
    - empty list of unique chars
    -loop through s and add unique chars to list
        -if char is already in list then return false
        -else return true

Example 1
Input: s = "abcdef"
Expected Output: True

Example 2
Input: s = "aabbcc"
Output: False

Example 3
Example Input: s = ""
Expected Output: True

"""

# def has_all_unique_characters(s):    
#     unique_chars = []

#     for char in s:
#         if char not in unique_chars:
#             unique_chars.append(char)
#         else:
#             return False

#     return True

# s1 = "aabbcc"

# s2 = ""

# s3 = "abcdef"

# print(has_all_unique_characters(s1))
# print(has_all_unique_characters(s2))
# print(has_all_unique_characters(s3))


"""
Given 2 strings needle and haystack, return the index of the first occurence of needle in haystack or -1 if needle is not part of haystack

Understand:
-input: 2 strings
-output: index of needle in haystack
-edge cases: one or more strings is empty

Plan:
-check needle is not longer than haystack if it is return -1

-loop through haystack char and index and compare to needle to see if it is in haystack
    - record index of first char found from needle in haystack to index var
    -compare list to needle to see if they have the same chars
        -if not return -1

return index 

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs twice, starting at indices 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Example 3:
Input: haystack = "mad" needle = "madden"
Needle is longer than haystack, so we return -1. 
"""

# def find_needle(haystack, needle):
#     if len(needle) > len(haystack):
#         return -1
    
#     h_len = len(haystack)
#     n_len = len(needle)

#     for i in range(h_len - n_len + 1):
#         match = 0

#         for j in range(n_len):
#             if haystack[i + j] == needle[j]:
#                 match += 1
#             else:
#                 break

#         if match == n_len:
#             return i

#     return -1



"""
You have a single long flowerbed in which some of the plots arre planted and some are not. 
However, flowers cabbot be placed directly adjacent to another flower

Given an int arr 'flowerbed' containing 0's and 1's w/ 0 = empty 7 1 = not empty and an int n, 
return TRUE of n new flowers can be planted in the flowerbed w/o violating the no-adjacent rule and FALSE otherwise 

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

"""

# def can_place_flowers(flowerbed, n):

#     length = len(flowerbed)

#     for i in range(length):
#         current = flowerbed[i]

#         if i == 0:
#             left = 0
#         else:
#             left = flowerbed[i - 1]

#         if i == length - 1:
#             right = 0

#         else:
#            right = flowerbed[ i + 1] 


#         if left == 0  and current == 0 and right == 0:
#             flowerbed[i] = 1
#             n -= 1

#             if n <= 0:
#                 return True

#     return n <=0



# name = "codepath"
# name[0] = "C"
# print(name)



# def mys_func(s):
#     count = 0
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#     return count

# result = mys_func("AABBAB")
# print(result)


# def reverse_lst(lst):
#     left = 0
#     right = len(lst) - 1

#     while left < right:
#         temp = lst[left]
#         lst[left] = lst[right]
#         lst[right] = temp
#         left += 1
#         right -= 1

#     return lst


# lst = [1,2,3,4,5]
# print(reverse_lst(lst))