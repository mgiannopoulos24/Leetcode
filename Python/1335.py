class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1  # More days than jobs, impossible to schedule
        
        # dp[i][k] represents the minimum difficulty of scheduling first i jobs in k days
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
        
        # Base case: dp[0][0] = 0 (no jobs and no days)
        dp[0][0] = 0
        
        # Fill DP table
        for k in range(1, d + 1):  # For each day
            for i in range(k, n + 1):  # For each job, considering at least k jobs
                max_difficulty = 0
                # We need to try different partitions
                for j in range(i - 1, k - 2, -1):  # Partition at position j
                    max_difficulty = max(max_difficulty, jobDifficulty[j])
                    dp[i][k] = min(dp[i][k], dp[j][k - 1] + max_difficulty)
        
        return dp[n][d] if dp[n][d] != float('inf') else -1
