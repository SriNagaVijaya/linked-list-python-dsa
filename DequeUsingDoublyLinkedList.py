class DequeNode:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class LinkedListDeque:
    def __init__(self):
        self.front = self.rear = None

    def add_front(self, data):
        node = DequeNode(data)
        if not self.front:
            self.front = self.rear = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node

    def add_rear(self, data):
        node = DequeNode(data)
        if not self.rear:
            self.front = self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node

    def remove_front(self):
        if not self.front:
            raise IndexError("Deque underflow")
        data = self.front.data
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        return data

    def remove_rear(self):
        if not self.rear:
            raise IndexError("Deque underflow")
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear:
            self.rear.next = None
        else:
            self.front = None
        return data

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        while current:
            print(f"<- {current.data} ->", end=' ')
            current = current.next
        print()
