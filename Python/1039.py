from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        # dp[i][j] will hold the minimum score triangulation for the polygon from vertex i to vertex j
        dp = [[0] * n for _ in range(n)]
        
        # We fill the table for increasing sizes of the polygon (difference between j and i)
        for length in range(2, n):  # length is the difference between j and i (we need at least 2 points between i and j)
            for i in range(n - length):  # i is the starting vertex
                j = i + length  # j is the ending vertex
                dp[i][j] = float('inf')  # Initialize to infinity
                for k in range(i + 1, j):  # k is the middle vertex forming the triangle (i, k, j)
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])
        
        return dp[0][n - 1]  # The minimum triangulation of the full polygon from vertex 0 to vertex n-1
