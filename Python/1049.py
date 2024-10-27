class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        
        # dp[i] will represent if we can achieve sum `i` using the stones
        dp = [False] * (target + 1)
        dp[0] = True  # We can always make sum 0 by choosing no stones
        
        # Process each stone
        for stone in stones:
            # Update dp array backwards to prevent overwriting in the same iteration
            for i in range(target, stone - 1, -1):
                dp[i] = dp[i] or dp[i - stone]
        
        # Find the largest sum that can be achieved that's <= target
        for i in range(target, -1, -1):
            if dp[i]:
                return total_sum - 2 * i  # This is the smallest possible last stone weight
