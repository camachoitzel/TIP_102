
# nums = [3,1,4,1,5,9,2,6]
# target = 9
# # search ---> O(n)

# nums.sort()
# # binary_search



# def bin_search(nums, target):
#     left, right = 0, len(nums) -1

#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] ==target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1

# nums = [2,5,8,12,16,23,38,56,72,91]
# target = 23

# print(bin_search(nums))



def bin_search_recursive(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] < target:
        # left = mid + 1
        return bin_search_recursive(nums, target, mid + 1 , right)
    else:
        # right = mid -1
        return bin_search_recursive(nums, target, mid - 1 , right)


# print(bin_search_recursive(nums, target, 1, len(nums)))


"""
Write a function that performs binary search to find the index of a target value in a sorted list. 
If the value does not exist, return -1.
Example:
Input: nums = [1, 3, 5, 7, 9, 11], target = 5
Output: 2

"""
def find_left(nums, target):
    left, right = 0, len(nums) -1
    index = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] ==target:
            index = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return index

def find_right(nums, target):
    left, right = 0, len(nums) -1
    index = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] ==target:
            index = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return index


nums = [1, 3, 5, 5, 5, 7, 9, 11]

target = 5