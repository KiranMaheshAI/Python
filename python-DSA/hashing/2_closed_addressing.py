# Closed Addressing is a process of hashing where we have each position  of bucket array as head of linkedlist.
# In this we will use linkedlist to store the data.


class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        newNode = LLNode(key, value)
        newNode.next = self.head
        self.head = newNode
        
    def search(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def delete(self, key):
        current = self.head
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def print(self):
        current = self.head
        while current is not None:
            print(current.key, current.value, end=" ")
            current = current.next
        print()
    

class HashMapsUsingChaining:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [LinkedList() for _ in range(capacity)]
        self.size = 0

    def hash_function(self, key):
        return abs(hash(key))%self.capacity
    
    def insert(self, key, value):
        bucket_index = self.hash_function(key)
        bucket = self.buckets[bucket_index]
        node = bucket.search(key)
        if node is None:
            bucket.insert(key, value)
            self.size += 1
        else:
            node.value = value # Update existing value
    
    def get(self, key):
        bucket_index = self.hash_function(key)
        bucket = self.buckets[bucket_index]
        node = bucket.search(key)
        if node is None:
            return None
        else:
            return node.value
    
    def delete(self, key):
        bucket_index = self.hash_function(key)
        bucket = self.buckets[bucket_index]
        removed = bucket.delete(key)
        if removed:
            self.size -= 1
            return f"Deleted {key} from the hashmap"
        else:
            return f"Key {key} not found in the hashmap"

    def print(self):
        for i in range(self.capacity):
            print(f"Bucket {i}: ", end="")
            self.buckets[i].print()
    
    def __setitem__(self, key, value):
        return self.insert(key, value)
    def __getitem__(self, key):
        return self.get(key)
    def __delitem__(self, key):
        return self.delete(key)
    def __len__(self):
        return self.size
    def __contains__(self, key):
        return self.get(key) is not None
    def __iter__(self):
        return iter(self.buckets)

hashmaps = HashMapsUsingChaining(5)
hashmaps.insert(10, 15)
hashmaps.insert(11, 16)
hashmaps.insert(12, 17)
hashmaps.insert(13, 18)
hashmaps.insert(14, 19)

print(hashmaps[10])
print(hashmaps[11])
print(hashmaps[12])
print(hashmaps[13])
print(hashmaps[14])