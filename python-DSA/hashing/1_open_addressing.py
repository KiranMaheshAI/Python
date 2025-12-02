# Hash Map Implementations using Open Addressing
# Open Addressing is a kind of hashing where if the value is present in the index, we check whether next index is empty, if it is not we check next.

class Hashmaps:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [None] * capacity
        self.values = [None] * capacity
        self.size = 0
        
    def hash_function(self, key):
        return abs(hash(key))%self.capacity
    
    def rehash(self, hash_value):
        # Linear Probing: where we will check if the value is available, if not add 1 to the hash value 
        # This will avoid collision
        return (hash_value+1)%self.capacity
        
    def insert(self, key, value):
        if self.size == self.capacity:
            print("Slots are booked")
            return
        hash_value = self.hash_function(key)
        if self.slots[hash_value] in [None, key]:
            self.slots[hash_value] = key
            self.values[hash_value] = value
        else:
            updated_hash_value = hash_value
            while self.slots[updated_hash_value] != None and self.slots[updated_hash_value] != key:
                updated_hash_value = self.rehash(updated_hash_value)
            if self.slots[updated_hash_value] == None:
                self.slots[updated_hash_value] = key
                self.values[updated_hash_value] = value
            else:
                self.values[updated_hash_value] = value
        self.size += 1
        
    def get(self, key):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] == key:
            return self.values[hash_value]
        updated_hash_value = hash_value 
        count = 1
        while(self.slots[updated_hash_value] != key and count != self.capacity):
            updated_hash_value = self.rehash(updated_hash_value)
            count += 1
        if self.slots[updated_hash_value] == key:
            return self.values[hash_value]
        return None
        
    def print(self):
        for i in range(self.capacity):
            print(f"{self.slots[i]} : {self.values[i]}")
            
    def delete(self, key):
        initial_index = self.hash_function(key)
        current_position = initial_index
        count = 1
        while(self.slots[current_position] != key and count != self.capacity):
            current_position = self.rehash(current_position)
        if self.slots[current_position] == key:
            self.slots[current_position] = None
            self.values[current_position] = None
            self.size -= 1
        return

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
        return iter(self.slots)
            
hashmaps = Hashmaps(5)
hashmaps.insert(10, 15)
hashmaps.insert(11, 16)
hashmaps.insert(12, 17)
hashmaps.insert(13, 18)
hashmaps.insert(14, 19)

# calling magic methods
hashmaps[15] = 20
hashmaps[16] = 21
hashmaps[17] = 22
hashmaps[18] = 23
hashmaps[19] = 24

print(hashmaps[15])
print(hashmaps[16])
print(hashmaps[17])
print(hashmaps[18])
print(hashmaps[19])

print(hashmaps.get(14))
print(hashmaps.get(20))
hashmaps.delete(14)


hashmaps.print()

