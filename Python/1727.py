from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Calculate heights
        heights = [[0] * n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == 1:
                    heights[i][j] = heights[i - 1][j] + 1 if i > 0 else 1
        
        # Step 2: Compute the largest area by sorting heights in each row
        max_area = 0
        for row in heights:
            # Sort the heights in descending order
            sorted_heights = sorted(row, reverse=True)
            for k in range(n):
                # Calculate area with sorted_heights[k] as the minimum height in the submatrix
                max_area = max(max_area, sorted_heights[k] * (k + 1))
        
        return max_area
