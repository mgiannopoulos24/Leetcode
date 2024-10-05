from typing import List
from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Create a counter to count occurrences of each element
        count = Counter(nums)
        
        # Iterate through the counter to find the element with exactly n occurrences
        n = len(nums) // 2
        for key, value in count.items():
            if value == n:
                return key
