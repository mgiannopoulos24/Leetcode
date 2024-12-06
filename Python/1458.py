from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # Initialize DP table with -inf
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        # Iterate from the end towards the beginning
        for i in range(m -1, -1, -1):
            for j in range(n -1, -1, -1):
                # Calculate the dot product if we pair nums1[i] and nums2[j]
                current = nums1[i] * nums2[j]
                
                # Option 1: Pair these two and add the best from dp[i+1][j+1]
                pair = current
                if dp[i+1][j+1] != float('-inf'):
                    pair += dp[i+1][j+1]
                
                # Option 2: Skip nums1[i]
                skip1 = dp[i+1][j]
                
                # Option 3: Skip nums2[j]
                skip2 = dp[i][j+1]
                
                # Take the maximum of pairing or skipping
                dp[i][j] = max(pair, skip1, skip2, current)
        
        return dp[0][0]
