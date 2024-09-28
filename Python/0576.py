class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # DP table with dimension (maxMove+1) x m x n
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        
        dp[0][startRow][startColumn] = 1
        result = 0
        
        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for direction in directions:
                        ni, nj = i + direction[0], j + direction[1]
                        
                        if 0 <= ni < m and 0 <= nj < n:
                            dp[move][i][j] = (dp[move][i][j] + dp[move - 1][ni][nj]) % MOD
                        else:
                            result = (result + dp[move - 1][i][j]) % MOD
        
        return result
