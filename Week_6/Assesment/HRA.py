"""
Given a list of ints write a function create_linked_list(values) that creates a singly linked list 
where each node contains one of the integers from the list in the same order.
The function should return the head of the linked list. If values is empty, return None

Constraints:
the list of integers will not exceed 100 elements


Understand:
Input: list of int
Output: linked list of ints in same order
Edge cases: empty list, list w/ 1 element, list over 1000 ints

Plan:
check for empty list
    return None
check for list of < 2
    return values[0]
check if len(values) > 1000:
    return error stating max size of list has been exceeded

create empty linked list



for i in range(len(values)):
    temp = values[i]
    curr = temp
    curr = curr.next


return print_linked_list(new linked list head)
     

"""
import math
import os
import random
import re
import sys
import ast

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insert_node(self, val):
#         node = ListNode(val)

#         if not self.head:
#             self.head = node
#         else:
#             self.tail.next = node

#         self.tail = node

def print_linked_list(head):
    current = head
    while current:
        if current.next:
            sys.stdout.write(str(current.val) + " -> ")
        else:
            sys.stdout.write(str(current.val) + "\n")
        current = current.next


# def create_linked_list(values):
#     if not values:
#         return None

#     head = ListNode(values[0])
#     current = head

#     for i in range(1, len(values)):
#         current.next = ListNode(values[i])
#         current = current.next

#     return head

# values = [1,2,3,4]
# print_linked_list(create_linked_list(values))

# output 1-> 2 -> 3 -> 4


"""
You are given the head of a sorted singly linked list and a value. Create a nee Node w/value 'value' and insert it into
the provided linked list while maintaining the sorted order of the nodes.


Example 1:
Input: head = 1 -> 3 -> 5, value = 4  
Output: 1 -> 3 -> 4 -> 5

Example 2:
Input: head = 2 -> 6 -> 8, value = 1  
Output: 1 -> 2 -> 6 -> 8

Understand:
Input: head of linked list and a int val
Output: linked list with inserted value no return statement needed
Edge cases: empty linked list

Plan:
new_node = ListNode(value)
If list is empty:
    return new_node

curr = head
prev = none

while curr:
    if curr.val < value:
        new_node.next = head
        return new_node
    elif curr.val > value:
        
"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# def insert_sorted(head, value):
#     new_node = ListNode(value)

#     if head is None:
#         return new_node

    
#     curr = head
#     prev = None

#     while curr is not None and curr.val < value:

#         prev = curr
#         curr = curr.next

#     if prev is None:
#         new_node.next = head
#         return new_node
        
    

#     prev.next = new_node
#     new_node.next = curr

#     return head



# head = ListNode(1) 
# head.next = ListNode(3)
# head.next.next = ListNode(5) 

# value = 4

# new_list = insert_sorted(head, value)

# print_linked_list(new_list)

"""
Implemet a function longer_list() that accepts the heads of 2 singly linked lists head_a and head_b. 
Return the head of the linked list w/ the greatest length. if both list have the same length return head_a

Plan:
Set current to head_a.
Count the nodes in list A.
Set current to head_b.
Count the nodes in list B.
If length_b > length_a, return head_b.
Otherwise return head_a.

"""

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, val):
        node = ListNode(val)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    while current:
        if current.next:
            sys.stdout.write(str(current.val) + " -> ")
        else:
            sys.stdout.write(str(current.val) + "\n")
        current = current.next
    
# Helper function to create a linked list from a list of values
def create_linked_list(vals):
    temp = ListNode()
    current = temp
    for val in vals:
        current.next = ListNode(val)
        current = current.next
    return temp.next

def longer_list(head_a, head_b):
    len_a = 0
    current = head_a

    while current is not None:
        len_a += 1
        current = current.next

    len_b = 0
    current = head_b

    while current is not None:
        len_b += 1
        current = current.next

    if len_b > len_a:
        return head_b

    return head_a


def mys_function(head):
    if not head or head.next:
        return head
    prev = None

    tail = head

    while tail.next:
        prev = tail
        tail = tail.next

    if not prev:
        return head

    tail.next = head.next
    prev.next = head
    head = None



def remove_duplicates(head: ListNode) -> ListNode:
    if not head:
        return None  
    
    current = head
    while current: 
        if current.val == current.next.val:  
            current.next = current.next.next  
        current = current.next  
    
    return head

