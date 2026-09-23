# Write a function that takes a list of words and returns a dictionary where the keys are the words and the values are the number of times each word appears in the list.
# Example Input: words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# Example Output: {'apple': 3, 'banana': 2, 'orange': 1}

"""
UNDESTAND:
Input: list of words (strings) pss w/ repeats
Output: dict
Edge Cases: empty list ---> empty dict


PLAN:
-edge cases
-start w/ emopty dict
-loop through each word
-if words exists in a dict, increment counter
-else, add that to dict with the counter 1
-return dict
"""

def word_counter(words):
    if len(words) == 0:
        return {}
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            