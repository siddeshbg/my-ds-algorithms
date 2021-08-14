"""
Reference:
 Concepts: https://www.techiedelight.com/introduction-linked-lists/
 Impl: https://www.techiedelight.com/linked-list-implementation-python/
"""


# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        # Set data
        self.data = data
        # set the next field to point to a given node of the list
        self.next = next


# Function to print a given linked list
def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print("None")


# Function to construct a linked list from a given set of keys
def construct(keys):
    head = None
    # start from the end of the list
    for i in reversed(range(len(keys))):
        # allocate a new node in a heap and set its data
        head = Node(keys[i], head)
    return head


if __name__ == '__main__':
    # input keys
    keys = [1, 2, 3, 4]

    # points to the head node of the linked list
    head = construct(keys)

    # print linked list
    printList(head)

