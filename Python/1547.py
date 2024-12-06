class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Step 1: Sort the cuts array
        cuts.sort()
        
        # Step 2: Add the boundaries (0 and n) to the cuts array
        cuts = [0] + cuts + [n]
        
        # Step 3: Initialize the DP table
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]
        
        # Step 4: Fill the DP table
        # We will iterate over the length of the segment
        for length in range(2, m):  # length = j - i
            for i in range(m - length):  # i is the start index
                j = i + length  # j is the end index
                dp[i][j] = float('inf')
                
                # Try each possible cut between i and j
                for k in range(i + 1, j):
                    cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], cost)
        
        # Step 5: The answer is in dp[0][m-1], which covers the full stick
        return dp[0][m - 1]
