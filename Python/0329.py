from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[-1] * n for _ in range(m)]  # Initialize memoization matrix with -1
        
        def dfs(i: int, j: int) -> int:
            if memo[i][j] != -1:
                return memo[i][j]
            
            # The directions array represents: up, down, left, right moves
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            max_path = 1  # Each cell has at least a path length of 1 (itself)
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(ni, nj))
            
            memo[i][j] = max_path
            return max_path
        
        longest_path = 0
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))
        
        return longest_path