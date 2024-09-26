import random
from typing import List

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.blacklist = set(blacklist)
        self.size = n - len(self.blacklist)
        
        # Create a map for blacklisted numbers to valid numbers
        self.mapping = {}
        # Convert blacklist to sorted list for easy handling
        blacklist = sorted(blacklist)
        # The position we are mapping blacklisted numbers to
        valid_number = n - len(self.blacklist)
        
        for b in blacklist:
            if b < self.size:
                # Find a valid number for this blacklisted number
                while valid_number in self.blacklist:
                    valid_number += 1
                self.mapping[b] = valid_number
                valid_number += 1

    def pick(self) -> int:
        # Pick a random index from the valid range
        idx = random.randint(0, self.size - 1)
        # If the index is in the mapping, return the mapped value
        return self.mapping.get(idx, idx)



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()