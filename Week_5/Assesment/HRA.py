"""
Write a function create_linked_list(values) that creates a linked list from a list of numbers, nums and returns the head of the linked list

"""

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add(self, val):
#         new_node = Node(val)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next

# def create_linked_list(values):
#     if not values:
#         return None

#     head = Node(values[0])
#     curr = head

#     for i in range(a, len(values)):
#         curr.next = Node(values[i])
#         curr = curr.next

#     return head


"""

You are given a class ListNode representing a node ina singly liked list, and a function print_linked_list to print the linked list

Your task is to implememt the function insert that inserts a new node with a given value at a specified pos in the linked list

Ex
Input:
LL = 1->2->4
Insert val = 3
Pos: 2

Output:
1->2->3->4->None
"""

def insert(head, value, postion):

    new_node = Node(value)

    if position == 0:
        new_node.next = head
        return new_node

    curr = head
    count = 0

    while curr.next():
        curr = curr.next()


"""
You are given the haeds of 2 singly lionked lists head_a and head_b. Your task is to determine which list contains more prime nums. 
The function should return the head of the list that has a greater count of prime numbers. If both lists have the same num of prime nums return head_a

Constraints:
the list contains at least one node and at mose 10^3 nodes
node cals are in the range [-10^5, 10^5]
the is_prime function is provided can can be used to determine if a num is prime
"""

import math
import os
import random
import re
import sys
import ast

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

# Helper function to create a linked list from a list of values
def create_linked_list(vals):
    temp = SinglyLinkedListNode(0)  # Dummy node
    current = temp
    for val in vals:
        current.next = SinglyLinkedListNode(val)
        current = current.next
    return temp.next

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Complete the 'most_primes_list' function below.
#
# The function is expected to return a SinglyLinkedListNode.
# The function accepts two SinglyLinkedListNode parameters: head_a and head_b.
#
def most_primes_list(head_a, head_b):
    count_a = 0
    current = head_a

    while current is not None:
        if is_prime(current.data):
            count_a += 1
        current = current.next

    count_b = 0
    current = head_b

    while current is not None:
        if is_prime(current.data):
            count_b += 1
        current = current.next

    if count_b > count_a:
        return head_b
    return head_a







