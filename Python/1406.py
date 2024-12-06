class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0  # If there are no stones left, the score is 0
        
        # Loop backwards through the stoneValue array
        for i in range(n - 1, -1, -1):
            total = 0
            # Check the maximum score Alice can get by taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    total += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], total - dp[i + k])
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"