class Solution:
    def numTrees(self, n: int) -> int:
        # Array to store the number of unique BSTs for each number of nodes
        dp = [0] * (n + 1)
        # Base cases
        dp[0] = 1  # There is exactly one BST for zero nodes (empty tree)
        dp[1] = 1  # There is exactly one BST for one node
        
        # Fill dp array
        for i in range(2, n + 1):
            dp[i] = 0
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        
        return dp[n]
