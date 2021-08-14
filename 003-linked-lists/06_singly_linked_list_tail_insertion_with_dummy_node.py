"""
Reference: https://www.techiedelight.com/linked-list-implementation-part-2/

The idea is to use a temporary dummy node at the head of the list during
computation. The trick is that every node appears to be added after the .next
field of a node with the dummy. The tail pointer plays the same role as in the
previous example. It also now handles the first node.
"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Function to print a given linked list
def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end="->")
        ptr = ptr.next
    print("None")


# Takes a list and a data value, creates a new link with the given data
# and pushes it onto the list's front.
def push(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode


# Function to implement a linked list from a given set of keys
# using a dummy node
def constructList(keys):
    dummy = Node()  # dummy node is temporarily the first node
    tail = dummy

    # Build the list on `dummy.next` (aka `tail.next`)
    for key in keys:
        tail.next = push(tail.next, key)
        tail = tail.next

    # The real result list is now in `dummy.next`
    # dummy.next == key[0], key[1], key[2], key[3]
    return dummy.next

if __name__ == '__main__':
    keys = [1, 2, 3, 4]
    # points to the head node of the linked list
    head = constructList(keys)
    printList(head)
