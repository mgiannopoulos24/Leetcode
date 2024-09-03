from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize the DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            # Count zeros and ones in the current string
            zeros = s.count('0')
            ones = s.count('1')
            
            # Update the DP table in reverse to avoid recomputation issues
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
        # The answer is the maximum number of strings that fit in m zeros and n ones
        return dp[m][n]
