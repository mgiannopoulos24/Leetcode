from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # Initialize the DP table
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single element subarrays
        for i in range(n):
            dp[i][i] = nums[i]
        
        # Fill the DP table
        for length in range(2, n + 1):  # length of subarray
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        # Player 1 can guarantee a win if dp[0][n-1] >= 0
        return dp[0][n - 1] >= 0
