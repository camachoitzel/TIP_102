"""
Problem 1: Counting Iron Man's Suits
Tony Stark, aka Iron Man, has designed many different suits over the years. 
Given a list of strings suits where each string is a suit in Stark's collection, count the total number of suits in the list.

Implement the solution iteratively without the use of the len() function.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?

Base case - empty list . 
# same 
"""

def count_suits_iterative(suits):
    suits_seen = set()
    
    if not suits:
        return -1
    
    for suit in suits:
        if suit not in suits_seen:
            suits_seen.add(suit)
            
    return len(suits_seen)



def count_suits_recursive(suits):
    
    if not suits:
        return 0
    
    
    return count_suits_recursive(suits[1:]) + 1



print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))




'''
Example Output:

3
3
'''








'''
Problem 2: Collecting Infinity Stones
Thanos is collecting Infinity Stones. Given an array of integers stones representing the power of each stone, return the total power using a recursive approach.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.




logic: iterate throuhg list, each number 

sum_stones([20, 25, 30])  [<20>, 25, 30] <<  20
sum_stones([25, 30])  [<25>, 30] <<  25
sum_stones([30]) [30] << 30
<>


'''





def sum_stones(stones):
    
    if not stones:
        return 0
    
    return sum_stones(stones[1:]) + stones[0]



#Example Usage:

print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))

'''
Example Output:

105
68

'''

'''
Problem 3: Counting Iron Man's Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where each string is a suit in Stark's collection, count the total number of distinct suits in the list.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
Evaluate the time complexity of each solution. Are they the same? Define your variables and provide a rationale for why you believe your solution has the stated time complexity.



'''

def count_suits_iterative(suits):
    suits_seen = set()
    
    if not suits:
        return -1
    
    for suit in suits:
        if suit not in suits_seen:
            suits_seen.add(suit)
            
    return len(suits_seen)



def count_suits_recursive(suits):
    
    if not suits:
        return 0
    
    
    return count_suits_recursive(suits[1:]) + 1



print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"])












