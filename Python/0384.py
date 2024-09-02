import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        # Save the original array
        self.original = nums[:]
        # Save a copy of the array for shuffling
        self.array = nums[:]
        
    def reset(self) -> List[int]:
        # Return the original array
        return self.original

    def shuffle(self) -> List[int]:
        # Return a shuffled version of the array
        array = self.array[:]
        n = len(array)
        for i in range(n - 1, 0, -1):
            # Pick a random index from 0 to i
            j = random.randint(0, i)
            # Swap array[i] with array[j]
            array[i], array[j] = array[j], array[i]
        return array
