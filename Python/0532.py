from typing import List
from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        # Count the frequency of each number in nums
        count = Counter(nums)
        result = 0
        
        if k == 0:
            # For k = 0, we need to count how many numbers appear more than once
            for num in count:
                if count[num] > 1:
                    result += 1
        else:
            # For k > 0, we need to find pairs (num, num + k)
            for num in count:
                if num + k in count:
                    result += 1
        
        return result
