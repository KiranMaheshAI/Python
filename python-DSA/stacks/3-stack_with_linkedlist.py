"""
Stack with linkedlist:

A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
It is a collection of elements that are inserted and removed from the same end, called the top.
The stack is a fundamental data structure in computer science and is used in many algorithms and applications.

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLinkedList:
    def __init__(self):
        self.__stack = None
        self.__count = 0

    def push(self, data): # O(1) time complexity 
        newNode = Node(data)
        newNode.next = self.__stack
        self.__stack = newNode
        self.__count += 1
        print(f"Pushed {data} to the stack")

    def length(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.__stack.data

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        data = self.__stack.data
        self.__stack = self.__stack.next
        self.__count -= 1
        return data
        
    def print(self):
        current = self.__stack
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def clear(self):
        self.__stack = None
        self.__count = 0

if __name__ == "__main__":
    stack = StackUsingLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print()
    stack.pop()
    stack.print()
    stack.top()
    stack.print()
    stack.clear()
    stack.print()