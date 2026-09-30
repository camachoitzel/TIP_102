# Stack
# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)

# print(stack)
# print(stack[-1])

# popped = stack.pop()
# print(popped)
# print(stack)

# stack.pop()
# print(stack)

# stack.pop()
# print(stack)

# stack.pop()
# print(stack)

# Queue
# queue = []
# queue.append("Messi")
# queue.append("Ronaldo")
# queue.append("Haaland")
# print(queue)

# print(queue.pop())
# print(queue.pop(0))

# from collections import deque

# queue= deque()
# queue.append("Messi")
# queue.append("Ronaldo")
# queue.append("Haaland")


# print(queue.popleft())
# print(queue)


# print(queue.popleft())
# print(queue)


"""

Write a function that checks if a given string containing parentheses is balanced. 
The function should return True if every opening parenthesis 
has a corresponding closing parenthesis in the correct order, and False otherwise.


UNDESTAND:
Input - string
Output - boolean
    valid: every open bracket has a corresponding closing bracket
Edge Cases - 
- empty string
- odd # of chars
- other chars


MATCH:
-stack
-map (dict)

PLAN:
- create empty syack
- create map of opening to closing braces
- loop through each char
    -if opening brace, check if correcsponding opening brace, else return False
-check if stack is empty, if not return False
"""

def is_valid_parenthesis(s):
    if len(s) %2 == 1:
        return False
    stack = []
    pairs = {")":"(" , "}":"{", "[":"]"}

    for char in s:
        if char in set('(' , '{' , '['):
            stack.append(char)
        elif char in set(')', '}', ']'):
            if not stack:
                return False
            top = stack.pop()
            if top !=pairs[char]:
                return False
    return len(stack) == 0



print(is_valid_parenthesis("]"))
