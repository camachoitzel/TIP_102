"""
You get 2 linked list and you have to return the combo if both sorted as 1 list and return the head of that list
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head

def print_list(head):
    current = head
    while current:
        print(current.val, end=" → ")
        current = current.next
    print("None")

# TODO: implement this function
def merge_two_lists(l1, l2):
    results = []

    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            results.append(l1.val)
            l1 = l1.next
        else:
            results.append(l2.val)
            l2 = l2.next

    # Add remaining values from whichever list is not exhausted
    while l1 is not None:
        results.append(l1.val)
        l1 = l1.next

    while l2 is not None:
        results.append(l2.val)
        l2 = l2.next

    return build_list(results)

        


    

l1 = build_list([1, 2, 4])
l2 = build_list([1, 3, 4])
print_list(merge_two_lists(l1, l2))