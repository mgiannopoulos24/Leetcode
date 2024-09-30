from collections import defaultdict

class FreqStack:

    def __init__(self):
        # Initialize frequency map and group map
        self.freq_map = defaultdict(int)
        self.group_map = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Increment the frequency of the element
        self.freq_map[val] += 1
        freq = self.freq_map[val]
        
        # Update the max frequency
        if freq > self.max_freq:
            self.max_freq = freq
        
        # Add the element to the stack for the current frequency
        self.group_map[freq].append(val)

    def pop(self) -> int:
        # Pop the most frequent element
        val = self.group_map[self.max_freq].pop()
        
        # Decrement the frequency of the element
        self.freq_map[val] -= 1
        
        # If no elements have the current max frequency, decrement max_freq
        if not self.group_map[self.max_freq]:
            del self.group_map[self.max_freq]
            self.max_freq -= 1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()