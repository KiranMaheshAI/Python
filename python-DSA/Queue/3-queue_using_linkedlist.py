class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLinkedList:
    def __init__(self):
        self.__head = None
        self.__rear = None
        self.__count = 0

    def enqueue(self, data): # O(1) time complexity
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
            self.__rear = newNode
        else:
            self.__rear.next = newNode
            self.__rear = newNode
        self.__count += 1
        print(f"Enqueued {data} to the queue")

    def dequeue(self): # O(1) time complexity
        if self.__head is None:
            print("Queue is empty")
            return None
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        print(f"Dequeued {data} from the queue")
        return data

    def length(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def front(self):
        if self.__head is None:
            print("Queue is empty")
            return None
        return self.__head.data

    def rear(self):
        if self.__rear is None:
            print("Queue is empty")
            return None
        return self.__rear.data

    def print(self):
        current = self.__head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def clear(self):
        self.__head = None
        self.__rear = None
        self.__count = 0

if __name__ == "__main__":
    queue = QueueUsingLinkedList()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print()