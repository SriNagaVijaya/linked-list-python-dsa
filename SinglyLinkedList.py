class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur:
            prev.next = cur.next

    def search(self, key):
        cur = self.head
        while cur:
            if cur.data == key:
                return True
            cur = cur.next
        return False

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")
