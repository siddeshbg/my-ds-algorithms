
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end="->")
        ptr = ptr.next
    print("None")

def construct():
    return Node(1, Node(2, Node(3, Node(4))))


if __name__ == '__main__':
    head = construct()
    printList(head)
