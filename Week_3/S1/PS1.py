"""
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, 
such as () for mentions, [] for hashtags, and {} for links. 
You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.
def is_valid_post_format(posts):
  pass
Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
Example Output:

True
True
False

UNDERSTAND:
Input - string of a post
Output - boolean
Edge Cases - 
- empty string
- odd # of chars
- other chars

PLAN:
- check if string is empty 
- create a empty stack
- create a dict w/ key of corresponding braces
-loop through the string
    -add char to stack as long as it is an open brace
    -if a closed brace 
        -pop from stack to see if it matches the closed brace
    -else return false



"""

def is_valid_post_format(posts):
  if not posts:
     return False

  stack = []
  dict = {")": "(", "}":"{", "]": "["}
  
  for char in posts:
    
    if char in set("({["):
        stack.append(char)
    
    elif char in set(")}]"):
        if not stack:
           return False
        
        top = stack.pop()
        
        if top != dict.get(char):
           return False
  return not stack

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
print(is_valid_post_format("("))

"""
Problem 2: Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to reverse the order of comments before displaying them. 
Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
  pass
Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']

UNDERSTAND:
Input - queue of comments (strings)
Output - stack of reversed comments 
Edge Cases - 
-empty queue


PLAN:
-check if the queue is empty
-create empty stack for reverse
-while queue is not empty
-popleft items from queue and add to stack
-return stack

"""
# from collections import deque

# def reverse_comments_queue(comments):
#     comments = deque(comments)
    
#     reverse = []

#     while comments:
#         reverse.append(comments.pop())

#     return reverse


# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


"""
Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, 
meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. 
Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.

def is_symmetrical_title(title):
  pass
Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
Example Output:

True
False

UNDERSTAND:
Input -
Output - 
Edge Cases - 

PLAN:




"""