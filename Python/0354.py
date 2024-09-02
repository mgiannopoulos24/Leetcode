from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Step 1: Sort the envelopes
        # Sort by width in ascending order, and by height in descending order if widths are the same
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Step 2: Extract the heights and apply LIS on heights
        heights = [h for _, h in envelopes]
        
        # Step 3: Find the length of the longest increasing subsequence
        dp = []
        for height in heights:
            # Find the position to replace or extend in dp using binary search
            pos = bisect.bisect_left(dp, height)
            if pos == len(dp):
                dp.append(height)
            else:
                dp[pos] = height
        
        # The length of dp array gives the maximum number of envelopes that can be nested
        return len(dp)
