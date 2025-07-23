class CDNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = CDNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node.prev = new_node
            return
        tail = self.head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        cur = self.head
        while True:
            print(cur.data, end=" <-> ")
            cur = cur.next
            if cur == self.head:
                break
        print("(Back to head)")
