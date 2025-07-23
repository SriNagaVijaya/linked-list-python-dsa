class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None

    def insert_at_end(self, data):
        new_node = CNode(data)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail
            return
        new_node.next = self.tail.next
        self.tail.next = new_node
        self.tail = new_node

    def display(self):
        if not self.tail:
            print("List is empty.")
            return
        cur = self.tail.next
        while True:
            print(cur.data, end=" -> ")
            cur = cur.next
            if cur == self.tail.next:
                break
        print("(Back to head)")
