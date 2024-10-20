class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        
        # Check if it's possible to merge into one pile
        if (n - 1) % (k - 1) != 0:
            return -1
        
        # Prefix sum to quickly calculate sum of subarrays
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
        # dp[i][j] will store the minimum cost to merge stones[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Length of the range we're considering
        for length in range(k, n + 1):  # length varies from k to n
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                
                # Try all possible partitions into smaller ranges
                for m in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
                
                # If we can merge this entire range into one pile
                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix_sum[j + 1] - prefix_sum[i]
        
        return dp[0][n - 1]
