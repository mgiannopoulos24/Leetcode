from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        num_count = Counter(nums)
        sorted_nums = sorted(num_count.keys())
        
        for num in sorted_nums:
            if num_count[num] > 0:
                count = num_count[num]
                for i in range(num, num + k):
                    if num_count[i] < count:
                        return False
                    num_count[i] -= count
        
        return True
