class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        node = QueueNode(data)
        if not self.rear:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if not self.front:
            raise IndexError("Queue underflow")
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return data

    def peek(self):
        if not self.front:
            raise IndexError("Queue is empty")
        return self.front.data

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        while current:
            print(f"{current.data} -> ", end='')
            current = current.next
        print("None")
