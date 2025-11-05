"""
Stack with arrays:

A stack is a linear data structure that follows the Last In First Out (LIFO) principle.
It is a collection of elements that are inserted and removed from the same end, called the top.
The stack is a fundamental data structure in computer science and is used in many algorithms and applications.

The stack is a linear data structure that follows the Last In First Out (LIFO) principle.
It is a collection of elements that are inserted and removed from the same end, called the top.
The stack is a fundamental data structure in computer science and is used in many algorithms and applications.

"""

class StackUsingArrays:
    def __init__(self):
        self.__stack = []  # Very important to use __stack instead of stack to make it private

    def push(self, data): # O(1) time complexity
        self.__stack.append(data)
        print(f"Pushed {data} to the stack")
    
    def length(self):
        return len(self.__stack)

    def isEmpty(self):
        return len(self.__stack) == 0

    def top(self): 
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.__stack[-1]

    def pop(self): # O(1) time complexity
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.__stack.pop()

    def print(self):
        print(self.__stack)

    def clear(self):
        self.stack = []

if __name__ == "__main__":
    stack = StackUsingArrays()
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