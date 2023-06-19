"""
    You are given a singly linked list having head node A. You have to reverse the linked list and return the head node of that reversed list.

    NOTE: You have to do it in-place and in one-pass.
"""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        new_node = Node(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print_list(self):
        current = self.head
        if current is None:
            print(current)
        while current:
            print(current.data, end=" ")
            current = current.next


def reverse_linked_list(ll):
    if ll.head is None or ll.head.next is None:
        return ll
    current = ll.head
    prev = None
    while current is not None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    ll.head = prev


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)
reverse_linked_list(linked_list)
linked_list.print_list()
