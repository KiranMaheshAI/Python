class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def update(self, data, newData):
        current = self.head
        while current is not None:
            if current.data == data:
                current.data = newData
                return True
            current = current.next
        return False

    def reverse(self):
        current = self.head
        previous = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def reverseRecursively(self):   
        if self.head is None:
            return
        self.reverseRecursively(self.head.next)
        self.head.next.next = self.head
        self.head.next = None
        self.head = self.head.next
