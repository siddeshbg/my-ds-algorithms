"""
Reference: https://www.techiedelight.com/linked-list-implementation-python/
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Function to print a given linked list
def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end="->")
        ptr = ptr.next
    print("None")

# Naive function for linked list implementation containing three nodes
def construct():
    # construct individual linked list nodes
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    # rearrange the references to construct a list
    head = first
    first.next = second
    second.next = third
    third.next = fourth

    return head


if __name__ == '__main__':
    # `head` points to the head node of the linked list
    head = construct()

    # print linked list
    printList(head)

