class QueueUsingList:
    def __init__(self):
        self.__queue = []
        self.__count = 0

    def enqueue(self, data): # O(1) time complexity
        self.__queue.append(data)
        self.__count += 1
        print(f"Enqueued {data} to the queue")

    def dequeue(self): # O(1) time complexity
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.__queue.pop(0)
        self.__count -= 1
        print(f"Dequeued {data} from the queue")

    def length(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0
        
    def front(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.__queue[0]

    def print(self):
        print(self.__queue)

    def clear(self):
        self.__queue = []
        self.__count = 0
    def rear(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.__queue[-1]

if __name__ == "__main__":
    queue = QueueUsingList()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print()
    queue.dequeue()
    queue.print()
    queue.front()
    queue.print()
    queue.clear()
    queue.print()