class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        
        # dp[i][j] will hold the minimum cost of non-leaf nodes for the subarray arr[i..j]
        dp = [[float('inf')] * n for _ in range(n)]
        
        # max_in_subarray[i][j] will hold the maximum value in arr[i..j]
        max_in_subarray = [[0] * n for _ in range(n)]
        
        # Precompute the maximum value for every subarray arr[i..j]
        for i in range(n):
            max_in_subarray[i][i] = arr[i]
            for j in range(i + 1, n):
                max_in_subarray[i][j] = max(max_in_subarray[i][j - 1], arr[j])
        
        # Base case: dp[i][i] = 0 since a single leaf can't have any non-leaf nodes
        for i in range(n):
            dp[i][i] = 0
        
        # Fill dp for subarrays of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # Try every possible way to split arr[i..j] into two parts
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], 
                                   dp[i][k] + dp[k + 1][j] + 
                                   max_in_subarray[i][k] * max_in_subarray[k + 1][j])
        
        return dp[0][n - 1]
