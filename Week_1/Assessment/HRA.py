# given an int array, find the index of the first repeating element in it. If there is no repeating element, return None.



# def find_min_index_of_repeating(arr):
#     seen = {}

#     for i, num in enumerate(arr):
#         if num in seen:
#             return seen[num]  
#         seen[num] = i

#     return None


# arr = [1,2,3,4,5]

# print(find_min_index_of_repeating(arr)) 
# arr_2 = [1,2,3,1] 

# print(find_min_index_of_repeating(arr_2)) 

# given 2 int arrays nums1 N and nums2 M, find the intersection of the two arrays. 
# Each element in the result must be unique and you may return the result in any ascending order.

# def intersection(nums1, nums2):
#     result = []
    
#     for num1 in nums1:
#         if num1 in nums2 and num1 not in result:
#             result.append(num1)
    
#     return sorted(result)


# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

# print(intersection(nums1, nums2))  

# nums_1 = [4, 9, 5]
# nums_2 = [9, 4, 9, 8, 4]


# def roman_to_integer(s):
#     roman_numerals = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
    
#     total = 0
#     prev_value = 0
    
#     for char in reversed(s):
#         value = roman_numerals[char]
        
#         if value < prev_value:
#             total -= value
#         else:
#             total += value
        
#         prev_value = value
    
#     return total


# ex1 = "III"
# ex2 = "LVIII"
# ex3 = "MCMXCIV"

# print(roman_to_integer(ex1))  
# print(roman_to_integer(ex2))  
# print(roman_to_integer(ex3))  


# word = "encourage"

# character_count = {}
# for char in word:
#     if char not in character_count:
#         character_count[char] = 1
#     else:
#         character_count[char] += 1
# character_count['e'] += 2

# print(character_count['e'])  # Output: 4

# def mys_function(old_dict):
#     new_dict = {}
#     for key, value in old_dict.items():
#         new_dict[value] = key
#     return new_dict

# old_dict = {'a': 1, 'b': 2, 'c': 3}
# new_dict = mys_function(old_dict)
# print(new_dict) 


def get_top_player(dictionary):
    high_score = 0
    top_player = ""

    for name, score in dictionary.items():
        if score <= high_score:
            high_score = score
            print(high_score)
            top_player = name
            print(top_player)

    return [top_player, high_score]