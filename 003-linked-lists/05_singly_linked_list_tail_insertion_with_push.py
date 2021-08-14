"""
Reference: https://www.techiedelight.com/linked-list-implementation-part-2/

The following version relies on push() to build the new node.
"""

class Node:
    next = None

    # Constructor
    def __init__(self, data=None):
        self.data = data


# Function to print a given linked list
def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" —> ")
        ptr = ptr.next
    print("None")


def push(head, data):
    # allocate a new node in a heap and set its data
    newNode = Node(data)

    # set the next field of the node to point to the current
    # first node of the list.
    newNode.next = head

    # return the head to point to the node, so it is
    # now the first node in the list.
    return newNode


def appendNode(head, key):
    current = head
    # special case for the empty list
    if current is None:
        head = push(head, key)
    else:
        # locate the last node
        while current.next:
            current = current.next
        current.next = push(current.next, key)
    return head


if __name__ == '__main__':
    # input keys
    keys = [1, 2, 3, 4]

    # points to the head node of the linked list
    head = None
    for key in keys:
        head = appendNode(head, key)

    printList(head)
