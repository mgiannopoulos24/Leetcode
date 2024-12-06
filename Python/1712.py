from typing import List
from itertools import accumulate
from bisect import bisect_left, bisect_right

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Calculate the prefix sum
        prefix = list(accumulate(nums))
        
        count = 0
        for i in range(n - 2):
            left_sum = prefix[i]
            
            # Find the minimum j such that prefix[j] >= 2 * prefix[i]
            j = bisect_left(prefix, 2 * left_sum, i + 1, n - 1)
            
            # Find the maximum k such that prefix[k] <= (prefix[i] + prefix[-1]) / 2
            k = bisect_right(prefix, left_sum + (prefix[-1] - left_sum) // 2, i + 1, n - 1) - 1
            
            if j <= k:
                count = (count + (k - j + 1)) % MOD
        
        return count
