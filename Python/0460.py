from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_value = {}
        self.key_to_freq = defaultdict(int)
        self.freq_to_keys = defaultdict(OrderedDict)  # Frequency -> OrderedDict of keys
        
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1
        
        # Update frequency
        freq = self.key_to_freq[key]
        self.key_to_freq[key] += 1
        new_freq = freq + 1
        
        # Remove key from old frequency list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        
        # Add key to new frequency list
        self.freq_to_keys[new_freq][key] = None
        self.min_freq = min(self.min_freq, new_freq)
        
        return self.key_to_value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_value:
            # Update the value and frequency
            self.key_to_value[key] = value
            self.get(key)  # This will update the frequency of the key
        else:
            if len(self.key_to_value) >= self.capacity:
                # Remove the least frequently used key
                lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_value[lfu_key]
                del self.key_to_freq[lfu_key]
                if not self.freq_to_keys[self.min_freq]:
                    del self.freq_to_keys[self.min_freq]
            
            # Insert the new key
            self.key_to_value[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1

