#!/usr/bin/env python3
from Stack import Stack


def rev_string(my_str):
    stack = Stack()
    for s in my_str:
        stack.add(s)

    reversed_str = []
    while not stack.is_empty():
        reversed_str.append(stack.remove())

    return ''.join(reversed_str)


if __name__ == '__main__':
    print(rev_string("stop"))
    print(rev_string("heavy rain tonight"))
    print(rev_string(""))
