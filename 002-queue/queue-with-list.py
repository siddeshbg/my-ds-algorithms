"""
Reference: https://www.techiedelight.com/queue-implementation-python/
with little change to pop()
"""
class Queue:
    # Initialize queue
    def __init__(self, size):
        self.q = [None] * size
        self.capacity = size
        self.front = 0
        self.rear = -1
        self.count = 0

    # Function to add an element to the queue
    def append(self, item):
        # check for queue overflow
        if self.isFull():
            print("Overflow!! Terminating process.")
            exit(1)
        print("Inserting element ...", item)
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
        self.q[self.rear] = item

    def pop(self):
        if self.isEmpty():
            print("Queue Underflow!! Terminating process.")
            exit(1)

        print("Removing element", self.q[self.front])
        self.q[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1

    # Function to return the size of the queue
    def size(self):
        return self.count

    # Function to check if the queue is empty or not
    def isEmpty(self):
        return self.count == 0

    # Function to check if the queue is full or not
    def isFull(self):
        return self.size() == self.capacity

    # Function to return the front element of the queue
    def peek(self):
        if self.isEmpty():
            print("Queue UnderFlow!! Terminating process.")
            exit(1)
        return self.q[self.front]

    def display(self):
        print(self.q)


if __name__ == '__main__':
    q = Queue(5)
    q.append(1)
    q.append(2)
    q.append(3)
    q.display()

    print("The queue size is", q.size())
    print("The front elemement is", q.peek())
    q.pop()
    q.display()
    print("The front element is", q.peek())

    q.append(4)
    q.display()
    q.append(5)
    q.display()
    q.append(6)
    q.display()
    print("The front element is", q.peek())
    q.pop()
    q.pop()
    q.display()
    print("The front element is", q.peek())

