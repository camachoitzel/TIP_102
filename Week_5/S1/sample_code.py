class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next

# ll = LinkedList()
# for value in [1,2,3,4,5]:
#     ll.add(value)


"""
Write a function to find the middle node of a sigly liked list. If the list has an even number of nodes, return the second middle node

Examples:
Input: head - [1,2,3,4,5]


UNDESTAND:
Input: head of linked list
Output: middle node(if even # of nodes, then return 2nd middle)
Edge Cases: empty --> None, single --> that item, [3,4] ->return second node

Match:
- slow and fast pointer technique

Plan:
-edge cases
-start slow and fast at the head
-move slow 1 step, fast 2 steps
-when fast reaches end, slow will be the middle
"""

def find_middle(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow= slow.next
        fast = fast.next.next

    return slow

ll1 = LinkedList()

for value in [1,2,3,4,5]:
    ll1.add(value)

print(find_middle(ll1.head).val)


# Check for a cycle
def find_middle(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow= slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        

    return False