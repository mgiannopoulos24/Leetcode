from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_num = max(nums)
        freq = [0] * (max_num + 1)
        
        # Step 1: Frequency counting
        for num in nums:
            freq[num] +=1
        
        count = 0
        
        # Step 2: Iterate through all possible GCDs
        for x in range(1, max_num +1):
            gcd_current = 0
            for y in range(x, max_num +1, x):
                if freq[y] >0:
                    normalized = y // x
                    gcd_current = gcd(gcd_current, normalized)
                    if gcd_current ==1:
                        break  # Early exit if GCD becomes 1
            if gcd_current ==1:
                count +=1
        
        return count
