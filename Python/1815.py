from typing import List
from functools import lru_cache
from collections import Counter

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        # Count groups by remainder
        remainder_counts = Counter()
        initial_happy = 0
        for g in groups:
            r = g % batchSize
            if r == 0:
                initial_happy +=1
            else:
                remainder_counts[r] +=1
        
        # Prepare counts list from 1 to batchSize-1
        counts = [0] * (batchSize)
        for r in remainder_counts:
            counts[r] = remainder_counts[r]
        
        counts = tuple(counts)
        
        @lru_cache(None)
        def dp(freq, r):
            ans = 0
            for i in range(1, batchSize):
                if freq[i] >0:
                    # Choose group with remainder i
                    new_freq = list(freq)
                    new_freq[i] -=1
                    new_freq = tuple(new_freq)
                    new_r = (r + i) % batchSize
                    # If current remainder is 0, this group starts fresh
                    if r ==0:
                        temp = 1 + dp(new_freq, new_r)
                    else:
                        temp = dp(new_freq, new_r)
                    if temp > ans:
                        ans = temp
            return ans
        
        additional_happy = dp(counts, 0)
        return initial_happy + additional_happy
