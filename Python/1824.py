from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        # Initialize DP array for 3 lanes
        dp = [1, 0, 1]  # dp[0] -> lane 1, dp[1] -> lane 2, dp[2] -> lane 3
        
        for i in range(1, n + 1):
            # First, set infinity for lanes with obstacles at position i
            for lane in range(3):
                if obstacles[i] == lane + 1:
                    dp[lane] = float('inf')
            
            # Update DP for lanes without obstacles at position i
            for lane in range(3):
                if obstacles[i] != lane + 1:
                    dp[lane] = min(dp[lane], 1 + min(dp[(lane + 1) % 3], dp[(lane + 2) % 3]))
        
        # The answer is the minimum of the three lanes at the last position
        return min(dp)
