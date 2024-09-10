class MyHashMap:
    def __init__(self):
        self.size = 1000  # Number of buckets
        self.buckets = [[] for _ in range(self.size)]  # Initialize the hash table with empty lists

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update the value
                return
        
        # Key does not exist, add a new key-value pair
        bucket.append((key, value))

    def get(self, key: int) -> int:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Search for the key in the bucket
        for k, v in bucket:
            if k == key:
                return v
        
        return -1  # Key not found

    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Search for the key in the bucket and remove it
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)  # Remove the key-value pair
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)