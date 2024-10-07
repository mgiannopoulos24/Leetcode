from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        # Dictionary to store the history of each key
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the value along with its timestamp to the list for the key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If the key does not exist, return an empty string
        if key not in self.store:
            return ""
        
        # Retrieve the list of (timestamp, value) for the given key
        values = self.store[key]
        
        # Binary search to find the right position
        i = bisect.bisect_right(values, (timestamp, chr(127)))
        
        # If i is 0, it means there's no timestamp <= the given timestamp
        if i == 0:
            return ""
        else:
            return values[i-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)