'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

 Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.



Understand:
Input: array of characters s
Output: reversed string of original characters
Edge Cases: empty array

Match:
-2 pointers
-one pointer at beg and 1 pointer at end

Plan:
if len(s) < 2:
    return s

start a pointer at start of list s[0]
start a pointer at end of string s[-1] or s [len(s) - 1]


while left < right:
    dummy_pointer = left
    left = right
    right = dummy_pointer

    left += 1
    right -= 1


    

  
    
'''


# def reverseString(s):
#     """
#     :type s: List[str]
#     :rtype: None Do not return anything, modify s in-place instead.
#     """
#     if len(s) < 2:
#         return s
    
#     left = 0
#     right = len(s) - 1
    
#     while left < right:
#         dummy_ptr = s[left]
#         s[left] = s[right]
#         s[right] = dummy_ptr
#         left += 1
#         right -=1


# s = ["h","e","l","l","o"]
# reverseString(s)
# print(s)



"""

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.


Understand:
Input: int arr in non-decreasing order (increasing order)
Output: squares of the numbers in og arr in increasing order
Edge Cases: empty array, 1 <= nums.length <= 10^4, -10^4 <= nums[i] <= 10^4

Match:
-iterate through list

Plan:
check the array is >= 1 but not <= 10**4

iterate through list at i
    square each value at i

sort list
return list
"""


# def sortedSquares(nums):
#     if len(nums) <= 1:
#         return nums**2

#     for i in range(len(nums)):

#         nums[i] = nums[i]**2
        

#     return sorted(nums)

# def sortedSquares(nums):
#     # Create a result list with the same number of empty positions as nums.
#     result = [0] * len(nums)

#     # Start one pointer at the beginning of the list.
#     left = 0

#     # Start the other pointer at the end of the list.
#     right = len(nums) - 1

#     # Fill result from the last position toward the first position.
#     # for position in range(start, stop, step)
#     # start at pos 4 , stop before -1 so 0 inclusive, step back -1 step -> 4,3,2,1,0
#     for position in range(len(nums) - 1, -1, -1):

#         # Square the number currently at the left pointer.
#         left_square = nums[left] ** 2

#         # Square the number currently at the right pointer.
#         right_square = nums[right] ** 2

#         # Compare the two squared values.
#         if left_square > right_square:

#             # The larger square belongs at the current position.
#             result[position] = left_square

#             # Move the left pointer one position to the right.
#             left += 1

#         else:
#             # The right square is larger or equal, so place it here.
#             result[position] = right_square

#             # Move the right pointer one position to the left.
#             right -= 1

#     # Return the completed list of sorted squares.
#     return result

def sortedSquares(nums):
    result = [0] * len(nums)

    left = 0
    right = len(nums) - 1
    position = len(nums) - 1

    while left <= right:
        left_val = nums[left]
        right_val = nums[right]

        left_val = left_val**2
        right_val = right_val**2

        if left_val > right_val:
            result[position] = left_val
            left += 1
        else:
            result[position] = right_val
            right -= 1
        position -= 1

    return result 

nums = [-7,-3,2,3,11]
print(sortedSquares(nums))