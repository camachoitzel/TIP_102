"""
Given a string, return true if it can be a palindrome after deleting at most one character.

UNDERSTAND:
Input - str

Output - boolean

Edge Case - diff caps


PLAN:
-initialize left ptr to 0
- initialize right to len - 1
- initialize counter for deletes to 0
-while left ptr != right ptrt and del counter < 2
- check that char @ left = char @ right
- return False, True

"""

def palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

    if del_count == 2:
        return False
    else:
        return True
