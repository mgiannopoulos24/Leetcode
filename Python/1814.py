from typing import List
from collections import defaultdict

class Solution:
    MOD = 10**9 + 7

    def rev(self, x: int) -> int:
        return int(str(x)[::-1])

    def countNicePairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        result = 0
        
        for num in nums:
            diff = num - self.rev(num)
            # Count pairs based on the same `diff` value
            result = (result + count[diff]) % self.MOD
            count[diff] += 1
        
        return result
