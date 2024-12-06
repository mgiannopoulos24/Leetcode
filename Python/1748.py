from typing import List
from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # Step 1: Count the frequency of each element in nums
        freq = Counter(nums)
        
        # Step 2: Sum elements that have a frequency of exactly 1
        return sum(num for num, count in freq.items() if count == 1)
