import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        # Compute the prefix sum array
        self.prefix_sum = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sum.append(current_sum)
        self.total_sum = current_sum  # Total sum of weights

    def pickIndex(self) -> int:
        # Generate a random number between 1 and total_sum
        target = random.randint(1, self.total_sum)
        
        # Binary search to find the right index
        low, high = 0, len(self.prefix_sum) - 1
        while low < high:
            mid = (low + high) // 2
            if self.prefix_sum[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()