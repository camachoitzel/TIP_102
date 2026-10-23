"""
Given a 0-indexed integer array nums of length n and an integer target, write
a function count_pairs() that return the number of pairs i, j where 0 <= i < j < n and nums[i] + nums[j] < target

Understand:
Input: array of ints, ints can be neg
Output: an int that counts the num of pairs that satisfy the conditions
Edge Cases: empty array

Plan:
check for empty array
    if empty return 0

output var = 0

use a for loop to loop thorugh array and check i w/ each j
i = 0
j = i + 1
check 0 <= i < j 
check nums[i] + nums[j] < target
advance only j then once you reach the end of the array advance i and start again
"""

# def count_pairs(nums, target):
#     count = 0

#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] < target:
#                 count += 1

#     return count



"""
Given an arr nums return True if the array was originally sorted in non-decreasing order, then rotated some num of pos (including zero).
Otherwise return False

There may be duplicates in the og arr

Note: Rotating an arr by a certain num of pos means shiftinf wach element that many pos to the right or left.
When shifter one pos to the right the lst elem in the arr becomes the first elem. Formally and arr A rotated by x positions results in an array B
of the same length such that A[i] == B(i + x) % A.length. Where % is the modulo operation

Understand:
Input: Array of nums w/ duplicates
Output: Boolean if arr can be sorted w/ x num of shifta
Edge Cases: empty array 

Plan:
1. If the array has fewer than two elements, return True.
2. Initialize a counter called decreases to 0.
3. Loop through every index i in the array.
4. Let next_index be (i + 1) % len(nums), so the last element is
   compared with the first element.
5. If nums[i] > nums[next_index], increment decreases.
6. If decreases becomes greater than 1, return False.
7. After the loop, return True.



Time complexity: O(n)
Space complexity: O(1)


"""

# def is_sorted_rotated(nums):
#     decreases = 0

#     n = len(nums)
    
#     if n < 2:
#         return True 

#     for i in range(n):
#         next_index = (i + 1) % n

#         if nums[i] > nums[next_index]:
#             decreases += 1

#         if decreases > 1:
#             return False

#     return True


"""
Given an array of int nums and an int k, return the total num of cont subarrays whose sum = k

Ex. 
Input: [1,1,1] , 2
Output: 2

Input: [1,2,3] , 7
Output: 0

Understand:
Input: array of integers and an int for a target val
Output: int of subarrays that have values that add up to target values (no limit on subarray size but will be smaller than og array)
Edge Cases: target of 0, empty array, negative numbers

Plan:
1. Initialize count to 0.
2. Initialize current_sum to 0.
3. Create a dictionary prefix_counts with {0: 1}.
   This represents a prefix sum of 0 occurring once before the
   array begins.
4. Loop through each number in nums:
   a. Add the number to current_sum.
   b. Calculate needed_sum = current_sum - k.
   c. If needed_sum is in prefix_counts, add its frequency to count.
   d. Add current_sum to prefix_counts, or increase its frequency.
5. Return count.

Time complexity: O(n)
Space complexity: O(n)

"""

# def count_subarrays(nums, k):
#     count = 0
#     current_sum = 0
#     prefix_counts = {0: 1}

#     for num in nums:
#         current_sum += num
#         needed_sum = current_sum - k

#         if needed_sum in prefix_counts:
#             count += prefix_counts[needed_sum]

#         prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

#     return count

# def process_nums(nums, threshold):
#     stack = []

#     for num in nums:
#         if num < threshold:
#             stack.append(num)
#         elif num <= 10 and stack:
#             stack.pop()
#     return stack

# print(process_nums([3,5,1,9,6,15], 8))

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_freq = {}
    t_freq = {}

    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1

    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1 
        
    return s_freq == t_freq