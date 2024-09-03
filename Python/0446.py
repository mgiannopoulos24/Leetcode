from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # dp will store the count of subsequences ending at index `i` with a specific difference
        dp = [defaultdict(int) for _ in range(n)]
        total_count = 0
        
        # Iterate over all pairs (i, j) with i < j
        for j in range(1, n):
            for i in range(j):
                diff = nums[j] - nums[i]
                if diff in dp[i]:
                    # There are dp[i][diff] subsequences ending at i with difference `diff`
                    dp[j][diff] += dp[i][diff]
                    # Adding all these subsequences to the total count
                    total_count += dp[i][diff]
                # Always include the pair (nums[i], nums[j]) as a new subsequence if it forms an arithmetic sequence
                dp[j][diff] += 1
        
        return total_count
