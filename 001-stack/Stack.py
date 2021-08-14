#!/usr/bin/env python3


class Stack:
    def __init__(self):
        self._list = []

    def add(self, item):
        self._list.append(item)

    def remove(self):
        return self._list.pop()

    def show(self):
        print(self._list)

    def is_empty(self):
        if not self._list:
            return True
        else:
            return False

    def peek(self):
        """Get the top item, without removing it."""
        return self._list[-1]

    def size(self):
        return len(self._list)


def main():
    stack = Stack()
    print(stack.is_empty())
    stack.add(5)
    stack.add('little')
    stack.add('monkeys')
    stack.add('dancing')
    stack.show()
    print(stack.peek())
    stack.remove()
    stack.show()
    stack.add('jumping')
    stack.add('on')
    stack.add('bed')
    stack.show()
    stack.remove()
    stack.show()
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size())


if __name__ == '__main__':
    main()
