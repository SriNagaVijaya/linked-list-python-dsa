class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = StackNode(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            raise IndexError("Stack underflow")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if not self.top:
            raise IndexError("Stack is empty")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        while current:
            print(f"| {current.data} |")
            current = current.next
        print("-----")
