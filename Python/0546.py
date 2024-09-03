from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        # DP table initialized to -1 for uncomputed values
        dp = [[[ -1 for _ in range(n) ] for _ in range(n) ] for _ in range(n)]
        
        def dfs(i: int, j: int, k: int) -> int:
            # Base case: if segment is invalid
            if i > j:
                return 0
            
            # Check if already computed
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            
            # Extend the segment to include extra boxes of the same color
            max_score = (k + 1) * (k + 1) + dfs(i + 1, j, 0)
            
            for m in range(i + 1, j + 1):
                if boxes[m] == boxes[i]:
                    max_score = max(max_score, dfs(i, m - 1, k + 1) + dfs(m + 1, j, 0))
            
            dp[i][j][k] = max_score
            return max_score
        
        return dfs(0, n - 1, 0)
